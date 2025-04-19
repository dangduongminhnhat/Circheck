from AST import *
from Visitor import *
from Errors import *
from Report import Report, ReportType
from enum import Enum, auto


class Symbol:
    def __init__(self, name, mtype, xtype, value=None):
        self.name = name
        self.mtype = mtype  # PrimeField, ArrayCircom, TemplateCircom, FunctionCircom
        self.xtype = xtype  # VarCircom, SignalCircom, ComponentCircom, AnonymousComponentCircom
        self.value = value


class Type:
    pass


class SignalType(Enum):
    INPUT = auto()
    OUTPUT = auto()
    INTERMEDIATE = auto()


class PrimeField(Type):
    def __init__(self, is_known=True):
        self.is_known = is_known


class SignalCircom(Type):
    def __init__(self, signal_type):
        self.sinal_type = signal_type


class VarCircom(Type):
    pass


class ComponentCircom(Type):
    pass


class AnonymousComponentCircom(Type):
    pass


class ArrayCircom(Type):
    def __init__(self, eleType, dims):
        self.dims = dims
        self.eleType = eleType


class TemplateCircom(Type):
    def __init__(self, name, params, signals={}, signals_in=[], signals_out=[]):
        self.name = name
        self.params = params
        self.signals = signals
        self.signals_in = signals_in
        self.signals_out = signals_out


class FunctionCircom(Type):
    def __init__(self, name, params, return_type):
        self.name = name
        self.params = params
        self.return_type = return_type


def is_same_type(type1, type2):
    if type(type1) != type(type2):
        return False
    if isinstance(type1, ArrayCircom) and isinstance(type2, ArrayCircom):
        return type1.dims == type2.dims and is_same_type(type1.eleType, type2.eleType)
    return True


