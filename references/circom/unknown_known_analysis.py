import sys
import copy  # Needed for deep copying environment in branches/loops
from enum import IntEnum  # Use IntEnum for easy comparison with max()
from typing import Optional, List, Tuple, Set, Any, Dict, Callable
# Assume these imports mirror the Rust structure and previous conversions
from program_structure.ast import (
    Statement, Expression, Meta, Access, Declaration, Substitution,
    UnderscoreSubstitution, ConstraintEquality, IfThenElse, While, Block,
    InitializationBlock, VariableType, SignalType, AssignOp, Variable,
    Number, ArrayInLine, Call, BusCall, UniformArray, InlineSwitchOp,
    # Added TypeReduction
    InfixOp, PrefixOp, ParallelOp, ArrayAccess, ComponentAccess, TypeReduction
)
# Assume Environment class handles the specific types for this analysis
from program_structure.environment import CircomEnvironment
from program_structure.error_code import ReportCode
from program_structure.error_definition import Report, ReportCollection
from program_structure.file_definition import generate_file_location, FileID
from program_structure.program_archive import ProgramArchive

# --- Tag Enum ---


class Tag(IntEnum):
    Known = 0
    Unknown = 1


# --- Environment Type Alias (for documentation) ---
# Python doesn't enforce this, but helps clarity.
# Assumes CircomEnvironment is adapted for Dict[str, Tag] or Dict[str, Tuple[Tag, bool]] etc.
AnalysisEnvironment = CircomEnvironment

# --- Information Structs ---


class EntryInformation:
    def __init__(self, file_id: FileID, environment: AnalysisEnvironment):
        self.file_id: FileID = file_id
        self.environment: AnalysisEnvironment = environment


class ExitInformation:
    def __init__(self,
                 reports: ReportCollection,
                 environment: AnalysisEnvironment,
                 constraints_declared: bool,
                 tags_modified: bool,
                 signals_declared: bool,
                 modified_variables: Set[str]):
        self.reports: ReportCollection = reports
        self.environment: AnalysisEnvironment = environment
        self.constraints_declared: bool = constraints_declared
        self.tags_modified: bool = tags_modified
        self.signals_declared: bool = signals_declared
        self.modified_variables: Set[str] = modified_variables

# --- Main Analysis Function ---


def unknown_known_analysis(name: str, program_archive: ProgramArchive) -> Optional[ReportCollection]:
    """
    Performs static analysis to determine if values are known at compile time.

    Args:
        name: The name of the template or bus to analyze.
        program_archive: Provides access to program structure.

    Returns:
        None if analysis is successful (no errors found).
        ReportCollection containing errors if issues are detected.
    """
    # print(f"Analyzing: {name}") # Debug statement
    # Initialize specific environment for this analysis
    environment = AnalysisEnvironment()
    body: Optional[Statement] = None
    file_id: Optional[FileID] = None

    if program_archive.contains_template(name):
        template_data = program_archive.get_template_data(name)
        body = template_data.get_body()
        file_id = template_data.get_file_id()
        for arg in template_data.get_name_of_params():
            # Params are known inputs to the template body, but might be arrays
            # Rust comment: "We do not know if it is an array or not, so we use the most restrictive option" -> (Known, True)
            # Store as tuple (Tag, is_array)
            environment.add_variable(arg, (Tag.Known, True))
    elif program_archive.contains_bus(name):
        bus_data = program_archive.get_bus_data(name)
        body = bus_data.get_body()
        file_id = bus_data.get_file_id()
        for arg in bus_data.get_name_of_params():
            # Same logic for bus parameters
            environment.add_variable(arg, (Tag.Known, True))
    else:
        # Should not happen if called correctly
        raise ValueError(
            f"Target '{name}' not found as template or bus in program archive.")

    if body is None or file_id is None:
        # Should not happen if contains_template/bus were true
        raise ValueError(f"Could not retrieve body or file_id for '{name}'.")

    entry = EntryInformation(file_id, environment)
    result = analyze(body, entry)

    if result.reports.is_empty():
        return None
    else:
        return result.reports

