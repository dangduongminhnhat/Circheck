import sys
# Use Any for AST nodes for brevity
from typing import Optional, List, Tuple, Set, Dict, Any
# Assume these imports mirror the Rust structure
from .type_given_function import type_given_function
from .type_register import TypeRegister  # Assume this class exists
from program_structure.ast import (  # Assume these AST node classes exist
    Expression, Statement, Meta, Call, Declaration, InitializationBlock,
    Substitution, ConstraintEquality, LogCall, Assert, Return, IfThenElse,
    While, Block, UnderscoreSubstitution, Access, ArrayAccess, ComponentAccess,
    Number, ArrayInLine, UniformArray, InfixOp, PrefixOp, ParallelOp,
    InlineSwitchOp, Variable, BusCall, VariableType, SignalType, AssignOp,
    LogArgument, WireType  # Include WireType here
)
from program_structure.environment import CircomEnvironment  # Assume this class exists
from program_structure.error_code import ReportCode  # Assume this Enum exists
# Assume these classes exist
from program_structure.error_definition import Report, ReportCollection
# Assume FileID is int or str
from program_structure.file_definition import generate_file_location, FileID
# Assume this class exists
from program_structure.program_archive import ProgramArchive
# from program_structure.wire_data import WireType # Already imported above

# Type Aliases (using typing for hints)
ArithmeticType = int
ComponentInfo = Tuple[Optional[str], ArithmeticType]
BusInfo = Tuple[Optional[str], ArithmeticType, List[str]]
SignalInfo = Tuple[ArithmeticType, List[str]]
VarInfo = ArithmeticType
# Assume CircomEnvironment is generic in Python or handles types internally
TypingEnvironment = CircomEnvironment  # Simplified representation
# Assuming TypeRegister handles the type
CallRegister = TypeRegister[ArithmeticType]

# --- FoldedType Class ---


class FoldedType:
    def __init__(self, arithmetic: Optional[ArithmeticType] = None,
                 template: Optional[str] = None, bus: Optional[str] = None):
        self.arithmetic = arithmetic
        self.template = template
        self.bus = bus

    @classmethod
    def arithmetic_type(cls, dimensions: ArithmeticType) -> 'FoldedType':
        return cls(arithmetic=dimensions)

    @classmethod
    def template(cls, name: str) -> 'FoldedType':
        return cls(template=name)

    def is_template(self) -> bool:
        return self.template is not None and self.arithmetic is None

    @classmethod
    def bus(cls, name: str, dimensions: ArithmeticType) -> 'FoldedType':
        return cls(bus=name, arithmetic=dimensions)

    def is_bus(self) -> bool:
        return self.bus is not None

    def dim(self) -> int:
        return self.arithmetic if self.arithmetic is not None else 0

    @staticmethod
    def same_type(left: 'FoldedType', right: 'FoldedType') -> bool:
        # Simplified logic, Python compares Nones correctly
        return (left.template == right.template and
                left.bus == right.bus and
                left.arithmetic == right.arithmetic)

# --- AnalysisInformation Class ---
# Using a simple class to hold state, similar to the Rust struct


class AnalysisInformation:
    def __init__(self, file_id: FileID, program_archive: ProgramArchive):
        self.program_archive = program_archive  # Keep ref for convenience
        self.file_id: FileID = file_id
        self.reached: Set[str] = set()
        # Assume ReportCollection class exists
        self.reports: ReportCollection = ReportCollection()
        # Assume TypeRegister class exists
        self.registered_calls: CallRegister = CallRegister()
        # Assume CircomEnvironment class exists
        self.environment: TypingEnvironment = CircomEnvironment()
        self.return_type: Optional[ArithmeticType] = None

# --- OutInfo Class ---


class OutInfo:
    def __init__(self, reached: Set[str]):
        self.reached = reached

# --- Error Handling Helper ---


class TypeErrorFound(Exception):
    """Custom exception to signal a type error was found and added."""
    pass


def add_report(error_code: ReportCode, meta: Meta, reports: ReportCollection, program_archive: ProgramArchive):
    # Find file_id from meta if possible, otherwise use current context?
    # Rust version uses meta directly. Let's assume Meta has file_id.
    file_id = meta.get_file_id()  # Assume meta has this method
    # Assume Report class has 'error' factory
    report = Report.error("Typing error found", error_code)
    location = generate_file_location(
        meta.start, meta.end)  # Assume function exists

    # Map ReportCode to messages (simplified example)
    message = f"Error Code: {error_code.name}"  # Default message
    if error_code == ReportCode.EmptyArrayInlineDeclaration:
        message = "Empty arrays can not be declared inline"
    elif error_code == ReportCode.NonHomogeneousArray:
        # Note: Rust version takes dims, need to adjust if passing dims here
        message = "All the elements in a array must have the same type."
    elif error_code == ReportCode.InvalidArraySize:
        # How to get associated data? Assume it's stored if needed
        dim = getattr(error_code, 'dim', '?')
        message = f"Array indexes and lengths must be single arithmetic expressions. Found expression with {dim} dimensions."
    elif error_code == ReportCode.InvalidArraySizeT:
        message = "Array indexes and lengths must be single arithmetic expressions. Found component instead of expression."
    elif error_code == ReportCode.InvalidArraySizeB:
        message = "Array indexes and lengths must be single arithmetic expressions. Found bus instead of expression."
    elif error_code == ReportCode.InvalidArrayAccess:
        expected = getattr(error_code, 'expected', '?')
        given = getattr(error_code, 'given', '?')
        message = f"Array access does not match the dimensions of the expression. Expected {expected} dimensions, given {given}."
    elif error_code == ReportCode.InvalidSignalAccess:
        message = "Signal not found in component: only accesses to input/output signals are allowed"
    elif error_code == ReportCode.InvalidTagAccess:
        message = "Tag not found in signal: only accesses to tags that appear in the definition of the signal are allowed"
    elif error_code == ReportCode.InvalidTagAccessAfterArray:
        message = "Invalid access to the tag of an array element: tags belong to complete arrays, not to individual positions.\n Hint: instead of signal[pos].tag use signal.tag"
    elif error_code == ReportCode.InvalidArrayType:
        message = "Components can not be declared inside inline arrays"
    elif error_code == ReportCode.InvalidArrayTypeB:
        message = "Buses can not be declared inside inline arrays"
    elif error_code in (ReportCode.InfixOperatorWithWrongTypes, ReportCode.PrefixOperatorWithWrongTypes):
        message = "Type not allowed by the operator"
    elif error_code == ReportCode.ParallelOperatorWithWrongTypes:
        message = "Type not allowed by the operator parallel (parallel operator can only be applied to templates)"
    elif error_code == ReportCode.InvalidPartialArray:
        message = "Only variable arrays can be accessed partially"
    elif error_code == ReportCode.UninitializedSymbolInExpression:
        message = "The type of this symbol is not known"
    elif error_code == ReportCode.WrongTypesInAssignOperationOperatorSignal:
        message = ("The operator does not match the types of the assigned elements.\n "
                   "Assignments to signals do not allow the operator =, try using <== or <-- instead")
    elif error_code == ReportCode.WrongTypesInAssignOperationOperatorNoSignal:
        message = ("The operator does not match the types of the assigned elements.\n "
                   "Only assignments to signals allow the operators <== and <--, try using = instead")
    elif error_code == ReportCode.WrongTypesInAssignOperationArrayTemplates:
        message = "Assignee and assigned types do not match.\n All components of an array must be instances of the same template."
    elif error_code == ReportCode.WrongTypesInAssignOperationTemplate:
        message = "Assignee and assigned types do not match.\n Expected template but found expression."
    elif error_code == ReportCode.WrongTypesInAssignOperationArrayBuses:
        message = "Assignee and assigned types do not match.\n All buses of an array must be the same type."
    elif error_code == ReportCode.WrongTypesInAssignOperationBus:
        message = "Assignee and assigned types do not match.\n Expected bus but found a different expression."
    elif error_code == ReportCode.WrongTypesInAssignOperationExpression:
        message = "Assignee and assigned types do not match.\n Expected expression found template."
    elif error_code == ReportCode.WrongTypesInAssignOperationDims:
        expected = getattr(error_code, 'expected', '?')
        found = getattr(error_code, 'found', '?')
        message = f"Assignee and assigned types do not match. Expected dimensions: {expected}, found {found}"
    elif error_code == ReportCode.InvalidArgumentInCall:
        message = "Components can not be passed as arguments"
    elif error_code == ReportCode.InvalidArgumentInBusInstantiationT:
        message = "Components can not be passed as arguments"
    elif error_code == ReportCode.InvalidArgumentInBusInstantiationB:
        message = "Buses can not be passed as arguments"
    elif error_code == ReportCode.UnableToTypeFunction:
        message = "Unable to infer the type of this function"
    elif error_code == ReportCode.MustBeSingleArithmetic:
        dim = getattr(error_code, 'dim', '?')
        message = f"Must be a single arithmetic expression. Found expression of {dim} dimensions"
    elif error_code == ReportCode.MustBeSingleArithmeticT:
        message = "Must be a single arithmetic expression. Found component"
    elif error_code == ReportCode.MustBeSingleArithmeticB:
        message = "Must be a single arithmetic expression. Found bus"
    elif error_code == ReportCode.MustBeArithmetic:
        message = "Must be a single arithmetic expression or an array of arithmetic expressions. Found component"
    elif error_code == ReportCode.OutputTagCannotBeModifiedOutside:
        message = "Output tag from a subcomponent cannot be modified"
    elif error_code == ReportCode.InputTagCannotBeModifiedOutside:
        message = "Input tag from a subcomponent cannot be modified"
    elif error_code == ReportCode.InputTagCannotBeAccessedOutside:
        message = "Input tag from a subcomponent cannot be accessed"
    elif error_code == ReportCode.MustBeSameDimension:
        dim_1 = getattr(error_code, 'dim_1', '?')
        dim_2 = getattr(error_code, 'dim_2', '?')
        message = f"Must be two arrays of the same dimensions. Found {dim_1} and {dim_2} dimensions"
    elif error_code == ReportCode.MainComponentWithTags:
        message = "Main component cannot have inputs with tags"
    elif error_code == ReportCode.ExpectedDimDiffGotDim:
        expected = getattr(error_code, 'expected', '?')
        got = getattr(error_code, 'got', '?')
        message = f"All branches of a function should return an element of the same dimensions. Found {expected} and {got} dimensions"
    elif error_code == ReportCode.WrongNumberOfArguments:
        expected = getattr(error_code, 'expected', '?')
        got = getattr(error_code, 'got', '?')
        message = f"Expecting {expected} arguments, {got} where obtained"
    elif error_code == ReportCode.UninitializedComponent:
        message = "Trying to access to a signal of a component that has not been initialized"
    elif error_code == ReportCode.NonCompatibleBranchTypes:
        message = "Inline switch operator branches types are non compatible"
    elif error_code == ReportCode.MustBeSameBus:
        message = "Both kind of buses must be equals"
    elif error_code == ReportCode.MustBeBus:
        message = "Expected to be a bus"
    # ReportCode::InvalidSignalAccessInBus missing in Rust snippet provided? Add if needed.
    elif error_code == ReportCode.IllegalMainExpression:
        message = "Invalid main component: the main component should be a template, not a function call or expression"
    # Add more specific messages based on ReportCode here...
    # This part needs careful mapping from the Rust source or ReportCode definition.

    # Assume Report has add_primary
    report.add_primary(location, file_id, message)
    reports.push(report)  # Assume ReportCollection has push


