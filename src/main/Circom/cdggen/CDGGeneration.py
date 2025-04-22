from typing import Union
from CDG import *
from Visitor import *
from Errors import *
from AST import *
from Report import Report, ReportType
from StaticCheck import *


# Define the prime modulus p used in Circom field arithmetic
p = 21888242871839275222246405745257275088548364400416034343698204186575808495617


def val(z: int) -> int:
    """Definition of val(z) function used for relational operators."""
    if z >= (p // 2 + 1):
        return z - p
    return z


def mod(x: int) -> int:
    return x % p


def circom_add(a: int, b: int) -> int:
    return (a + b) % p


def circom_sub(a: int, b: int) -> int:
    return (a - b) % p


def circom_mul(a: int, b: int) -> int:
    return (a * b) % p


def circom_pow(a: int, b: int) -> int:
    return pow(a, b, p)


def circom_div(a: int, b: int) -> int:
    return (a * pow(b, -1, p)) % p


def circom_int_div(a: int, b: int) -> int:
    return (a // b) % p


def circom_mod(a: int, b: int) -> int:
    return (a % b) % p


def circom_eq(a: int, b: int) -> bool:
    return mod(a) == mod(b)


def circom_neq(a: int, b: int) -> bool:
    return mod(a) != mod(b)


def circom_lt(a: int, b: int) -> bool:
    return val(mod(a)) < val(mod(b))


def circom_leq(a: int, b: int) -> bool:
    return val(mod(a)) <= val(mod(b))


def circom_gt(a: int, b: int) -> bool:
    return val(mod(a)) > val(mod(b))


def circom_geq(a: int, b: int) -> bool:
    return val(mod(a)) >= val(mod(b))


def circom_and(a: bool, b: bool) -> bool:
    return a and b


def circom_or(a: bool, b: bool) -> bool:
    return a or b


def circom_not(a: bool) -> bool:
    return not a


def circom_bitand(a: int, b: int) -> int:
    return mod(a) & mod(b)


def circom_bitor(a: int, b: int) -> int:
    return mod(a) | mod(b)


def circom_bitxor(a: int, b: int) -> int:
    return mod(a) ^ mod(b)


def circom_bitnot(a: int) -> int:
    b = p.bit_length()
    mask = (1 << b) - 1
    return (~a) & mask


def circom_shr(a: int, k: int) -> int:
    if 0 <= k <= p // 2:
        return a // (2 ** k)
    else:
        return circom_shl(a, p - k)


def circom_shl(a: int, k: int) -> int:
    b = p.bit_length()
    mask = (1 << b) - 1
    if 0 <= k <= p // 2:
        return ((a * (2 ** k)) & mask) % p
    else:
        return circom_shr(a, p - k)


def circom_cond(condition: bool, true_val: Union[int, bool], false_val: Union[int, bool]) -> Union[int, bool]:
    return true_val if condition else false_val


class CDGGeneration(BaseVisitor):
    def __init__(self, ast: AST, param):
        self.graphs = {}
        self.remaining = {}
        self.ast = ast
        self.in_template = False

    def visitFileLocation(self, ast: FileLocation, param):
        return None

    def visitMainComponent(self, param):
        return None

    def visitInclude(self, ast: Include, param):
        return None

    def visitTemplate(self, param):
        return None

    def visitFunction(self, param):
        return None

    def visitProgram(self, ast: Program, param):
        return None

    def visitIfThenElse(self, param):
        return None

    def visitWhile(self, param):
        return None

    def visitReturn(self, ast: Return, param):
        return None

    def visitInitializationBlock(self, ast: InitializationBlock, param):
        for stmt in ast.initializations:
            self.visit(stmt, param)

    def visitDeclaration(self, ast: Declaration, param):
        TypeCheck(ast).visit(ast, param["env"])
        xtype = self.visit(ast.xtype)

    def visitSubstitution(self, param):
        return None

    def visitMultiSubstitution(self, param):
        return None

    def visitConstraintEquality(self, param):
        return None

    def visitLogCall(self, ast: LogCall, param):
        return None

    def visitBlock(self, ast: Block, param):
        env = param["env"]
        if self.in_template:
            self.in_template = False
        else:
            param["env"] = [{}] + env
        for stmt in ast.stmts:
            self.visit(stmt, param)
        param["env"] = env

    def visitAssert(self, ast: Assert, param):
        return None

    def visitVar(self, ast: Var, param):
        return VarCircom()

    def visitSignal(self, ast: Signal, param):
        if ast.signal_type == "input":
            signal_type = SignalType.INPUT
        elif ast.signal_type == "output":
            signal_type = SignalType.OUTPUT
        elif ast.signal_type == "intermediate":
            signal_type = SignalType.INTERMEDIATE
        return SignalCircom(signal_type)

    def visitComponent(self, ast: Component, param):
        return ComponentCircom()

    def visitAnonymousComponent(self, ast: AnonymousComponent, param):
        return AnonymousComponentCircom()

    def visitInfixOp(self, ast: InfixOp, param):
        lhe_val = self.visit(ast.lhe, param).value
        rhe_val = self.visit(ast.rhe, param).value
        if lhe_val is None or rhe_val is None:
            return Symbol("", PrimeField(), None, ast, None)
        op = ast.infix_op
        if op == "&&":
            return Symbol("", PrimeField(), None, ast, circom_and(lhe_val, rhe_val))
        elif op == "||":
            return Symbol("", PrimeField(), None, ast, circom_or(lhe_val, rhe_val))
        elif op == ">":
            return Symbol("", PrimeField(), None, ast, circom_gt(lhe_val, rhe_val))
        elif op == "<":
            return Symbol("", PrimeField(), None, ast, circom_lt(lhe_val, rhe_val))
        elif op == ">=":
            return Symbol("", PrimeField(), None, ast, circom_geq(lhe_val, rhe_val))
        elif op == "<=":
            return Symbol("", PrimeField(), None, ast, circom_leq(lhe_val, rhe_val))
        elif op == "+":
            return Symbol("", PrimeField(), None, ast, circom_add(lhe_val, rhe_val))
        elif op == "-":
            return Symbol("", PrimeField(), None, ast, circom_sub(lhe_val, rhe_val))
        elif op == "*":
            return Symbol("", PrimeField(), None, ast, circom_mul(lhe_val, rhe_val))
        elif op == "**":
            return Symbol("", PrimeField(), None, ast, circom_pow(lhe_val, rhe_val))
        elif op == "/":
            if rhe_val == 0:
                raise Report(ReportType.ERROR, ast.locate, "Division by zero")
            return Symbol("", PrimeField(), None, ast, circom_div(lhe_val, rhe_val))
        elif op == "\\":
            return Symbol("", PrimeField(), None, ast, circom_int_div(lhe_val, rhe_val))
        elif op == "%":
            return Symbol("", PrimeField(), None, ast, circom_mod(lhe_val, rhe_val))
        elif op == "&":
            return Symbol("", PrimeField(), None, ast, circom_bitand(lhe_val, rhe_val))
        elif op == "|":
            return Symbol("", PrimeField(), None, ast, circom_bitor(lhe_val, rhe_val))
        elif op == "^":
            return Symbol("", PrimeField(), None, ast, circom_bitxor(lhe_val, rhe_val))
        elif op == ">>":
            return Symbol("", PrimeField(), None, ast, circom_shr(lhe_val, rhe_val))
        elif op == "<<":
            return Symbol("", PrimeField(), None, ast, circom_shl(lhe_val, rhe_val))
        elif op == "==":
            return Symbol("", PrimeField(), None, ast, circom_eq(lhe_val, rhe_val))
        elif op == "!=":
            return Symbol("", PrimeField(), None, ast, circom_neq(lhe_val, rhe_val))

    def visitPrefixOp(self, ast: PrefixOp, param):
        rhe_val = self.visit(ast.rhe, param).value
        if rhe_val is None:
            return Symbol("", PrimeField(), None, ast, None)
        op = ast.prefix_op
        if op == "!":
            return Symbol("", PrimeField(), None, ast, circom_not(rhe_val))
        elif op == "-":
            return Symbol("", PrimeField(), None, ast, circom_sub(0, rhe_val))
        elif op == "+":
            return Symbol("", PrimeField(), None, ast, circom_add(0, rhe_val))
        elif op == "~":
            return Symbol("", PrimeField(), None, ast, circom_bitnot(rhe_val))
        elif op == "++":
            return Symbol("", PrimeField(), None, ast, circom_add(rhe_val, 1))
        elif op == "--":
            return Symbol("", PrimeField(), None, ast, circom_sub(rhe_val, 1))

    def visitInlineSwitchOp(self, ast: InlineSwitchOp, param):
        cond_val = self.visit(ast.cond, param).value
        if cond_val is None:
            return Symbol("", PrimeField(), None, ast, None)
        if cond_val:
            return self.visit(ast.if_true, param)
        else:
            return self.visit(ast.if_false, param)

    def visitParrallelOp(self, ast: ParallelOp, param):
        return self.visit(ast.rhe, param)

    def visitVariable(self, ast: Variable, param):
        name = ast.name
        symbol = None
        for env in param["env"]:
            if ast.name in env:
                symbol = env[ast.name]
                break
        value = symbol.value
        if isinstance(symbol.mtype, ArrayCircom):
            var_type = ArrayCircom(symbol.mtype.eleType, symbol.mtype.dims)
        else:
            var_type = symbol.mtype
        if isinstance(symbol.xtype, VarCircom):
            for i in range(len(ast.access)):
                access_value = self.visit(ast.access[i], param["env"])
                if var_type.dims == 1:
                    var_type = var_type.eleType
                else:
                    var_type.dims -= 1
                if value:
                    value = value[access_value]
            return Symbol("", var_type, VarCircom(), ast, value)
        elif isinstance(symbol.xtype, ComponentCircom):
            template_name = None
            for i in range(len(ast.access)):
                access_value = self.visit(ast.access[i], param["env"])
                if isinstance(access_value, str):
                    name += "." + access_value
                    template_name = var_type.name
                    if access_value in var_type.signals_in:
                        signal_type = SignalType.INPUT
                    else:
                        signal_type = SignalType.OUTPUT
                    var_type = var_type.signals[access_value]
                else:
                    if var_type.dims == 1:
                        var_type = var_type.eleType
                    else:
                        var_type.dims -= 1
                    name += "[" + str(access_value) + "]"
            if template_name and name not in param["node"]:
                param["node"][name] = Node(
                    name, NodeType.SIGNAL, signal_type, template_name)
                param["component"][template_name][signal_type].append(name)
                return Symbol(name, var_type, SignalType(signal_type), ast, None)
            else:
                return Symbol(name, var_type, ComponentCircom(), ast, None)
        elif isinstance(symbol.xtype, SignalCircom):
            for i in range(len(ast.access)):
                access_value = self.visit(ast.access[i], param["env"])
                if var_type.dims == 1:
                    var_type = var_type.eleType
                else:
                    var_type.dims -= 1
                name += "[" + str(access_value) + "]"
            if name not in param["node"]:
                param["node"][name] = Node(
                    name, NodeType.SIGNAL, symbol.xtype.signal_type, param["name"])
                param["component"][param["name"]
                                   ][symbol.xtype.signal_type].append(name)
            return Symbol(name, var_type, symbol.xtype, ast, value)

    def visitNumber(self, ast: Number, param):
        return Symbol("", PrimeField(), None, ast, ast.value)

    def visitCall(self, param):
        return None

    def visitAnonymousComponentExpr(self, param):
        return None

    def visitArrayInLine(self, ast: ArrayInLine, param):
        values = []
        for expr in ast.values:
            value = self.visit(expr, param).value
            values.append(value)
        return values

    def visitTupleExpr(self, ast: TupleExpr, param):
        return ast.values

    def visitComponentAccess(self, ast: ComponentAccess, param):
        return ast.name

    def visitArrayAccess(self, ast: ArrayAccess, param):
        val = self.visit(ast.expr, param).value
        if val is None:
            raise Report(ReportType.ERROR, ast.locate,
                         "Array access with None value")
        return val

    def visitLogStr(self, ast: LogStr, param):
        return None

    def visitLogExp(self, ast: LogExp, param):
        return None


class FindNode(BaseVisitor):
    def visitFileLocation(self, param):
        return None

    def visitMainComponent(self, param):
        return None

    def visitInclude(self, param):
        return None

    def visitTemplate(self, param):
        return None

    def visitFunction(self, param):
        return None

    def visitProgram(self, param):
        return None

    def visitIfThenElse(self, param):
        return None

    def visitWhile(self, param):
        return None

    def visitReturn(self, param):
        return None

    def visitInitializationBlock(self, param):
        return None

    def visitDeclaration(self, param):
        return None

    def visitSubstitution(self, param):
        return None

    def visitMultiSubstitution(self, param):
        return None

    def visitConstraintEquality(self, param):
        return None

    def visitLogCall(self, param):
        return None

    def visitBlock(self, param):
        return None

    def visitAssert(self, param):
        return None

    def visitVar(self, param):
        return None

    def visitSignal(self, param):
        return None

    def visitComponent(self, param):
        return None

    def visitAnonymousComponent(self, param):
        return None

    def visitInfixOp(self, param):
        return None

    def visitPrefixOp(self, param):
        return None

    def visitInlineSwitchOp(self, param):
        return None

    def visitParrallelOp(self, param):
        return None

    def visitVariable(self, param):
        return None

    def visitNumber(self, param):
        return None

    def visitCall(self, param):
        return None

    def visitAnonymousComponentExpr(self, param):
        return None

    def visitArrayInLine(self, param):
        return None

    def visitTupleExpr(self, param):
        return None

    def visitComponentAccess(self, param):
        return None

    def visitArrayAccess(self, param):
        return None

    def visitLogStr(self, param):
        return None

    def visitLogExp(self, param):
        return None
