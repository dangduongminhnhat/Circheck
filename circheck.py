from antlr4 import *
import unittest
import subprocess
import sys
import os
import traceback
from antlr4.error.ErrorListener import ConsoleErrorListener, ErrorListener

locpath = ['./main/Circom/parser/', './main/Circom/astgen/',
           './main/Circom/utils/', "./target"]

for p in locpath:
    if not p in sys.path:
        sys.path.append(p)


def main():
    print("Oke")


if __name__ == "__main__":
    main()