def add_report_and_raise(error_code: ReportCode, meta: Meta, analysis_information: AnalysisInformation):
    """Adds a report and raises an exception to stop current analysis path."""
    add_report(error_code, meta, analysis_information.reports,
               analysis_information.program_archive)
    raise TypeErrorFound()


# --- SymbolInformation Helper Enum/Classes ---
# Using simple strings or tuples as stand-ins for the Rust enum SymbolInformation
# Or define dedicated classes if more structure is needed.
# e.g., ("Component", Optional[str]), ("Var", int), ("Signal", int), ("Bus", Tuple[Optional[str], int]), ("Tag", None)
SymbolInfoType = Tuple[str, Any]

# --- Main Type Check Function ---


def type_check(program_archive: ProgramArchive) -> Tuple[Optional[OutInfo], Optional[ReportCollection]]:
    main_file_id = program_archive.get_file_id_main()  # Assume method exists
    analysis_information = AnalysisInformation(main_file_id, program_archive)
    initial_expression = program_archive.get_main_expression()  # Assume method exists

    try:
        _ = type_expression(initial_expression, analysis_information)
    except TypeErrorFound:
        # Error already added to reports, stop processing this path
        return None, analysis_information.reports  # Return errors collected so far

    # Check main tags separately, even if type_expression succeeded partially
    try:
        check_main_has_tags(initial_expression, analysis_information)
    except TypeErrorFound:
        # Error added, will be reflected in the final check
        pass

    if analysis_information.reports.is_empty():  # Assume method exists
        return OutInfo(analysis_information.reached), None
    else:
        return None, analysis_information.reports

# --- Tag Checking Helpers ---


def check_bus_contains_tag_recursive(bus_name: str, program_archive: ProgramArchive) -> bool:
    bus_data = program_archive.get_bus_data(bus_name)  # Assume method exists
    tag_in_inputs = False
    for _name, info in bus_data.get_fields():  # Assume method exists
        if not info.get_tags().is_empty():  # Assume method exists
            tag_in_inputs = True
            break
        # Python needs explicit type checking for the WireType variant
        wire_type = info.get_type()
        if isinstance(wire_type, WireType.Bus):  # Assuming WireType.Bus holds the name
            # Adjust access if needed
            if check_bus_contains_tag_recursive(wire_type.name, program_archive):
                tag_in_inputs = True
                break
    return tag_in_inputs


def check_main_has_tags(initial_expression: Expression, analysis_information: AnalysisInformation):
    program_archive = analysis_information.program_archive
    reports = analysis_information.reports
    meta = initial_expression.get_meta()  # Assume method exists

    if isinstance(initial_expression, Call):
        template_id = initial_expression.id
        # Assume method exists
        if program_archive.contains_template(template_id):
            template_data = program_archive.get_template_data(
                template_id)  # Assume method exists
            inputs = template_data.get_inputs()  # Assume method exists
            for _name, info in inputs:
                if not info.get_tags().is_empty():
                    add_report(ReportCode.MainComponentWithTags,
                               meta, reports, program_archive)
                    raise TypeErrorFound()  # Signal error found
                wire_type = info.get_type()
                if isinstance(wire_type, WireType.Bus):
                    if check_bus_contains_tag_recursive(wire_type.name, program_archive):
                        add_report(ReportCode.MainComponentWithTags,
                                   meta, reports, program_archive)
                        raise TypeErrorFound()  # Signal error found
        else:
            # If it's a Call but not a template -> Error
            add_report(ReportCode.IllegalMainExpression,
                       meta, reports, program_archive)
            raise TypeErrorFound()  # Signal error found
    else:
        # If it's not a Call -> Error
        add_report(ReportCode.IllegalMainExpression,
                   meta, reports, program_archive)
        raise TypeErrorFound()  # Signal error found