# --- Core Recursive Analyzer ---


def analyze(stmt: Statement, entry_information: EntryInformation) -> ExitInformation:
    """Recursive function to analyze a single statement."""

    # Helper to iterate sequences (like in Rust)
    def iterate_statements(
        stmts: List[Statement],
        initial_reports: ReportCollection,
        initial_environment: AnalysisEnvironment,
        file_id: FileID,
    ) -> Tuple[bool, bool, bool, ReportCollection, AnalysisEnvironment, Set[str]]:
        current_environment = initial_environment
        accumulated_reports = initial_reports
        accumulated_modified_variables: Set[str] = set()
        all_constraints_declared = False
        all_tags_modified = False
        all_signals_declared = False

        for s in stmts:
            entry = EntryInformation(file_id, current_environment)
            exit_info = analyze(s, entry)  # Recursive call

            # Update state sequentially
            all_constraints_declared = all_constraints_declared or exit_info.constraints_declared
            all_tags_modified = all_tags_modified or exit_info.tags_modified
            all_signals_declared = all_signals_declared or exit_info.signals_declared
            accumulated_modified_variables.update(exit_info.modified_variables)
            # Assuming ReportCollection has extend
            accumulated_reports.extend(exit_info.reports)
            current_environment = exit_info.environment  # Environment flows through

        return (all_constraints_declared, all_tags_modified, all_signals_declared,
                accumulated_reports, current_environment, accumulated_modified_variables)

    # --- analyze function body ---
    file_id = entry_information.file_id
    # Start with a fresh report collection for this level
    reports = ReportCollection()
    # Work on a copy? No, Rust passes env down. Let's modify in place or return new.
    # Rust returns new ExitInfo containing the final env. Let's follow that.
    environment = entry_information.environment
    modified_variables: Set[str] = set()
    constraints_declared = False
    tags_modified = False
    signals_declared = False

    # Use isinstance checks instead of match
    if isinstance(stmt, Declaration):
        name = stmt.name
        dimensions = stmt.dimensions
        xtype = stmt.xtype

        # Add symbol to environment based on type
        if isinstance(xtype, VariableType.Var):
            is_array = len(dimensions) > 0
            environment.add_variable(name, (Tag.Known, is_array))
            modified_variables.add(name)
        elif isinstance(xtype, VariableType.Signal):
            # Signals are initially unknown from the perspective of compile-time values
            environment.add_intermediate(name, Tag.Unknown)
            signals_declared = True
        elif isinstance(xtype, VariableType.Bus):
            environment.add_intermediate_bus(name, Tag.Unknown)
            signals_declared = True
        elif isinstance(xtype, (VariableType.Component, VariableType.AnonymousComponent)):
            # Component instances also start Unknown
            environment.add_component(name, Tag.Unknown)
            signals_declared = True

        # Check dimension expressions for Unknown tags
        # Anon components don't have explicit dims here
        if not isinstance(xtype, VariableType.AnonymousComponent):
            for dimension_expr in dimensions:
                if tag(dimension_expr, environment) == Tag.Unknown:
                    add_report(
                        ReportCode.UnknownDimension,
                        dimension_expr.get_meta(),
                        file_id,
                        reports,  # Add to current reports
                        program_archive  # Pass archive if needed by add_report
                    )

    elif isinstance(stmt, Substitution):
        meta = stmt.meta
        var = stmt.var
        access = stmt.access
        op = stmt.op
        rhe = stmt.rhe

        # Assume meta has type knowledge attached by previous phases
        # Need methods like get_type_knowledge().get_reduces_to()
        reduced_type = meta.get_type_knowledge().get_reduces_to()
        expression_tag = tag(rhe, environment)

        # Determine tag of access path (worst case over all array indices)
        access_tag = Tag.Known
        for acc in access:
            if isinstance(acc, ArrayAccess):
                index_expr = acc.index  # Adjust if attribute name is different
                access_tag = max(access_tag, tag(index_expr, environment))
            # ComponentAccess doesn't affect the 'Known' status of the access path itself
            if access_tag == Tag.Unknown:
                break  # Short-circuit

        # --- Handle based on the type the LHS reduces to ---
        if reduced_type == TypeReduction.Variable:
            # Need to update the variable's tag in the environment
            current_value_tuple = environment.get_variable(
                var)  # Get (Tag, bool)
            if current_value_tuple is None:
                # Should not happen if analysis is correct
                raise LookupError(
                    f"Variable {var} not found in environment during substitution analysis.")
            current_tag, is_array = current_value_tuple

            new_tag: Tag
            if not is_array:
                # Simple variable: tag becomes worst of access path and RHS
                new_tag = max(expression_tag, access_tag)
            else:
                # Array variable: if any access is Unknown, it becomes Unknown.
                # If it was already Unknown, stays Unknown.
                if current_tag == Tag.Known:
                    new_tag = max(expression_tag, access_tag)
                else:
                    new_tag = Tag.Unknown  # Stays unknown

            # Update environment (assuming method exists or it returns mutable object)
            environment.update_variable(
                var, (new_tag, is_array))  # Need this method
            modified_variables.add(var)

        elif isinstance(reduced_type, TypeReduction.Component):  # Check specific type if Enum
            constraints_declared = True  # Instantiating components implies constraints
            if expression_tag == Tag.Unknown:
                add_report(ReportCode.UnknownTemplate, rhe.get_meta(),
                           file_id, reports, program_archive)
            if access_tag == Tag.Unknown:
                # Accessing component array with unknown index
                add_report(ReportCode.UnknownTemplate, meta, file_id,
                           reports, program_archive)  # Use substitution meta

        elif isinstance(reduced_type, TypeReduction.Bus):  # Check specific type if Enum
            if op == AssignOp.AssignVar:  # Assigning a bus instance
                if expression_tag == Tag.Unknown:
                    add_report(ReportCode.UnknownBus, meta,
                               file_id, reports, program_archive)
            elif op == AssignOp.AssignConstraintSignal:  # Constraining signals within a bus
                constraints_declared = True
                if is_non_quadratic(rhe, environment):
                    add_report(ReportCode.NonQuadratic, rhe.get_meta(),
                               file_id, reports, program_archive)
                # e.g., mybus[idx].signal <== ... where idx is Unknown
                if access_tag == Tag.Unknown:
                    add_report(ReportCode.NonQuadratic, meta,
                               file_id, reports, program_archive)
            # AssignSignal is implicitly handled (no quadratic check needed usually)

        elif reduced_type == TypeReduction.Tag:
            tags_modified = True
            if expression_tag == Tag.Unknown:
                add_report(ReportCode.NonValidTagAssignment,
                           rhe.get_meta(), file_id, reports, program_archive)
            # e.g. myarray[idx].tag = ... where idx is Unknown
            if access_tag == Tag.Unknown:
                add_report(ReportCode.NonValidTagAssignment, meta,
                           file_id, reports, program_archive)

        else:  # Default case (likely TypeReduction.Signal)
            if op == AssignOp.AssignConstraintSignal:
                constraints_declared = True
                if is_non_quadratic(rhe, environment):
                    add_report(ReportCode.NonQuadratic, rhe.get_meta(),
                               file_id, reports, program_archive)
                if access_tag == Tag.Unknown:
                    # Accessing signal array with unknown index in constraint
                    add_report(ReportCode.NonQuadratic, meta,
                               file_id, reports, program_archive)
            # Check for assigning TO a component signal via unknown index
            # This relies on environment knowing 'var' is a component instance
            elif environment.has_component(var):
                if access_tag == Tag.Unknown:
                    add_report(ReportCode.UnknownTemplateAssignment,
                               meta, file_id, reports, program_archive)
            # AssignVar or AssignSignal to a regular signal array with unknown index is generally allowed,
            # but doesn't generate non-quadratic constraints itself.

    elif isinstance(stmt, UnderscoreSubstitution):
        op = stmt.op
        rhe = stmt.rhe
        # expression_tag = tag(rhe, environment) # Value not used directly, only for checks
        if op == AssignOp.AssignConstraintSignal:
            constraints_declared = True
            if is_non_quadratic(rhe, environment):
                add_report(ReportCode.NonQuadratic, rhe.get_meta(),
                           file_id, reports, program_archive)

    elif isinstance(stmt, ConstraintEquality):
        lhe = stmt.lhe
        rhe = stmt.rhe
        constraints_declared = True
        if is_non_quadratic(lhe, environment):
            add_report(ReportCode.NonQuadratic, lhe.get_meta(),
                       file_id, reports, program_archive)
        if is_non_quadratic(rhe, environment):
            add_report(ReportCode.NonQuadratic, rhe.get_meta(),
                       file_id, reports, program_archive)

    elif isinstance(stmt, IfThenElse):
        cond = stmt.cond
        if_case = stmt.if_case
        else_case = stmt.else_case

        tag_cond = tag(cond, environment)

        # Analyze branches with copies of the current environment
        # Use deepcopy if environment contains mutable objects that shouldn't be shared
        # Assumes copy method exists
        if_entry = EntryInformation(file_id, environment.copy())
        if_case_info = analyze(if_case, if_entry)

        else_entry = EntryInformation(
            file_id, environment.copy())  # Separate copy
        if else_case:
            else_case_info = analyze(else_case, else_entry)
        else:
            # No else branch, outcome is just the entry state
            else_case_info = ExitInformation(
                reports=ReportCollection(),  # Empty reports
                environment=else_entry.environment,  # The copied env
                constraints_declared=False,
                tags_modified=False,
                signals_declared=False,
                modified_variables=set()
            )

        # Combine results
        constraints_declared = if_case_info.constraints_declared or else_case_info.constraints_declared
        tags_modified = if_case_info.tags_modified or else_case_info.tags_modified
        signals_declared = if_case_info.signals_declared or else_case_info.signals_declared
        # Collect modified variables from both branches
        modified_variables.update(if_case_info.modified_variables)
        modified_variables.update(else_case_info.modified_variables)
        # Collect reports
        reports.extend(if_case_info.reports)
        reports.extend(else_case_info.reports)

        # Merge environments: tag is the max (worst case)
        environment = AnalysisEnvironment.merge(
            if_case_info.environment,
            else_case_info.environment,
            lambda a, b: max(a, b)  # Merge function for tags/tuples
            # Note: merge needs to handle the tuple (Tag, bool) for variables correctly
        )

        # If condition was Unknown, potentially taint modified variables
        if tag_cond == Tag.Unknown:
            for var_name in modified_variables:
                if environment.has_variable(var_name):
                    current_tag, is_array = environment.get_variable(var_name)
                    # Taint the variable's tag to Unknown in the merged environment
                    environment.update_variable(
                        var_name, (Tag.Unknown, is_array))  # Need update method

            # Report potential issues if branches had declarations/modifications
            if constraints_declared:
                add_report(ReportCode.UnreachableConstraints,
                           cond.get_meta(), file_id, reports, program_archive)
            if tags_modified:
                add_report(ReportCode.UnreachableTags, cond.get_meta(),
                           file_id, reports, program_archive)
            if signals_declared:
                add_report(ReportCode.UnreachableSignals,
                           cond.get_meta(), file_id, reports, program_archive)

    elif isinstance(stmt, While):
        cond = stmt.cond
        loop_stmt = stmt.stmt

        # Fixed-point iteration for the loop
        previous_env = None
        # Start with the environment entering the loop
        current_environment = environment

        # Loop until environment stabilizes
        iteration_count = 0
        max_iterations = 100  # Safety break for potential infinite loops

        while iteration_count < max_iterations:
            iteration_count += 1
            env_before_body = current_environment.copy()  # Env at start of this iteration

            # Analyze loop body with current environment state
            body_entry = EntryInformation(file_id, env_before_body)
            body_exit = analyze(loop_stmt, body_entry)

            # Now, body_exit.environment contains the state *after* one loop execution
            # Merge the state *before* the loop iteration with the state *after*
            # This represents the state *potentially* exiting the loop OR re-entering
            merged_environment = AnalysisEnvironment.merge(
                current_environment,  # State before this iteration started
                body_exit.environment,  # State after this iteration finished
                lambda a, b: max(a, b)  # Merge using max (worst-case)
            )

            # Check if the merged state has changed from the state before this iteration
            # We need a way to compare environments or check modification flags precisely
            # The Rust code uses a custom check_modified. Let's adapt that idea.

            # Check if any variable tracked as modified actually changed its tag to Unknown
            # during this merge process compared to the start of the iteration.
            # This check is complex. Let's simplify: loop until environment stops changing.
            if merged_environment == current_environment:  # Requires __eq__ on Environment
                current_environment = merged_environment  # Final stable environment
                # Need last body_exit info for flags/reports
                final_body_exit = body_exit
                break
            else:
                current_environment = merged_environment  # Continue iteration

            # Update reports and modified vars accumulated during the last body execution
            # These might change each iteration, take the last ones? Or accumulate?
            # Rust seems to use the flags/reports from the *last* iteration.
            # Accumulate reports? Or just take last? Let's take last.
            reports.extend(body_exit.reports)
            # Overwrite with reports from last successful body analysis
            reports = body_exit.reports
            modified_variables = body_exit.modified_variables  # Take last set
            constraints_declared = body_exit.constraints_declared  # Take last flags
            tags_modified = body_exit.tags_modified
            signals_declared = body_exit.signals_declared

        else:  # Loop finished due to max_iterations
            # Report potential issue or handle gracefully
            print(
                f"Warning: While loop analysis might not have stabilized after {max_iterations} iterations.", file=sys.stderr)
            # Use the state from the last iteration
            final_body_exit = body_exit

        # --- Post-Loop Analysis ---
        environment = current_environment  # The stabilized environment after the loop
        # Use flags from the last iteration's exit info
        constraints_declared = final_body_exit.constraints_declared
        tags_modified = final_body_exit.tags_modified
        signals_declared = final_body_exit.signals_declared
        modified_variables = final_body_exit.modified_variables  # Vars modified in last iter

        # Check the condition tag *using the stabilized environment*
        tag_cond_after_loop = tag(cond, environment)

        if tag_cond_after_loop == Tag.Unknown:
            # Taint variables modified within the loop if the exit condition is unknown
            for var_name in modified_variables:  # Use modified from *last* iteration
                if environment.has_variable(var_name):
                    current_tag, is_array = environment.get_variable(var_name)
                    environment.update_variable(
                        var_name, (Tag.Unknown, is_array))

            # Report potential issues
            if constraints_declared:  # Use flag from last iteration
                add_report(ReportCode.UnreachableConstraints,
                           cond.get_meta(), file_id, reports, program_archive)
            if tags_modified:
                add_report(ReportCode.UnreachableTags, cond.get_meta(),
                           file_id, reports, program_archive)
            if signals_declared:
                add_report(ReportCode.UnreachableSignals,
                           cond.get_meta(), file_id, reports, program_archive)

    elif isinstance(stmt, Block):
        environment.add_variable_block()
        # Use helper to iterate statements within the block's scope
        (constraints_declared, tags_modified, signals_declared,
         reports, environment, modified_variables) = iterate_statements(
             stmt.stmts, reports, environment, file_id
        )
        environment.remove_variable_block()  # Pop the scope

    elif isinstance(stmt, InitializationBlock):
        # Treat same as a block for analysis flow
        (constraints_declared, tags_modified, signals_declared,
         reports, environment, modified_variables) = iterate_statements(
            stmt.initializations, reports, environment, file_id
        )

    # Other statement types (Return, Log, Assert, etc.) don't directly impact
    # the known/unknown status in this specific analysis, though their arguments are checked by `tag`.

    # --- Return the exit state ---
    return ExitInformation(reports, environment, constraints_declared, tags_modified, signals_declared, modified_variables)