class TypeCheck(BaseVisitor):
    def __init__(self, ast):
        self.ast = ast
        self.global_env = [{}]
        self.list_function = {}
        self.in_function = False
        self.return_func = None
        self.list_template = {}
        self.in_template = False
        self.template_signals = None
        self.signal_in = None
        self.signal_out = None

    def check(self):
        self.visit(self.ast, self.global_env)

    def visitFileLocation(self, ast: FileLocation, param):
        return None

    def visitMainComponent(self, param):
        return None

    def visitInclude(self, ast: Include, param):
        return None

    def visitTemplate(self, ast: TemplateCircom, param):
        if ast.name_field in self.list_template:
            raise Report(ReportType.ERROR, ast.locate,
                         f"Template '{ast.name_field}' already declared")
        env = [{}] + param
        for arg in ast.args:
            if arg in env[0]:
                raise Report(ReportType.ERROR, ast.locate,
                             f"Argument '{arg}' already declared")
            env[0][arg] = Symbol(arg, PrimeField(), VarCircom())
        self.in_template = True
        self.template_signals = {}
        self.signal_in = []
        self.signal_out = []
        self.visit(ast.body, env)
        if self.return_func is not None:
            raise Report(ReportType.ERROR, ast.locate,
                         "Template can not have a return statement")
        self.in_template = False
        arg_list = []
        for arg in ast.args:
            arg_list.append(env[0][arg].mtype)
        self.list_template[ast.name_field] = param[0] = Symbol(ast.name_field, TemplateCircom(
            ast.name_field, ast.args, self.template_signals, self.signal_in, self.signal_out), None)
        self.template_signals = None
        self.signal_in = None
        self.signal_out = None

    def visitFunction(self, ast: Function, param):
        if ast.name_field in self.list_function:
            raise Report(ReportType.ERROR, ast.locate,
                         f"Function '{ast.name_field}' already declared")
        self.in_function = True
        env = [{}] + param
        for arg in ast.args:
            if arg in env[0]:
                raise Report(ReportType.ERROR, ast.locate,
                             f"Argument '{arg}' already declared")
            env[0][arg] = Symbol(arg, PrimeField(), VarCircom())
        self.visit(ast.body, env)
        if self.return_func is None:
            raise Report(ReportType.ERROR, ast.locate,
                         "Unable to infer the type of this function")
        return_type = self.return_func
        self.return_func = None
        arg_list = []
        for arg in ast.args:
            arg_list.append(env[0][arg].mtype)
        self.list_function[ast.name_field] = param[0] = Symbol(
            ast.name_field, FunctionCircom(ast.name_field, arg_list, return_type), None)
        self.in_function = False

    def visitProgram(self, param):
        return None

    def visitIfthenelse(self, ast: IfThenElse, param):
        cond_type = self.visit(ast.cond, param)
        if isinstance(cond_type, TemplateCircom):
            raise Report(ReportType.ERROR, ast.cond.locate,
                         "Must be a single arithmetic expression. Found component")
        elif isinstance(cond_type, ArrayCircom):
            raise Report(ReportType.ERROR, ast.cond.locate,
                         "Must be a single arithmetic expression. Found array")
        self.visit(ast.if_case, param)
        if ast.else_case:
            self.visit(ast.else_case, param)

    def visitWhile(self, ast: While, param):
        cond_type = self.visit(ast.cond, param)
        if isinstance(cond_type, TemplateCircom):
            raise Report(ReportType.ERROR, ast.cond.locate,
                         "Must be a single arithmetic expression. Found component")
        elif isinstance(cond_type, ArrayCircom):
            raise Report(ReportType.ERROR, ast.cond.locate,
                         "Must be a single arithmetic expression. Found array")
        self.visit(ast.stmt, param)

    def visitReturn(self, ast: Return, param):
        if self.in_function:
            value_type = self.visit(ast.value, param)
            if isinstance(value_type, TemplateCircom):
                raise Report(ReportType.ERROR, ast.value.locate,
                             "Must be a single arithmetic expression. Found component")
            if not is_same_type(value_type, self.return_func):
                raise Report(ReportType.ERROR, ast.value.locate,
                             "Return type is not compatible with the function return type")
        else:
            raise Report(ReportType.ERROR, ast.locate,
                         "Return statement outside of a function")

    def visitInitializationBlock(self, ast: InitializationBlock, param):
        for init in ast.initializations:
            self.visit(init, param)

    def visitDeclaration(self, ast: Declaration, param):
        if ast.name in param[0]:
            raise Report(ReportType.ERROR, ast.locate,
                         f"Variable '{ast.name}' already declared")
        for expr in ast.dimensions:
            expr_type = self.visit(expr, param)
            if isinstance(expr_type, TemplateCircom):
                raise Report(ReportType.ERROR, expr.locate,
                             "Array indexes and lengths must be single arithmetic expressions. Found component instead of expression.")
            elif isinstance(expr_type, ArrayCircom):
                raise Report(ReportType.ERROR, expr.locate,
                             "Array indexes and lengths must be single arithmetic expressions. Found array instead of expression.")
        xtype = self.visit(ast.xtype, param)
        if isinstance(xtype, SignalCircom):
            if xtype.sinal_type == SignalType.INPUT:
                self.signal_in.append(ast.name)
            elif xtype.sinal_type == SignalType.OUTPUT:
                self.signal_out.append(ast.name)
            self.template_signals[ast.name] = xtype
            if len(ast.dimensions) > 0:
                mtype = ArrayCircom(PrimeField(), len(ast.dimensions))
            else:
                mtype = PrimeField()
            param[0][ast.name] = Symbol(ast.name, mtype, xtype)
        elif isinstance(xtype, VarCircom):
            if len(ast.dimensions) > 0:
                mtype = ArrayCircom(PrimeField(), len(ast.dimensions))
            else:
                mtype = PrimeField()
            param[0][ast.name] = Symbol(ast.name, mtype, xtype)
        elif isinstance(xtype, ComponentCircom):
            template_type = TemplateCircom("", None)
            if len(ast.dimensions) > 0:
                mtype = ArrayCircom(template_type, len(ast.dimensions))
            else:
                mtype = template_type
            param[0][ast.name] = Symbol(ast.name, mtype, xtype)

    def visitSubstitution(self, ast: Substitution, param):
        rhe_type = self.visit(ast.rhe, param)
        if ast.var == "_":
            if isinstance(rhe_type, TemplateCircom):
                raise Report(ReportType.ERROR, ast.rhe.locate,
                             "Must be a single arithmetic expression. Found component")
        else:
            lhe_type = self.visit(Variable(ast.var, ast.access), param)
            if isinstance(lhe_type, TemplateCircom) and isinstance(rhe_type, TemplateCircom):

    def visitMultiSubstitution(self, param):
        return None

    def visitConstraintEquality(self, ast: ConstraintEquality, param):
        lhe_type = self.visit(ast.lhe, param)
        rhe_type = self.visit(ast.rhe, param)
        if isinstance(lhe_type, TemplateCircom):
            raise Report(ReportType.ERROR, ast.lhe.locate,
                         "Must be a single arithmetic expression. Found component")
        if isinstance(rhe_type, TemplateCircom):
            raise Report(ReportType.ERROR, ast.rhe.locate,
                         "Must be a single arithmetic expression. Found component")
        if not is_same_type(lhe_type, rhe_type):
            raise Report(ReportType.ERROR, ast.rhe.locate,
                         "Types of the two sides of the equality are not compatible")

    def visitLogCall(self, ast: LogCall, param):
        for arg in ast.args:
            if isinstance(arg, LogExp):
                arg_type = self.visit(arg, param)
                if isinstance(arg_type, TemplateCircom):
                    raise Report(ReportType.ERROR, arg.locate,
                                 "Must be a single arithmetic expression. Found component")
                elif isinstance(arg_type, ArrayCircom):
                    raise Report(ReportType.ERROR, arg.locate,
                                 "Must be a single arithmetic expression. Found array")

    def visitBlock(self, ast: Block, param):
        if self.in_template or self.in_function:
            env = param
            self.in_template = False
            self.in_function = False
        else:
            env = [{}] + param
        for stmt in ast.stmts:
            self.visit(stmt, env)

    def visitAssert(self, ast: Assert, param):
        arg_type = self.visit(ast.arg, param)
        if isinstance(arg_type, TemplateCircom):
            raise Report(ReportType.ERROR, ast.locate,
                         "Must be a single arithmetic expression. Found component")
        elif isinstance(arg_type, ArrayCircom):
            raise Report(ReportType.ERROR, ast.locate,
                         "Must be a single arithmetic expression. Found array")

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
        lhe_type = self.visit(ast.lhe, param)
        rhe_type = self.visit(ast.rhe, param)
        if isinstance(lhe_type, TemplateCircom) or isinstance(lhe_type, ArrayCircom):
            raise Report(ReportType.ERROR, ast.lhe.locate,
                         "Type not allowed by the operator")
        if isinstance(rhe_type, TemplateCircom) or isinstance(rhe_type, ArrayCircom):
            raise Report(ReportType.ERROR, ast.rhe.locate,
                         "Type not allowed by the operator")
        return PrimeField()

    def visitPrefixOp(self, ast: PrefixOp, param):
        rhe_type = self.visit(ast.rhe, param)
        if isinstance(rhe_type, TemplateCircom) or isinstance(rhe_type, ArrayCircom):
            raise Report(ReportType.ERROR, ast.rhe.locate,
                         "Type not allowed by the operator")
        return PrimeField()

    def visitInlineSwitchOp(self, ast: InlineSwitchOp, param):
        cond_type = self.visit(ast.cond, param)
        if isinstance(cond_type, TemplateCircom):
            raise Report(ReportType.ERROR, ast.cond.locate,
                         "Must be a single arithmetic expression. Found component")
        elif isinstance(cond_type, ArrayCircom):
            raise Report(ReportType.ERROR, ast.cond.locate,
                         "Must be a single arithmetic expression. Found array")
        if_true_type = self.visit(ast.if_true, param)
        if_false_type = self.visit(ast.if_false, param)
        if not is_same_type(if_true_type, if_false_type):
            raise Report(ReportType.ERROR, ast.if_false.locate,
                         "Inline switch operator branches types are non compatible")
        return if_true_type

    def visitParrallelOp(self, ast: ParallelOp, param):
        rhe_type = self.visit(ast.rhe, param)
        if not isinstance(rhe_type, TemplateCircom):
            raise Report(ReportType.ERROR, ast.rhe.locate,
                         "Type not allowed by the operator parallel (parallel operator can only be applied to templates)")
        return rhe_type

    def visitVariable(self, ast: Variable, param):
        var_type = None
        for env in param:
            if ast.name in env:
                var_type = env[ast.name].mtype
        if var_type is None:
            raise Report(ReportType.ERROR, ast.locate,
                         f"Variable '{ast.name}' not declared")
        if len(ast.access) > 0:
            if isinstance(var_type, PrimeField):
                raise Report(ReportType.ERROR, ast.locate,
                             f"Variable '{ast.name}' is not an array")
            elif isinstance(var_type, ArrayCircom):
                ele_type = var_type.eleType
                last_access = self.visit(ast.access[-1], param)
                if isinstance(last_access, PrimeField):
                    if len(ast.access) > var_type.dims:
                        raise Report(ReportType.ERROR, ast.locate,
                                     f"Array '{ast.name}' has only {var_type.dims} dimensions")
                else:
                    if not isinstance(ele_type, TemplateCircom) or (len(ast.access) - 1) > var_type.dims:
                        raise Report(ReportType.ERROR, ast.locate,
                                     "Not a valid array access or component access")
                for i in range(len(ast.access) - 1):
                    access_type = self.visit(ast.access[i], param)
                    if not isinstance(access_type, PrimeField):
                        raise Report(ReportType.ERROR, ast.locate,
                                     "Not a valid array access")
                if isinstance(last_access, PrimeField):
                    if len(ast.access) == var_type.dims:
                        return ele_type
                    else:
                        return ArrayCircom(ele_type, var_type.dims - len(ast.access))
                else:
                    if len(ast.access) - 1 == var_type.dims:
                        if last_access not in var_type.signals:
                            raise Report(
                                ReportType.ERROR, ast.locate, f"Variable '{ast.name}' does not have signal '{last_access}'")
                        return var_type.signals[last_access]
                    else:
                        return ArrayCircom(ele_type, var_type.dims - len(ast.access))
            elif isinstance(var_type, TemplateCircom):
                if len(ast.access) > 1:
                    raise Report(ReportType.ERROR, ast.locate,
                                 f"Variable '{ast.name}' is not an array")
                else:
                    access_type = self.visit(ast.access[0], param)
                    if isinstance(access_type, PrimeField):
                        raise Report(ReportType.ERROR, ast.locate,
                                     f"Variable '{ast.name}' is not an array")
                    elif access_type not in var_type.signals:
                        raise Report(ReportType.ERROR, ast.locate,
                                     f"Variable '{ast.name}' does not have signal '{access_type}'")
                    return var_type.signal_out[access_type]
        return var_type

    def visitNumber(self, ast: Number, param):
        return PrimeField()

    def visitCall(self, ast: Call, param):
        func_type = None
        for env in param:
            if ast.id in env:
                func_type = env[ast.id].mtype
        if func_type is None:
            raise Report(ReportType.ERROR, ast.locate,
                         f"Function '{ast.id}' not declared")
        if not isinstance(func_type, FunctionCircom):
            raise Report(ReportType.ERROR, ast.locate,
                         f"'{ast.id}' is not a function")
        if len(ast.args) != len(func_type.params):
            raise Report(ReportType.ERROR, ast.locate,
                         f"Function '{ast.id}' has {len(func_type.params)} arguments, but {len(ast.args)} were provided")
        for arg in ast.args:
            arg_type = self.visit(arg, param)
            if not isinstance(arg_type, PrimeField):
                raise Report(ReportType.ERROR, ast.locate,
                             f"Function '{ast.id}' argument must be a single arithmetic expression.")
        return func_type.return_type

    def visitAnonymousComponentExpr(self, param):
        return None

    def visitArrayInLine(self, ast: ArrayInLine, param):
        type_list = []
        for value in ast.values:
            type_list.append(self.visit(value, param))
        first_type = type_list[0]
        if isinstance(first_type, TemplateCircom):
            raise Report(
                ReportType.ERROR, ast.values[0].locate, "Components can not be declared inside inline arrays")
        for i in range(1, len(type_list)):
            if isinstance(type_list[i], TemplateCircom):
                raise Report(
                    ReportType.ERROR, ast.values[i].locate, "Components can not be declared inside inline arrays")
            elif not is_same_type(first_type, type_list[i]):
                raise Report(ReportType.ERROR, ast.values[i].locate,
                             "All elements in the array must be of the same type")
        return ArrayCircom(first_type, len(ast.values))

    def visitTupleExpr(self, param):
        return None

    def visitComponentAccess(self, ast: ComponentAccess, param):
        return ast.name

    def visitArrayAccess(self, ast: ArrayAccess, param):
        expr_type = self.visit(ast.expr, param)
        if isinstance(expr_type, TemplateCircom):
            raise Report(ReportType.ERROR, ast.expr.locate,
                         "Array indexes and lengths must be single arithmetic expressions. Found component instead of expression.")
        elif isinstance(expr_type, ArrayCircom):
            raise Report(ReportType.ERROR, ast.expr.locate,
                         "Array indexes and lengths must be single arithmetic expressions. Found array instead of expression.")
        return PrimeField()

    def visitLogStr(self, ast: LogStr, param):
        return None

    def visitLogExp(self, ast: LogExp, param):
        return self.visit(ast.expr, param)