# --- Statement Typing ---
def type_statement(statement: Statement, analysis_information: AnalysisInformation):
    program_archive = analysis_information.program_archive
    environment = analysis_information.environment
    reports = analysis_information.reports

    # Use isinstance to mimic Rust's match
    if isinstance(statement, InitializationBlock):
        treat_sequence_of_statements(
            statement.initializations, analysis_information)

    elif isinstance(statement, Declaration):
        dimensions_types: List[FoldedType] = []
        try:
            dimensions_types = type_array_of_expressions(
                statement.dimensions, analysis_information)
        except TypeErrorFound:
            # Error already reported, but declaration might still be processed partially
            # Or decide to return early here? Let's continue for now.
            # Ensure dimensions_types has the same length for zip
            dimensions_types = [FoldedType.arithmetic_type(
                0)] * len(statement.dimensions)  # Placeholder

        for dim_expr, dim_type in zip(statement.dimensions, dimensions_types):
            meta = dim_expr.get_meta()
            if dim_type.is_template():
                add_report(ReportCode.InvalidArraySizeT,
                           meta, reports, program_archive)
                # Continue checking other dimensions
            elif dim_type.is_bus():
                add_report(ReportCode.InvalidArraySizeB,
                           meta, reports, program_archive)
                # Continue checking other dimensions
            elif dim_type.dim() > 0:
                # Pass the dimension to the error code if needed
                # Assuming ReportCode constructor or a wrapper handles this
                add_report(ReportCode.InvalidArraySize(
                    dim_type.dim()), meta, reports, program_archive)
                # Continue checking other dimensions

        # Process declaration based on xtype
        xtype = statement.xtype
        name = statement.name
        dims_len = len(statement.dimensions)
        tags = getattr(xtype, 'tags', [])  # Get tags if available
        meta = statement.meta  # Declaration meta

        if isinstance(xtype, VariableType.Signal):
            signal_info: SignalInfo = (dims_len, tags)
            if xtype.stype == SignalType.Input:
                environment.add_input(name, signal_info)
            elif xtype.stype == SignalType.Output:
                environment.add_output(name, signal_info)
            elif xtype.stype == SignalType.Intermediate:
                environment.add_intermediate(name, signal_info)
        elif isinstance(xtype, VariableType.Var):
            environment.add_variable(name, dims_len)
        elif isinstance(xtype, (VariableType.Component, VariableType.AnonymousComponent)):
            # component_inference needs to be accessed from meta
            comp_inference = meta.component_inference if hasattr(
                meta, 'component_inference') else None
            component_info: ComponentInfo = (comp_inference, dims_len)
            environment.add_component(name, component_info)
        elif isinstance(xtype, VariableType.Bus):
            tname = xtype.tname
            bus_info: BusInfo = (tname, dims_len, tags)
            if xtype.sstype == SignalType.Input:
                environment.add_input_bus(name, bus_info)
            elif xtype.sstype == SignalType.Output:
                environment.add_output_bus(name, bus_info)
            elif xtype.sstype == SignalType.Intermediate:
                environment.add_intermediate_bus(name, bus_info)

    elif isinstance(statement, Substitution):
        rhe = statement.rhe
        meta = statement.meta
        rhe_type: Optional[FoldedType] = None
        access_info: Optional[AccessInfo] = None
        symbol_info: Optional[SymbolInfoType] = None

        try:
            rhe_type = type_expression(rhe, analysis_information)
            access_info = treat_access(statement.access, analysis_information)
            symbol_info = apply_access_to_symbol(
                statement.var,
                meta,
                access_info,
                environment,
                reports,
                program_archive
            )
        except TypeErrorFound:
            return  # Stop processing this statement if critical parts failed

        # Check operator compatibility based on symbol type
        op = statement.op
        # e.g., "Signal", "Var", "Component", "Bus", "Tag"
        symbol_kind = symbol_info[0]

        allowed_ops_map = {
            "Signal": {AssignOp.AssignConstraintSignal, AssignOp.AssignSignal},
            "Var": {AssignOp.AssignVar},
            "Component": {AssignOp.AssignVar},  # Assigning template instances
            "Bus": {AssignOp.AssignConstraintSignal, AssignOp.AssignSignal, AssignOp.AssignVar},
            "Tag": {AssignOp.AssignVar}  # Assigning values to tags
        }

        is_compatible = False
        if symbol_kind in allowed_ops_map and op in allowed_ops_map[symbol_kind]:
            is_compatible = True
            # Special check for Bus assignment with AssignVar
            if symbol_kind == "Bus" and op == AssignOp.AssignVar:
                # Check if rhe is a BusCall or BusCallArray (needs methods on Expression)
                if not (hasattr(rhe, 'is_bus_call') and rhe.is_bus_call()) and \
                   not (hasattr(rhe, 'is_bus_call_array') and rhe.is_bus_call_array()):
                    add_report_and_raise(
                        ReportCode.WrongTypesInAssignOperationBus, meta, analysis_information)

            # Special checks for Tag assignment
            if symbol_kind == "Tag":
                # Check if tag is from an output/input wire of a subcomponent
                if environment.has_component(statement.var):
                    comp_info = environment.get_component(
                        statement.var)  # Returns ComponentInfo
                    if comp_info and comp_info[0] is not None and access_info[1] and len(access_info[1]) > 0:
                        template_name = comp_info[0]
                        # Name from (name, dim)
                        first_access_name = access_info[1][0][0]
                        template_data = program_archive.get_template_data(
                            template_name)
                        if template_data.get_output_info(first_access_name):
                            add_report_and_raise(
                                ReportCode.OutputTagCannotBeModifiedOutside, meta, analysis_information)
                        if template_data.get_input_info(first_access_name):
                            add_report_and_raise(
                                ReportCode.InputTagCannotBeModifiedOutside, meta, analysis_information)

        elif symbol_kind == "Signal" and op == AssignOp.AssignVar:
            add_report_and_raise(
                ReportCode.WrongTypesInAssignOperationOperatorSignal, meta, analysis_information)
        elif symbol_kind != "Signal" and op in (AssignOp.AssignSignal, AssignOp.AssignConstraintSignal):
            add_report_and_raise(
                ReportCode.WrongTypesInAssignOperationOperatorNoSignal, meta, analysis_information)
        else:
            # Default catch-all for incompatible ops/types if not covered above
            # This might indicate an issue in the allowed_ops_map or a new case
            # Choose the most appropriate error code
            if symbol_kind == "Signal":
                add_report_and_raise(
                    ReportCode.WrongTypesInAssignOperationOperatorSignal, meta, analysis_information)
            else:
                add_report_and_raise(
                    ReportCode.WrongTypesInAssignOperationOperatorNoSignal, meta, analysis_information)

        # Check type compatibility based on symbol type
        if symbol_kind == "Component":
            possible_template = symbol_info[1]  # Optional[str]
            if rhe_type.is_template():
                if possible_template is None:
                    # Infer the type - Python environment needs a way to update
                    # Assuming environment handles mutation directly or returns mutable object
                    # This is tricky, depends heavily on CircomEnvironment implementation
                    environment.update_component_template(
                        statement.var, rhe_type.template)  # Fictional method
                elif possible_template != rhe_type.template:
                    add_report_and_raise(
                        ReportCode.WrongTypesInAssignOperationArrayTemplates, meta, analysis_information)
            else:
                add_report_and_raise(
                    ReportCode.WrongTypesInAssignOperationTemplate, meta, analysis_information)

        elif symbol_kind == "Bus":
            possible_bus, dim = symbol_info[1]  # Tuple[Optional[str], int]
            if rhe_type.is_bus():
                if dim != rhe_type.dim():
                    add_report_and_raise(ReportCode.WrongTypesInAssignOperationDims(
                        dim, rhe_type.dim()), meta, analysis_information)
                elif possible_bus is None:
                    # Infer the bus type - Requires environment update method
                    environment.update_bus_type(
                        statement.var, rhe_type.bus)  # Fictional method
                elif possible_bus != rhe_type.bus:
                    if dim > 0:
                        add_report_and_raise(
                            ReportCode.WrongTypesInAssignOperationArrayBuses, meta, analysis_information)
                    else:
                        add_report_and_raise(
                            ReportCode.WrongTypesInAssignOperationBus, meta, analysis_information)
            else:
                add_report_and_raise(
                    ReportCode.WrongTypesInAssignOperationBus, meta, analysis_information)

        elif symbol_kind in ("Signal", "Var"):
            dim = symbol_info[1]  # int
            if rhe_type.is_template():
                add_report_and_raise(
                    ReportCode.WrongTypesInAssignOperationExpression, meta, analysis_information)
            elif rhe_type.is_bus():
                add_report_and_raise(
                    ReportCode.WrongTypesInAssignOperationBus, meta, analysis_information)
            elif dim != rhe_type.dim():
                add_report_and_raise(ReportCode.WrongTypesInAssignOperationDims(
                    dim, rhe_type.dim()), meta, analysis_information)

        elif symbol_kind == "Tag":
            # Dimension should be 0 for a tag symbol
            if rhe_type.is_template():
                add_report_and_raise(
                    ReportCode.WrongTypesInAssignOperationExpression, meta, analysis_information)
            elif rhe_type.is_bus():
                add_report_and_raise(
                    ReportCode.WrongTypesInAssignOperationBus, meta, analysis_information)
            elif 0 != rhe_type.dim():
                add_report_and_raise(ReportCode.WrongTypesInAssignOperationDims(
                    0, rhe_type.dim()), meta, analysis_information)

    elif isinstance(statement, ConstraintEquality):
        lhe_type: Optional[FoldedType] = None
        rhe_type: Optional[FoldedType] = None
        error_occurred = False
        try:
            lhe_type = type_expression(statement.lhe, analysis_information)
        except TypeErrorFound:
            error_occurred = True
            lhe_type = FoldedType.arithmetic_type(0)  # Placeholder
        try:
            rhe_type = type_expression(statement.rhe, analysis_information)
        except TypeErrorFound:
            error_occurred = True
            rhe_type = FoldedType.arithmetic_type(0)  # Placeholder

        # Continue checks even if typing failed, using placeholders
        if lhe_type.is_template():
            add_report(ReportCode.MustBeArithmetic,
                       statement.lhe.get_meta(), reports, program_archive)
        if rhe_type.is_template():
            add_report(ReportCode.MustBeArithmetic,
                       statement.rhe.get_meta(), reports, program_archive)

        if lhe_type.is_bus() or rhe_type.is_bus():
            if lhe_type.bus is not None and rhe_type.bus is not None:
                if lhe_type.bus != rhe_type.bus:
                    add_report(ReportCode.MustBeSameBus,
                               statement.lhe.get_meta(), reports, program_archive)
            elif lhe_type.bus is not None:  # Only LHE is bus
                add_report(ReportCode.MustBeBus,
                           statement.rhe.get_meta(), reports, program_archive)
            else:  # Only RHE is bus (or somehow both None but is_bus() was true)
                add_report(ReportCode.MustBeBus,
                           statement.lhe.get_meta(), reports, program_archive)
        # Only compare dimensions if neither is template and they are not mismatched buses
        elif not lhe_type.is_template() and not rhe_type.is_template() and \
                (lhe_type.bus is None or rhe_type.bus is None or lhe_type.bus == rhe_type.bus):
            if lhe_type.dim() != rhe_type.dim():
                add_report(ReportCode.MustBeSameDimension(lhe_type.dim(), rhe_type.dim()),
                           statement.rhe.get_meta(), reports, program_archive)  # Report on RHE like Rust

        if error_occurred:
            raise TypeErrorFound()  # Propagate if sub-expressions failed

    elif isinstance(statement, LogCall):
        meta = statement.meta
        error_occurred = False
        for arglog in statement.args:
            # Assuming LogArgument.LogExp holds the expression
            if isinstance(arglog, LogArgument.LogExp):
                arg = arglog.expr  # Adjust access based on actual LogArgument structure
                try:
                    arg_type = type_expression(arg, analysis_information)
                    if arg_type.is_template():
                        add_report(ReportCode.MustBeSingleArithmeticT,
                                   meta, reports, program_archive)
                    elif arg_type.is_bus():
                        add_report(ReportCode.MustBeSingleArithmeticB,
                                   meta, reports, program_archive)
                    elif arg_type.dim() > 0:
                        add_report(ReportCode.MustBeSingleArithmetic(
                            arg_type.dim()), meta, reports, program_archive)
                except TypeErrorFound:
                    error_occurred = True  # Mark error but continue checking other args
        if error_occurred:
            raise TypeErrorFound()

    elif isinstance(statement, Assert):
        meta = statement.meta
        try:
            arg_type = type_expression(statement.arg, analysis_information)
            if arg_type.is_template():
                add_report_and_raise(
                    ReportCode.MustBeSingleArithmeticT, meta, analysis_information)
            elif arg_type.is_bus():
                add_report_and_raise(
                    ReportCode.MustBeSingleArithmeticB, meta, analysis_information)
            elif arg_type.dim() > 0:
                add_report_and_raise(ReportCode.MustBeSingleArithmetic(
                    arg_type.dim()), meta, analysis_information)
        except TypeErrorFound:
            return  # Error already raised/reported

    elif isinstance(statement, Return):
        meta = statement.meta
        assert analysis_information.return_type is not None, "Return statement outside function context"
        try:
            value_type = type_expression(statement.value, analysis_information)
            expected_ret_type = analysis_information.return_type
            # Rust asserted !value_type.is_template(), check here if needed, but type_expression should handle
            if value_type.is_template():
                # This case might indicate an issue earlier, or needs a specific error
                add_report_and_raise(
                    ReportCode.MustBeArithmetic, meta, analysis_information)  # Example error
            elif value_type.is_bus():
                # Functions likely return arithmetic
                add_report_and_raise(
                    ReportCode.MustBeSingleArithmeticB, meta, analysis_information)
            elif expected_ret_type != value_type.dim():
                add_report_and_raise(ReportCode.ExpectedDimDiffGotDim(expected_ret_type, value_type.dim()),
                                     meta, analysis_information)
        except TypeErrorFound:
            return

    elif isinstance(statement, IfThenElse):
        cond_meta = statement.cond.get_meta()
        error_occurred = False
        try:
            cond_type = type_expression(statement.cond, analysis_information)
            if cond_type.is_template():
                add_report(ReportCode.MustBeSingleArithmeticT,
                           cond_meta, reports, program_archive)
                error_occurred = True
            elif cond_type.is_bus():
                add_report(ReportCode.MustBeSingleArithmeticB,
                           cond_meta, reports, program_archive)
                error_occurred = True
            elif cond_type.dim() > 0:
                add_report(ReportCode.MustBeSingleArithmetic(
                    cond_type.dim()), cond_meta, reports, program_archive)
                error_occurred = True
        except TypeErrorFound:
            error_occurred = True  # Condition typing failed

        # Type branches regardless of condition errors, but propagate failure
        try:
            type_statement(statement.if_case, analysis_information)
        except TypeErrorFound:
            error_occurred = True
        if statement.else_case:
            try:
                type_statement(statement.else_case, analysis_information)
            except TypeErrorFound:
                error_occurred = True

        if error_occurred:
            raise TypeErrorFound()

    elif isinstance(statement, While):
        cond_meta = statement.cond.get_meta()
        error_occurred = False
        try:
            cond_type = type_expression(statement.cond, analysis_information)
            if cond_type.is_template():
                add_report(ReportCode.MustBeSingleArithmeticT,
                           cond_meta, reports, program_archive)
                error_occurred = True
            elif cond_type.is_bus():
                add_report(ReportCode.MustBeSingleArithmeticB,
                           cond_meta, reports, program_archive)
                error_occurred = True
            elif cond_type.dim() > 0:
                add_report(ReportCode.MustBeSingleArithmetic(
                    cond_type.dim()), cond_meta, reports, program_archive)
                error_occurred = True
        except TypeErrorFound:
            error_occurred = True  # Condition typing failed

        # Type body regardless, propagate failure
        try:
            type_statement(statement.stmt, analysis_information)
        except TypeErrorFound:
            error_occurred = True

        if error_occurred:
            raise TypeErrorFound()

    elif isinstance(statement, Block):
        environment.add_variable_block()  # Assume method exists
        error_occurred = False
        try:
            treat_sequence_of_statements(statement.stmts, analysis_information)
        except TypeErrorFound:
            error_occurred = True  # Error occurred within the block
        finally:
            # Ensure block is removed even if error occurred inside
            environment.remove_variable_block()  # Assume method exists
        if error_occurred:
            raise TypeErrorFound()  # Propagate after cleanup

    elif isinstance(statement, UnderscoreSubstitution):
        rhe = statement.rhe
        try:
            rhe_type = type_expression(rhe, analysis_information)
            if rhe_type.is_template():
                add_report_and_raise(
                    ReportCode.MustBeArithmetic, rhe.get_meta(), analysis_information)
            # Underscore implies we don't care about the dimension matching LHS
        except TypeErrorFound:
            return

    # elif isinstance(statement, MultSubstitution):
    #     # Rust code says unreachable!()
    #     raise AssertionError("MultSubstitution should not be reachable here")

    else:
        # Should not happen if all statement types are covered
        raise NotImplementedError(
            f"Unhandled statement type: {type(statement)}")