# --- Helper Functions ---


def tag(expression: Expression, environment: AnalysisEnvironment) -> Tag:
    """Determines if an expression's value is Known or Unknown."""
    if isinstance(expression, Number):
        return Tag.Known

    elif isinstance(expression, Variable):
        name = expression.name
        meta = expression.meta  # Assume meta has type info
        # Need access to the type reduction information
        reduced_type = meta.get_type_knowledge().get_reduces_to()

        if reduced_type == TypeReduction.Variable:
            value_tuple = environment.get_variable(name)
            if value_tuple is None:
                raise LookupError(f"Var {name} not found")
            var_tag, is_array = value_tuple
            # If it's an array, accessing it (even without index) implies potential unknownness
            # based on how it might be used later. But reading the whole array doesn't
            # reveal if *an element* is known. Rust returns Known if is_array=True.
            # This seems counter-intuitive? Maybe it means "the *reference* is known"?
            # Let's follow Rust: if it's treated as an array, its "tag" is Known,
            # meaning the array *structure* is known, but elements might be unknown.
            # The check happens during array access `tag(index_expr)`.
            return Tag.Known if is_array else var_tag
        elif reduced_type == TypeReduction.Signal:
            return Tag.Unknown  # Signals depend on inputs
        elif isinstance(reduced_type, TypeReduction.Bus):
            return Tag.Unknown  # Buses contain signals
        elif isinstance(reduced_type, TypeReduction.Component):
            comp_tag = environment.get_component(name)
            if comp_tag is None:
                raise LookupError(f"Comp {name} not found")
            return comp_tag  # Return the stored tag for the component instance
        elif reduced_type == TypeReduction.Tag:
            return Tag.Known  # Accessing a tag yields a known value conceptually
        else:
            raise TypeError(
                f"Unexpected reduced type for Variable: {reduced_type}")

    elif isinstance(expression, (ArrayInLine, Call, BusCall)):
        # Check if any argument/value is Unknown
        values = expression.values if isinstance(
            expression, ArrayInLine) else expression.args
        return expression_iterator(values, Tag.Known, Tag.Unknown, environment)

    elif isinstance(expression, UniformArray):
        tag_value = tag(expression.value, environment)
        tag_dimension = tag(expression.dimension, environment)
        return max(tag_value, tag_dimension)

    elif isinstance(expression, InlineSwitchOp):
        tag_cond = tag(expression.cond, environment)
        tag_true = tag(expression.if_true, environment)
        tag_false = tag(expression.if_false, environment)
        return max(tag_cond, tag_true, tag_false)

    elif isinstance(expression, InfixOp):
        tag_lhe = tag(expression.lhe, environment)
        tag_rhe = tag(expression.rhe, environment)
        return max(tag_rhe, tag_lhe)

    elif isinstance(expression, (PrefixOp, ParallelOp)):
        # ParallelOp might need special handling depending on semantics, assume same as prefix for now
        return tag(expression.rhe, environment)

    else:
        # Handle other expression types if necessary, or raise error
        raise NotImplementedError(
            f"Tag calculation not implemented for expression type: {type(expression)}")


