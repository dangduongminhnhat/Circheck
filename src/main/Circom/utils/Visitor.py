from abc import ABC, abstractmethod


class Visitor(ABC):
    def visit(self, ast, param):
        return ast.accept(self, param)

    @abstractmethod
    def visitFileLocation(self, param):
        pass

    @abstractmethod
    def visitMainComponent(self, param):
        pass

    @abstractmethod
    def visitInclude(self, param):
        pass

    @abstractmethod
    def visitTemplate(self, param):
        pass

    @abstractmethod
    def visitFunction(self, param):
        pass

    @abstractmethod
    def visitProgram(self, param):
        pass
