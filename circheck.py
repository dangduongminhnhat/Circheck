from functools import wraps
import time
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
    './src/main/Circom/detect/',
    "./target/"
]

for p in locpath:
    if not p in sys.path:
        sys.path.append(p)


def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[Timeit]     Analysis completed in {(end - start):.2f} s")
        return result
    return wrapper


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


@timeit
def detect(absolute_path):
    ast = generate_ast(absolute_path)
    if ast is None:
        print("[Error]      Failed to generate AST.")
        return
    print("[Success]    AST generated successfully.")

    checked = typecheck(ast)
    if checked is None:
        print("[Error]      Type checking failed.")
        return
    print("[Success]    Type checking passed.")

    graphs = generate_cdg(ast, checked)
    if graphs is None:
        print("[Error]      Created CDG failed.")
        return
    print("[Success]    CDG created successfully.")
    from Detect import Detector
    import json
    reports = Detector(graphs).detect()
    file = open("report.json", "w", encoding="utf-8")
    output = {}
    for graph in graphs.values():
        has_report = False
        for report_list in reports[graph.name].values():
            for report in report_list:
                has_report = True
                report.show()
        if not has_report:
            continue
        output[graph.name] = {}
        for vul in reports[graph.name].keys():
            if len(reports[graph.name][vul]) == 0:
                continue
            output[graph.name][vul] = {}
            for report in reports[graph.name][vul]:
                path = report.location.path
                if path not in output[graph.name][vul]:
                    output[graph.name][vul][path] = []
                line = report.location.start.line
                col = report.location.start.column
                output[graph.name][vul][path].append(
                    f"{line}:{col}:{report.message}")
    json.dump(output, file, indent=2)
    file.close()


def main():
    input_file = "./benchmarks/aes-circom/aes_256_ctr_test.circom"
    base_dir = os.path.dirname(os.path.abspath(__file__))
    absolute_path = os.path.abspath(os.path.join(base_dir, input_file))
    detect(absolute_path)


if __name__ == "__main__":
    main()