# --- Expression Typing ---
def type_expression(expression: Expression, analysis_information: AnalysisInformation) -> FoldedType:
    program_archive = analysis_information.program_archive
    environment = analysis_information.environment
    reports = analysis_information.reports

    if isinstance(expression, Number):
        return FoldedType.arithmetic_type(0)

    elif isinstance(expression, ArrayInLine):
        meta = expression.meta
        if not expression.values:
            add_report_and_raise(
                ReportCode.EmptyArrayInlineDeclaration, meta, analysis_information)

        values_types = type_array_of_expressions(
            expression.values, analysis_information)  # Raises on failure

        # If we reach here, type_array_of_expressions succeeded
        first_type = values_types[0]
        inferred_dim = first_type.dim()
        homogeneous = True

        if first_type.is_template():
            add_report(ReportCode.InvalidArrayType,
                       expression.values[0].get_meta(), reports, program_archive)
            homogeneous = False  # Treat as non-homogeneous if first is invalid
        elif first_type.is_bus():
            add_report(ReportCode.InvalidArrayTypeB,
                       expression.values[0].get_meta(), reports, program_archive)
            homogeneous = False

        for i, (expr_val, value_type) in enumerate(zip(expression.values[1:], values_types[1:]), 1):
            expr_meta = expr_val.get_meta()
            is_compatible = True
            if value_type.is_template():
                add_report(ReportCode.InvalidArrayType,
                           expr_meta, reports, program_archive)
                is_compatible = False
            elif value_type.is_bus():
                add_report(ReportCode.InvalidArrayTypeB,
                           expr_meta, reports, program_archive)
                is_compatible = False
            elif inferred_dim != value_type.dim():
                add_report(ReportCode.NonHomogeneousArray(inferred_dim, value_type.dim()),
                           expr_meta, reports, program_archive)
                is_compatible = False

            if not is_compatible:
                homogeneous = False  # Mark the whole array as non-homogeneous

        if not homogeneous:
            # If any element caused an error, raise to signal overall failure for this expression
            raise TypeErrorFound()

        # All elements are valid and homogeneous arithmetic types
        return FoldedType.arithmetic_type(inferred_dim + 1)

    elif isinstance(expression, UniformArray):
        meta = expression.meta
        value_type = type_expression(
            expression.value, analysis_information)  # Raises on failure
        if value_type.is_template():
            add_report_and_raise(ReportCode.InvalidArrayType,
                                 meta, analysis_information)

        dim_type = type_expression(
            expression.dimension, analysis_information)  # Raises on failure
        dim_meta = expression.dimension.get_meta()
        if dim_type.is_template():
            add_report_and_raise(ReportCode.InvalidArraySizeT,
                                 dim_meta, analysis_information)
        elif dim_type.is_bus():
            add_report_and_raise(ReportCode.InvalidArraySizeB,
                                 dim_meta, analysis_information)
        elif dim_type.dim() != 0:
            add_report_and_raise(ReportCode.InvalidArraySize(
                dim_type.dim()), dim_meta, analysis_information)

        # If successful so far
        if value_type.bus is not None:
            return FoldedType.bus(value_type.bus, value_type.dim() + 1)
        else:
            return FoldedType.arithmetic_type(value_type.dim() + 1)

    elif isinstance(expression, InfixOp):
        lhe_type = type_expression(
            expression.lhe, analysis_information)  # Raises on failure
        rhe_type = type_expression(
            expression.rhe, analysis_information)  # Raises on failure

        error_occurred = False
        if lhe_type.is_template() or lhe_type.is_bus() or lhe_type.dim() > 0:
            add_report(ReportCode.InfixOperatorWithWrongTypes,
                       expression.lhe.get_meta(), reports, program_archive)
            error_occurred = True
        if rhe_type.is_template() or rhe_type.is_bus() or rhe_type.dim() > 0:
            add_report(ReportCode.InfixOperatorWithWrongTypes,
                       expression.rhe.get_meta(), reports, program_archive)
            error_occurred = True

        if error_occurred:
            raise TypeErrorFound()
        return FoldedType.arithmetic_type(0)

    elif isinstance(expression, PrefixOp):
        rhe_type = type_expression(
            expression.rhe, analysis_information)  # Raises on failure
        if rhe_type.is_template() or rhe_type.is_bus() or rhe_type.dim() > 0:
            add_report_and_raise(ReportCode.PrefixOperatorWithWrongTypes,
                                 expression.rhe.get_meta(), analysis_information)
        return FoldedType.arithmetic_type(0)

    elif isinstance(expression, ParallelOp):
        rhe_type = type_expression(
            expression.rhe, analysis_information)  # Raises on failure
        if not rhe_type.is_template():
            add_report_and_raise(ReportCode.ParallelOperatorWithWrongTypes,
                                 expression.rhe.get_meta(), analysis_information)
        return rhe_type  # Returns the template type

    elif isinstance(expression, InlineSwitchOp):
        cond_type: Optional[FoldedType] = None
        if_true_type: Optional[FoldedType] = None
        if_false_type: Optional[FoldedType] = None
        error_occurred = False

        try:
            cond_type = type_expression(expression.cond, analysis_information)
            cond_meta = expression.cond.get_meta()
            if cond_type.is_template():
                add_report(ReportCode.MustBeSingleArithmeticT,
                           cond_meta, reports, program_archive)
                error_occurred = True
            elif cond_type.is_bus():
                add_report(ReportCode.MustBeSingleArithmeticB,
                           cond_meta, reports, program_archive)
                error_occurred = True
            elif cond_type.dim() > 0:
                add_report(ReportCode.MustBeSingleArithmetic(
                    cond_type.dim()), cond_meta, reports, program_archive)
                error_occurred = True
        except TypeErrorFound:
            error_occurred = True  # Cond failed, but try typing branches

        try:
            if_true_type = type_expression(
                expression.if_true, analysis_information)
        except TypeErrorFound:
            error_occurred = True
            # Cannot determine return type if true branch fails
            raise TypeErrorFound("Cannot type true branch of inline switch")

        try:
            if_false_type = type_expression(
                expression.if_false, analysis_information)
        except TypeErrorFound:
            error_occurred = True
            # If false branch fails, we might still be able to return true_type if compatible
            # but the expression as a whole has an error.
            # For now, just mark error and let comparison fail if false_type is None
            if_false_type = None  # Mark as untyped

        # Compare branches if both typed successfully (even if cond failed)
        if if_true_type and if_false_type:
            if not FoldedType.same_type(if_true_type, if_false_type):
                add_report(ReportCode.NonCompatibleBranchTypes,
                           expression.if_false.get_meta(), reports, program_archive)
                error_occurred = True
        elif if_true_type and not if_false_type:
            # False branch failed typing, consider this incompatible
            error_occurred = True

        if error_occurred:
            raise TypeErrorFound()
        # If no errors, return the type of the branches (which must be the same)
        return if_true_type

    elif isinstance(expression, Variable):
        name = expression.name
        meta = expression.meta
        assert environment.has_symbol(
            name), f"Symbol {name} not found in environment (should be caught earlier?)"

        access_info = treat_access(
            expression.access, analysis_information)  # Raises on failure
        symbol_info = apply_access_to_symbol(
            name, meta, access_info, environment, reports, program_archive
        )  # Raises on failure

        # Convert SymbolInfoType back to FoldedType
        symbol_kind = symbol_info[0]
        symbol_data = symbol_info[1]

        if symbol_kind == "Component":
            possible_template = symbol_data  # Optional[str]
            if possible_template is not None:
                return FoldedType.template(possible_template)
            else:
                add_report_and_raise(
                    ReportCode.UninitializedSymbolInExpression, meta, analysis_information)
        elif symbol_kind == "Bus":
            possible_bus, dim = symbol_data  # Tuple[Optional[str], int]
            if possible_bus is not None:
                return FoldedType.bus(possible_bus, dim)
            else:
                add_report_and_raise(
                    ReportCode.UninitializedSymbolInExpression, meta, analysis_information)
        elif symbol_kind in ("Var", "Signal"):
            dim = symbol_data  # int
            return FoldedType.arithmetic_type(dim)
        elif symbol_kind == "Tag":
            return FoldedType.arithmetic_type(0)
        else:
            # Should be unreachable
            raise AssertionError(f"Unexpected symbol kind: {symbol_kind}")

    elif isinstance(expression, Call):
        call_id = expression.id
        meta = expression.meta
        analysis_information.reached.add(call_id)

        arg_types: Optional[List[FoldedType]] = None
        args_typed_successfully = False
        try:
            arg_types = type_array_of_expressions(
                expression.args, analysis_information)
            args_typed_successfully = True
        except TypeErrorFound:
            # Arguments failed, but if it's a template call, we might return the template type
            if program_archive.contains_template(call_id):
                return FoldedType.template(call_id)
            else:
                # If it's a function call and args failed, re-raise
                raise

        # Args typed successfully, now check argument validity
        concrete_types: List[ArithmeticType] = []
        invalid_arg_found = False
        for arg_expr, arg_type in zip(expression.args, arg_types):
            if arg_type.is_template():
                add_report(ReportCode.InvalidArgumentInCall,
                           arg_expr.get_meta(), reports, program_archive)
                invalid_arg_found = True
            # Note: Rust code doesn't check for bus arguments here, only in BusCall. Assume correct.
            concrete_types.append(arg_type.dim())

        # If invalid args found and it's a template call, return template type
        if invalid_arg_found and program_archive.contains_template(call_id):
            return FoldedType.template(call_id)
        # If invalid args found and it's a function call, raise
        elif invalid_arg_found:
            raise TypeErrorFound()

        # Arguments are valid, proceed with call typing
        previous_file_id = analysis_information.file_id
        new_environment: Optional[TypingEnvironment] = None
        target_file_id: Optional[FileID] = None

        try:
            # Determine target file id
            if program_archive.contains_function(call_id):
                target_file_id = program_archive.get_function_data(
                    call_id).get_file_id()
            elif program_archive.contains_template(call_id):
                target_file_id = program_archive.get_template_data(
                    call_id).get_file_id()
            else:
                # Should not happen if contains_template/contains_function are accurate
                raise AssertionError(
                    f"Call target {call_id} not found as function or template")

            analysis_information.file_id = target_file_id

            # Prepare environment
            new_environment = prepare_environment_for_call(
                meta, call_id, concrete_types, program_archive, reports
            )  # Raises on failure (e.g., wrong arg count)

            # Swap environment
            previous_environment = analysis_information.environment
            analysis_information.environment = new_environment

            # Type the body
            returned_type: FoldedType
            if program_archive.contains_function(call_id):
                # type_function returns ArithmeticType (dimension)
                return_dim = type_function(
                    call_id, concrete_types, meta, analysis_information)  # Raises on failure
                returned_type = FoldedType.arithmetic_type(return_dim)
            else:  # Template call
                # type_template returns template name (string)
                # Does not raise? Assumes success.
                template_name = type_template(
                    call_id, concrete_types, analysis_information)
                returned_type = FoldedType.template(template_name)

            return returned_type

        except TypeErrorFound:
            # If any step failed (env prep, body typing), and it's a template, maybe return template type?
            # Rust logic seems to return template type if initial arg typing fails OR env prep fails.
            if program_archive.contains_template(call_id):
                return FoldedType.template(call_id)
            else:
                raise  # Re-raise for function calls
        finally:
            # Restore environment and file_id regardless of success/failure inside
            if new_environment is not None:  # Only restore if swap occurred
                analysis_information.environment = previous_environment
            analysis_information.file_id = previous_file_id

    elif isinstance(expression, BusCall):
        bus_id = expression.id
        meta = expression.meta
        analysis_information.reached.add(bus_id)  # Track bus usage

        arg_types: Optional[List[FoldedType]] = None
        args_typed_successfully = False
        default_bus_type = FoldedType.bus(
            bus_id, 0)  # Default return if args fail
        if program_archive.contains_bus(bus_id):
            # Get actual expected fields count for default dimension?
            # Rust seems to default to 0 in FoldedType::bus if body typing fails
            # Let's use 0 for now.
            pass
            # field_count = len(program_archive.get_bus_data(bus_id).get_fields())
            # default_bus_type = FoldedType.bus(bus_id, field_count) # Use actual field count?

        try:
            arg_types = type_array_of_expressions(
                expression.args, analysis_information)
            args_typed_successfully = True
        except TypeErrorFound:
            if program_archive.contains_bus(bus_id):
                return default_bus_type  # Return default bus type if args fail
            else:
                # Bus doesn't exist, error should be caught elsewhere?
                # For now, re-raise.
                raise

        # Args typed, check validity
        concrete_types: List[ArithmeticType] = []
        invalid_arg_found = False
        for arg_expr, arg_type in zip(expression.args, arg_types):
            arg_meta = arg_expr.get_meta()
            if arg_type.is_template():
                add_report(ReportCode.InvalidArgumentInBusInstantiationT,
                           arg_meta, reports, program_archive)
                invalid_arg_found = True
            elif arg_type.is_bus():
                add_report(ReportCode.InvalidArgumentInBusInstantiationB,
                           arg_meta, reports, program_archive)
                invalid_arg_found = True
            concrete_types.append(arg_type.dim())

        if invalid_arg_found:
            if program_archive.contains_bus(bus_id):
                return default_bus_type  # Return default bus type if args invalid
            else:
                raise TypeErrorFound()  # Raise if bus doesn't exist anyway

        # Args valid, proceed
        previous_file_id = analysis_information.file_id
        new_environment: Optional[TypingEnvironment] = None
        target_file_id: Optional[FileID] = None

        try:
            if not program_archive.contains_bus(bus_id):
                # This should ideally be caught earlier, maybe during parsing/name resolution
                raise AssertionError(
                    f"Bus {bus_id} not found in program archive.")

            target_file_id = program_archive.get_bus_data(bus_id).get_file_id()
            analysis_information.file_id = target_file_id

            new_environment = prepare_environment_for_call(
                meta, bus_id, concrete_types, program_archive, reports
            )  # Raises on failure

            previous_environment = analysis_information.environment
            analysis_information.environment = new_environment

            # Type the bus body (initialization block)
            # Returns FoldedType, Raises on failure
            returned_type = type_bus(
                bus_id, concrete_types, analysis_information)

            return returned_type

        except TypeErrorFound:
            # If body typing fails, return default bus type
            if program_archive.contains_bus(bus_id):
                return default_bus_type
            else:
                raise  # Should be unreachable if contains_bus check passed
        finally:
            if new_environment is not None:
                analysis_information.environment = previous_environment
            analysis_information.file_id = previous_file_id

    # elif isinstance(expression, AnonymousCall):
    #     # Rust code says unreachable!()
    #     raise AssertionError("Anonymous calls should not be reachable at this point.")

    else:
        # Should not happen if all expression types are covered
        raise NotImplementedError(
            f"Unhandled expression type: {type(expression)}")


