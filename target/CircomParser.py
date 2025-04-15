# Generated from main/Circom/parser/Circom.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3L")
        buf.write("\u0306\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\tL\4M\t")
        buf.write("M\4N\tN\4O\tO\4P\tP\3\2\5\2\u00a2\n\2\3\2\5\2\u00a5\n")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4")
        buf.write("\5\4\u00b4\n\4\3\5\3\5\5\5\u00b8\n\5\3\6\3\6\3\6\3\6\5")
        buf.write("\6\u00be\n\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3")
        buf.write("\t\3\t\3\t\5\t\u00cd\n\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\5\13\u00db\n\13\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\5\17\u00f6")
        buf.write("\n\17\3\20\3\20\5\20\u00fa\n\20\3\21\3\21\5\21\u00fe\n")
        buf.write("\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23\5\23\u0107\n\23")
        buf.write("\3\24\3\24\3\24\3\24\5\24\u010d\n\24\3\25\3\25\3\25\3")
        buf.write("\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\5\27\u0128\n\27\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3")
        buf.write("\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\5\31\u0149\n\31\3\32\3\32\3\32\3\32\3\32\3")
        buf.write("\32\3\32\3\32\3\32\5\32\u0154\n\32\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\5\33\u016a\n\33\3\34\3\34\3")
        buf.write("\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3")
        buf.write(" \3 \3 \3 \3 \3 \5 \u018b\n \3!\3!\3!\5!\u0190\n!\3\"")
        buf.write("\3\"\3\"\3\"\5\"\u0196\n\"\3#\3#\3#\3#\3$\3$\3$\3%\3%")
        buf.write("\3%\3&\3&\3&\3&\3&\5&\u01a7\n&\3\'\3\'\3\'\3\'\3\'\3(")
        buf.write("\3(\5(\u01b0\n(\3)\3)\3)\3)\3)\5)\u01b7\n)\3*\3*\3*\3")
        buf.write("*\3*\3*\3*\3*\3*\3*\3*\3*\3*\5*\u01c6\n*\3+\3+\3+\3+\3")
        buf.write("+\3+\3+\3+\3+\3+\3+\3+\3+\3+\5+\u01d6\n+\3,\3,\3,\3,\3")
        buf.write(",\3,\3,\3,\5,\u01e0\n,\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3")
        buf.write("-\5-\u01ed\n-\3.\3.\3.\3.\3.\5.\u01f4\n.\3/\3/\3/\3/\3")
        buf.write("/\3/\3/\3/\3/\3/\3/\3/\3/\5/\u0203\n/\3\60\3\60\5\60\u0207")
        buf.write("\n\60\3\61\3\61\3\61\3\61\5\61\u020d\n\61\3\62\3\62\3")
        buf.write("\62\3\62\3\63\3\63\3\63\3\63\5\63\u0217\n\63\3\64\3\64")
        buf.write("\3\64\3\65\3\65\3\65\3\66\3\66\3\66\5\66\u0222\n\66\3")
        buf.write("\67\3\67\3\67\3\67\3\67\3\67\3\67\5\67\u022b\n\67\38\3")
        buf.write("8\38\38\38\38\78\u0233\n8\f8\168\u0236\138\39\39\39\3")
        buf.write("9\39\39\79\u023e\n9\f9\169\u0241\139\3:\3:\3:\3:\3:\3")
        buf.write(":\3:\7:\u024a\n:\f:\16:\u024d\13:\3;\3;\3;\3;\3;\3;\7")
        buf.write(";\u0255\n;\f;\16;\u0258\13;\3<\3<\3<\3<\3<\3<\7<\u0260")
        buf.write("\n<\f<\16<\u0263\13<\3=\3=\3=\3=\3=\3=\7=\u026b\n=\f=")
        buf.write("\16=\u026e\13=\3>\3>\3>\3>\3>\3>\3>\7>\u0277\n>\f>\16")
        buf.write(">\u027a\13>\3?\3?\3?\3?\3?\3?\3?\7?\u0283\n?\f?\16?\u0286")
        buf.write("\13?\3@\3@\3@\3@\3@\3@\3@\7@\u028f\n@\f@\16@\u0292\13")
        buf.write("@\3A\3A\3A\3A\3A\3A\7A\u029a\nA\fA\16A\u029d\13A\3B\3")
        buf.write("B\3B\3B\5B\u02a3\nB\3C\3C\3C\3C\3C\3C\3C\3C\3C\3C\3C\3")
        buf.write("C\3C\3C\3C\3C\3C\3C\3C\3C\3C\3C\5C\u02bb\nC\3D\3D\3D\3")
        buf.write("D\3D\3D\3D\3D\5D\u02c5\nD\3E\3E\3E\3E\3E\3E\3E\3E\7E\u02cf")
        buf.write("\nE\fE\16E\u02d2\13E\3F\3F\5F\u02d6\nF\3G\3G\3G\3G\3G")
        buf.write("\5G\u02dd\nG\3H\3H\3H\3H\3H\5H\u02e4\nH\3I\3I\5I\u02e8")
        buf.write("\nI\3J\3J\3J\3J\3J\3J\3J\3J\3J\3J\3J\7J\u02f5\nJ\fJ\16")
        buf.write("J\u02f8\13J\3K\3K\3L\3L\3M\3M\3N\3N\3O\3O\3P\3P\3P\2\16")
        buf.write("nprtvxz|~\u0080\u0088\u0092Q\2\4\6\b\n\f\16\20\22\24\26")
        buf.write("\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\")
        buf.write("^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086\u0088\u008a")
        buf.write("\u008c\u008e\u0090\u0092\u0094\u0096\u0098\u009a\u009c")
        buf.write("\u009e\2\b\4\2\26\27\36\36\3\2$)\3\2\37 \3\2\35\36\3\2")
        buf.write("\31\34\4\2\21\22,,\2\u0304\2\u00a1\3\2\2\2\4\u00ab\3\2")
        buf.write("\2\2\6\u00b3\3\2\2\2\b\u00b7\3\2\2\2\n\u00bd\3\2\2\2\f")
        buf.write("\u00bf\3\2\2\2\16\u00c4\3\2\2\2\20\u00cc\3\2\2\2\22\u00ce")
        buf.write("\3\2\2\2\24\u00da\3\2\2\2\26\u00dc\3\2\2\2\30\u00e3\3")
        buf.write("\2\2\2\32\u00ea\3\2\2\2\34\u00f5\3\2\2\2\36\u00f9\3\2")
        buf.write("\2\2 \u00fd\3\2\2\2\"\u00ff\3\2\2\2$\u0106\3\2\2\2&\u010c")
        buf.write("\3\2\2\2(\u010e\3\2\2\2*\u0111\3\2\2\2,\u0127\3\2\2\2")
        buf.write(".\u0129\3\2\2\2\60\u0148\3\2\2\2\62\u0153\3\2\2\2\64\u0169")
        buf.write("\3\2\2\2\66\u016b\3\2\2\28\u0171\3\2\2\2:\u0176\3\2\2")
        buf.write("\2<\u017a\3\2\2\2>\u018a\3\2\2\2@\u018f\3\2\2\2B\u0195")
        buf.write("\3\2\2\2D\u0197\3\2\2\2F\u019b\3\2\2\2H\u019e\3\2\2\2")
        buf.write("J\u01a6\3\2\2\2L\u01a8\3\2\2\2N\u01af\3\2\2\2P\u01b6\3")
        buf.write("\2\2\2R\u01c5\3\2\2\2T\u01d5\3\2\2\2V\u01df\3\2\2\2X\u01ec")
        buf.write("\3\2\2\2Z\u01f3\3\2\2\2\\\u0202\3\2\2\2^\u0206\3\2\2\2")
        buf.write("`\u020c\3\2\2\2b\u020e\3\2\2\2d\u0216\3\2\2\2f\u0218\3")
        buf.write("\2\2\2h\u021b\3\2\2\2j\u0221\3\2\2\2l\u022a\3\2\2\2n\u022c")
        buf.write("\3\2\2\2p\u0237\3\2\2\2r\u0242\3\2\2\2t\u024e\3\2\2\2")
        buf.write("v\u0259\3\2\2\2x\u0264\3\2\2\2z\u026f\3\2\2\2|\u027b\3")
        buf.write("\2\2\2~\u0287\3\2\2\2\u0080\u0293\3\2\2\2\u0082\u02a2")
        buf.write("\3\2\2\2\u0084\u02ba\3\2\2\2\u0086\u02c4\3\2\2\2\u0088")
        buf.write("\u02c6\3\2\2\2\u008a\u02d5\3\2\2\2\u008c\u02dc\3\2\2\2")
        buf.write("\u008e\u02e3\3\2\2\2\u0090\u02e7\3\2\2\2\u0092\u02e9\3")
        buf.write("\2\2\2\u0094\u02f9\3\2\2\2\u0096\u02fb\3\2\2\2\u0098\u02fd")
        buf.write("\3\2\2\2\u009a\u02ff\3\2\2\2\u009c\u0301\3\2\2\2\u009e")
        buf.write("\u0303\3\2\2\2\u00a0\u00a2\5\f\7\2\u00a1\u00a0\3\2\2\2")
        buf.write("\u00a1\u00a2\3\2\2\2\u00a2\u00a4\3\2\2\2\u00a3\u00a5\5")
        buf.write("\16\b\2\u00a4\u00a3\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5")
        buf.write("\u00a6\3\2\2\2\u00a6\u00a7\5\20\t\2\u00a7\u00a8\5\n\6")
        buf.write("\2\u00a8\u00a9\5\6\4\2\u00a9\u00aa\7\2\2\3\u00aa\3\3\2")
        buf.write("\2\2\u00ab\u00ac\7I\2\2\u00ac\u00ad\7\13\2\2\u00ad\u00ae")
        buf.write("\7I\2\2\u00ae\u00af\7\13\2\2\u00af\u00b0\7I\2\2\u00b0")
        buf.write("\5\3\2\2\2\u00b1\u00b4\5\26\f\2\u00b2\u00b4\3\2\2\2\u00b3")
        buf.write("\u00b1\3\2\2\2\u00b3\u00b2\3\2\2\2\u00b4\7\3\2\2\2\u00b5")
        buf.write("\u00b8\5\30\r\2\u00b6\u00b8\5\32\16\2\u00b7\u00b5\3\2")
        buf.write("\2\2\u00b7\u00b6\3\2\2\2\u00b8\t\3\2\2\2\u00b9\u00ba\5")
        buf.write("\b\5\2\u00ba\u00bb\5\n\6\2\u00bb\u00be\3\2\2\2\u00bc\u00be")
        buf.write("\3\2\2\2\u00bd\u00b9\3\2\2\2\u00bd\u00bc\3\2\2\2\u00be")
        buf.write("\13\3\2\2\2\u00bf\u00c0\7@\2\2\u00c0\u00c1\7B\2\2\u00c1")
        buf.write("\u00c2\5\4\3\2\u00c2\u00c3\7\n\2\2\u00c3\r\3\2\2\2\u00c4")
        buf.write("\u00c5\7@\2\2\u00c5\u00c6\7C\2\2\u00c6\u00c7\7\n\2\2\u00c7")
        buf.write("\17\3\2\2\2\u00c8\u00c9\5\22\n\2\u00c9\u00ca\5\20\t\2")
        buf.write("\u00ca\u00cd\3\2\2\2\u00cb\u00cd\3\2\2\2\u00cc\u00c8\3")
        buf.write("\2\2\2\u00cc\u00cb\3\2\2\2\u00cd\21\3\2\2\2\u00ce\u00cf")
        buf.write("\7>\2\2\u00cf\u00d0\7H\2\2\u00d0\u00d1\7\n\2\2\u00d1\23")
        buf.write("\3\2\2\2\u00d2\u00d3\7\b\2\2\u00d3\u00d4\7\61\2\2\u00d4")
        buf.write("\u00d5\7\6\2\2\u00d5\u00d6\5B\"\2\u00d6\u00d7\7\7\2\2")
        buf.write("\u00d7\u00d8\7\t\2\2\u00d8\u00db\3\2\2\2\u00d9\u00db\3")
        buf.write("\2\2\2\u00da\u00d2\3\2\2\2\u00da\u00d9\3\2\2\2\u00db\25")
        buf.write("\3\2\2\2\u00dc\u00dd\7\63\2\2\u00dd\u00de\7E\2\2\u00de")
        buf.write("\u00df\5\24\13\2\u00df\u00e0\7,\2\2\u00e0\u00e1\5j\66")
        buf.write("\2\u00e1\u00e2\7\n\2\2\u00e2\27\3\2\2\2\u00e3\u00e4\7")
        buf.write("\65\2\2\u00e4\u00e5\7K\2\2\u00e5\u00e6\7\4\2\2\u00e6\u00e7")
        buf.write("\5\34\17\2\u00e7\u00e8\7\5\2\2\u00e8\u00e9\5\"\22\2\u00e9")
        buf.write("\31\3\2\2\2\u00ea\u00eb\7\62\2\2\u00eb\u00ec\5\36\20\2")
        buf.write("\u00ec\u00ed\5 \21\2\u00ed\u00ee\7K\2\2\u00ee\u00ef\7")
        buf.write("\4\2\2\u00ef\u00f0\5\34\17\2\u00f0\u00f1\7\5\2\2\u00f1")
        buf.write("\u00f2\5\"\22\2\u00f2\33\3\2\2\2\u00f3\u00f6\5B\"\2\u00f4")
        buf.write("\u00f6\3\2\2\2\u00f5\u00f3\3\2\2\2\u00f5\u00f4\3\2\2\2")
        buf.write("\u00f6\35\3\2\2\2\u00f7\u00fa\7D\2\2\u00f8\u00fa\3\2\2")
        buf.write("\2\u00f9\u00f7\3\2\2\2\u00f9\u00f8\3\2\2\2\u00fa\37\3")
        buf.write("\2\2\2\u00fb\u00fe\7?\2\2\u00fc\u00fe\3\2\2\2\u00fd\u00fb")
        buf.write("\3\2\2\2\u00fd\u00fc\3\2\2\2\u00fe!\3\2\2\2\u00ff\u0100")
        buf.write("\7\b\2\2\u0100\u0101\5&\24\2\u0101\u0102\7\t\2\2\u0102")
        buf.write("#\3\2\2\2\u0103\u0107\5(\25\2\u0104\u0107\5\60\31\2\u0105")
        buf.write("\u0107\5\62\32\2\u0106\u0103\3\2\2\2\u0106\u0104\3\2\2")
        buf.write("\2\u0106\u0105\3\2\2\2\u0107%\3\2\2\2\u0108\u0109\5$\23")
        buf.write("\2\u0109\u010a\5&\24\2\u010a\u010d\3\2\2\2\u010b\u010d")
        buf.write("\3\2\2\2\u010c\u0108\3\2\2\2\u010c\u010b\3\2\2\2\u010d")
        buf.write("\'\3\2\2\2\u010e\u010f\5@!\2\u010f\u0110\7\n\2\2\u0110")
        buf.write(")\3\2\2\2\u0111\u0112\5j\66\2\u0112\u0113\7\n\2\2\u0113")
        buf.write("+\3\2\2\2\u0114\u0115\5j\66\2\u0115\u0116\5\u009eP\2\u0116")
        buf.write("\u0117\5j\66\2\u0117\u0128\3\2\2\2\u0118\u0119\5j\66\2")
        buf.write("\u0119\u011a\7\24\2\2\u011a\u011b\5j\66\2\u011b\u0128")
        buf.write("\3\2\2\2\u011c\u011d\5j\66\2\u011d\u011e\7\23\2\2\u011e")
        buf.write("\u011f\5j\66\2\u011f\u0128\3\2\2\2\u0120\u0121\5h\65\2")
        buf.write("\u0121\u0122\7-\2\2\u0122\u0123\5j\66\2\u0123\u0128\3")
        buf.write("\2\2\2\u0124\u0125\5h\65\2\u0125\u0126\7\25\2\2\u0126")
        buf.write("\u0128\3\2\2\2\u0127\u0114\3\2\2\2\u0127\u0118\3\2\2\2")
        buf.write("\u0127\u011c\3\2\2\2\u0127\u0120\3\2\2\2\u0127\u0124\3")
        buf.write("\2\2\2\u0128-\3\2\2\2\u0129\u012a\5,\27\2\u012a\u012b")
        buf.write("\7\n\2\2\u012b/\3\2\2\2\u012c\u012d\7\67\2\2\u012d\u012e")
        buf.write("\7\4\2\2\u012e\u012f\5j\66\2\u012f\u0130\7\5\2\2\u0130")
        buf.write("\u0131\5\60\31\2\u0131\u0149\3\2\2\2\u0132\u0133\7\67")
        buf.write("\2\2\u0133\u0134\7\4\2\2\u0134\u0135\5j\66\2\u0135\u0136")
        buf.write("\7\5\2\2\u0136\u0137\5\62\32\2\u0137\u0149\3\2\2\2\u0138")
        buf.write("\u0139\7\67\2\2\u0139\u013a\7\4\2\2\u013a\u013b\5j\66")
        buf.write("\2\u013b\u013c\7\5\2\2\u013c\u013d\5\62\32\2\u013d\u013e")
        buf.write("\78\2\2\u013e\u013f\5\60\31\2\u013f\u0149\3\2\2\2\u0140")
        buf.write("\u0141\7\67\2\2\u0141\u0142\7\4\2\2\u0142\u0143\5j\66")
        buf.write("\2\u0143\u0144\7\5\2\2\u0144\u0145\5\62\32\2\u0145\u0146")
        buf.write("\78\2\2\u0146\u0147\5\62\32\2\u0147\u0149\3\2\2\2\u0148")
        buf.write("\u012c\3\2\2\2\u0148\u0132\3\2\2\2\u0148\u0138\3\2\2\2")
        buf.write("\u0148\u0140\3\2\2\2\u0149\61\3\2\2\2\u014a\u0154\5\"")
        buf.write("\22\2\u014b\u0154\5*\26\2\u014c\u0154\5.\30\2\u014d\u0154")
        buf.write("\5\64\33\2\u014e\u0154\5\66\34\2\u014f\u0154\58\35\2\u0150")
        buf.write("\u0154\5:\36\2\u0151\u0154\5<\37\2\u0152\u0154\5> \2\u0153")
        buf.write("\u014a\3\2\2\2\u0153\u014b\3\2\2\2\u0153\u014c\3\2\2\2")
        buf.write("\u0153\u014d\3\2\2\2\u0153\u014e\3\2\2\2\u0153\u014f\3")
        buf.write("\2\2\2\u0153\u0150\3\2\2\2\u0153\u0151\3\2\2\2\u0153\u0152")
        buf.write("\3\2\2\2\u0154\63\3\2\2\2\u0155\u0156\79\2\2\u0156\u0157")
        buf.write("\7\4\2\2\u0157\u0158\5@!\2\u0158\u0159\7\n\2\2\u0159\u015a")
        buf.write("\5j\66\2\u015a\u015b\7\n\2\2\u015b\u015c\5,\27\2\u015c")
        buf.write("\u015d\7\5\2\2\u015d\u015e\5\62\32\2\u015e\u016a\3\2\2")
        buf.write("\2\u015f\u0160\79\2\2\u0160\u0161\7\4\2\2\u0161\u0162")
        buf.write("\5,\27\2\u0162\u0163\7\n\2\2\u0163\u0164\5j\66\2\u0164")
        buf.write("\u0165\7\n\2\2\u0165\u0166\5,\27\2\u0166\u0167\7\5\2\2")
        buf.write("\u0167\u0168\5\62\32\2\u0168\u016a\3\2\2\2\u0169\u0155")
        buf.write("\3\2\2\2\u0169\u015f\3\2\2\2\u016a\65\3\2\2\2\u016b\u016c")
        buf.write("\7:\2\2\u016c\u016d\7\4\2\2\u016d\u016e\5j\66\2\u016e")
        buf.write("\u016f\7\5\2\2\u016f\u0170\5\62\32\2\u0170\67\3\2\2\2")
        buf.write("\u0171\u0172\5j\66\2\u0172\u0173\7\20\2\2\u0173\u0174")
        buf.write("\5j\66\2\u0174\u0175\7\n\2\2\u01759\3\2\2\2\u0176\u0177")
        buf.write("\7\66\2\2\u0177\u0178\5j\66\2\u0178\u0179\7\n\2\2\u0179")
        buf.write(";\3\2\2\2\u017a\u017b\7=\2\2\u017b\u017c\7\4\2\2\u017c")
        buf.write("\u017d\5j\66\2\u017d\u017e\7\5\2\2\u017e\u017f\7\n\2\2")
        buf.write("\u017f=\3\2\2\2\u0180\u0181\7<\2\2\u0181\u0182\7\4\2\2")
        buf.write("\u0182\u0183\5\u008cG\2\u0183\u0184\7\5\2\2\u0184\u0185")
        buf.write("\7\n\2\2\u0185\u018b\3\2\2\2\u0186\u0187\7<\2\2\u0187")
        buf.write("\u0188\7\4\2\2\u0188\u0189\7\5\2\2\u0189\u018b\7\n\2\2")
        buf.write("\u018a\u0180\3\2\2\2\u018a\u0186\3\2\2\2\u018b?\3\2\2")
        buf.write("\2\u018c\u0190\5R*\2\u018d\u0190\5T+\2\u018e\u0190\5\\")
        buf.write("/\2\u018f\u018c\3\2\2\2\u018f\u018d\3\2\2\2\u018f\u018e")
        buf.write("\3\2\2\2\u0190A\3\2\2\2\u0191\u0192\7K\2\2\u0192\u0193")
        buf.write("\7\f\2\2\u0193\u0196\5B\"\2\u0194\u0196\7K\2\2\u0195\u0191")
        buf.write("\3\2\2\2\u0195\u0194\3\2\2\2\u0196C\3\2\2\2\u0197\u0198")
        buf.write("\7\b\2\2\u0198\u0199\5B\"\2\u0199\u019a\7\t\2\2\u019a")
        buf.write("E\3\2\2\2\u019b\u019c\5\u009eP\2\u019c\u019d\5j\66\2\u019d")
        buf.write("G\3\2\2\2\u019e\u019f\7K\2\2\u019f\u01a0\5d\63\2\u01a0")
        buf.write("I\3\2\2\2\u01a1\u01a2\5H%\2\u01a2\u01a3\7\f\2\2\u01a3")
        buf.write("\u01a4\5J&\2\u01a4\u01a7\3\2\2\2\u01a5\u01a7\5H%\2\u01a6")
        buf.write("\u01a1\3\2\2\2\u01a6\u01a5\3\2\2\2\u01a7K\3\2\2\2\u01a8")
        buf.write("\u01a9\7K\2\2\u01a9\u01aa\5d\63\2\u01aa\u01ab\7,\2\2\u01ab")
        buf.write("\u01ac\5j\66\2\u01acM\3\2\2\2\u01ad\u01b0\5H%\2\u01ae")
        buf.write("\u01b0\5L\'\2\u01af\u01ad\3\2\2\2\u01af\u01ae\3\2\2\2")
        buf.write("\u01b0O\3\2\2\2\u01b1\u01b2\5N(\2\u01b2\u01b3\7\f\2\2")
        buf.write("\u01b3\u01b4\5P)\2\u01b4\u01b7\3\2\2\2\u01b5\u01b7\5N")
        buf.write("(\2\u01b6\u01b1\3\2\2\2\u01b6\u01b5\3\2\2\2\u01b7Q\3\2")
        buf.write("\2\2\u01b8\u01b9\7\64\2\2\u01b9\u01c6\5P)\2\u01ba\u01bb")
        buf.write("\7\64\2\2\u01bb\u01bc\7\4\2\2\u01bc\u01bd\5J&\2\u01bd")
        buf.write("\u01be\7\5\2\2\u01be\u01c6\3\2\2\2\u01bf\u01c0\7\64\2")
        buf.write("\2\u01c0\u01c1\7\4\2\2\u01c1\u01c2\5J&\2\u01c2\u01c3\7")
        buf.write("\5\2\2\u01c3\u01c4\5F$\2\u01c4\u01c6\3\2\2\2\u01c5\u01b8")
        buf.write("\3\2\2\2\u01c5\u01ba\3\2\2\2\u01c5\u01bf\3\2\2\2\u01c6")
        buf.write("S\3\2\2\2\u01c7\u01c8\5V,\2\u01c8\u01c9\5Z.\2\u01c9\u01d6")
        buf.write("\3\2\2\2\u01ca\u01cb\5V,\2\u01cb\u01cc\7\4\2\2\u01cc\u01cd")
        buf.write("\5J&\2\u01cd\u01ce\7\5\2\2\u01ce\u01d6\3\2\2\2\u01cf\u01d0")
        buf.write("\5V,\2\u01d0\u01d1\7\4\2\2\u01d1\u01d2\5J&\2\u01d2\u01d3")
        buf.write("\7\5\2\2\u01d3\u01d4\5F$\2\u01d4\u01d6\3\2\2\2\u01d5\u01c7")
        buf.write("\3\2\2\2\u01d5\u01ca\3\2\2\2\u01d5\u01cf\3\2\2\2\u01d6")
        buf.write("U\3\2\2\2\u01d7\u01e0\7.\2\2\u01d8\u01d9\7.\2\2\u01d9")
        buf.write("\u01e0\7\3\2\2\u01da\u01db\7.\2\2\u01db\u01e0\5D#\2\u01dc")
        buf.write("\u01dd\7.\2\2\u01dd\u01de\7\3\2\2\u01de\u01e0\5D#\2\u01df")
        buf.write("\u01d7\3\2\2\2\u01df\u01d8\3\2\2\2\u01df\u01da\3\2\2\2")
        buf.write("\u01df\u01dc\3\2\2\2\u01e0W\3\2\2\2\u01e1\u01ed\5H%\2")
        buf.write("\u01e2\u01e3\7K\2\2\u01e3\u01e4\5d\63\2\u01e4\u01e5\7")
        buf.write("\21\2\2\u01e5\u01e6\5j\66\2\u01e6\u01ed\3\2\2\2\u01e7")
        buf.write("\u01e8\7K\2\2\u01e8\u01e9\5d\63\2\u01e9\u01ea\7\22\2\2")
        buf.write("\u01ea\u01eb\5j\66\2\u01eb\u01ed\3\2\2\2\u01ec\u01e1\3")
        buf.write("\2\2\2\u01ec\u01e2\3\2\2\2\u01ec\u01e7\3\2\2\2\u01edY")
        buf.write("\3\2\2\2\u01ee\u01ef\5X-\2\u01ef\u01f0\7\f\2\2\u01f0\u01f1")
        buf.write("\5Z.\2\u01f1\u01f4\3\2\2\2\u01f2\u01f4\5X-\2\u01f3\u01ee")
        buf.write("\3\2\2\2\u01f3\u01f2\3\2\2\2\u01f4[\3\2\2\2\u01f5\u01f6")
        buf.write("\7\63\2\2\u01f6\u0203\5P)\2\u01f7\u01f8\7\63\2\2\u01f8")
        buf.write("\u01f9\7\4\2\2\u01f9\u01fa\5J&\2\u01fa\u01fb\7\5\2\2\u01fb")
        buf.write("\u0203\3\2\2\2\u01fc\u01fd\7\63\2\2\u01fd\u01fe\7\4\2")
        buf.write("\2\u01fe\u01ff\5J&\2\u01ff\u0200\7\5\2\2\u0200\u0201\5")
        buf.write("F$\2\u0201\u0203\3\2\2\2\u0202\u01f5\3\2\2\2\u0202\u01f7")
        buf.write("\3\2\2\2\u0202\u01fc\3\2\2\2\u0203]\3\2\2\2\u0204\u0207")
        buf.write("\5b\62\2\u0205\u0207\5f\64\2\u0206\u0204\3\2\2\2\u0206")
        buf.write("\u0205\3\2\2\2\u0207_\3\2\2\2\u0208\u0209\5^\60\2\u0209")
        buf.write("\u020a\5`\61\2\u020a\u020d\3\2\2\2\u020b\u020d\3\2\2\2")
        buf.write("\u020c\u0208\3\2\2\2\u020c\u020b\3\2\2\2\u020da\3\2\2")
        buf.write("\2\u020e\u020f\7\6\2\2\u020f\u0210\5j\66\2\u0210\u0211")
        buf.write("\7\7\2\2\u0211c\3\2\2\2\u0212\u0213\5b\62\2\u0213\u0214")
        buf.write("\5d\63\2\u0214\u0217\3\2\2\2\u0215\u0217\3\2\2\2\u0216")
        buf.write("\u0212\3\2\2\2\u0216\u0215\3\2\2\2\u0217e\3\2\2\2\u0218")
        buf.write("\u0219\7\13\2\2\u0219\u021a\7K\2\2\u021ag\3\2\2\2\u021b")
        buf.write("\u021c\7K\2\2\u021c\u021d\5`\61\2\u021di\3\2\2\2\u021e")
        buf.write("\u021f\7?\2\2\u021f\u0222\5l\67\2\u0220\u0222\5l\67\2")
        buf.write("\u0221\u021e\3\2\2\2\u0221\u0220\3\2\2\2\u0222k\3\2\2")
        buf.write("\2\u0223\u0224\5n8\2\u0224\u0225\7\16\2\2\u0225\u0226")
        buf.write("\5n8\2\u0226\u0227\7\17\2\2\u0227\u0228\5n8\2\u0228\u022b")
        buf.write("\3\2\2\2\u0229\u022b\5n8\2\u022a\u0223\3\2\2\2\u022a\u0229")
        buf.write("\3\2\2\2\u022bm\3\2\2\2\u022c\u022d\b8\1\2\u022d\u022e")
        buf.write("\5p9\2\u022e\u0234\3\2\2\2\u022f\u0230\f\4\2\2\u0230\u0231")
        buf.write("\7+\2\2\u0231\u0233\5p9\2\u0232\u022f\3\2\2\2\u0233\u0236")
        buf.write("\3\2\2\2\u0234\u0232\3\2\2\2\u0234\u0235\3\2\2\2\u0235")
        buf.write("o\3\2\2\2\u0236\u0234\3\2\2\2\u0237\u0238\b9\1\2\u0238")
        buf.write("\u0239\5r:\2\u0239\u023f\3\2\2\2\u023a\u023b\f\4\2\2\u023b")
        buf.write("\u023c\7*\2\2\u023c\u023e\5r:\2\u023d\u023a\3\2\2\2\u023e")
        buf.write("\u0241\3\2\2\2\u023f\u023d\3\2\2\2\u023f\u0240\3\2\2\2")
        buf.write("\u0240q\3\2\2\2\u0241\u023f\3\2\2\2\u0242\u0243\b:\1\2")
        buf.write("\u0243\u0244\5t;\2\u0244\u024b\3\2\2\2\u0245\u0246\f\4")
        buf.write("\2\2\u0246\u0247\5\u0096L\2\u0247\u0248\5t;\2\u0248\u024a")
        buf.write("\3\2\2\2\u0249\u0245\3\2\2\2\u024a\u024d\3\2\2\2\u024b")
        buf.write("\u0249\3\2\2\2\u024b\u024c\3\2\2\2\u024cs\3\2\2\2\u024d")
        buf.write("\u024b\3\2\2\2\u024e\u024f\b;\1\2\u024f\u0250\5v<\2\u0250")
        buf.write("\u0256\3\2\2\2\u0251\u0252\f\4\2\2\u0252\u0253\7#\2\2")
        buf.write("\u0253\u0255\5v<\2\u0254\u0251\3\2\2\2\u0255\u0258\3\2")
        buf.write("\2\2\u0256\u0254\3\2\2\2\u0256\u0257\3\2\2\2\u0257u\3")
        buf.write("\2\2\2\u0258\u0256\3\2\2\2\u0259\u025a\b<\1\2\u025a\u025b")
        buf.write("\5x=\2\u025b\u0261\3\2\2\2\u025c\u025d\f\4\2\2\u025d\u025e")
        buf.write("\7\"\2\2\u025e\u0260\5x=\2\u025f\u025c\3\2\2\2\u0260\u0263")
        buf.write("\3\2\2\2\u0261\u025f\3\2\2\2\u0261\u0262\3\2\2\2\u0262")
        buf.write("w\3\2\2\2\u0263\u0261\3\2\2\2\u0264\u0265\b=\1\2\u0265")
        buf.write("\u0266\5z>\2\u0266\u026c\3\2\2\2\u0267\u0268\f\4\2\2\u0268")
        buf.write("\u0269\7!\2\2\u0269\u026b\5z>\2\u026a\u0267\3\2\2\2\u026b")
        buf.write("\u026e\3\2\2\2\u026c\u026a\3\2\2\2\u026c\u026d\3\2\2\2")
        buf.write("\u026dy\3\2\2\2\u026e\u026c\3\2\2\2\u026f\u0270\b>\1\2")
        buf.write("\u0270\u0271\5|?\2\u0271\u0278\3\2\2\2\u0272\u0273\f\4")
        buf.write("\2\2\u0273\u0274\5\u0098M\2\u0274\u0275\5|?\2\u0275\u0277")
        buf.write("\3\2\2\2\u0276\u0272\3\2\2\2\u0277\u027a\3\2\2\2\u0278")
        buf.write("\u0276\3\2\2\2\u0278\u0279\3\2\2\2\u0279{\3\2\2\2\u027a")
        buf.write("\u0278\3\2\2\2\u027b\u027c\b?\1\2\u027c\u027d\5~@\2\u027d")
        buf.write("\u0284\3\2\2\2\u027e\u027f\f\4\2\2\u027f\u0280\5\u009a")
        buf.write("N\2\u0280\u0281\5~@\2\u0281\u0283\3\2\2\2\u0282\u027e")
        buf.write("\3\2\2\2\u0283\u0286\3\2\2\2\u0284\u0282\3\2\2\2\u0284")
        buf.write("\u0285\3\2\2\2\u0285}\3\2\2\2\u0286\u0284\3\2\2\2\u0287")
        buf.write("\u0288\b@\1\2\u0288\u0289\5\u0080A\2\u0289\u0290\3\2\2")
        buf.write("\2\u028a\u028b\f\4\2\2\u028b\u028c\5\u009cO\2\u028c\u028d")
        buf.write("\5\u0080A\2\u028d\u028f\3\2\2\2\u028e\u028a\3\2\2\2\u028f")
        buf.write("\u0292\3\2\2\2\u0290\u028e\3\2\2\2\u0290\u0291\3\2\2\2")
        buf.write("\u0291\177\3\2\2\2\u0292\u0290\3\2\2\2\u0293\u0294\bA")
        buf.write("\1\2\u0294\u0295\5\u0082B\2\u0295\u029b\3\2\2\2\u0296")
        buf.write("\u0297\f\4\2\2\u0297\u0298\7\30\2\2\u0298\u029a\5\u0082")
        buf.write("B\2\u0299\u0296\3\2\2\2\u029a\u029d\3\2\2\2\u029b\u0299")
        buf.write("\3\2\2\2\u029b\u029c\3\2\2\2\u029c\u0081\3\2\2\2\u029d")
        buf.write("\u029b\3\2\2\2\u029e\u029f\5\u0094K\2\u029f\u02a0\5\u0082")
        buf.write("B\2\u02a0\u02a3\3\2\2\2\u02a1\u02a3\5\u0084C\2\u02a2\u029e")
        buf.write("\3\2\2\2\u02a2\u02a1\3\2\2\2\u02a3\u0083\3\2\2\2\u02a4")
        buf.write("\u02a5\7K\2\2\u02a5\u02a6\7\4\2\2\u02a6\u02a7\5\u008e")
        buf.write("H\2\u02a7\u02a8\7\5\2\2\u02a8\u02a9\7\4\2\2\u02a9\u02aa")
        buf.write("\5\u0090I\2\u02aa\u02ab\7\5\2\2\u02ab\u02bb\3\2\2\2\u02ac")
        buf.write("\u02ad\7K\2\2\u02ad\u02ae\7\4\2\2\u02ae\u02af\5\u008e")
        buf.write("H\2\u02af\u02b0\7\5\2\2\u02b0\u02bb\3\2\2\2\u02b1\u02b2")
        buf.write("\7\6\2\2\u02b2\u02b3\5\u008eH\2\u02b3\u02b4\7\7\2\2\u02b4")
        buf.write("\u02bb\3\2\2\2\u02b5\u02b6\7\4\2\2\u02b6\u02b7\5\u0088")
        buf.write("E\2\u02b7\u02b8\7\5\2\2\u02b8\u02bb\3\2\2\2\u02b9\u02bb")
        buf.write("\5\u0086D\2\u02ba\u02a4\3\2\2\2\u02ba\u02ac\3\2\2\2\u02ba")
        buf.write("\u02b1\3\2\2\2\u02ba\u02b5\3\2\2\2\u02ba\u02b9\3\2\2\2")
        buf.write("\u02bb\u0085\3\2\2\2\u02bc\u02c5\5h\65\2\u02bd\u02c5\7")
        buf.write("\r\2\2\u02be\u02c5\7I\2\2\u02bf\u02c5\7J\2\2\u02c0\u02c1")
        buf.write("\7\4\2\2\u02c1\u02c2\5j\66\2\u02c2\u02c3\7\5\2\2\u02c3")
        buf.write("\u02c5\3\2\2\2\u02c4\u02bc\3\2\2\2\u02c4\u02bd\3\2\2\2")
        buf.write("\u02c4\u02be\3\2\2\2\u02c4\u02bf\3\2\2\2\u02c4\u02c0\3")
        buf.write("\2\2\2\u02c5\u0087\3\2\2\2\u02c6\u02c7\bE\1\2\u02c7\u02c8")
        buf.write("\5j\66\2\u02c8\u02c9\7\f\2\2\u02c9\u02ca\5j\66\2\u02ca")
        buf.write("\u02d0\3\2\2\2\u02cb\u02cc\f\4\2\2\u02cc\u02cd\7\f\2\2")
        buf.write("\u02cd\u02cf\5j\66\2\u02ce\u02cb\3\2\2\2\u02cf\u02d2\3")
        buf.write("\2\2\2\u02d0\u02ce\3\2\2\2\u02d0\u02d1\3\2\2\2\u02d1\u0089")
        buf.write("\3\2\2\2\u02d2\u02d0\3\2\2\2\u02d3\u02d6\5j\66\2\u02d4")
        buf.write("\u02d6\7H\2\2\u02d5\u02d3\3\2\2\2\u02d5\u02d4\3\2\2\2")
        buf.write("\u02d6\u008b\3\2\2\2\u02d7\u02d8\5\u008aF\2\u02d8\u02d9")
        buf.write("\7\f\2\2\u02d9\u02da\5\u008cG\2\u02da\u02dd\3\2\2\2\u02db")
        buf.write("\u02dd\5\u008aF\2\u02dc\u02d7\3\2\2\2\u02dc\u02db\3\2")
        buf.write("\2\2\u02dd\u008d\3\2\2\2\u02de\u02e4\5j\66\2\u02df\u02e0")
        buf.write("\5j\66\2\u02e0\u02e1\7\f\2\2\u02e1\u02e2\5\u008eH\2\u02e2")
        buf.write("\u02e4\3\2\2\2\u02e3\u02de\3\2\2\2\u02e3\u02df\3\2\2\2")
        buf.write("\u02e4\u008f\3\2\2\2\u02e5\u02e8\5\u008eH\2\u02e6\u02e8")
        buf.write("\5\u0092J\2\u02e7\u02e5\3\2\2\2\u02e7\u02e6\3\2\2\2\u02e8")
        buf.write("\u0091\3\2\2\2\u02e9\u02ea\bJ\1\2\u02ea\u02eb\7K\2\2\u02eb")
        buf.write("\u02ec\5\u009eP\2\u02ec\u02ed\5j\66\2\u02ed\u02f6\3\2")
        buf.write("\2\2\u02ee\u02ef\f\4\2\2\u02ef\u02f0\7\f\2\2\u02f0\u02f1")
        buf.write("\7K\2\2\u02f1\u02f2\5\u009eP\2\u02f2\u02f3\5j\66\2\u02f3")
        buf.write("\u02f5\3\2\2\2\u02f4\u02ee\3\2\2\2\u02f5\u02f8\3\2\2\2")
        buf.write("\u02f6\u02f4\3\2\2\2\u02f6\u02f7\3\2\2\2\u02f7\u0093\3")
        buf.write("\2\2\2\u02f8\u02f6\3\2\2\2\u02f9\u02fa\t\2\2\2\u02fa\u0095")
        buf.write("\3\2\2\2\u02fb\u02fc\t\3\2\2\u02fc\u0097\3\2\2\2\u02fd")
        buf.write("\u02fe\t\4\2\2\u02fe\u0099\3\2\2\2\u02ff\u0300\t\5\2\2")
        buf.write("\u0300\u009b\3\2\2\2\u0301\u0302\t\6\2\2\u0302\u009d\3")
        buf.write("\2\2\2\u0303\u0304\t\7\2\2\u0304\u009f\3\2\2\2\66\u00a1")
        buf.write("\u00a4\u00b3\u00b7\u00bd\u00cc\u00da\u00f5\u00f9\u00fd")
        buf.write("\u0106\u010c\u0127\u0148\u0153\u0169\u018a\u018f\u0195")
        buf.write("\u01a6\u01af\u01b6\u01c5\u01d5\u01df\u01ec\u01f3\u0202")
        buf.write("\u0206\u020c\u0216\u0221\u022a\u0234\u023f\u024b\u0256")
        buf.write("\u0261\u026c\u0278\u0284\u0290\u029b\u02a2\u02ba\u02c4")
        buf.write("\u02d0\u02d5\u02dc\u02e3\u02e7\u02f6")
        return buf.getvalue()


class CircomParser ( Parser ):

    grammarFileName = "Circom.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'('", "')'", "'['", "']'", 
                     "'{'", "'}'", "';'", "'.'", "','", "'_'", "'?'", "':'", 
                     "'==='", "'<=='", "'<--'", "'==>'", "'-->'", "<INVALID>", 
                     "'!'", "'~'", "'**'", "'*'", "'/'", "'\\'", "'%'", 
                     "'+'", "'-'", "'<<'", "'>>'", "'&'", "'^'", "'|'", 
                     "'=='", "'!='", "'>'", "'<'", "'<='", "'>='", "'&&'", 
                     "'||'", "'='", "<INVALID>", "'signal'", "'input'", 
                     "'output'", "'public'", "'template'", "'component'", 
                     "'var'", "'function'", "'return'", "'if'", "'else'", 
                     "'for'", "'while'", "'do'", "'log'", "'assert'", "'include'", 
                     "'parallel'", "'pragma'", "'bus'", "'circom'", "'custom_templates'", 
                     "'custom'", "'main'" ]

    symbolicNames = [ "<INVALID>", "SIGNAL_TYPE", "LP", "RP", "LB", "RB", 
                      "LC", "RC", "SEMICOLON", "DOT", "COMMA", "UNDERSCORE", 
                      "TERNARY_CONDITION", "TERNARY_ALTERNATIVE", "EQ_CONSTRAINT", 
                      "LEFT_CONSTRAINT", "LEFT_ASSIGNMENT", "RIGHT_CONSTRAINT", 
                      "RIGHT_ASSIGNMENT", "SELF_OP", "NOT", "BNOT", "POW", 
                      "MUL", "DIV", "QUO", "MOD", "ADD", "SUB", "SHL", "SHR", 
                      "BAND", "BXOR", "BOR", "EQ", "NEQ", "GT", "LT", "LE", 
                      "GE", "AND", "OR", "ASSIGNMENT", "ASSIGNMENT_WITH_OP", 
                      "SIGNAL", "INPUT", "OUTPUT", "PUBLIC", "TEMPLATE", 
                      "COMPONENT", "VAR", "FUNCTION", "RETURN", "IF", "ELSE", 
                      "FOR", "WHILE", "DO", "LOG", "ASSERT", "INCLUDE", 
                      "PARALLEL", "PRAGMA", "BUS", "CIRCOM", "CUSTOM_TEMPLATES", 
                      "CUSTOM", "MAIN", "SINGLE_LINE_COMMENT", "MULTI_LINES_COMMENT", 
                      "STRING", "NUMBER", "HEXNUMBER", "IDENTIFIER", "WHITESPACE" ]

    RULE_program = 0
    RULE_version = 1
    RULE_main_option = 2
    RULE_definition_block = 3
    RULE_definition_list = 4
    RULE_pragma_definition = 5
    RULE_custom_gate = 6
    RULE_include_list = 7
    RULE_include_definition = 8
    RULE_public_list = 9
    RULE_main_component = 10
    RULE_function_definition = 11
    RULE_template_definition = 12
    RULE_identifier_list_option = 13
    RULE_custom_option = 14
    RULE_parallel_option = 15
    RULE_block = 16
    RULE_statement = 17
    RULE_statement_list = 18
    RULE_declaration_statement = 19
    RULE_expression_statement = 20
    RULE_substitutions = 21
    RULE_substitutions_statement = 22
    RULE_if_statement = 23
    RULE_regular_statement = 24
    RULE_for_statement = 25
    RULE_while_statement = 26
    RULE_equal_constraint_statement = 27
    RULE_return_statement = 28
    RULE_assert_statement = 29
    RULE_log_statement = 30
    RULE_declaration = 31
    RULE_identifier_list = 32
    RULE_tag_list = 33
    RULE_tuple_initialization = 34
    RULE_simple_symbol = 35
    RULE_simple_symbol_list = 36
    RULE_complex_symbol = 37
    RULE_some_symbol = 38
    RULE_some_symbol_list = 39
    RULE_var_decl = 40
    RULE_signal_decl = 41
    RULE_signal_header = 42
    RULE_signal_symbol = 43
    RULE_signal_symbol_list = 44
    RULE_component_decl = 45
    RULE_var_access = 46
    RULE_var_access_list = 47
    RULE_array_access = 48
    RULE_array_access_list = 49
    RULE_component_access = 50
    RULE_variable = 51
    RULE_expression = 52
    RULE_expression1 = 53
    RULE_expression2 = 54
    RULE_expression3 = 55
    RULE_expression4 = 56
    RULE_expression5 = 57
    RULE_expression6 = 58
    RULE_expression7 = 59
    RULE_expression8 = 60
    RULE_expression9 = 61
    RULE_expression10 = 62
    RULE_expression11 = 63
    RULE_expression12 = 64
    RULE_expression13 = 65
    RULE_expression14 = 66
    RULE_twoElemsListable = 67
    RULE_log_arguement = 68
    RULE_log_list = 69
    RULE_listable = 70
    RULE_listableAnon = 71
    RULE_listableWithInputNames = 72
    RULE_prefixOpcode = 73
    RULE_compareOpcode = 74
    RULE_shiftOpcode = 75
    RULE_add_sub_opcode = 76
    RULE_mul_div_opcode = 77
    RULE_assign_opcode = 78

    ruleNames =  [ "program", "version", "main_option", "definition_block", 
                   "definition_list", "pragma_definition", "custom_gate", 
                   "include_list", "include_definition", "public_list", 
                   "main_component", "function_definition", "template_definition", 
                   "identifier_list_option", "custom_option", "parallel_option", 
                   "block", "statement", "statement_list", "declaration_statement", 
                   "expression_statement", "substitutions", "substitutions_statement", 
                   "if_statement", "regular_statement", "for_statement", 
                   "while_statement", "equal_constraint_statement", "return_statement", 
                   "assert_statement", "log_statement", "declaration", "identifier_list", 
                   "tag_list", "tuple_initialization", "simple_symbol", 
                   "simple_symbol_list", "complex_symbol", "some_symbol", 
                   "some_symbol_list", "var_decl", "signal_decl", "signal_header", 
                   "signal_symbol", "signal_symbol_list", "component_decl", 
                   "var_access", "var_access_list", "array_access", "array_access_list", 
                   "component_access", "variable", "expression", "expression1", 
                   "expression2", "expression3", "expression4", "expression5", 
                   "expression6", "expression7", "expression8", "expression9", 
                   "expression10", "expression11", "expression12", "expression13", 
                   "expression14", "twoElemsListable", "log_arguement", 
                   "log_list", "listable", "listableAnon", "listableWithInputNames", 
                   "prefixOpcode", "compareOpcode", "shiftOpcode", "add_sub_opcode", 
                   "mul_div_opcode", "assign_opcode" ]

    EOF = Token.EOF
    SIGNAL_TYPE=1
    LP=2
    RP=3
    LB=4
    RB=5
    LC=6
    RC=7
    SEMICOLON=8
    DOT=9
    COMMA=10
    UNDERSCORE=11
    TERNARY_CONDITION=12
    TERNARY_ALTERNATIVE=13
    EQ_CONSTRAINT=14
    LEFT_CONSTRAINT=15
    LEFT_ASSIGNMENT=16
    RIGHT_CONSTRAINT=17
    RIGHT_ASSIGNMENT=18
    SELF_OP=19
    NOT=20
    BNOT=21
    POW=22
    MUL=23
    DIV=24
    QUO=25
    MOD=26
    ADD=27
    SUB=28
    SHL=29
    SHR=30
    BAND=31
    BXOR=32
    BOR=33
    EQ=34
    NEQ=35
    GT=36
    LT=37
    LE=38
    GE=39
    AND=40
    OR=41
    ASSIGNMENT=42
    ASSIGNMENT_WITH_OP=43
    SIGNAL=44
    INPUT=45
    OUTPUT=46
    PUBLIC=47
    TEMPLATE=48
    COMPONENT=49
    VAR=50
    FUNCTION=51
    RETURN=52
    IF=53
    ELSE=54
    FOR=55
    WHILE=56
    DO=57
    LOG=58
    ASSERT=59
    INCLUDE=60
    PARALLEL=61
    PRAGMA=62
    BUS=63
    CIRCOM=64
    CUSTOM_TEMPLATES=65
    CUSTOM=66
    MAIN=67
    SINGLE_LINE_COMMENT=68
    MULTI_LINES_COMMENT=69
    STRING=70
    NUMBER=71
    HEXNUMBER=72
    IDENTIFIER=73
    WHITESPACE=74

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def include_list(self):
            return self.getTypedRuleContext(CircomParser.Include_listContext,0)


        def definition_list(self):
            return self.getTypedRuleContext(CircomParser.Definition_listContext,0)


        def main_option(self):
            return self.getTypedRuleContext(CircomParser.Main_optionContext,0)


        def EOF(self):
            return self.getToken(CircomParser.EOF, 0)

        def pragma_definition(self):
            return self.getTypedRuleContext(CircomParser.Pragma_definitionContext,0)


        def custom_gate(self):
            return self.getTypedRuleContext(CircomParser.Custom_gateContext,0)


        def getRuleIndex(self):
            return CircomParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = CircomParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 158
                self.pragma_definition()


            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CircomParser.PRAGMA:
                self.state = 161
                self.custom_gate()


            self.state = 164
            self.include_list()
            self.state = 165
            self.definition_list()
            self.state = 166
            self.main_option()
            self.state = 167
            self.match(CircomParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VersionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(CircomParser.NUMBER)
            else:
                return self.getToken(CircomParser.NUMBER, i)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(CircomParser.DOT)
            else:
                return self.getToken(CircomParser.DOT, i)

        def getRuleIndex(self):
            return CircomParser.RULE_version

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVersion" ):
                return visitor.visitVersion(self)
            else:
                return visitor.visitChildren(self)




    def version(self):

        localctx = CircomParser.VersionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_version)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(CircomParser.NUMBER)
            self.state = 170
            self.match(CircomParser.DOT)
            self.state = 171
            self.match(CircomParser.NUMBER)
            self.state = 172
            self.match(CircomParser.DOT)
            self.state = 173
            self.match(CircomParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Main_optionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def main_component(self):
            return self.getTypedRuleContext(CircomParser.Main_componentContext,0)


        def getRuleIndex(self):
            return CircomParser.RULE_main_option

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMain_option" ):
                return visitor.visitMain_option(self)
            else:
                return visitor.visitChildren(self)




    def main_option(self):

        localctx = CircomParser.Main_optionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_main_option)
        try:
            self.state = 177
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CircomParser.COMPONENT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                self.main_component()
                pass
            elif token in [CircomParser.EOF]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Definition_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_definition(self):
            return self.getTypedRuleContext(CircomParser.Function_definitionContext,0)


        def template_definition(self):
            return self.getTypedRuleContext(CircomParser.Template_definitionContext,0)


        def getRuleIndex(self):
            return CircomParser.RULE_definition_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefinition_block" ):
                return visitor.visitDefinition_block(self)
            else:
                return visitor.visitChildren(self)




    def definition_block(self):

        localctx = CircomParser.Definition_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_definition_block)
        try:
            self.state = 181
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CircomParser.FUNCTION]:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                self.function_definition()
                pass
            elif token in [CircomParser.TEMPLATE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 180
                self.template_definition()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Definition_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def definition_block(self):
            return self.getTypedRuleContext(CircomParser.Definition_blockContext,0)


        def definition_list(self):
            return self.getTypedRuleContext(CircomParser.Definition_listContext,0)


        def getRuleIndex(self):
            return CircomParser.RULE_definition_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefinition_list" ):
                return visitor.visitDefinition_list(self)
            else:
                return visitor.visitChildren(self)




    def definition_list(self):

        localctx = CircomParser.Definition_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_definition_list)
        try:
            self.state = 187
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CircomParser.TEMPLATE, CircomParser.FUNCTION]:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.definition_block()
                self.state = 184
                self.definition_list()
                pass
            elif token in [CircomParser.EOF, CircomParser.COMPONENT]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pragma_definitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRAGMA(self):
            return self.getToken(CircomParser.PRAGMA, 0)

        def CIRCOM(self):
            return self.getToken(CircomParser.CIRCOM, 0)

        def version(self):
            return self.getTypedRuleContext(CircomParser.VersionContext,0)


        def SEMICOLON(self):
            return self.getToken(CircomParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CircomParser.RULE_pragma_definition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPragma_definition" ):
                return visitor.visitPragma_definition(self)
            else:
                return visitor.visitChildren(self)




    def pragma_definition(self):

        localctx = CircomParser.Pragma_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_pragma_definition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(CircomParser.PRAGMA)
            self.state = 190
            self.match(CircomParser.CIRCOM)
            self.state = 191
            self.version()
            self.state = 192
            self.match(CircomParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Custom_gateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRAGMA(self):
            return self.getToken(CircomParser.PRAGMA, 0)

        def CUSTOM_TEMPLATES(self):
            return self.getToken(CircomParser.CUSTOM_TEMPLATES, 0)

        def SEMICOLON(self):
            return self.getToken(CircomParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CircomParser.RULE_custom_gate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCustom_gate" ):
                return visitor.visitCustom_gate(self)
            else:
                return visitor.visitChildren(self)




    def custom_gate(self):

        localctx = CircomParser.Custom_gateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_custom_gate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(CircomParser.PRAGMA)
            self.state = 195
            self.match(CircomParser.CUSTOM_TEMPLATES)
            self.state = 196
            self.match(CircomParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Include_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def include_definition(self):
            return self.getTypedRuleContext(CircomParser.Include_definitionContext,0)


        def include_list(self):
            return self.getTypedRuleContext(CircomParser.Include_listContext,0)


        def getRuleIndex(self):
            return CircomParser.RULE_include_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInclude_list" ):
                return visitor.visitInclude_list(self)
            else:
                return visitor.visitChildren(self)




    def include_list(self):

        localctx = CircomParser.Include_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_include_list)
        try:
            self.state = 202
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CircomParser.INCLUDE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 198
                self.include_definition()
                self.state = 199
                self.include_list()
                pass
            elif token in [CircomParser.EOF, CircomParser.TEMPLATE, CircomParser.COMPONENT, CircomParser.FUNCTION]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Include_definitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INCLUDE(self):
            return self.getToken(CircomParser.INCLUDE, 0)

        def STRING(self):
            return self.getToken(CircomParser.STRING, 0)

        def SEMICOLON(self):
            return self.getToken(CircomParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CircomParser.RULE_include_definition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInclude_definition" ):
                return visitor.visitInclude_definition(self)
            else:
                return visitor.visitChildren(self)




    def include_definition(self):

        localctx = CircomParser.Include_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_include_definition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(CircomParser.INCLUDE)
            self.state = 205
            self.match(CircomParser.STRING)
            self.state = 206
            self.match(CircomParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Public_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LC(self):
            return self.getToken(CircomParser.LC, 0)

        def PUBLIC(self):
            return self.getToken(CircomParser.PUBLIC, 0)

        def LB(self):
            return self.getToken(CircomParser.LB, 0)

        def identifier_list(self):
            return self.getTypedRuleContext(CircomParser.Identifier_listContext,0)


        def RB(self):
            return self.getToken(CircomParser.RB, 0)

        def RC(self):
            return self.getToken(CircomParser.RC, 0)

        def getRuleIndex(self):
            return CircomParser.RULE_public_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPublic_list" ):
                return visitor.visitPublic_list(self)
            else:
                return visitor.visitChildren(self)




    def public_list(self):

        localctx = CircomParser.Public_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_public_list)
        try:
            self.state = 216
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CircomParser.LC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                self.match(CircomParser.LC)
                self.state = 209
                self.match(CircomParser.PUBLIC)
                self.state = 210
                self.match(CircomParser.LB)
                self.state = 211
                self.identifier_list()
                self.state = 212
                self.match(CircomParser.RB)
                self.state = 213
                self.match(CircomParser.RC)
                pass
            elif token in [CircomParser.ASSIGNMENT]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Main_componentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMPONENT(self):
            return self.getToken(CircomParser.COMPONENT, 0)

        def MAIN(self):
            return self.getToken(CircomParser.MAIN, 0)

        def public_list(self):
            return self.getTypedRuleContext(CircomParser.Public_listContext,0)


        def ASSIGNMENT(self):
            return self.getToken(CircomParser.ASSIGNMENT, 0)

        def expression(self):
            return self.getTypedRuleContext(CircomParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(CircomParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CircomParser.RULE_main_component

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMain_component" ):
                return visitor.visitMain_component(self)
            else:
                return visitor.visitChildren(self)




    def main_component(self):

        localctx = CircomParser.Main_componentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_main_component)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.match(CircomParser.COMPONENT)
            self.state = 219
            self.match(CircomParser.MAIN)
            self.state = 220
            self.public_list()
            self.state = 221
            self.match(CircomParser.ASSIGNMENT)
            self.state = 222
            self.expression()
            self.state = 223
            self.match(CircomParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_definitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(CircomParser.FUNCTION, 0)

        def IDENTIFIER(self):
            return self.getToken(CircomParser.IDENTIFIER, 0)

        def LP(self):
            return self.getToken(CircomParser.LP, 0)

        def identifier_list_option(self):
            return self.getTypedRuleContext(CircomParser.Identifier_list_optionContext,0)


        def RP(self):
            return self.getToken(CircomParser.RP, 0)

        def block(self):
            return self.getTypedRuleContext(CircomParser.BlockContext,0)


        def getRuleIndex(self):
            return CircomParser.RULE_function_definition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_definition" ):
                return visitor.visitFunction_definition(self)
            else:
                return visitor.visitChildren(self)




    def function_definition(self):

        localctx = CircomParser.Function_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_function_definition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(CircomParser.FUNCTION)
            self.state = 226
            self.match(CircomParser.IDENTIFIER)
            self.state = 227
            self.match(CircomParser.LP)
            self.state = 228
            self.identifier_list_option()
            self.state = 229
            self.match(CircomParser.RP)
            self.state = 230
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Template_definitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEMPLATE(self):
            return self.getToken(CircomParser.TEMPLATE, 0)

        def custom_option(self):
            return self.getTypedRuleContext(CircomParser.Custom_optionContext,0)


        def parallel_option(self):
            return self.getTypedRuleContext(CircomParser.Parallel_optionContext,0)


        def IDENTIFIER(self):
            return self.getToken(CircomParser.IDENTIFIER, 0)

        def LP(self):
            return self.getToken(CircomParser.LP, 0)

        def identifier_list_option(self):
            return self.getTypedRuleContext(CircomParser.Identifier_list_optionContext,0)


        def RP(self):
            return self.getToken(CircomParser.RP, 0)

        def block(self):
            return self.getTypedRuleContext(CircomParser.BlockContext,0)


        def getRuleIndex(self):
            return CircomParser.RULE_template_definition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTemplate_definition" ):
                return visitor.visitTemplate_definition(self)
            else:
                return visitor.visitChildren(self)




    def template_definition(self):

        localctx = CircomParser.Template_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_template_definition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.match(CircomParser.TEMPLATE)
            self.state = 233
            self.custom_option()
            self.state = 234
            self.parallel_option()
            self.state = 235
            self.match(CircomParser.IDENTIFIER)
            self.state = 236
            self.match(CircomParser.LP)
            self.state = 237
            self.identifier_list_option()
            self.state = 238
            self.match(CircomParser.RP)
            self.state = 239
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Identifier_list_optionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier_list(self):
            return self.getTypedRuleContext(CircomParser.Identifier_listContext,0)


        def getRuleIndex(self):
            return CircomParser.RULE_identifier_list_option

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier_list_option" ):
                return visitor.visitIdentifier_list_option(self)
            else:
                return visitor.visitChildren(self)




    def identifier_list_option(self):

        localctx = CircomParser.Identifier_list_optionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_identifier_list_option)
        try:
            self.state = 243
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CircomParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 241
                self.identifier_list()
                pass
            elif token in [CircomParser.RP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Custom_optionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CUSTOM(self):
            return self.getToken(CircomParser.CUSTOM, 0)

        def getRuleIndex(self):
            return CircomParser.RULE_custom_option

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCustom_option" ):
                return visitor.visitCustom_option(self)
            else:
                return visitor.visitChildren(self)




    def custom_option(self):

        localctx = CircomParser.Custom_optionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_custom_option)
        try:
            self.state = 247
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CircomParser.CUSTOM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 245
                self.match(CircomParser.CUSTOM)
                pass
            elif token in [CircomParser.PARALLEL, CircomParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parallel_optionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARALLEL(self):
            return self.getToken(CircomParser.PARALLEL, 0)

        def getRuleIndex(self):
            return CircomParser.RULE_parallel_option

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParallel_option" ):
                return visitor.visitParallel_option(self)
            else:
                return visitor.visitChildren(self)




    def parallel_option(self):

        localctx = CircomParser.Parallel_optionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_parallel_option)
        try:
            self.state = 251
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CircomParser.PARALLEL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 249
                self.match(CircomParser.PARALLEL)
                pass
            elif token in [CircomParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LC(self):
            return self.getToken(CircomParser.LC, 0)

        def statement_list(self):
            return self.getTypedRuleContext(CircomParser.Statement_listContext,0)


        def RC(self):
            return self.getToken(CircomParser.RC, 0)

        def getRuleIndex(self):
            return CircomParser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = CircomParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.match(CircomParser.LC)
            self.state = 254
            self.statement_list()
            self.state = 255
            self.match(CircomParser.RC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration_statement(self):
            return self.getTypedRuleContext(CircomParser.Declaration_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(CircomParser.If_statementContext,0)


        def regular_statement(self):
            return self.getTypedRuleContext(CircomParser.Regular_statementContext,0)


        def getRuleIndex(self):
            return CircomParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = CircomParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_statement)
        try:
            self.state = 260
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CircomParser.SIGNAL, CircomParser.COMPONENT, CircomParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 257
                self.declaration_statement()
                pass
            elif token in [CircomParser.IF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 258
                self.if_statement()
                pass
            elif token in [CircomParser.LP, CircomParser.LB, CircomParser.LC, CircomParser.UNDERSCORE, CircomParser.NOT, CircomParser.BNOT, CircomParser.SUB, CircomParser.RETURN, CircomParser.FOR, CircomParser.WHILE, CircomParser.LOG, CircomParser.ASSERT, CircomParser.PARALLEL, CircomParser.NUMBER, CircomParser.HEXNUMBER, CircomParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 259
                self.regular_statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(CircomParser.StatementContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(CircomParser.Statement_listContext,0)


        def getRuleIndex(self):
            return CircomParser.RULE_statement_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_list" ):
                return visitor.visitStatement_list(self)
            else:
                return visitor.visitChildren(self)




    def statement_list(self):

        localctx = CircomParser.Statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_statement_list)
        try:
            self.state = 266
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CircomParser.LP, CircomParser.LB, CircomParser.LC, CircomParser.UNDERSCORE, CircomParser.NOT, CircomParser.BNOT, CircomParser.SUB, CircomParser.SIGNAL, CircomParser.COMPONENT, CircomParser.VAR, CircomParser.RETURN, CircomParser.IF, CircomParser.FOR, CircomParser.WHILE, CircomParser.LOG, CircomParser.ASSERT, CircomParser.PARALLEL, CircomParser.NUMBER, CircomParser.HEXNUMBER, CircomParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 262
                self.statement()
                self.state = 263
                self.statement_list()
                pass
            elif token in [CircomParser.RC]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaration_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(CircomParser.DeclarationContext,0)


        def SEMICOLON(self):
            return self.getToken(CircomParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CircomParser.RULE_declaration_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration_statement" ):
                return visitor.visitDeclaration_statement(self)
            else:
                return visitor.visitChildren(self)




    def declaration_statement(self):

        localctx = CircomParser.Declaration_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_declaration_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.declaration()
            self.state = 269
            self.match(CircomParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(CircomParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(CircomParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CircomParser.RULE_expression_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_statement" ):
                return visitor.visitExpression_statement(self)
            else:
                return visitor.visitChildren(self)




    def expression_statement(self):

        localctx = CircomParser.Expression_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_expression_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.expression()
            self.state = 272
            self.match(CircomParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubstitutionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircomParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CircomParser.ExpressionContext,i)


        def assign_opcode(self):
            return self.getTypedRuleContext(CircomParser.Assign_opcodeContext,0)


        def RIGHT_ASSIGNMENT(self):
            return self.getToken(CircomParser.RIGHT_ASSIGNMENT, 0)

        def RIGHT_CONSTRAINT(self):
            return self.getToken(CircomParser.RIGHT_CONSTRAINT, 0)

        def variable(self):
            return self.getTypedRuleContext(CircomParser.VariableContext,0)


        def ASSIGNMENT_WITH_OP(self):
            return self.getToken(CircomParser.ASSIGNMENT_WITH_OP, 0)

        def SELF_OP(self):
            return self.getToken(CircomParser.SELF_OP, 0)

        def getRuleIndex(self):
            return CircomParser.RULE_substitutions

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubstitutions" ):
                return visitor.visitSubstitutions(self)
            else:
                return visitor.visitChildren(self)




    def substitutions(self):

        localctx = CircomParser.SubstitutionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_substitutions)
        try:
            self.state = 293
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 274
                self.expression()
                self.state = 275
                self.assign_opcode()
                self.state = 276
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 278
                self.expression()
                self.state = 279
                self.match(CircomParser.RIGHT_ASSIGNMENT)
                self.state = 280
                self.expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 282
                self.expression()
                self.state = 283
                self.match(CircomParser.RIGHT_CONSTRAINT)
                self.state = 284
                self.expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 286
                self.variable()
                self.state = 287
                self.match(CircomParser.ASSIGNMENT_WITH_OP)
                self.state = 288
                self.expression()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 290
                self.variable()
                self.state = 291
                self.match(CircomParser.SELF_OP)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Substitutions_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def substitutions(self):
            return self.getTypedRuleContext(CircomParser.SubstitutionsContext,0)


        def SEMICOLON(self):
            return self.getToken(CircomParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CircomParser.RULE_substitutions_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubstitutions_statement" ):
                return visitor.visitSubstitutions_statement(self)
            else:
                return visitor.visitChildren(self)




    def substitutions_statement(self):

        localctx = CircomParser.Substitutions_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_substitutions_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.substitutions()
            self.state = 296
            self.match(CircomParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(CircomParser.IF, 0)

        def LP(self):
            return self.getToken(CircomParser.LP, 0)

        def expression(self):
            return self.getTypedRuleContext(CircomParser.ExpressionContext,0)


        def RP(self):
            return self.getToken(CircomParser.RP, 0)

        def if_statement(self):
            return self.getTypedRuleContext(CircomParser.If_statementContext,0)


        def regular_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircomParser.Regular_statementContext)
            else:
                return self.getTypedRuleContext(CircomParser.Regular_statementContext,i)


        def ELSE(self):
            return self.getToken(CircomParser.ELSE, 0)

        def getRuleIndex(self):
            return CircomParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = CircomParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_if_statement)
        try:
            self.state = 326
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 298
                self.match(CircomParser.IF)
                self.state = 299
                self.match(CircomParser.LP)
                self.state = 300
                self.expression()
                self.state = 301
                self.match(CircomParser.RP)
                self.state = 302
                self.if_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 304
                self.match(CircomParser.IF)
                self.state = 305
                self.match(CircomParser.LP)
                self.state = 306
                self.expression()
                self.state = 307
                self.match(CircomParser.RP)
                self.state = 308
                self.regular_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 310
                self.match(CircomParser.IF)
                self.state = 311
                self.match(CircomParser.LP)
                self.state = 312
                self.expression()
                self.state = 313
                self.match(CircomParser.RP)
                self.state = 314
                self.regular_statement()
                self.state = 315
                self.match(CircomParser.ELSE)
                self.state = 316
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 318
                self.match(CircomParser.IF)
                self.state = 319
                self.match(CircomParser.LP)
                self.state = 320
                self.expression()
                self.state = 321
                self.match(CircomParser.RP)
                self.state = 322
                self.regular_statement()
                self.state = 323
                self.match(CircomParser.ELSE)
                self.state = 324
                self.regular_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Regular_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(CircomParser.BlockContext,0)


        def expression_statement(self):
            return self.getTypedRuleContext(CircomParser.Expression_statementContext,0)


        def substitutions_statement(self):
            return self.getTypedRuleContext(CircomParser.Substitutions_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(CircomParser.For_statementContext,0)


        def while_statement(self):
            return self.getTypedRuleContext(CircomParser.While_statementContext,0)


        def equal_constraint_statement(self):
            return self.getTypedRuleContext(CircomParser.Equal_constraint_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(CircomParser.Return_statementContext,0)


        def assert_statement(self):
            return self.getTypedRuleContext(CircomParser.Assert_statementContext,0)


        def log_statement(self):
            return self.getTypedRuleContext(CircomParser.Log_statementContext,0)


        def getRuleIndex(self):
            return CircomParser.RULE_regular_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRegular_statement" ):
                return visitor.visitRegular_statement(self)
            else:
                return visitor.visitChildren(self)




    def regular_statement(self):

        localctx = CircomParser.Regular_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_regular_statement)
        try:
            self.state = 337
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 328
                self.block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 329
                self.expression_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 330
                self.substitutions_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 331
                self.for_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 332
                self.while_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 333
                self.equal_constraint_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 334
                self.return_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 335
                self.assert_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 336
                self.log_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(CircomParser.FOR, 0)

        def LP(self):
            return self.getToken(CircomParser.LP, 0)

        def declaration(self):
            return self.getTypedRuleContext(CircomParser.DeclarationContext,0)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(CircomParser.SEMICOLON)
            else:
                return self.getToken(CircomParser.SEMICOLON, i)

        def expression(self):
            return self.getTypedRuleContext(CircomParser.ExpressionContext,0)


        def substitutions(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircomParser.SubstitutionsContext)
            else:
                return self.getTypedRuleContext(CircomParser.SubstitutionsContext,i)


        def RP(self):
            return self.getToken(CircomParser.RP, 0)

        def regular_statement(self):
            return self.getTypedRuleContext(CircomParser.Regular_statementContext,0)


        def getRuleIndex(self):
            return CircomParser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = CircomParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_for_statement)
        try:
            self.state = 359
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 339
                self.match(CircomParser.FOR)
                self.state = 340
                self.match(CircomParser.LP)
                self.state = 341
                self.declaration()
                self.state = 342
                self.match(CircomParser.SEMICOLON)
                self.state = 343
                self.expression()
                self.state = 344
                self.match(CircomParser.SEMICOLON)
                self.state = 345
                self.substitutions()
                self.state = 346
                self.match(CircomParser.RP)
                self.state = 347
                self.regular_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 349
                self.match(CircomParser.FOR)
                self.state = 350
                self.match(CircomParser.LP)
                self.state = 351
                self.substitutions()
                self.state = 352
                self.match(CircomParser.SEMICOLON)
                self.state = 353
                self.expression()
                self.state = 354
                self.match(CircomParser.SEMICOLON)
                self.state = 355
                self.substitutions()
                self.state = 356
                self.match(CircomParser.RP)
                self.state = 357
                self.regular_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(CircomParser.WHILE, 0)

        def LP(self):
            return self.getToken(CircomParser.LP, 0)

        def expression(self):
            return self.getTypedRuleContext(CircomParser.ExpressionContext,0)


        def RP(self):
            return self.getToken(CircomParser.RP, 0)

        def regular_statement(self):
            return self.getTypedRuleContext(CircomParser.Regular_statementContext,0)


        def getRuleIndex(self):
            return CircomParser.RULE_while_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_statement" ):
                return visitor.visitWhile_statement(self)
            else:
                return visitor.visitChildren(self)




    def while_statement(self):

        localctx = CircomParser.While_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self.match(CircomParser.WHILE)
            self.state = 362
            self.match(CircomParser.LP)
            self.state = 363
            self.expression()
            self.state = 364
            self.match(CircomParser.RP)
            self.state = 365
            self.regular_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Equal_constraint_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircomParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CircomParser.ExpressionContext,i)


        def EQ_CONSTRAINT(self):
            return self.getToken(CircomParser.EQ_CONSTRAINT, 0)

        def SEMICOLON(self):
            return self.getToken(CircomParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CircomParser.RULE_equal_constraint_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqual_constraint_statement" ):
                return visitor.visitEqual_constraint_statement(self)
            else:
                return visitor.visitChildren(self)




    def equal_constraint_statement(self):

        localctx = CircomParser.Equal_constraint_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_equal_constraint_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.expression()
            self.state = 368
            self.match(CircomParser.EQ_CONSTRAINT)
            self.state = 369
            self.expression()
            self.state = 370
            self.match(CircomParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(CircomParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(CircomParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(CircomParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CircomParser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = CircomParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            self.match(CircomParser.RETURN)
            self.state = 373
            self.expression()
            self.state = 374
            self.match(CircomParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assert_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSERT(self):
            return self.getToken(CircomParser.ASSERT, 0)

        def LP(self):
            return self.getToken(CircomParser.LP, 0)

        def expression(self):
            return self.getTypedRuleContext(CircomParser.ExpressionContext,0)


        def RP(self):
            return self.getToken(CircomParser.RP, 0)

        def SEMICOLON(self):
            return self.getToken(CircomParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CircomParser.RULE_assert_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssert_statement" ):
                return visitor.visitAssert_statement(self)
            else:
                return visitor.visitChildren(self)




    def assert_statement(self):

        localctx = CircomParser.Assert_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_assert_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self.match(CircomParser.ASSERT)
            self.state = 377
            self.match(CircomParser.LP)
            self.state = 378
            self.expression()
            self.state = 379
            self.match(CircomParser.RP)
            self.state = 380
            self.match(CircomParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Log_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOG(self):
            return self.getToken(CircomParser.LOG, 0)

        def LP(self):
            return self.getToken(CircomParser.LP, 0)

        def log_list(self):
            return self.getTypedRuleContext(CircomParser.Log_listContext,0)


        def RP(self):
            return self.getToken(CircomParser.RP, 0)

        def SEMICOLON(self):
            return self.getToken(CircomParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CircomParser.RULE_log_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLog_statement" ):
                return visitor.visitLog_statement(self)
            else:
                return visitor.visitChildren(self)




    def log_statement(self):

        localctx = CircomParser.Log_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_log_statement)
        try:
            self.state = 392
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 382
                self.match(CircomParser.LOG)
                self.state = 383
                self.match(CircomParser.LP)
                self.state = 384
                self.log_list()
                self.state = 385
                self.match(CircomParser.RP)
                self.state = 386
                self.match(CircomParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 388
                self.match(CircomParser.LOG)
                self.state = 389
                self.match(CircomParser.LP)
                self.state = 390
                self.match(CircomParser.RP)
                self.state = 391
                self.match(CircomParser.SEMICOLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(CircomParser.Var_declContext,0)


        def signal_decl(self):
            return self.getTypedRuleContext(CircomParser.Signal_declContext,0)


        def component_decl(self):
            return self.getTypedRuleContext(CircomParser.Component_declContext,0)


        def getRuleIndex(self):
            return CircomParser.RULE_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = CircomParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_declaration)
        try:
            self.state = 397
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CircomParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 394
                self.var_decl()
                pass
            elif token in [CircomParser.SIGNAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 395
                self.signal_decl()
                pass
            elif token in [CircomParser.COMPONENT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 396
                self.component_decl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Identifier_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(CircomParser.IDENTIFIER, 0)

        def COMMA(self):
            return self.getToken(CircomParser.COMMA, 0)

        def identifier_list(self):
            return self.getTypedRuleContext(CircomParser.Identifier_listContext,0)


        def getRuleIndex(self):
            return CircomParser.RULE_identifier_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier_list" ):
                return visitor.visitIdentifier_list(self)
            else:
                return visitor.visitChildren(self)




    def identifier_list(self):

        localctx = CircomParser.Identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_identifier_list)
        try:
            self.state = 403
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 399
                self.match(CircomParser.IDENTIFIER)
                self.state = 400
                self.match(CircomParser.COMMA)
                self.state = 401
                self.identifier_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 402
                self.match(CircomParser.IDENTIFIER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tag_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LC(self):
            return self.getToken(CircomParser.LC, 0)

        def identifier_list(self):
            return self.getTypedRuleContext(CircomParser.Identifier_listContext,0)


        def RC(self):
            return self.getToken(CircomParser.RC, 0)

        def getRuleIndex(self):
            return CircomParser.RULE_tag_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTag_list" ):
                return visitor.visitTag_list(self)
            else:
                return visitor.visitChildren(self)




    def tag_list(self):

        localctx = CircomParser.Tag_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_tag_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
            self.match(CircomParser.LC)
            self.state = 406
            self.identifier_list()
            self.state = 407
            self.match(CircomParser.RC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tuple_initializationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_opcode(self):
            return self.getTypedRuleContext(CircomParser.Assign_opcodeContext,0)


        def expression(self):
            return self.getTypedRuleContext(CircomParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CircomParser.RULE_tuple_initialization

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTuple_initialization" ):
                return visitor.visitTuple_initialization(self)
            else:
                return visitor.visitChildren(self)




    def tuple_initialization(self):

        localctx = CircomParser.Tuple_initializationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_tuple_initialization)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409
            self.assign_opcode()
            self.state = 410
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Simple_symbolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(CircomParser.IDENTIFIER, 0)

        def array_access_list(self):
            return self.getTypedRuleContext(CircomParser.Array_access_listContext,0)


        def getRuleIndex(self):
            return CircomParser.RULE_simple_symbol

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimple_symbol" ):
                return visitor.visitSimple_symbol(self)
            else:
                return visitor.visitChildren(self)




    def simple_symbol(self):

        localctx = CircomParser.Simple_symbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_simple_symbol)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
            self.match(CircomParser.IDENTIFIER)
            self.state = 413
            self.array_access_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Simple_symbol_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple_symbol(self):
            return self.getTypedRuleContext(CircomParser.Simple_symbolContext,0)


        def COMMA(self):
            return self.getToken(CircomParser.COMMA, 0)

        def simple_symbol_list(self):
            return self.getTypedRuleContext(CircomParser.Simple_symbol_listContext,0)


        def getRuleIndex(self):
            return CircomParser.RULE_simple_symbol_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimple_symbol_list" ):
                return visitor.visitSimple_symbol_list(self)
            else:
                return visitor.visitChildren(self)




    def simple_symbol_list(self):

        localctx = CircomParser.Simple_symbol_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_simple_symbol_list)
        try:
            self.state = 420
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 415
                self.simple_symbol()
                self.state = 416
                self.match(CircomParser.COMMA)
                self.state = 417
                self.simple_symbol_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 419
                self.simple_symbol()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Complex_symbolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(CircomParser.IDENTIFIER, 0)

        def array_access_list(self):
            return self.getTypedRuleContext(CircomParser.Array_access_listContext,0)


        def ASSIGNMENT(self):
            return self.getToken(CircomParser.ASSIGNMENT, 0)

        def expression(self):
            return self.getTypedRuleContext(CircomParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CircomParser.RULE_complex_symbol

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComplex_symbol" ):
                return visitor.visitComplex_symbol(self)
            else:
                return visitor.visitChildren(self)




    def complex_symbol(self):

        localctx = CircomParser.Complex_symbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_complex_symbol)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.match(CircomParser.IDENTIFIER)
            self.state = 423
            self.array_access_list()
            self.state = 424
            self.match(CircomParser.ASSIGNMENT)
            self.state = 425
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Some_symbolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple_symbol(self):
            return self.getTypedRuleContext(CircomParser.Simple_symbolContext,0)


        def complex_symbol(self):
            return self.getTypedRuleContext(CircomParser.Complex_symbolContext,0)


        def getRuleIndex(self):
            return CircomParser.RULE_some_symbol

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSome_symbol" ):
                return visitor.visitSome_symbol(self)
            else:
                return visitor.visitChildren(self)




    def some_symbol(self):

        localctx = CircomParser.Some_symbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_some_symbol)
        try:
            self.state = 429
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 427
                self.simple_symbol()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 428
                self.complex_symbol()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Some_symbol_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def some_symbol(self):
            return self.getTypedRuleContext(CircomParser.Some_symbolContext,0)


        def COMMA(self):
            return self.getToken(CircomParser.COMMA, 0)

        def some_symbol_list(self):
            return self.getTypedRuleContext(CircomParser.Some_symbol_listContext,0)


        def getRuleIndex(self):
            return CircomParser.RULE_some_symbol_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSome_symbol_list" ):
                return visitor.visitSome_symbol_list(self)
            else:
                return visitor.visitChildren(self)




    def some_symbol_list(self):

        localctx = CircomParser.Some_symbol_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_some_symbol_list)
        try:
            self.state = 436
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 431
                self.some_symbol()
                self.state = 432
                self.match(CircomParser.COMMA)
                self.state = 433
                self.some_symbol_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 435
                self.some_symbol()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(CircomParser.VAR, 0)

        def some_symbol_list(self):
            return self.getTypedRuleContext(CircomParser.Some_symbol_listContext,0)


        def LP(self):
            return self.getToken(CircomParser.LP, 0)

        def simple_symbol_list(self):
            return self.getTypedRuleContext(CircomParser.Simple_symbol_listContext,0)


        def RP(self):
            return self.getToken(CircomParser.RP, 0)

        def tuple_initialization(self):
            return self.getTypedRuleContext(CircomParser.Tuple_initializationContext,0)


        def getRuleIndex(self):
            return CircomParser.RULE_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = CircomParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_var_decl)
        try:
            self.state = 451
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 438
                self.match(CircomParser.VAR)
                self.state = 439
                self.some_symbol_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 440
                self.match(CircomParser.VAR)
                self.state = 441
                self.match(CircomParser.LP)
                self.state = 442
                self.simple_symbol_list()
                self.state = 443
                self.match(CircomParser.RP)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 445
                self.match(CircomParser.VAR)
                self.state = 446
                self.match(CircomParser.LP)
                self.state = 447
                self.simple_symbol_list()
                self.state = 448
                self.match(CircomParser.RP)
                self.state = 449
                self.tuple_initialization()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Signal_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def signal_header(self):
            return self.getTypedRuleContext(CircomParser.Signal_headerContext,0)


        def signal_symbol_list(self):
            return self.getTypedRuleContext(CircomParser.Signal_symbol_listContext,0)


        def LP(self):
            return self.getToken(CircomParser.LP, 0)

        def simple_symbol_list(self):
            return self.getTypedRuleContext(CircomParser.Simple_symbol_listContext,0)


        def RP(self):
            return self.getToken(CircomParser.RP, 0)

        def tuple_initialization(self):
            return self.getTypedRuleContext(CircomParser.Tuple_initializationContext,0)


        def getRuleIndex(self):
            return CircomParser.RULE_signal_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSignal_decl" ):
                return visitor.visitSignal_decl(self)
            else:
                return visitor.visitChildren(self)




    def signal_decl(self):

        localctx = CircomParser.Signal_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_signal_decl)
        try:
            self.state = 467
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 453
                self.signal_header()
                self.state = 454
                self.signal_symbol_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 456
                self.signal_header()
                self.state = 457
                self.match(CircomParser.LP)
                self.state = 458
                self.simple_symbol_list()
                self.state = 459
                self.match(CircomParser.RP)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 461
                self.signal_header()
                self.state = 462
                self.match(CircomParser.LP)
                self.state = 463
                self.simple_symbol_list()
                self.state = 464
                self.match(CircomParser.RP)
                self.state = 465
                self.tuple_initialization()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Signal_headerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SIGNAL(self):
            return self.getToken(CircomParser.SIGNAL, 0)

        def SIGNAL_TYPE(self):
            return self.getToken(CircomParser.SIGNAL_TYPE, 0)

        def tag_list(self):
            return self.getTypedRuleContext(CircomParser.Tag_listContext,0)


        def getRuleIndex(self):
            return CircomParser.RULE_signal_header

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSignal_header" ):
                return visitor.visitSignal_header(self)
            else:
                return visitor.visitChildren(self)




    def signal_header(self):

        localctx = CircomParser.Signal_headerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_signal_header)
        try:
            self.state = 477
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 469
                self.match(CircomParser.SIGNAL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 470
                self.match(CircomParser.SIGNAL)
                self.state = 471
                self.match(CircomParser.SIGNAL_TYPE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 472
                self.match(CircomParser.SIGNAL)
                self.state = 473
                self.tag_list()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 474
                self.match(CircomParser.SIGNAL)
                self.state = 475
                self.match(CircomParser.SIGNAL_TYPE)
                self.state = 476
                self.tag_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Signal_symbolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple_symbol(self):
            return self.getTypedRuleContext(CircomParser.Simple_symbolContext,0)


        def IDENTIFIER(self):
            return self.getToken(CircomParser.IDENTIFIER, 0)

        def array_access_list(self):
            return self.getTypedRuleContext(CircomParser.Array_access_listContext,0)


        def LEFT_CONSTRAINT(self):
            return self.getToken(CircomParser.LEFT_CONSTRAINT, 0)

        def expression(self):
            return self.getTypedRuleContext(CircomParser.ExpressionContext,0)


        def LEFT_ASSIGNMENT(self):
            return self.getToken(CircomParser.LEFT_ASSIGNMENT, 0)

        def getRuleIndex(self):
            return CircomParser.RULE_signal_symbol

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSignal_symbol" ):
                return visitor.visitSignal_symbol(self)
            else:
                return visitor.visitChildren(self)




    def signal_symbol(self):

        localctx = CircomParser.Signal_symbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_signal_symbol)
        try:
            self.state = 490
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 479
                self.simple_symbol()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 480
                self.match(CircomParser.IDENTIFIER)
                self.state = 481
                self.array_access_list()
                self.state = 482
                self.match(CircomParser.LEFT_CONSTRAINT)
                self.state = 483
                self.expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 485
                self.match(CircomParser.IDENTIFIER)
                self.state = 486
                self.array_access_list()
                self.state = 487
                self.match(CircomParser.LEFT_ASSIGNMENT)
                self.state = 488
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Signal_symbol_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def signal_symbol(self):
            return self.getTypedRuleContext(CircomParser.Signal_symbolContext,0)


        def COMMA(self):
            return self.getToken(CircomParser.COMMA, 0)

        def signal_symbol_list(self):
            return self.getTypedRuleContext(CircomParser.Signal_symbol_listContext,0)


        def getRuleIndex(self):
            return CircomParser.RULE_signal_symbol_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSignal_symbol_list" ):
                return visitor.visitSignal_symbol_list(self)
            else:
                return visitor.visitChildren(self)




    def signal_symbol_list(self):

        localctx = CircomParser.Signal_symbol_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_signal_symbol_list)
        try:
            self.state = 497
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 492
                self.signal_symbol()
                self.state = 493
                self.match(CircomParser.COMMA)
                self.state = 494
                self.signal_symbol_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 496
                self.signal_symbol()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Component_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMPONENT(self):
            return self.getToken(CircomParser.COMPONENT, 0)

        def some_symbol_list(self):
            return self.getTypedRuleContext(CircomParser.Some_symbol_listContext,0)


        def LP(self):
            return self.getToken(CircomParser.LP, 0)

        def simple_symbol_list(self):
            return self.getTypedRuleContext(CircomParser.Simple_symbol_listContext,0)


        def RP(self):
            return self.getToken(CircomParser.RP, 0)

        def tuple_initialization(self):
            return self.getTypedRuleContext(CircomParser.Tuple_initializationContext,0)


        def getRuleIndex(self):
            return CircomParser.RULE_component_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComponent_decl" ):
                return visitor.visitComponent_decl(self)
            else:
                return visitor.visitChildren(self)




    def component_decl(self):

        localctx = CircomParser.Component_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_component_decl)
        try:
            self.state = 512
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 499
                self.match(CircomParser.COMPONENT)
                self.state = 500
                self.some_symbol_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 501
                self.match(CircomParser.COMPONENT)
                self.state = 502
                self.match(CircomParser.LP)
                self.state = 503
                self.simple_symbol_list()
                self.state = 504
                self.match(CircomParser.RP)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 506
                self.match(CircomParser.COMPONENT)
                self.state = 507
                self.match(CircomParser.LP)
                self.state = 508
                self.simple_symbol_list()
                self.state = 509
                self.match(CircomParser.RP)
                self.state = 510
                self.tuple_initialization()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_access(self):
            return self.getTypedRuleContext(CircomParser.Array_accessContext,0)


        def component_access(self):
            return self.getTypedRuleContext(CircomParser.Component_accessContext,0)


        def getRuleIndex(self):
            return CircomParser.RULE_var_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_access" ):
                return visitor.visitVar_access(self)
            else:
                return visitor.visitChildren(self)




    def var_access(self):

        localctx = CircomParser.Var_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_var_access)
        try:
            self.state = 516
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CircomParser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 514
                self.array_access()
                pass
            elif token in [CircomParser.DOT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 515
                self.component_access()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_access_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_access(self):
            return self.getTypedRuleContext(CircomParser.Var_accessContext,0)


        def var_access_list(self):
            return self.getTypedRuleContext(CircomParser.Var_access_listContext,0)


        def getRuleIndex(self):
            return CircomParser.RULE_var_access_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_access_list" ):
                return visitor.visitVar_access_list(self)
            else:
                return visitor.visitChildren(self)




    def var_access_list(self):

        localctx = CircomParser.Var_access_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_var_access_list)
        try:
            self.state = 522
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 518
                self.var_access()
                self.state = 519
                self.var_access_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(CircomParser.LB, 0)

        def expression(self):
            return self.getTypedRuleContext(CircomParser.ExpressionContext,0)


        def RB(self):
            return self.getToken(CircomParser.RB, 0)

        def getRuleIndex(self):
            return CircomParser.RULE_array_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_access" ):
                return visitor.visitArray_access(self)
            else:
                return visitor.visitChildren(self)




    def array_access(self):

        localctx = CircomParser.Array_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_array_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 524
            self.match(CircomParser.LB)
            self.state = 525
            self.expression()
            self.state = 526
            self.match(CircomParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_access_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_access(self):
            return self.getTypedRuleContext(CircomParser.Array_accessContext,0)


        def array_access_list(self):
            return self.getTypedRuleContext(CircomParser.Array_access_listContext,0)


        def getRuleIndex(self):
            return CircomParser.RULE_array_access_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_access_list" ):
                return visitor.visitArray_access_list(self)
            else:
                return visitor.visitChildren(self)




    def array_access_list(self):

        localctx = CircomParser.Array_access_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_array_access_list)
        try:
            self.state = 532
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CircomParser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 528
                self.array_access()
                self.state = 529
                self.array_access_list()
                pass
            elif token in [CircomParser.RP, CircomParser.SEMICOLON, CircomParser.COMMA, CircomParser.LEFT_CONSTRAINT, CircomParser.LEFT_ASSIGNMENT, CircomParser.ASSIGNMENT]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Component_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(CircomParser.DOT, 0)

        def IDENTIFIER(self):
            return self.getToken(CircomParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return CircomParser.RULE_component_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComponent_access" ):
                return visitor.visitComponent_access(self)
            else:
                return visitor.visitChildren(self)




    def component_access(self):

        localctx = CircomParser.Component_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_component_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 534
            self.match(CircomParser.DOT)
            self.state = 535
            self.match(CircomParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(CircomParser.IDENTIFIER, 0)

        def var_access_list(self):
            return self.getTypedRuleContext(CircomParser.Var_access_listContext,0)


        def getRuleIndex(self):
            return CircomParser.RULE_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = CircomParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 537
            self.match(CircomParser.IDENTIFIER)
            self.state = 538
            self.var_access_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARALLEL(self):
            return self.getToken(CircomParser.PARALLEL, 0)

        def expression1(self):
            return self.getTypedRuleContext(CircomParser.Expression1Context,0)


        def getRuleIndex(self):
            return CircomParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = CircomParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_expression)
        try:
            self.state = 543
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CircomParser.PARALLEL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 540
                self.match(CircomParser.PARALLEL)
                self.state = 541
                self.expression1()
                pass
            elif token in [CircomParser.LP, CircomParser.LB, CircomParser.UNDERSCORE, CircomParser.NOT, CircomParser.BNOT, CircomParser.SUB, CircomParser.NUMBER, CircomParser.HEXNUMBER, CircomParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 542
                self.expression1()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircomParser.Expression2Context)
            else:
                return self.getTypedRuleContext(CircomParser.Expression2Context,i)


        def TERNARY_CONDITION(self):
            return self.getToken(CircomParser.TERNARY_CONDITION, 0)

        def TERNARY_ALTERNATIVE(self):
            return self.getToken(CircomParser.TERNARY_ALTERNATIVE, 0)

        def getRuleIndex(self):
            return CircomParser.RULE_expression1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression1" ):
                return visitor.visitExpression1(self)
            else:
                return visitor.visitChildren(self)




    def expression1(self):

        localctx = CircomParser.Expression1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_expression1)
        try:
            self.state = 552
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 545
                self.expression2(0)
                self.state = 546
                self.match(CircomParser.TERNARY_CONDITION)
                self.state = 547
                self.expression2(0)
                self.state = 548
                self.match(CircomParser.TERNARY_ALTERNATIVE)
                self.state = 549
                self.expression2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 551
                self.expression2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression3(self):
            return self.getTypedRuleContext(CircomParser.Expression3Context,0)


        def expression2(self):
            return self.getTypedRuleContext(CircomParser.Expression2Context,0)


        def OR(self):
            return self.getToken(CircomParser.OR, 0)

        def getRuleIndex(self):
            return CircomParser.RULE_expression2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression2" ):
                return visitor.visitExpression2(self)
            else:
                return visitor.visitChildren(self)



    def expression2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CircomParser.Expression2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 108
        self.enterRecursionRule(localctx, 108, self.RULE_expression2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 555
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 562
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CircomParser.Expression2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                    self.state = 557
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 558
                    self.match(CircomParser.OR)
                    self.state = 559
                    self.expression3(0) 
                self.state = 564
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression4(self):
            return self.getTypedRuleContext(CircomParser.Expression4Context,0)


        def expression3(self):
            return self.getTypedRuleContext(CircomParser.Expression3Context,0)


        def AND(self):
            return self.getToken(CircomParser.AND, 0)

        def getRuleIndex(self):
            return CircomParser.RULE_expression3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression3" ):
                return visitor.visitExpression3(self)
            else:
                return visitor.visitChildren(self)



    def expression3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CircomParser.Expression3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 110
        self.enterRecursionRule(localctx, 110, self.RULE_expression3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 566
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 573
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CircomParser.Expression3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                    self.state = 568
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 569
                    self.match(CircomParser.AND)
                    self.state = 570
                    self.expression4(0) 
                self.state = 575
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression5(self):
            return self.getTypedRuleContext(CircomParser.Expression5Context,0)


        def expression4(self):
            return self.getTypedRuleContext(CircomParser.Expression4Context,0)


        def compareOpcode(self):
            return self.getTypedRuleContext(CircomParser.CompareOpcodeContext,0)


        def getRuleIndex(self):
            return CircomParser.RULE_expression4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression4" ):
                return visitor.visitExpression4(self)
            else:
                return visitor.visitChildren(self)



    def expression4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CircomParser.Expression4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 112
        self.enterRecursionRule(localctx, 112, self.RULE_expression4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 577
            self.expression5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 585
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CircomParser.Expression4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                    self.state = 579
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 580
                    self.compareOpcode()
                    self.state = 581
                    self.expression5(0) 
                self.state = 587
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression6(self):
            return self.getTypedRuleContext(CircomParser.Expression6Context,0)


        def expression5(self):
            return self.getTypedRuleContext(CircomParser.Expression5Context,0)


        def BOR(self):
            return self.getToken(CircomParser.BOR, 0)

        def getRuleIndex(self):
            return CircomParser.RULE_expression5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression5" ):
                return visitor.visitExpression5(self)
            else:
                return visitor.visitChildren(self)



    def expression5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CircomParser.Expression5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 114
        self.enterRecursionRule(localctx, 114, self.RULE_expression5, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 589
            self.expression6(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 596
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CircomParser.Expression5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression5)
                    self.state = 591
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 592
                    self.match(CircomParser.BOR)
                    self.state = 593
                    self.expression6(0) 
                self.state = 598
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression7(self):
            return self.getTypedRuleContext(CircomParser.Expression7Context,0)


        def expression6(self):
            return self.getTypedRuleContext(CircomParser.Expression6Context,0)


        def BXOR(self):
            return self.getToken(CircomParser.BXOR, 0)

        def getRuleIndex(self):
            return CircomParser.RULE_expression6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression6" ):
                return visitor.visitExpression6(self)
            else:
                return visitor.visitChildren(self)



    def expression6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CircomParser.Expression6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 116
        self.enterRecursionRule(localctx, 116, self.RULE_expression6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 600
            self.expression7(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 607
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CircomParser.Expression6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression6)
                    self.state = 602
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 603
                    self.match(CircomParser.BXOR)
                    self.state = 604
                    self.expression7(0) 
                self.state = 609
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression8(self):
            return self.getTypedRuleContext(CircomParser.Expression8Context,0)


        def expression7(self):
            return self.getTypedRuleContext(CircomParser.Expression7Context,0)


        def BAND(self):
            return self.getToken(CircomParser.BAND, 0)

        def getRuleIndex(self):
            return CircomParser.RULE_expression7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression7" ):
                return visitor.visitExpression7(self)
            else:
                return visitor.visitChildren(self)



    def expression7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CircomParser.Expression7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 118
        self.enterRecursionRule(localctx, 118, self.RULE_expression7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 611
            self.expression8(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 618
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CircomParser.Expression7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression7)
                    self.state = 613
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 614
                    self.match(CircomParser.BAND)
                    self.state = 615
                    self.expression8(0) 
                self.state = 620
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression9(self):
            return self.getTypedRuleContext(CircomParser.Expression9Context,0)


        def expression8(self):
            return self.getTypedRuleContext(CircomParser.Expression8Context,0)


        def shiftOpcode(self):
            return self.getTypedRuleContext(CircomParser.ShiftOpcodeContext,0)


        def getRuleIndex(self):
            return CircomParser.RULE_expression8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression8" ):
                return visitor.visitExpression8(self)
            else:
                return visitor.visitChildren(self)



    def expression8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CircomParser.Expression8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 120
        self.enterRecursionRule(localctx, 120, self.RULE_expression8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 622
            self.expression9(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 630
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CircomParser.Expression8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression8)
                    self.state = 624
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 625
                    self.shiftOpcode()
                    self.state = 626
                    self.expression9(0) 
                self.state = 632
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression10(self):
            return self.getTypedRuleContext(CircomParser.Expression10Context,0)


        def expression9(self):
            return self.getTypedRuleContext(CircomParser.Expression9Context,0)


        def add_sub_opcode(self):
            return self.getTypedRuleContext(CircomParser.Add_sub_opcodeContext,0)


        def getRuleIndex(self):
            return CircomParser.RULE_expression9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression9" ):
                return visitor.visitExpression9(self)
            else:
                return visitor.visitChildren(self)



    def expression9(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CircomParser.Expression9Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 122
        self.enterRecursionRule(localctx, 122, self.RULE_expression9, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 634
            self.expression10(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 642
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CircomParser.Expression9Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression9)
                    self.state = 636
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 637
                    self.add_sub_opcode()
                    self.state = 638
                    self.expression10(0) 
                self.state = 644
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression10Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression11(self):
            return self.getTypedRuleContext(CircomParser.Expression11Context,0)


        def expression10(self):
            return self.getTypedRuleContext(CircomParser.Expression10Context,0)


        def mul_div_opcode(self):
            return self.getTypedRuleContext(CircomParser.Mul_div_opcodeContext,0)


        def getRuleIndex(self):
            return CircomParser.RULE_expression10

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression10" ):
                return visitor.visitExpression10(self)
            else:
                return visitor.visitChildren(self)



    def expression10(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CircomParser.Expression10Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 124
        self.enterRecursionRule(localctx, 124, self.RULE_expression10, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 646
            self.expression11(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 654
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CircomParser.Expression10Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression10)
                    self.state = 648
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 649
                    self.mul_div_opcode()
                    self.state = 650
                    self.expression11(0) 
                self.state = 656
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression11Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression12(self):
            return self.getTypedRuleContext(CircomParser.Expression12Context,0)


        def expression11(self):
            return self.getTypedRuleContext(CircomParser.Expression11Context,0)


        def POW(self):
            return self.getToken(CircomParser.POW, 0)

        def getRuleIndex(self):
            return CircomParser.RULE_expression11

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression11" ):
                return visitor.visitExpression11(self)
            else:
                return visitor.visitChildren(self)



    def expression11(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CircomParser.Expression11Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 126
        self.enterRecursionRule(localctx, 126, self.RULE_expression11, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 658
            self.expression12()
            self._ctx.stop = self._input.LT(-1)
            self.state = 665
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CircomParser.Expression11Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression11)
                    self.state = 660
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 661
                    self.match(CircomParser.POW)
                    self.state = 662
                    self.expression12() 
                self.state = 667
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression12Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def prefixOpcode(self):
            return self.getTypedRuleContext(CircomParser.PrefixOpcodeContext,0)


        def expression12(self):
            return self.getTypedRuleContext(CircomParser.Expression12Context,0)


        def expression13(self):
            return self.getTypedRuleContext(CircomParser.Expression13Context,0)


        def getRuleIndex(self):
            return CircomParser.RULE_expression12

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression12" ):
                return visitor.visitExpression12(self)
            else:
                return visitor.visitChildren(self)




    def expression12(self):

        localctx = CircomParser.Expression12Context(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_expression12)
        try:
            self.state = 672
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CircomParser.NOT, CircomParser.BNOT, CircomParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 668
                self.prefixOpcode()
                self.state = 669
                self.expression12()
                pass
            elif token in [CircomParser.LP, CircomParser.LB, CircomParser.UNDERSCORE, CircomParser.NUMBER, CircomParser.HEXNUMBER, CircomParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 671
                self.expression13()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression13Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(CircomParser.IDENTIFIER, 0)

        def LP(self, i:int=None):
            if i is None:
                return self.getTokens(CircomParser.LP)
            else:
                return self.getToken(CircomParser.LP, i)

        def listable(self):
            return self.getTypedRuleContext(CircomParser.ListableContext,0)


        def RP(self, i:int=None):
            if i is None:
                return self.getTokens(CircomParser.RP)
            else:
                return self.getToken(CircomParser.RP, i)

        def listableAnon(self):
            return self.getTypedRuleContext(CircomParser.ListableAnonContext,0)


        def LB(self):
            return self.getToken(CircomParser.LB, 0)

        def RB(self):
            return self.getToken(CircomParser.RB, 0)

        def twoElemsListable(self):
            return self.getTypedRuleContext(CircomParser.TwoElemsListableContext,0)


        def expression14(self):
            return self.getTypedRuleContext(CircomParser.Expression14Context,0)


        def getRuleIndex(self):
            return CircomParser.RULE_expression13

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression13" ):
                return visitor.visitExpression13(self)
            else:
                return visitor.visitChildren(self)




    def expression13(self):

        localctx = CircomParser.Expression13Context(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_expression13)
        try:
            self.state = 696
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 674
                self.match(CircomParser.IDENTIFIER)
                self.state = 675
                self.match(CircomParser.LP)
                self.state = 676
                self.listable()
                self.state = 677
                self.match(CircomParser.RP)
                self.state = 678
                self.match(CircomParser.LP)
                self.state = 679
                self.listableAnon()
                self.state = 680
                self.match(CircomParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 682
                self.match(CircomParser.IDENTIFIER)
                self.state = 683
                self.match(CircomParser.LP)
                self.state = 684
                self.listable()
                self.state = 685
                self.match(CircomParser.RP)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 687
                self.match(CircomParser.LB)
                self.state = 688
                self.listable()
                self.state = 689
                self.match(CircomParser.RB)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 691
                self.match(CircomParser.LP)
                self.state = 692
                self.twoElemsListable(0)
                self.state = 693
                self.match(CircomParser.RP)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 695
                self.expression14()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression14Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(CircomParser.VariableContext,0)


        def UNDERSCORE(self):
            return self.getToken(CircomParser.UNDERSCORE, 0)

        def NUMBER(self):
            return self.getToken(CircomParser.NUMBER, 0)

        def HEXNUMBER(self):
            return self.getToken(CircomParser.HEXNUMBER, 0)

        def LP(self):
            return self.getToken(CircomParser.LP, 0)

        def expression(self):
            return self.getTypedRuleContext(CircomParser.ExpressionContext,0)


        def RP(self):
            return self.getToken(CircomParser.RP, 0)

        def getRuleIndex(self):
            return CircomParser.RULE_expression14

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression14" ):
                return visitor.visitExpression14(self)
            else:
                return visitor.visitChildren(self)




    def expression14(self):

        localctx = CircomParser.Expression14Context(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_expression14)
        try:
            self.state = 706
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CircomParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 698
                self.variable()
                pass
            elif token in [CircomParser.UNDERSCORE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 699
                self.match(CircomParser.UNDERSCORE)
                pass
            elif token in [CircomParser.NUMBER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 700
                self.match(CircomParser.NUMBER)
                pass
            elif token in [CircomParser.HEXNUMBER]:
                self.enterOuterAlt(localctx, 4)
                self.state = 701
                self.match(CircomParser.HEXNUMBER)
                pass
            elif token in [CircomParser.LP]:
                self.enterOuterAlt(localctx, 5)
                self.state = 702
                self.match(CircomParser.LP)
                self.state = 703
                self.expression()
                self.state = 704
                self.match(CircomParser.RP)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TwoElemsListableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CircomParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CircomParser.ExpressionContext,i)


        def COMMA(self):
            return self.getToken(CircomParser.COMMA, 0)

        def twoElemsListable(self):
            return self.getTypedRuleContext(CircomParser.TwoElemsListableContext,0)


        def getRuleIndex(self):
            return CircomParser.RULE_twoElemsListable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTwoElemsListable" ):
                return visitor.visitTwoElemsListable(self)
            else:
                return visitor.visitChildren(self)



    def twoElemsListable(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CircomParser.TwoElemsListableContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 134
        self.enterRecursionRule(localctx, 134, self.RULE_twoElemsListable, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 709
            self.expression()
            self.state = 710
            self.match(CircomParser.COMMA)
            self.state = 711
            self.expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 718
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,46,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CircomParser.TwoElemsListableContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_twoElemsListable)
                    self.state = 713
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 714
                    self.match(CircomParser.COMMA)
                    self.state = 715
                    self.expression() 
                self.state = 720
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,46,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Log_arguementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(CircomParser.ExpressionContext,0)


        def STRING(self):
            return self.getToken(CircomParser.STRING, 0)

        def getRuleIndex(self):
            return CircomParser.RULE_log_arguement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLog_arguement" ):
                return visitor.visitLog_arguement(self)
            else:
                return visitor.visitChildren(self)




    def log_arguement(self):

        localctx = CircomParser.Log_arguementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_log_arguement)
        try:
            self.state = 723
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CircomParser.LP, CircomParser.LB, CircomParser.UNDERSCORE, CircomParser.NOT, CircomParser.BNOT, CircomParser.SUB, CircomParser.PARALLEL, CircomParser.NUMBER, CircomParser.HEXNUMBER, CircomParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 721
                self.expression()
                pass
            elif token in [CircomParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 722
                self.match(CircomParser.STRING)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Log_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def log_arguement(self):
            return self.getTypedRuleContext(CircomParser.Log_arguementContext,0)


        def COMMA(self):
            return self.getToken(CircomParser.COMMA, 0)

        def log_list(self):
            return self.getTypedRuleContext(CircomParser.Log_listContext,0)


        def getRuleIndex(self):
            return CircomParser.RULE_log_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLog_list" ):
                return visitor.visitLog_list(self)
            else:
                return visitor.visitChildren(self)




    def log_list(self):

        localctx = CircomParser.Log_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_log_list)
        try:
            self.state = 730
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 725
                self.log_arguement()
                self.state = 726
                self.match(CircomParser.COMMA)
                self.state = 727
                self.log_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 729
                self.log_arguement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(CircomParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(CircomParser.COMMA, 0)

        def listable(self):
            return self.getTypedRuleContext(CircomParser.ListableContext,0)


        def getRuleIndex(self):
            return CircomParser.RULE_listable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListable" ):
                return visitor.visitListable(self)
            else:
                return visitor.visitChildren(self)




    def listable(self):

        localctx = CircomParser.ListableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_listable)
        try:
            self.state = 737
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 732
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 733
                self.expression()
                self.state = 734
                self.match(CircomParser.COMMA)
                self.state = 735
                self.listable()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListableAnonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def listable(self):
            return self.getTypedRuleContext(CircomParser.ListableContext,0)


        def listableWithInputNames(self):
            return self.getTypedRuleContext(CircomParser.ListableWithInputNamesContext,0)


        def getRuleIndex(self):
            return CircomParser.RULE_listableAnon

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListableAnon" ):
                return visitor.visitListableAnon(self)
            else:
                return visitor.visitChildren(self)




    def listableAnon(self):

        localctx = CircomParser.ListableAnonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_listableAnon)
        try:
            self.state = 741
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 739
                self.listable()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 740
                self.listableWithInputNames(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListableWithInputNamesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(CircomParser.IDENTIFIER, 0)

        def assign_opcode(self):
            return self.getTypedRuleContext(CircomParser.Assign_opcodeContext,0)


        def expression(self):
            return self.getTypedRuleContext(CircomParser.ExpressionContext,0)


        def listableWithInputNames(self):
            return self.getTypedRuleContext(CircomParser.ListableWithInputNamesContext,0)


        def COMMA(self):
            return self.getToken(CircomParser.COMMA, 0)

        def getRuleIndex(self):
            return CircomParser.RULE_listableWithInputNames

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListableWithInputNames" ):
                return visitor.visitListableWithInputNames(self)
            else:
                return visitor.visitChildren(self)



    def listableWithInputNames(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CircomParser.ListableWithInputNamesContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 144
        self.enterRecursionRule(localctx, 144, self.RULE_listableWithInputNames, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 744
            self.match(CircomParser.IDENTIFIER)
            self.state = 745
            self.assign_opcode()
            self.state = 746
            self.expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 756
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,51,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CircomParser.ListableWithInputNamesContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_listableWithInputNames)
                    self.state = 748
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 749
                    self.match(CircomParser.COMMA)
                    self.state = 750
                    self.match(CircomParser.IDENTIFIER)
                    self.state = 751
                    self.assign_opcode()
                    self.state = 752
                    self.expression() 
                self.state = 758
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,51,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PrefixOpcodeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(CircomParser.NOT, 0)

        def BNOT(self):
            return self.getToken(CircomParser.BNOT, 0)

        def SUB(self):
            return self.getToken(CircomParser.SUB, 0)

        def getRuleIndex(self):
            return CircomParser.RULE_prefixOpcode

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrefixOpcode" ):
                return visitor.visitPrefixOpcode(self)
            else:
                return visitor.visitChildren(self)




    def prefixOpcode(self):

        localctx = CircomParser.PrefixOpcodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 146, self.RULE_prefixOpcode)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 759
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CircomParser.NOT) | (1 << CircomParser.BNOT) | (1 << CircomParser.SUB))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompareOpcodeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(CircomParser.EQ, 0)

        def NEQ(self):
            return self.getToken(CircomParser.NEQ, 0)

        def GT(self):
            return self.getToken(CircomParser.GT, 0)

        def LT(self):
            return self.getToken(CircomParser.LT, 0)

        def GE(self):
            return self.getToken(CircomParser.GE, 0)

        def LE(self):
            return self.getToken(CircomParser.LE, 0)

        def getRuleIndex(self):
            return CircomParser.RULE_compareOpcode

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompareOpcode" ):
                return visitor.visitCompareOpcode(self)
            else:
                return visitor.visitChildren(self)




    def compareOpcode(self):

        localctx = CircomParser.CompareOpcodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 148, self.RULE_compareOpcode)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 761
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CircomParser.EQ) | (1 << CircomParser.NEQ) | (1 << CircomParser.GT) | (1 << CircomParser.LT) | (1 << CircomParser.LE) | (1 << CircomParser.GE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ShiftOpcodeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SHL(self):
            return self.getToken(CircomParser.SHL, 0)

        def SHR(self):
            return self.getToken(CircomParser.SHR, 0)

        def getRuleIndex(self):
            return CircomParser.RULE_shiftOpcode

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShiftOpcode" ):
                return visitor.visitShiftOpcode(self)
            else:
                return visitor.visitChildren(self)




    def shiftOpcode(self):

        localctx = CircomParser.ShiftOpcodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 150, self.RULE_shiftOpcode)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 763
            _la = self._input.LA(1)
            if not(_la==CircomParser.SHL or _la==CircomParser.SHR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Add_sub_opcodeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(CircomParser.ADD, 0)

        def SUB(self):
            return self.getToken(CircomParser.SUB, 0)

        def getRuleIndex(self):
            return CircomParser.RULE_add_sub_opcode

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd_sub_opcode" ):
                return visitor.visitAdd_sub_opcode(self)
            else:
                return visitor.visitChildren(self)




    def add_sub_opcode(self):

        localctx = CircomParser.Add_sub_opcodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_add_sub_opcode)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 765
            _la = self._input.LA(1)
            if not(_la==CircomParser.ADD or _la==CircomParser.SUB):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mul_div_opcodeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MUL(self):
            return self.getToken(CircomParser.MUL, 0)

        def DIV(self):
            return self.getToken(CircomParser.DIV, 0)

        def QUO(self):
            return self.getToken(CircomParser.QUO, 0)

        def MOD(self):
            return self.getToken(CircomParser.MOD, 0)

        def getRuleIndex(self):
            return CircomParser.RULE_mul_div_opcode

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMul_div_opcode" ):
                return visitor.visitMul_div_opcode(self)
            else:
                return visitor.visitChildren(self)




    def mul_div_opcode(self):

        localctx = CircomParser.Mul_div_opcodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 154, self.RULE_mul_div_opcode)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 767
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CircomParser.MUL) | (1 << CircomParser.DIV) | (1 << CircomParser.QUO) | (1 << CircomParser.MOD))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_opcodeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGNMENT(self):
            return self.getToken(CircomParser.ASSIGNMENT, 0)

        def LEFT_ASSIGNMENT(self):
            return self.getToken(CircomParser.LEFT_ASSIGNMENT, 0)

        def LEFT_CONSTRAINT(self):
            return self.getToken(CircomParser.LEFT_CONSTRAINT, 0)

        def getRuleIndex(self):
            return CircomParser.RULE_assign_opcode

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_opcode" ):
                return visitor.visitAssign_opcode(self)
            else:
                return visitor.visitChildren(self)




    def assign_opcode(self):

        localctx = CircomParser.Assign_opcodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 156, self.RULE_assign_opcode)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 769
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CircomParser.LEFT_CONSTRAINT) | (1 << CircomParser.LEFT_ASSIGNMENT) | (1 << CircomParser.ASSIGNMENT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[54] = self.expression2_sempred
        self._predicates[55] = self.expression3_sempred
        self._predicates[56] = self.expression4_sempred
        self._predicates[57] = self.expression5_sempred
        self._predicates[58] = self.expression6_sempred
        self._predicates[59] = self.expression7_sempred
        self._predicates[60] = self.expression8_sempred
        self._predicates[61] = self.expression9_sempred
        self._predicates[62] = self.expression10_sempred
        self._predicates[63] = self.expression11_sempred
        self._predicates[67] = self.twoElemsListable_sempred
        self._predicates[72] = self.listableWithInputNames_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression2_sempred(self, localctx:Expression2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expression3_sempred(self, localctx:Expression3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expression4_sempred(self, localctx:Expression4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expression5_sempred(self, localctx:Expression5Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expression6_sempred(self, localctx:Expression6Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def expression7_sempred(self, localctx:Expression7Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def expression8_sempred(self, localctx:Expression8Context, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         

    def expression9_sempred(self, localctx:Expression9Context, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

    def expression10_sempred(self, localctx:Expression10Context, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 2)
         

    def expression11_sempred(self, localctx:Expression11Context, predIndex:int):
            if predIndex == 9:
                return self.precpred(self._ctx, 2)
         

    def twoElemsListable_sempred(self, localctx:TwoElemsListableContext, predIndex:int):
            if predIndex == 10:
                return self.precpred(self._ctx, 2)
         

    def listableWithInputNames_sempred(self, localctx:ListableWithInputNamesContext, predIndex:int):
            if predIndex == 11:
                return self.precpred(self._ctx, 2)
         




