from dataclasses import dataclass
from antlr4.error.ErrorListener import ConsoleErrorListener, ErrorListener


class NewErrorListener(ConsoleErrorListener):
    INSTANCE = None

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxException("Error on line " + str(line) +
                              " col " + str(column) + ": " + offendingSymbol.text)


NewErrorListener.INSTANCE = NewErrorListener()


class SyntaxException(Exception):
    def __init__(self, msg):
        self.message = msg


class UnclosedComment(Exception):
    """Error raised when a comment is not closed."""

    def __init__(self, line: int, column: int):
        self.line = line
        self.column = column

    def __str__(self):
        return f"Unclosed comment at line {self.line}, column {self.column}."


class StaticError(Exception):
    """Base class for static errors."""
    pass


class NoMainFoundInProject(StaticError):
    """Error raised when no main function is found in the project."""

    def __str__(self):
        return "No main function found in the project."


@dataclass
class CustomGatesVersionError(StaticError):
    """Error raised when the custom gates version is not supported."""
    version: str

    def __str__(self):
        return f"Custom gates version {self.version} is not supported."


@dataclass
class IllegalExpression(StaticError):
    """Error raised when an illegal expression is encountered."""
    message: str

    def __str__(self):
        return f"Illegal expression: {self.message}"


@dataclass
class IncludeNotFound(StaticError):
    """Error raised when an include file is not found."""
    filename: str

    def __str__(self):
        return f"Include file '{self.filename}' not found."


@dataclass
class AnonymousCompError(StaticError):
    """Error raised when an anonymous component is encountered."""
    message: str

    def __str__(self):
        return f"Anonymous component error: {self.message}"


@dataclass
class TupleError(StaticError):
    """Error raised when a tuple is not well formed."""
    message: str

    def __str__(self):
        return f"Tuple error: {self.message}"


@dataclass
class SameSymbolDeclaredTwice(StaticError):
    """Error raised when a symbol is declared twice."""
    symbol: str

    def __str__(self):
        return f"Symbol '{self.symbol}' declared twice."


@dataclass
class FunctionReturnError(StaticError):
    """Error raised when a function return type is not well formed."""
    message: str

    def __str__(self):
        return f"Function return error: {self.message}"


@dataclass
class UndefinedFunction(StaticError):
    """Error raised when a function is not defined."""
    function_name: str

    def __str__(self):
        return f"Function '{self.function_name}' is not defined."


@dataclass
class TemplateWithReturnStatement(StaticError):
    """Error raised when a template has a return statement."""
    template_name: str

    def __str__(self):
        return f"Template '{self.template_name}' cannot have a return statement."


@dataclass
class SignalOutsideOriginalScope(StaticError):
    """Error raised when a signal is used outside its original scope."""
    signal_name: str

    def __str__(self):
        return f"Signal '{self.signal_name}' used outside its original scope."


@dataclass
class NonExistentSymbol(StaticError):
    """Error raised when a symbol does not exist."""
    symbol: str

    def __str__(self):
        return f"Symbol '{self.symbol}' does not exist."


@dataclass
class FunctionWrongNumberOfArguments(StaticError):
    """Error raised when a function is called with the wrong number of arguments."""
    function_name: str
    expected: int
    actual: int

    def __str__(self):
        return f"Function '{self.function_name}' expected {self.expected} arguments, but got {self.actual}."


@dataclass
class InvalidArraySizeT(StaticError):
    """Error raised when a template array size is invalid."""
    size: str

    def __str__(self):
        return f"Invalid template array size: {self.size}."


@dataclass
class InvalidArraySize(StaticError):
    """Error raised when an array size is invalid."""
    size: str

    def __str__(self):
        return f"Invalid array size: {self.size}."


@dataclass
class WrongTypesInAssignOperationOperatorSignal(StaticError):
    """Error raised when the types in an assignment operation are wrong."""
    message: str

    def __str__(self):
        return f"Wrong types in assignment operation: {self.message}."


@dataclass
class WrongTypesInAssignOperationOperatorNoSignal(StaticError):
    """Error raised when the types in an assignment operation are wrong."""
    message: str

    def __str__(self):
        return f"Wrong types in assignment operation: {self.message}."


@dataclass
class WrongTypesInAssignOperationArrayTemplates(StaticError):
    """Error raised when the types in an assignment operation are wrong."""
    message: str

    def __str__(self):
        return f"Wrong types in assignment operation: {self.message}."


@dataclass
class WrongTypesInAssignOperationExpression(StaticError):
    """Error raised when the types in an assignment operation are wrong."""
    message: str

    def __str__(self):
        return f"Wrong types in assignment operation: {self.message}."


@dataclass
class WrongTypesInAssignOperationDims(StaticError):
    """Error raised when the types in an assignment operation are wrong."""
    message: str

    def __str__(self):
        return f"Wrong types in assignment operation: {self.message}."


@dataclass
class InvalidSignalAccess(StaticError):
    """Error raised when a signal is accessed incorrectly."""
    message: str

    def __str__(self):
        return f"Invalid signal access: {self.message}."


@dataclass
class NonConstantArrayLength(StaticError):
    """Error raised when an array length is not constant."""
    message: str

    def __str__(self):
        return f"Non-constant array length: {self.message}."
