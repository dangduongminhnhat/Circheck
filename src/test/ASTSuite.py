import unittest
from TestUtils import TestAST
from AST import *


class ASTSuite(unittest.TestCase):
    def test_ast_1(self):
        input = """
template Foo(n) {
                signal input a[2];

                a[0] === a[1];
            }
"""
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input, expect, "ast_1"))