# --- Helper Functions ---

def treat_sequence_of_statements(stmts: List[Statement], analysis_information: AnalysisInformation):
    error_occurred = False
    for stmt in stmts:
        try:
            type_statement(stmt, analysis_information)
        except TypeErrorFound:
            error_occurred = True  # Mark error but continue processing sequence
    if error_occurred:
        # Propagate the failure after processing all statements in the sequence
        raise TypeErrorFound()


# 0: symbol dimensions accessed
# 1: Optional List of (Name accessed, dimensions accessed in that name)
AccessInfo = Tuple[ArithmeticType, Optional[List[Tuple[str, ArithmeticType]]]]


def treat_access(accesses: List[Access], analysis_information: AnalysisInformation) -> AccessInfo:
    symbol_dim_accessed: ArithmeticType = 0
    # Using list to preserve order
    component_access_path: Optional[List[Tuple[str, ArithmeticType]]] = None
    error_occurred = False

    for access in accesses:
        if isinstance(access, ArrayAccess):
            index_expr = access.index  # Adjust attribute name if needed
            index_meta = index_expr.get_meta()
            try:
                index_type = type_expression(index_expr, analysis_information)
                if index_type.is_template():
                    add_report(ReportCode.InvalidArraySizeT, index_meta,
                               analysis_information.reports, analysis_information.program_archive)
                    error_occurred = True
                elif index_type.is_bus():
                    add_report(ReportCode.InvalidArraySizeB, index_meta,
                               analysis_information.reports, analysis_information.program_archive)
                    error_occurred = True
                elif index_type.dim() > 0:
                    add_report(ReportCode.InvalidArraySize(index_type.dim(
                    )), index_meta, analysis_information.reports, analysis_information.program_archive)
                    error_occurred = True
                # Only update counts if type check passed (or partially if needed?)
                # Rust updates counts regardless of index type error. Let's mimic that.

                if component_access_path is not None and component_access_path:
                    # Increment dimension count of the last component access
                    last_name, last_dim = component_access_path.pop()
                    component_access_path.append((last_name, last_dim + 1))
                else:
                    symbol_dim_accessed += 1

            except TypeErrorFound:
                error_occurred = True
                # Still update counts like Rust? Seems reasonable.
                if component_access_path is not None and component_access_path:
                    last_name, last_dim = component_access_path.pop()
                    component_access_path.append((last_name, last_dim + 1))
                else:
                    symbol_dim_accessed += 1

        elif isinstance(access, ComponentAccess):
            name = access.name  # Adjust attribute name if needed
            if component_access_path is None:
                component_access_path = []
            # Start with 0 dimensions accessed for this part
            component_access_path.append((name, 0))

        else:
            raise NotImplementedError(f"Unhandled access type: {type(access)}")

    if error_occurred:
        # Raise even if counts were updated, signal overall failure
        raise TypeErrorFound()

    return symbol_dim_accessed, component_access_path