def expression_iterator(
    values: List[Expression],
    end_tag: Tag,  # Tag if loop completes without finding look_for
    look_for: Tag,  # Tag to search for
    environment: AnalysisEnvironment,
) -> Tag:
    """Iterates expressions, returns look_for if found, else end_tag."""
    for value in values:
        value_tag = tag(value, environment)
        if value_tag == look_for:
            return look_for
    return end_tag

# --- Non-Quadratic Check ---


def is_non_quadratic(exp: Expression, environment: AnalysisEnvironment) -> bool:
    """Checks if an expression might lead to a non-quadratic constraint (due to unknown index)."""
    return unknown_index(exp, environment)


def unknown_index(exp: Expression, environment: AnalysisEnvironment) -> bool:
    """Recursively checks if any array access within the expression uses an Unknown index."""
    if isinstance(exp, Number):
        return False

    elif isinstance(exp, Variable):
        # Check indices in the access path
        for acc in exp.access:
            if isinstance(acc, ArrayAccess):
                index_expr = acc.index  # Adjust attribute name if needed
                if tag(index_expr, environment) == Tag.Unknown:
                    return True
        return False  # No unknown index found in access path

    elif isinstance(exp, InfixOp):
        return unknown_index(exp.lhe, environment) or unknown_index(exp.rhe, environment)

    elif isinstance(exp, (PrefixOp, ParallelOp)):
        return unknown_index(exp.rhe, environment)

    elif isinstance(exp, InlineSwitchOp):
        return (unknown_index(exp.cond, environment) or
                unknown_index(exp.if_true, environment) or
                unknown_index(exp.if_false, environment))

    elif isinstance(exp, (Call, BusCall, ArrayInLine)):
        # Check args/values
        exprs = exp.args if isinstance(exp, (Call, BusCall)) else exp.values
        for sub_exp in exprs:
            if unknown_index(sub_exp, environment):
                return True
        return False

    elif isinstance(exp, UniformArray):
        return unknown_index(exp.value, environment) or unknown_index(exp.dimension, environment)

    # Handle other expression types like Tuple if they exist in AST
    # elif isinstance(exp, Tuple):
    #     for sub_exp in exp.values:
    #         if unknown_index(sub_exp, environment):
    #             return True
    #     return False

    else:
        raise NotImplementedError(
            f"Unknown index check not implemented for expr type: {type(exp)}")


