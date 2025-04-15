import sys
import os
from antlr4 import *
from antlr4.error.ErrorListener import ConsoleErrorListener, ErrorListener
from CircomLexer import CircomLexer
from CircomParser import CircomParser
from lexererr import *
from ASTGeneration import ASTGeneration
# from StaticError import *
# from StaticCheck import StaticChecker


class TestUtil:
    @staticmethod
    def makeSource(inputStr, num):
        filename = "./test/testcases/" + str(num) + ".txt"
        file = open(filename, "w")
        file.write(inputStr)
        file.close()
        return FileStream(filename)


class TestLexer:
    @staticmethod
    def checkLexeme(input, expect, num):
        inputfile = TestUtil.makeSource(input, num)
        dest = open("./test/solutions/" + str(num) + ".txt", "w")
        lexer = CircomLexer(inputfile)
        try:
            TestLexer.printLexeme(dest, lexer)
        except (ErrorToken, UncloseString, IllegalEscape) as err:
            dest.write(err.message)
        finally:
            dest.close()
        dest = open("./test/solutions/" + str(num) + ".txt", "r")
        line = dest.read()
        return line == expect

    @staticmethod
    def printLexeme(dest, lexer):
        tok = lexer.nextToken()
        if tok.type != Token.EOF:
            dest.write(tok.text+",")
            TestLexer.printLexeme(dest, lexer)
        else:
            dest.write("<EOF>")


class NewErrorListener(ConsoleErrorListener):
    INSTANCE = None

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxException("Error on line " + str(line) +
                              " col " + str(column) + ": " + offendingSymbol.text)


NewErrorListener.INSTANCE = NewErrorListener()


class SyntaxException(Exception):
    def __init__(self, msg):
        self.message = msg


class TestParser:
    @staticmethod
    def createErrorListener():
        return NewErrorListener.INSTANCE

    @staticmethod
    def checkParser(input, expect, num):
        inputfile = TestUtil.makeSource(input, num)
        dest = open("./test/solutions/" + str(num) + ".txt", "w")
        lexer = CircomLexer(inputfile)
        listener = TestParser.createErrorListener()

        tokens = CommonTokenStream(lexer)

        parser = CircomParser(tokens)
        parser.removeErrorListeners()
        parser.addErrorListener(listener)
        try:
            parser.program()
            dest.write("successful")
        except SyntaxException as f:
            dest.write(f.message)
        except Exception as e:
            dest.write(str(e))
        finally:
            dest.close()
        dest = open("./test/solutions/" + str(num) + ".txt", "r")
        line = dest.read()
        return line == expect


class TestAST:
    @staticmethod
    def checkASTGen(input, expect, num):
        inputfile = TestUtil.makeSource(input, num)
        with open("./test/solutions/" + str(num) + ".txt", "w", encoding="utf-8") as dest:
            # Create the lexer, token stream, and parser
            lexer = CircomLexer(inputfile)
            tokens = CommonTokenStream(lexer)
            parser = CircomParser(tokens)
            tree = parser.program()

            # Generate the AST and write it to the file
            asttree = ASTGeneration().visit(tree)
            dest.write(str(asttree))

        # Open the destination file for reading with utf-8 encoding
        with open("./test/solutions/" + str(num) + ".txt", "r", encoding="utf-8") as dest:
            line = dest.read()
        return line == expect


# class TestChecker:
#     @staticmethod
#     def test(input, expect, num):
#         return TestChecker.checkStatic(input, expect, num)

#     @staticmethod
#     def checkStatic(input, expect, num):
#         dest = open("./test/solutions/" + str(num) + ".txt", "w")

#         if type(input) is str:
#             inputfile = TestUtil.makeSource(input, num)
#             lexer = CircomLexer(inputfile)
#             tokens = CommonTokenStream(lexer)
#             parser = CircomParser(tokens)
#             tree = parser.program()
#             asttree = ASTGeneration().visit(tree)
#         else:
#             inputfile = TestUtil.makeSource(str(input), num)
#             asttree = input

#         checker = StaticChecker(asttree)
#         try:
#             res = checker.check()
#             # dest.write(str(list(res)))
#         except StaticError as e:
#             dest.write(str(e)+'\n')
#         finally:
#             dest.close()
#         dest = open("./test/solutions/" + str(num) + ".txt", "r")
#         line = dest.read()
#         return line == expect

#     @staticmethod
#     def test1(inputdir, outputdir, num):

#         dest = open(outputdir + "/" + str(num) + ".txt", "w")

#         try:
#             lexer = CircomLexer(FileStream(inputdir + "/" + str(num) + ".txt"))
#             tokens = CommonTokenStream(lexer)
#             parser = CircomParser(tokens)
#             tree = parser.program()
#             asttree = ASTGeneration().visit(tree)

#             checker = StaticChecker(asttree)
#             res = checker.check()

#         except StaticError as e:
#             dest.write(str(e)+'\n')
#         except:
#             trace = traceback.format_exc()
#             print("Test " + str(num) + " catches unexpected error:" + trace + "\n")
#         finally:
#             dest.close()