def check_if_it_is_a_tag(
    symbol: str,
    meta: Meta,
    access_info: AccessInfo,
    environment: TypingEnvironment,
    reports: ReportCollection,
    program_archive: ProgramArchive
) -> bool:
    # Simplified Python translation - This function is complex and depends heavily
    # on the exact methods of ProgramArchive and Environment.
    # Returning False as a placeholder. A full translation requires detailed logic.
    # The Rust code checks the access path against bus/template definitions recursively.

    symbol_dim_accessed, component_access_path = access_info
    if not component_access_path:
        return False  # No component access means cannot be a tag access via .

    # --- Start of complex logic simulation ---
    current_name = symbol
    current_dim = 0
    current_tags: Set[str] = set()
    # Represents WireType::Signal or WireType::Bus(...)
    current_wire_type: Optional[Any] = None
    # Track if source is input of subcomponent
    current_source_is_subcomponent_input = False

    # 1. Determine initial type (component, bus, signal) and dimensions/tags
    if environment.has_component(symbol):
        comp_info = environment.get_component(symbol)  # (Optional[str], int)
        if not comp_info or comp_info[0] is None:
            # Component exists but not initialized, cannot access tags yet
            add_report(ReportCode.UninitializedComponent, meta, reports,
                       program_archive)  # Or maybe UninitializedSymbol?
            raise TypeErrorFound()
        template_name = comp_info[0]
        template_dim = comp_info[1]

        if template_dim != symbol_dim_accessed:
            # Accessing component partially before signal/bus access
            add_report(ReportCode.InvalidPartialArray, meta, reports,
                       program_archive)  # Or InvalidArrayAccess?
            raise TypeErrorFound()

        # Now look at the first element of component_access_path
        if not component_access_path:
            return False  # Should have been caught

        accessed_element, accessed_dims_in_element = component_access_path[0]
        template_data = program_archive.get_template_data(template_name)
        input_info = template_data.get_input_info(accessed_element)
        output_info = template_data.get_output_info(accessed_element)

        wire_data = input_info or output_info
        if not wire_data:
            add_report(ReportCode.InvalidSignalAccess,
                       meta, reports, program_archive)
            raise TypeErrorFound()

        current_wire_type = wire_data.get_type()
        current_tags = wire_data.get_tags()  # Assume returns set
        current_dim = wire_data.get_dimension()  # Dimension of the signal/bus itself
        current_source_is_subcomponent_input = (input_info is not None)

        # Check dimension access for this first element
        if accessed_dims_in_element > current_dim:
            add_report(ReportCode.InvalidArrayAccess(
                current_dim, accessed_dims_in_element), meta, reports, program_archive)
            raise TypeErrorFound()
        current_dim -= accessed_dims_in_element  # Remaining dimensions

        path_index = 1  # Start next check from the second element

    elif environment.has_bus(symbol):
        # (Optional[str], int, list[str])
        bus_info = environment.get_bus(symbol)
        if not bus_info or bus_info[0] is None:
            add_report(ReportCode.UninitializedSymbolInExpression,
                       meta, reports, program_archive)  # Or InvalidTagAccess?
            raise TypeErrorFound()
        bus_name = bus_info[0]
        bus_dim = bus_info[1]
        bus_tags = set(bus_info[2])

        if symbol_dim_accessed > bus_dim:
            add_report(ReportCode.InvalidArrayAccess(
                bus_dim, symbol_dim_accessed), meta, reports, program_archive)
            raise TypeErrorFound()

        current_wire_type = WireType.Bus(
            bus_name)  # Assume WireType.Bus exists
        current_tags = bus_tags
        current_dim = bus_dim - symbol_dim_accessed
        path_index = 0  # Start check from the first element of component_access_path

    elif environment.has_signal(symbol):
        sig_info = environment.get_signal(symbol)  # (int, list[str])
        sig_dim = sig_info[0]
        sig_tags = set(sig_info[1])

        if symbol_dim_accessed > sig_dim:
            add_report(ReportCode.InvalidArrayAccess(
                sig_dim, symbol_dim_accessed), meta, reports, program_archive)
            raise TypeErrorFound()

        current_wire_type = WireType.Signal  # Assume WireType.Signal exists
        current_tags = sig_tags
        current_dim = sig_dim - symbol_dim_accessed
        path_index = 0  # Start check from the first element of component_access_path

    else:
        # If it's a variable, it cannot have tags accessed via '.'
        return False

    # 2. Traverse the remaining component_access_path
    total_dims_accessed_in_path = 0
    last_element_dims_accessed = 0

    while path_index < len(component_access_path):
        accessed_element, accessed_dims_in_element = component_access_path[path_index]
        total_dims_accessed_in_path += accessed_dims_in_element
        last_element_dims_accessed = accessed_dims_in_element  # Keep track for final check

        if isinstance(current_wire_type, WireType.Signal):
            # Can only access tags from a signal
            if accessed_element in current_tags:
                # Found a tag
                if path_index == len(component_access_path) - 1:
                    # This is the last element of the access path
                    if current_dim == 0 and accessed_dims_in_element == 0:
                        # Check if it's an input tag being accessed externally
                        if current_source_is_subcomponent_input:
                            add_report(
                                ReportCode.InputTagCannotBeAccessedOutside, meta, reports, program_archive)
                            raise TypeErrorFound()
                        else:
                            return True  # Valid tag access
                    elif current_dim > 0 or accessed_dims_in_element > 0:
                        # Tried to access tag with array index (e.g., signal[i].tag or signal.tag[i])
                        add_report(ReportCode.InvalidTagAccessAfterArray,
                                   meta, reports, program_archive)
                        raise TypeErrorFound()
                    else:  # current_dim == 0 and accessed_dims_in_element == 0
                        # This case seems covered above, but include for completeness
                        return True  # Valid tag access (unless input tag)
                else:
                    # Found a tag, but it's not the last element in the path (e.g., signal.tag.something)
                    # Or a more specific error?
                    add_report(ReportCode.InvalidTagAccess,
                               meta, reports, program_archive)
                    raise TypeErrorFound()
            else:
                # Accessed something from a signal that isn't a known tag
                add_report(ReportCode.InvalidTagAccess, meta, reports,
                           program_archive)  # Or InvalidSignalAccess?
                raise TypeErrorFound()

        elif isinstance(current_wire_type, WireType.Bus):
            bus_name = current_wire_type.name  # Adjust access
            bus_data = program_archive.get_bus_data(bus_name)
            field_info = bus_data.get_field_info(accessed_element)

            if field_info:
                # Accessed a valid field in the bus
                current_wire_type = field_info.get_type()
                current_tags = field_info.get_tags()
                field_dim = field_info.get_dimension()

                if accessed_dims_in_element > field_dim:
                    add_report(ReportCode.InvalidArrayAccess(
                        field_dim, accessed_dims_in_element), meta, reports, program_archive)
                    raise TypeErrorFound()
                current_dim = field_dim - accessed_dims_in_element

                if path_index == len(component_access_path) - 1:
                    # Last element is a valid field, not a tag
                    return False
                # Continue to the next element in the path

            elif accessed_element in current_tags:
                # Accessed a tag defined for this bus
                if path_index == len(component_access_path) - 1:
                    # This tag is the last element
                    if current_dim == 0 and accessed_dims_in_element == 0:
                        # Check if it's an input tag being accessed externally
                        if current_source_is_subcomponent_input:
                            add_report(
                                ReportCode.InputTagCannotBeAccessedOutside, meta, reports, program_archive)
                            raise TypeErrorFound()
                        else:
                            return True  # Valid tag access
                    elif current_dim > 0 or accessed_dims_in_element > 0:
                        add_report(ReportCode.InvalidTagAccessAfterArray,
                                   meta, reports, program_archive)
                        raise TypeErrorFound()
                    else:
                        return True  # Valid tag access (unless input tag)
                else:
                    # Found tag, but not the last element
                    add_report(ReportCode.InvalidTagAccess,
                               meta, reports, program_archive)
                    raise TypeErrorFound()
            else:
                # Accessed name is neither a field nor a tag in the bus
                # Use InvalidSignalAccessInBus or a general InvalidTagAccess?
                add_report(ReportCode.InvalidTagAccess, meta, reports,
                           program_archive)  # Or InvalidSignalAccess?
                raise TypeErrorFound()
        else:
            # Should be unreachable if current_wire_type is always Signal or Bus
            raise AssertionError("Unexpected wire type during tag check")

        path_index += 1

    # If the loop finishes, it means the last element was a field, not a tag
    return False


