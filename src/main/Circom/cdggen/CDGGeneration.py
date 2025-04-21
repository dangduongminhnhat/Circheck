from CDG import *
from Visitor import *
from Errors import *
from AST import *
from Report import Report, ReportType
from StaticCheck import *

FIELD_ELEMENT = 21888242871839275222246405745257275088548364400416034343698204186575808495617


class CDGGeneration(BaseVisitor):
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

    def visitProgram(self, param):
        return None

    def visitIfThenElse(self, param):
        return None

    def visitWhile(self, param):
        return None

    def visitReturn(self, ast: Return, param):
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

    def visitLogCall(self, ast: LogCall, param):
        return None

    def visitBlock(self, param):
        return None

    def visitAssert(self, ast: Assert, param):
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

    def visitNumber(self, ast: Number, param):
        return Symbol("", PrimeField(), None, ast, ast.value)

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

    def visitLogStr(self, ast: LogStr, param):
        return None

    def visitLogExp(self, ast: LogExp, param):
        return None