# --- Report Helper ---
# (Assuming ProgramArchive might be needed for context, add as arg if so)
def add_report(
    error_code: ReportCode,
    meta: Meta,
    file_id: FileID,
    reports: ReportCollection,
    program_archive: Optional[ProgramArchive] = None,  # Added optional archive
):
    """Adds a report to the collection."""
    # Map ReportCode to messages
    message_map = {
        ReportCode.UnknownTemplateAssignment: "Assigments to signals within an unknown access to an array of components are not allowed",
        ReportCode.UnknownBus: "Parameters of a bus must be known during the constraint generation phase",
        ReportCode.UnknownDimension: "The length of every array must be known during the constraint generation phase",
        ReportCode.UnknownTemplate: "Every component instantiation must be resolved during the constraint generation phase. This component declaration uses a value that can be unknown during the constraint generation phase.",
        ReportCode.NonValidTagAssignment: "Tags cannot be assigned to values that can be unknown during the constraint generation phase",
        ReportCode.NonQuadratic: "Non-quadratic constraint was detected statically, using unknown index will cause the constraint to be non-quadratic",
        ReportCode.UnreachableConstraints: "There are constraints depending on the value of the condition and it can be unknown during the constraint generation phase",
        ReportCode.UnreachableTags: "There are tag assignments depending on the value of the condition and it can be unknown during the constraint generation phase",
        ReportCode.UnreachableSignals: "There are signal, bus or component declarations depending on the value of the condition and it can be unknown during the constraint generation phase",
    }
    message = message_map.get(
        error_code, f"Unknown or unimplemented error code: {error_code}")

    report = Report.error("Static analysis error found",
                          error_code)  # Assume Report class exists
    location = generate_file_location(
        meta.start, meta.end)  # Assume function exists
    report.add_primary(location, file_id, message)  # Assume method exists
    reports.push(report)  # Assume method exists


# Note: The check_modified function from Rust is implicitly handled within the
# fixed-point iteration logic of the While loop analysis using environment comparison
# and the merge function. A direct translation might be needed if environment comparison
# is inefficient or not implemented, or if the exact logic of only setting `modified=True`
# when transitioning to Unknown is critical.