def apply_access_to_symbol(
    symbol: str,
    meta: Meta,
    access_info: AccessInfo,
    environment: TypingEnvironment,
    reports: ReportCollection,
    program_archive: ProgramArchive
) -> SymbolInfoType:
    # Check if it's a tag access first
    if check_if_it_is_a_tag(symbol, meta, access_info, environment, reports, program_archive):
        return ("Tag", None)

    # Not a tag, proceed with normal symbol type resolution + access application
    symbol_dim_accessed, component_access_path = access_info

    current_symbol_name = symbol
    current_dim: ArithmeticType = 0
    current_type_name: Optional[str] = None  # For template or bus name
    current_tags: List[str] = []  # For signals/buses defined in env
    is_component = False
    is_bus = False
    is_signal = False
    is_var = False

    # 1. Get base symbol info from environment
    if environment.has_component(symbol):
        is_component = True
        comp_info = environment.get_component(symbol)  # (Optional[str], int)
        current_type_name, current_dim = comp_info
    elif environment.has_bus(symbol):
        is_bus = True
        # (Optional[str], int, list[str])
        bus_info = environment.get_bus(symbol)
        current_type_name, current_dim, current_tags = bus_info
    elif environment.has_signal(symbol):
        is_signal = True
        sig_info = environment.get_signal(symbol)  # (int, list[str])
        current_dim, current_tags = sig_info
        current_type_name = None  # Signals don't have a type name like templates/buses
    elif environment.has_variable(symbol):
        is_var = True
        current_dim = environment.get_variable(symbol)  # int
        current_type_name = None
        current_tags = []
    else:
        # Should be caught earlier by has_symbol check
        raise AssertionError(
            f"Symbol {symbol} not found in environment during access application.")

    # 2. Apply initial array access (symbol_dim_accessed)
    if symbol_dim_accessed > current_dim:
        add_report_and_raise(ReportCode.InvalidArrayAccess(
            current_dim, symbol_dim_accessed), meta, analysis_information)
    current_dim -= symbol_dim_accessed

    # 3. Process component access path (.) if it exists
    if component_access_path:
        if is_var:
            # Cannot use . access on a simple variable
            add_report_and_raise(ReportCode.InvalidSignalAccess,
                                 meta, analysis_information)  # Or different code?

        if is_component and current_type_name is None:
            # Trying to access signal/bus of uninitialized component
            add_report_and_raise(
                ReportCode.UninitializedComponent, meta, analysis_information)

        if is_component and current_dim > 0:
            # Cannot use . access after partial array access of component array
            # e.g., comp[i].signal is invalid if comp is array of components
            # This differs slightly from Rust check, which seemed to allow it if len==1? Revisit.
            # Let's assume InvalidPartialArray is appropriate here too.
            add_report_and_raise(
                ReportCode.InvalidPartialArray, meta, analysis_information)

        # --- Traverse the path ---
        wire_type_obj: Optional[Any] = None  # Holds WireType instance
        # Start with env tags if bus/signal
        wire_tags: Set[str] = set(current_tags)

        if is_component:
            # Look up the first element in the template definition
            template_name = current_type_name
            template_data = program_archive.get_template_data(template_name)
            accessed_element, accessed_dims = component_access_path[0]

            input_info = template_data.get_input_info(accessed_element)
            output_info = template_data.get_output_info(accessed_element)
            wire_data = input_info or output_info

            if not wire_data:
                # Check if it's a tag defined directly on the component? (Unlikely based on grammar)
                # Assume it's an invalid access
                add_report_and_raise(
                    ReportCode.InvalidSignalAccess, meta, analysis_information)

            wire_type_obj = wire_data.get_type()
            wire_tags = wire_data.get_tags()
            defined_dim = wire_data.get_dimension()

            if accessed_dims > defined_dim:
                add_report_and_raise(ReportCode.InvalidArrayAccess(
                    defined_dim, accessed_dims), meta, analysis_information)
            current_dim = defined_dim - accessed_dims
            path_index = 1

        elif is_bus:
            # Start with the base bus type
            wire_type_obj = WireType.Bus(current_type_name)
            # current_dim already adjusted for symbol_dim_accessed
            path_index = 0
        elif is_signal:
            wire_type_obj = WireType.Signal
            # current_dim already adjusted for symbol_dim_accessed
            path_index = 0

        # --- Loop through remaining path ---
        while path_index < len(component_access_path):
            accessed_element, accessed_dims = component_access_path[path_index]

            # Cannot apply further . access if current element is an array and partially accessed
            if current_dim > 0:
                # Unless it's the very last element AND it's a tag access? Tag check handled this.
                # So, if current_dim > 0 here, it's an error.
                # Or InvalidArrayAccess?
                add_report_and_raise(
                    ReportCode.InvalidPartialArray, meta, analysis_information)

            if isinstance(wire_type_obj, WireType.Signal):
                # Cannot chain . access after a signal (unless it was a tag, handled by check_if_it_is_a_tag)
                add_report_and_raise(
                    ReportCode.InvalidSignalAccess, meta, analysis_information)

            elif isinstance(wire_type_obj, WireType.Bus):
                bus_name = wire_type_obj.name  # Adjust access
                bus_data = program_archive.get_bus_data(bus_name)
                field_info = bus_data.get_field_info(accessed_element)

                if not field_info:
                    # Not a field. Tag check already happened. Invalid access.
                    # Or InvalidSignalAccessInBus?
                    add_report_and_raise(
                        ReportCode.InvalidTagAccess, meta, analysis_information)

                # It's a valid field
                wire_type_obj = field_info.get_type()
                wire_tags = field_info.get_tags()
                defined_dim = field_info.get_dimension()

                if accessed_dims > defined_dim:
                    add_report_and_raise(ReportCode.InvalidArrayAccess(
                        defined_dim, accessed_dims), meta, analysis_information)
                current_dim = defined_dim - accessed_dims

            else:
                # Should be Signal or Bus
                raise AssertionError(
                    "Unexpected wire type during access path traversal")

            path_index += 1

        # --- End of path traversal ---
        # Determine final type based on the final wire_type_obj
        if isinstance(wire_type_obj, WireType.Signal):
            return ("Signal", current_dim)
        elif isinstance(wire_type_obj, WireType.Bus):
            bus_name = wire_type_obj.name
            return ("Bus", (bus_name, current_dim))
        else:
            # Path was processed, but ended on something unexpected?
            raise AssertionError("Access path ended on unexpected type")

    else:
        # No component access path (.), return type based on initial symbol info
        if is_component:
            # Needs full array access if array, otherwise just the template name
            if current_dim > 0:
                add_report_and_raise(
                    ReportCode.InvalidPartialArray, meta, analysis_information)
            # current_type_name is Optional[str]
            return ("Component", current_type_name)
        elif is_bus:
            # current_type_name is Optional[str]
            return ("Bus", (current_type_name, current_dim))
        elif is_signal:
            return ("Signal", current_dim)
        elif is_var:
            return ("Var", current_dim)
        else:
            raise AssertionError("Unreachable state")


