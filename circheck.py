from antlr4 import *
import unittest
import subprocess
import sys
import os
import traceback
locpath = ['./src/main/Circom/parser/', './src/main/Circom/astgen/',
           './src/main/Circom/utils/', "./target/"]

for p in locpath:
    if not p in sys.path:
        sys.path.append(p)


def generate_ast(filename):
    from CircomLexer import CircomLexer
    from CircomParser import CircomParser
    from ASTGeneration import ASTGeneration
    import Errors
    from Report import Report, ReportType
    from AST import FileLocation

    try:
        inputstream = FileStream(filename, encoding='utf-8')
        lexer = CircomLexer(inputstream)
        listener = Errors.NewErrorListener.INSTANCE
        tokens = CommonTokenStream(lexer)

        parser = CircomParser(tokens)
        parser.removeErrorListeners()
        parser.addErrorListener(listener)

        try:
            tree = parser.program()
        except Errors.SyntaxException as f:
            Report(ReportType.ERROR, FileLocation(
                filename, None, None), f.message, False).show()
            return None
        except Exception as e:
            Report(ReportType.ERROR, FileLocation(
                filename, None, None), str(e), False).show()
            return None
        path_env = [filename]
        asttree = ASTGeneration().generate_ast(filename, tree, path_env)
        return asttree
    except Exception as e:
        Report(ReportType.ERROR, FileLocation(filename, None, None),
               "Error generating AST: " + str(e), False).show()
        return None


def main():
    input_file = "./benchmarks/aes-circom/aes_256_ctr_test.circom"
    base_dir = os.path.dirname(os.path.abspath(__file__))
    absolute_path = os.path.abspath(os.path.join(base_dir, input_file))
    ast = generate_ast(absolute_path)
    if ast is None:
        print("[Error]  Failed to generate AST.")
    else:
        from AST import Template
        file = open("text.txt", "wb")
        for item in ast.definitions:
            if isinstance(item, Template):
                file.write(str(item.name_field + "\n").encode('utf-8'))
        file.close()
        print("[AST]    AST generated successfully.")


if __name__ == "__main__":
    main()
