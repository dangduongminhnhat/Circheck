from __future__ import annotations
from dataclasses import dataclass, fields
from typing import Optional, List, Tuple
from abc import ABC, abstractmethod
from Visitor import Visitor
from antlr4 import Token


class AST(ABC):
    # @abstractmethod
    # def accept(self, v: Visitor, param):
    #     return v.visit(self, param)

    def __str__(self, indent: str = "", is_last: bool = True):
        label = self.__class__.__name__
        branch = "└── " if is_last else "├── "
        output = [f"{indent}{branch}{label}"]
        indent += "    " if is_last else "│   "

        for i, field in enumerate(fields(self)):
            value = getattr(self, field.name)
            is_last_field = i == len(fields(self)) - 1
            branch = "└── " if is_last_field else "├── "
            line = f"{indent}{branch}{field.name}:"

            if isinstance(value, AST):
                output.append(line)
                output.append(value.__str__(
                    indent + ("    " if is_last_field else "│   "), True))
            elif isinstance(value, list):
                output.append(line)
                for j, item in enumerate(value):
                    is_last_item = j == len(value) - 1
                    if isinstance(item, AST):
                        output.append(item.__str__(
                            indent + ("    " if is_last_field else "│   "), is_last_item))
                    else:
                        branch = "└── " if is_last_item else "├── "
                        output.append(f"{indent}    {branch}{item}")
            else:
                output.append(f"{line} {value}")

        return "\n".join(output)


class Expression(AST):
    pass


class Definition(AST):
    pass


class Statement(AST):
    pass


class VariableType(AST):
    pass


class Access(AST):
    pass


class LogArgument(AST):
    pass


@dataclass
class FileLocation(AST):
    start: Token
    stop: Token

    def __str__(self, indent: str = "", is_last: bool = True):
        label = self.__class__.__name__
        branch = "└── " if is_last else "├── "
        output = [f"{indent}{branch}{label}"]
        indent += "    " if is_last else "│   "

        start_line = self.start.line
        start_column = self.start.column
        output.append(
            f"{indent}├── start: line {start_line}, column {start_column}")
        stop_line = self.stop.line
        stop_column = self.stop.column
        output.append(
            f"{indent}└── stop: line {stop_line}, column {stop_column}")

        return "\n".join(output)

    # def accept(self, v: Visitor, param):
    #     return v.visitFileLocation(self, param)


@dataclass
class MainComponent(AST):
    locate: FileLocation
    publics: List[str]
    expr: Expression

    # def accept(self, v: Visitor, param):
    #     return v.visitMainComponent(self, param)


@dataclass
class Include(AST):
    locate: FileLocation
    path: str

    # def accept(self, v: Visitor, param):
    #     return v.visitInclude(self, param)


@dataclass
class Program(AST):
    locate: FileLocation
    compile_version: Optional[Tuple[int, int, int]]
    custom_gates: bool
    custom_gates_declare: bool
    includes: List[Include]
    definitions: List[Definition]
    main_component: Optional[MainComponent]

    # def accept(self, v: Visitor, param):
    #     return v.visitProgram(self, param)


@dataclass
class Template(Definition):
    locate: FileLocation
    name_field: str
    args: List[str]
    body: Statement
    parallel: bool
    is_custom_gate: bool

    # def accept(self, v, param):
    #     return v.visitTemplate(self, param)


@dataclass
class Function(Definition):
    locate: FileLocation
    name_field: str
    args: List[str]
    body: Statement

    # def accept(self, v, param):
    #     return v.visitFunction(self, param)


@dataclass
class IfThenElse(Statement):
    locate: FileLocation
    cond: Expression
    if_case: Statement
    else_case: Optional[Statement]


@dataclass
class While(Statement):
    locate: FileLocation
    cond: Expression
    stmt: Statement


@dataclass
class Return(Statement):
    locate: FileLocation
    value: Expression


@dataclass
class InitializationBlock(Statement):
    locate: FileLocation
    xtype: VariableType
    initializations: List[Statement]


@dataclass
class Declaration(Statement):
    locate: FileLocation
    xtype: VariableType
    name: str
    dimensions: List[Expression]
    is_constant: bool


@dataclass
class Substitution(Statement):
    locate: FileLocation
    var: str
    access: List[Access]
    op: str
    rhe: Expression


@dataclass
class MultiSubstitution(Statement):
    locate: FileLocation
    lhe: Expression
    op: str
    rhe: Expression


@dataclass
class ConstraintEquality(Statement):
    locate: FileLocation
    lhe: Expression
    rhe: Expression


@dataclass
class LogCall(Statement):
    locate: FileLocation
    args: List[LogArgument]


@dataclass
class Block(Statement):
    locate: FileLocation
    stmts: List[Statement]


@dataclass
class Assert(Statement):
    locate: FileLocation
    arg: Expression


@dataclass
class Var(VariableType):
    pass


@dataclass
class Signal(VariableType):
    locate: FileLocation
    signal_type: str
    tag_list: List[str]


@dataclass
class Component(VariableType):
    pass


@dataclass
class AnonymousComponent(VariableType):
    pass


@dataclass
class InfixOp(Expression):
    locate: FileLocation
    lhe: Expression
    infix_op: str
    rhe: Expression


@dataclass
class PrefixOp(Expression):
    locate: FileLocation
    prefix_op: str
    rhe: Expression


@dataclass
class InlineSwitchOp(Expression):
    locate: FileLocation
    cond: Expression
    if_true: Expression
    if_false: Expression


@dataclass
class ParallelOp(Expression):
    locate: FileLocation
    rhe: Expression


@dataclass
class Variable(Expression):
    locate: FileLocation
    name: str
    access: List[Access]


@dataclass
class Number(Expression):
    locate: FileLocation
    value: int


@dataclass
class Call(Expression):
    locate: FileLocation
    id: str
    args: List[Expression]


@dataclass
class AnonymousComponentExpr(Expression):
    locate: FileLocation
    id: str
    is_parallel: bool
    params: List[Expression]
    signals: List[Expression]
    names: Optional[List[Tuple[str, str]]]


@dataclass
class ArrayInLine(Expression):
    locate: FileLocation
    values: List[Expression]


@dataclass
class TupleExpr(Expression):
    locate: FileLocation
    values: List[Expression]


@dataclass
class ComponentAccess(Access):
    locate: FileLocation
    name: str


@dataclass
class ArrayAccess(Access):
    locate: FileLocation
    expr: Expression


@dataclass
class LogStr(LogArgument):
    locate: FileLocation
    value: str


@dataclass
class LogExp(LogArgument):
    locate: FileLocation
    expr: Expression