def type_array_of_expressions(expressions: List[Expression], analysis_information: AnalysisInformation) -> List[FoldedType]:
    types: List[FoldedType] = []
    error_occurred = False
    for expr in expressions:
        try:
            types.append(type_expression(expr, analysis_information))
        except TypeErrorFound:
            error_occurred = True
            # Add a placeholder to keep list length consistent if needed downstream?
            # Or just stop? Let's stop and raise immediately.
            raise  # Re-raise the TypeErrorFound

    # If loop completes without error
    return types


def prepare_environment_for_call(
    meta: Meta,
    call_id: str,
    args_dims: List[ArithmeticType],
    program_archive: ProgramArchive,
    reports: ReportCollection
) -> TypingEnvironment:
    args_names: List[str] = []
    if program_archive.contains_function(call_id):
        args_names = program_archive.get_function_data(
            call_id).get_name_of_params()
    elif program_archive.contains_template(call_id):
        args_names = program_archive.get_template_data(
            call_id).get_name_of_params()
    elif program_archive.contains_bus(call_id):
        args_names = program_archive.get_bus_data(call_id).get_name_of_params()
    else:
        # This should be caught before calling prepare_environment...
        raise AssertionError(f"Target {call_id} not found in program archive")

    if len(args_dims) != len(args_names):
        error_code = ReportCode.WrongNumberOfArguments(
            len(args_names), len(args_dims))
        # Need to use add_report and raise custom exception
        add_report(error_code, meta, reports, program_archive)
        raise TypeErrorFound()  # Signal the error

    # Create a new environment instance for the call scope
    new_environment = CircomEnvironment()  # Assuming a fresh instance is needed
    for name, dim in zip(args_names, args_dims):
        # Add call arguments as variables
        new_environment.add_variable(name, dim)

    return new_environment

# --- Template, Bus, Function Typing ---


def type_template(
    call_id: str,
    args_dims: List[ArithmeticType],
    analysis_information: AnalysisInformation
) -> str:
    program_archive = analysis_information.program_archive
    assert program_archive.contains_template(call_id)

    # Use tuple for cache key as lists aren't hashable
    instance_key = (call_id, tuple(args_dims))

    if analysis_information.registered_calls.get_instance(instance_key) is None:
        # Mark as visited *before* processing body to handle recursion
        # Value (0) is arbitrary for templates, not used like function return dim
        analysis_information.registered_calls.add_instance(instance_key, 0)

        stmts = program_archive.get_template_data(call_id).get_body_as_vec()
        try:
            # Environment should already be swapped at the call site
            treat_sequence_of_statements(stmts, analysis_information)
        except TypeErrorFound:
            # Errors within the template body were reported.
            # Still return the template name as the 'type'.
            pass  # Don't propagate the exception out of template typing itself

    return call_id  # Return the template name as its type identifier


def type_bus(
    bus_id: str,
    args_dims: List[ArithmeticType],
    analysis_information: AnalysisInformation
) -> FoldedType:
    program_archive = analysis_information.program_archive
    assert program_archive.contains_bus(bus_id)

    instance_key = (bus_id, tuple(args_dims))
    if analysis_information.registered_calls.get_instance(instance_key) is None:
        analysis_information.registered_calls.add_instance(
            instance_key, 0)  # Value 0 is placeholder
        stmts = program_archive.get_bus_data(bus_id).get_body_as_vec()
        try:
            # Environment already swapped at call site
            treat_sequence_of_statements(stmts, analysis_information)
        except TypeErrorFound:
            # Errors reported within, still return the bus type
            pass

    # Determine dimension based on fields? Rust returns FoldedType::bus(id, 0)
    # Let's stick to returning dim 0 for the bus type itself, consistent with FoldedType::bus
    # The dimension check happens during assignment/usage based on apply_access_to_symbol
    return FoldedType.bus(bus_id, 0)


def type_function(
    call_id: str,
    args_dims: List[ArithmeticType],
    meta: Meta,  # Meta of the call site for error reporting
    analysis_information: AnalysisInformation
) -> ArithmeticType:
    program_archive = analysis_information.program_archive
    assert program_archive.contains_function(call_id)

    instance_key = (call_id, tuple(args_dims))
    cached_instance = analysis_information.registered_calls.get_instance(
        instance_key)
    if cached_instance is not None:
        # TODO: Check for recursive calls currently being processed? Rust register might handle this.
        # Assuming get_instance returns obj with returns()
        return cached_instance.returns()

    # Function signature typing (external, e.g., from C++ definitions)
    # Assuming program_archive provides access to this, not just the AST body
    # And type_given_function handles this external check.
    # Need to pass necessary info (like all function signatures) to type_given_function.
    all_functions_data = program_archive.get_functions()  # Assume method exists
    given_type: Optional[ArithmeticType] = type_given_function(
        call_id, all_functions_data, args_dims)

    if given_type is None:
        # If signature typing fails (e.g., no definition, arg mismatch in definition)
        add_report_and_raise(ReportCode.UnableToTypeFunction,
                             meta, analysis_information)

    # Mark as visited *before* processing body
    analysis_information.registered_calls.add_instance(
        instance_key, given_type)

    # Type check the function body AST
    stmts = program_archive.get_function_data(call_id).get_body_as_vec()
    previous_return_type = analysis_information.return_type
    # Set expected return type for 'return' statements
    analysis_information.return_type = given_type

    try:
        # Environment already swapped at call site
        treat_sequence_of_statements(stmts, analysis_information)
    except TypeErrorFound:
        # Errors reported within the function body.
        # Still return the 'given_type' based on the signature check.
        pass  # Don't propagate exception out of function typing itself
    finally:
        # Restore previous return type context
        analysis_information.return_type = previous_return_type

    # Return the dimension determined by the function's signature
    return given_type
