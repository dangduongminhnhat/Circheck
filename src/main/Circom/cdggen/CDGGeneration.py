from CDG import *
from Visitor import *
from Errors import *
from AST import *
from Report import Report, ReportType
from StaticCheck import *


class CDGGeneration(BaseVisitor):
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
