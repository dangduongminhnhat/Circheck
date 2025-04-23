from antlr4 import *
import sys
import os
import traceback
locpath = [
    './src/main/Circom/parser/',
    './src/main/Circom/astgen/',
    './src/main/Circom/typecheck/',
    './src/main/Circom/utils/',
    './src/main/Circom/cdggen/',
    "./target/"
]

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


def typecheck(ast):
    from StaticCheck import TypeCheck
    from Report import Report, ReportType
    from AST import FileLocation
    checked = TypeCheck(ast)
    try:
        checked.check()
    except Exception as e:
        traceback.print_exc()
        print(e)
        return None
    return checked.global_env


def generate_cdg(ast, param):
    from CDGGeneration import CDGGeneration
    try:
        graphs = CDGGeneration(ast, param).generateCDG()
        return graphs
    except Exception as e:
        traceback.print_exc()
        print(e)
        return None


def main():
    input_file = "./benchmarks/aes-circom/aes_256_ctr_test.circom"
    base_dir = os.path.dirname(os.path.abspath(__file__))
    absolute_path = os.path.abspath(os.path.join(base_dir, input_file))
    ast = generate_ast(absolute_path)
    if ast is None:
        print("[Error]      Failed to generate AST.")
        return
    file = open("text.txt", "wb")
    file.write(str(ast).encode("utf-8"))
    file.close()
    print("[Success]    AST generated successfully.")

    checked = typecheck(ast)
    if checked is None:
        print("[Error]      Type checking failed.")
        return
    print("[Success]    Type checking passed.")

    graphs = generate_cdg(ast, checked)
    print(graphs)


if __name__ == "__main__":
    main()
