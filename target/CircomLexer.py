# Generated from main/Circom/parser/Circom.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2L")
        buf.write("\u0207\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\3\2")
        buf.write("\3\2\5\2\u009a\n\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7")
        buf.write("\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\5\24\u00cc\n\24\3\25\3\25\3\26\3")
        buf.write("\26\3\27\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33")
        buf.write("\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3 \3 \3!\3!\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3&\3&\3\'")
        buf.write("\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3,\3,\3,\3,")
        buf.write("\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3")
        buf.write(",\3,\3,\3,\3,\3,\5,\u0120\n,\3-\3-\3-\3-\3-\3-\3-\3.\3")
        buf.write(".\3.\3.\3.\3.\3/\3/\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60")
        buf.write("\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\61\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\66\3\66")
        buf.write("\3\66\3\67\3\67\3\67\3\67\3\67\38\38\38\38\39\39\39\3")
        buf.write("9\39\39\3:\3:\3:\3;\3;\3;\3;\3<\3<\3<\3<\3<\3<\3<\3=\3")
        buf.write("=\3=\3=\3=\3=\3=\3=\3>\3>\3>\3>\3>\3>\3>\3>\3>\3?\3?\3")
        buf.write("?\3?\3?\3?\3?\3@\3@\3@\3@\3A\3A\3A\3A\3A\3A\3A\3B\3B\3")
        buf.write("B\3B\3B\3B\3B\3B\3B\3B\3B\3B\3B\3B\3B\3B\3B\3C\3C\3C\3")
        buf.write("C\3C\3C\3C\3D\3D\3D\3D\3D\3E\3E\3E\3E\7E\u01c8\nE\fE\16")
        buf.write("E\u01cb\13E\3E\3E\3F\3F\3F\3F\7F\u01d3\nF\fF\16F\u01d6")
        buf.write("\13F\3F\3F\3F\3F\3F\3G\3G\7G\u01df\nG\fG\16G\u01e2\13")
        buf.write("G\3G\3G\3H\6H\u01e7\nH\rH\16H\u01e8\3I\3I\3I\3I\7I\u01ef")
        buf.write("\nI\fI\16I\u01f2\13I\3J\7J\u01f5\nJ\fJ\16J\u01f8\13J\3")
        buf.write("J\3J\7J\u01fc\nJ\fJ\16J\u01ff\13J\3K\6K\u0202\nK\rK\16")
        buf.write("K\u0203\3K\3K\3\u01d4\2L\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63")
        buf.write("e\64g\65i\66k\67m8o9q:s;u<w=y>{?}@\177A\u0081B\u0083C")
        buf.write("\u0085D\u0087E\u0089F\u008bG\u008dH\u008fI\u0091J\u0093")
        buf.write("K\u0095L\3\2\n\4\2\f\f\17\17\3\2$$\3\2\62;\5\2\62;CHc")
        buf.write("h\4\2&&aa\4\2C\\c|\7\2&&\62;C\\aac|\5\2\n\f\16\17\"\"")
        buf.write("\2\u021b\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2")
        buf.write("\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3")
        buf.write("\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2")
        buf.write("-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3")
        buf.write("\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2")
        buf.write("?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2")
        buf.write("\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2")
        buf.write("\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2")
        buf.write("\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3")
        buf.write("\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o")
        buf.write("\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2")
        buf.write("y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081")
        buf.write("\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2")
        buf.write("\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f")
        buf.write("\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2")
        buf.write("\2\3\u0099\3\2\2\2\5\u009b\3\2\2\2\7\u009d\3\2\2\2\t\u009f")
        buf.write("\3\2\2\2\13\u00a1\3\2\2\2\r\u00a3\3\2\2\2\17\u00a5\3\2")
        buf.write("\2\2\21\u00a7\3\2\2\2\23\u00a9\3\2\2\2\25\u00ab\3\2\2")
        buf.write("\2\27\u00ad\3\2\2\2\31\u00af\3\2\2\2\33\u00b1\3\2\2\2")
        buf.write("\35\u00b3\3\2\2\2\37\u00b7\3\2\2\2!\u00bb\3\2\2\2#\u00bf")
        buf.write("\3\2\2\2%\u00c3\3\2\2\2\'\u00cb\3\2\2\2)\u00cd\3\2\2\2")
        buf.write("+\u00cf\3\2\2\2-\u00d1\3\2\2\2/\u00d4\3\2\2\2\61\u00d6")
        buf.write("\3\2\2\2\63\u00d8\3\2\2\2\65\u00da\3\2\2\2\67\u00dc\3")
        buf.write("\2\2\29\u00de\3\2\2\2;\u00e0\3\2\2\2=\u00e3\3\2\2\2?\u00e6")
        buf.write("\3\2\2\2A\u00e8\3\2\2\2C\u00ea\3\2\2\2E\u00ec\3\2\2\2")
        buf.write("G\u00ef\3\2\2\2I\u00f2\3\2\2\2K\u00f4\3\2\2\2M\u00f6\3")
        buf.write("\2\2\2O\u00f9\3\2\2\2Q\u00fc\3\2\2\2S\u00ff\3\2\2\2U\u0102")
        buf.write("\3\2\2\2W\u011f\3\2\2\2Y\u0121\3\2\2\2[\u0128\3\2\2\2")
        buf.write("]\u012e\3\2\2\2_\u0135\3\2\2\2a\u013c\3\2\2\2c\u0145\3")
        buf.write("\2\2\2e\u014f\3\2\2\2g\u0153\3\2\2\2i\u015c\3\2\2\2k\u0163")
        buf.write("\3\2\2\2m\u0166\3\2\2\2o\u016b\3\2\2\2q\u016f\3\2\2\2")
        buf.write("s\u0175\3\2\2\2u\u0178\3\2\2\2w\u017c\3\2\2\2y\u0183\3")
        buf.write("\2\2\2{\u018b\3\2\2\2}\u0194\3\2\2\2\177\u019b\3\2\2\2")
        buf.write("\u0081\u019f\3\2\2\2\u0083\u01a6\3\2\2\2\u0085\u01b7\3")
        buf.write("\2\2\2\u0087\u01be\3\2\2\2\u0089\u01c3\3\2\2\2\u008b\u01ce")
        buf.write("\3\2\2\2\u008d\u01dc\3\2\2\2\u008f\u01e6\3\2\2\2\u0091")
        buf.write("\u01ea\3\2\2\2\u0093\u01f6\3\2\2\2\u0095\u0201\3\2\2\2")
        buf.write("\u0097\u009a\5[.\2\u0098\u009a\5]/\2\u0099\u0097\3\2\2")
        buf.write("\2\u0099\u0098\3\2\2\2\u009a\4\3\2\2\2\u009b\u009c\7*")
        buf.write("\2\2\u009c\6\3\2\2\2\u009d\u009e\7+\2\2\u009e\b\3\2\2")
        buf.write("\2\u009f\u00a0\7]\2\2\u00a0\n\3\2\2\2\u00a1\u00a2\7_\2")
        buf.write("\2\u00a2\f\3\2\2\2\u00a3\u00a4\7}\2\2\u00a4\16\3\2\2\2")
        buf.write("\u00a5\u00a6\7\177\2\2\u00a6\20\3\2\2\2\u00a7\u00a8\7")
        buf.write("=\2\2\u00a8\22\3\2\2\2\u00a9\u00aa\7\60\2\2\u00aa\24\3")
        buf.write("\2\2\2\u00ab\u00ac\7.\2\2\u00ac\26\3\2\2\2\u00ad\u00ae")
        buf.write("\7a\2\2\u00ae\30\3\2\2\2\u00af\u00b0\7A\2\2\u00b0\32\3")
        buf.write("\2\2\2\u00b1\u00b2\7<\2\2\u00b2\34\3\2\2\2\u00b3\u00b4")
        buf.write("\7?\2\2\u00b4\u00b5\7?\2\2\u00b5\u00b6\7?\2\2\u00b6\36")
        buf.write("\3\2\2\2\u00b7\u00b8\7>\2\2\u00b8\u00b9\7?\2\2\u00b9\u00ba")
        buf.write("\7?\2\2\u00ba \3\2\2\2\u00bb\u00bc\7>\2\2\u00bc\u00bd")
        buf.write("\7/\2\2\u00bd\u00be\7/\2\2\u00be\"\3\2\2\2\u00bf\u00c0")
        buf.write("\7?\2\2\u00c0\u00c1\7?\2\2\u00c1\u00c2\7@\2\2\u00c2$\3")
        buf.write("\2\2\2\u00c3\u00c4\7/\2\2\u00c4\u00c5\7/\2\2\u00c5\u00c6")
        buf.write("\7@\2\2\u00c6&\3\2\2\2\u00c7\u00c8\7-\2\2\u00c8\u00cc")
        buf.write("\7-\2\2\u00c9\u00ca\7/\2\2\u00ca\u00cc\7/\2\2\u00cb\u00c7")
        buf.write("\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cc(\3\2\2\2\u00cd\u00ce")
        buf.write("\7#\2\2\u00ce*\3\2\2\2\u00cf\u00d0\7\u0080\2\2\u00d0,")
        buf.write("\3\2\2\2\u00d1\u00d2\7,\2\2\u00d2\u00d3\7,\2\2\u00d3.")
        buf.write("\3\2\2\2\u00d4\u00d5\7,\2\2\u00d5\60\3\2\2\2\u00d6\u00d7")
        buf.write("\7\61\2\2\u00d7\62\3\2\2\2\u00d8\u00d9\7^\2\2\u00d9\64")
        buf.write("\3\2\2\2\u00da\u00db\7\'\2\2\u00db\66\3\2\2\2\u00dc\u00dd")
        buf.write("\7-\2\2\u00dd8\3\2\2\2\u00de\u00df\7/\2\2\u00df:\3\2\2")
        buf.write("\2\u00e0\u00e1\7>\2\2\u00e1\u00e2\7>\2\2\u00e2<\3\2\2")
        buf.write("\2\u00e3\u00e4\7@\2\2\u00e4\u00e5\7@\2\2\u00e5>\3\2\2")
        buf.write("\2\u00e6\u00e7\7(\2\2\u00e7@\3\2\2\2\u00e8\u00e9\7`\2")
        buf.write("\2\u00e9B\3\2\2\2\u00ea\u00eb\7~\2\2\u00ebD\3\2\2\2\u00ec")
        buf.write("\u00ed\7?\2\2\u00ed\u00ee\7?\2\2\u00eeF\3\2\2\2\u00ef")
        buf.write("\u00f0\7#\2\2\u00f0\u00f1\7?\2\2\u00f1H\3\2\2\2\u00f2")
        buf.write("\u00f3\7@\2\2\u00f3J\3\2\2\2\u00f4\u00f5\7>\2\2\u00f5")
        buf.write("L\3\2\2\2\u00f6\u00f7\7>\2\2\u00f7\u00f8\7?\2\2\u00f8")
        buf.write("N\3\2\2\2\u00f9\u00fa\7@\2\2\u00fa\u00fb\7?\2\2\u00fb")
        buf.write("P\3\2\2\2\u00fc\u00fd\7(\2\2\u00fd\u00fe\7(\2\2\u00fe")
        buf.write("R\3\2\2\2\u00ff\u0100\7~\2\2\u0100\u0101\7~\2\2\u0101")
        buf.write("T\3\2\2\2\u0102\u0103\7?\2\2\u0103V\3\2\2\2\u0104\u0105")
        buf.write("\7-\2\2\u0105\u0120\7?\2\2\u0106\u0107\7/\2\2\u0107\u0120")
        buf.write("\7?\2\2\u0108\u0109\7,\2\2\u0109\u0120\7?\2\2\u010a\u010b")
        buf.write("\7,\2\2\u010b\u010c\7,\2\2\u010c\u0120\7?\2\2\u010d\u010e")
        buf.write("\7\61\2\2\u010e\u0120\7?\2\2\u010f\u0110\7^\2\2\u0110")
        buf.write("\u0120\7?\2\2\u0111\u0112\7\'\2\2\u0112\u0120\7?\2\2\u0113")
        buf.write("\u0114\7>\2\2\u0114\u0115\7>\2\2\u0115\u0120\7?\2\2\u0116")
        buf.write("\u0117\7@\2\2\u0117\u0118\7@\2\2\u0118\u0120\7?\2\2\u0119")
        buf.write("\u011a\7(\2\2\u011a\u0120\7?\2\2\u011b\u011c\7`\2\2\u011c")
        buf.write("\u0120\7?\2\2\u011d\u011e\7~\2\2\u011e\u0120\7?\2\2\u011f")
        buf.write("\u0104\3\2\2\2\u011f\u0106\3\2\2\2\u011f\u0108\3\2\2\2")
        buf.write("\u011f\u010a\3\2\2\2\u011f\u010d\3\2\2\2\u011f\u010f\3")
        buf.write("\2\2\2\u011f\u0111\3\2\2\2\u011f\u0113\3\2\2\2\u011f\u0116")
        buf.write("\3\2\2\2\u011f\u0119\3\2\2\2\u011f\u011b\3\2\2\2\u011f")
        buf.write("\u011d\3\2\2\2\u0120X\3\2\2\2\u0121\u0122\7u\2\2\u0122")
        buf.write("\u0123\7k\2\2\u0123\u0124\7i\2\2\u0124\u0125\7p\2\2\u0125")
        buf.write("\u0126\7c\2\2\u0126\u0127\7n\2\2\u0127Z\3\2\2\2\u0128")
        buf.write("\u0129\7k\2\2\u0129\u012a\7p\2\2\u012a\u012b\7r\2\2\u012b")
        buf.write("\u012c\7w\2\2\u012c\u012d\7v\2\2\u012d\\\3\2\2\2\u012e")
        buf.write("\u012f\7q\2\2\u012f\u0130\7w\2\2\u0130\u0131\7v\2\2\u0131")
        buf.write("\u0132\7r\2\2\u0132\u0133\7w\2\2\u0133\u0134\7v\2\2\u0134")
        buf.write("^\3\2\2\2\u0135\u0136\7r\2\2\u0136\u0137\7w\2\2\u0137")
        buf.write("\u0138\7d\2\2\u0138\u0139\7n\2\2\u0139\u013a\7k\2\2\u013a")
        buf.write("\u013b\7e\2\2\u013b`\3\2\2\2\u013c\u013d\7v\2\2\u013d")
        buf.write("\u013e\7g\2\2\u013e\u013f\7o\2\2\u013f\u0140\7r\2\2\u0140")
        buf.write("\u0141\7n\2\2\u0141\u0142\7c\2\2\u0142\u0143\7v\2\2\u0143")
        buf.write("\u0144\7g\2\2\u0144b\3\2\2\2\u0145\u0146\7e\2\2\u0146")
        buf.write("\u0147\7q\2\2\u0147\u0148\7o\2\2\u0148\u0149\7r\2\2\u0149")
        buf.write("\u014a\7q\2\2\u014a\u014b\7p\2\2\u014b\u014c\7g\2\2\u014c")
        buf.write("\u014d\7p\2\2\u014d\u014e\7v\2\2\u014ed\3\2\2\2\u014f")
        buf.write("\u0150\7x\2\2\u0150\u0151\7c\2\2\u0151\u0152\7t\2\2\u0152")
        buf.write("f\3\2\2\2\u0153\u0154\7h\2\2\u0154\u0155\7w\2\2\u0155")
        buf.write("\u0156\7p\2\2\u0156\u0157\7e\2\2\u0157\u0158\7v\2\2\u0158")
        buf.write("\u0159\7k\2\2\u0159\u015a\7q\2\2\u015a\u015b\7p\2\2\u015b")
        buf.write("h\3\2\2\2\u015c\u015d\7t\2\2\u015d\u015e\7g\2\2\u015e")
        buf.write("\u015f\7v\2\2\u015f\u0160\7w\2\2\u0160\u0161\7t\2\2\u0161")
        buf.write("\u0162\7p\2\2\u0162j\3\2\2\2\u0163\u0164\7k\2\2\u0164")
        buf.write("\u0165\7h\2\2\u0165l\3\2\2\2\u0166\u0167\7g\2\2\u0167")
        buf.write("\u0168\7n\2\2\u0168\u0169\7u\2\2\u0169\u016a\7g\2\2\u016a")
        buf.write("n\3\2\2\2\u016b\u016c\7h\2\2\u016c\u016d\7q\2\2\u016d")
        buf.write("\u016e\7t\2\2\u016ep\3\2\2\2\u016f\u0170\7y\2\2\u0170")
        buf.write("\u0171\7j\2\2\u0171\u0172\7k\2\2\u0172\u0173\7n\2\2\u0173")
        buf.write("\u0174\7g\2\2\u0174r\3\2\2\2\u0175\u0176\7f\2\2\u0176")
        buf.write("\u0177\7q\2\2\u0177t\3\2\2\2\u0178\u0179\7n\2\2\u0179")
        buf.write("\u017a\7q\2\2\u017a\u017b\7i\2\2\u017bv\3\2\2\2\u017c")
        buf.write("\u017d\7c\2\2\u017d\u017e\7u\2\2\u017e\u017f\7u\2\2\u017f")
        buf.write("\u0180\7g\2\2\u0180\u0181\7t\2\2\u0181\u0182\7v\2\2\u0182")
        buf.write("x\3\2\2\2\u0183\u0184\7k\2\2\u0184\u0185\7p\2\2\u0185")
        buf.write("\u0186\7e\2\2\u0186\u0187\7n\2\2\u0187\u0188\7w\2\2\u0188")
        buf.write("\u0189\7f\2\2\u0189\u018a\7g\2\2\u018az\3\2\2\2\u018b")
        buf.write("\u018c\7r\2\2\u018c\u018d\7c\2\2\u018d\u018e\7t\2\2\u018e")
        buf.write("\u018f\7c\2\2\u018f\u0190\7n\2\2\u0190\u0191\7n\2\2\u0191")
        buf.write("\u0192\7g\2\2\u0192\u0193\7n\2\2\u0193|\3\2\2\2\u0194")
        buf.write("\u0195\7r\2\2\u0195\u0196\7t\2\2\u0196\u0197\7c\2\2\u0197")
        buf.write("\u0198\7i\2\2\u0198\u0199\7o\2\2\u0199\u019a\7c\2\2\u019a")
        buf.write("~\3\2\2\2\u019b\u019c\7d\2\2\u019c\u019d\7w\2\2\u019d")
        buf.write("\u019e\7u\2\2\u019e\u0080\3\2\2\2\u019f\u01a0\7e\2\2\u01a0")
        buf.write("\u01a1\7k\2\2\u01a1\u01a2\7t\2\2\u01a2\u01a3\7e\2\2\u01a3")
        buf.write("\u01a4\7q\2\2\u01a4\u01a5\7o\2\2\u01a5\u0082\3\2\2\2\u01a6")
        buf.write("\u01a7\7e\2\2\u01a7\u01a8\7w\2\2\u01a8\u01a9\7u\2\2\u01a9")
        buf.write("\u01aa\7v\2\2\u01aa\u01ab\7q\2\2\u01ab\u01ac\7o\2\2\u01ac")
        buf.write("\u01ad\7a\2\2\u01ad\u01ae\7v\2\2\u01ae\u01af\7g\2\2\u01af")
        buf.write("\u01b0\7o\2\2\u01b0\u01b1\7r\2\2\u01b1\u01b2\7n\2\2\u01b2")
        buf.write("\u01b3\7c\2\2\u01b3\u01b4\7v\2\2\u01b4\u01b5\7g\2\2\u01b5")
        buf.write("\u01b6\7u\2\2\u01b6\u0084\3\2\2\2\u01b7\u01b8\7e\2\2\u01b8")
        buf.write("\u01b9\7w\2\2\u01b9\u01ba\7u\2\2\u01ba\u01bb\7v\2\2\u01bb")
        buf.write("\u01bc\7q\2\2\u01bc\u01bd\7o\2\2\u01bd\u0086\3\2\2\2\u01be")
        buf.write("\u01bf\7o\2\2\u01bf\u01c0\7c\2\2\u01c0\u01c1\7k\2\2\u01c1")
        buf.write("\u01c2\7p\2\2\u01c2\u0088\3\2\2\2\u01c3\u01c4\7\61\2\2")
        buf.write("\u01c4\u01c5\7\61\2\2\u01c5\u01c9\3\2\2\2\u01c6\u01c8")
        buf.write("\n\2\2\2\u01c7\u01c6\3\2\2\2\u01c8\u01cb\3\2\2\2\u01c9")
        buf.write("\u01c7\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca\u01cc\3\2\2\2")
        buf.write("\u01cb\u01c9\3\2\2\2\u01cc\u01cd\bE\2\2\u01cd\u008a\3")
        buf.write("\2\2\2\u01ce\u01cf\7\61\2\2\u01cf\u01d0\7,\2\2\u01d0\u01d4")
        buf.write("\3\2\2\2\u01d1\u01d3\13\2\2\2\u01d2\u01d1\3\2\2\2\u01d3")
        buf.write("\u01d6\3\2\2\2\u01d4\u01d5\3\2\2\2\u01d4\u01d2\3\2\2\2")
        buf.write("\u01d5\u01d7\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d7\u01d8\7")
        buf.write(",\2\2\u01d8\u01d9\7\61\2\2\u01d9\u01da\3\2\2\2\u01da\u01db")
        buf.write("\bF\2\2\u01db\u008c\3\2\2\2\u01dc\u01e0\7$\2\2\u01dd\u01df")
        buf.write("\n\3\2\2\u01de\u01dd\3\2\2\2\u01df\u01e2\3\2\2\2\u01e0")
        buf.write("\u01de\3\2\2\2\u01e0\u01e1\3\2\2\2\u01e1\u01e3\3\2\2\2")
        buf.write("\u01e2\u01e0\3\2\2\2\u01e3\u01e4\7$\2\2\u01e4\u008e\3")
        buf.write("\2\2\2\u01e5\u01e7\t\4\2\2\u01e6\u01e5\3\2\2\2\u01e7\u01e8")
        buf.write("\3\2\2\2\u01e8\u01e6\3\2\2\2\u01e8\u01e9\3\2\2\2\u01e9")
        buf.write("\u0090\3\2\2\2\u01ea\u01eb\7\62\2\2\u01eb\u01ec\7z\2\2")
        buf.write("\u01ec\u01f0\3\2\2\2\u01ed\u01ef\t\5\2\2\u01ee\u01ed\3")
        buf.write("\2\2\2\u01ef\u01f2\3\2\2\2\u01f0\u01ee\3\2\2\2\u01f0\u01f1")
        buf.write("\3\2\2\2\u01f1\u0092\3\2\2\2\u01f2\u01f0\3\2\2\2\u01f3")
        buf.write("\u01f5\t\6\2\2\u01f4\u01f3\3\2\2\2\u01f5\u01f8\3\2\2\2")
        buf.write("\u01f6\u01f4\3\2\2\2\u01f6\u01f7\3\2\2\2\u01f7\u01f9\3")
        buf.write("\2\2\2\u01f8\u01f6\3\2\2\2\u01f9\u01fd\t\7\2\2\u01fa\u01fc")
        buf.write("\t\b\2\2\u01fb\u01fa\3\2\2\2\u01fc\u01ff\3\2\2\2\u01fd")
        buf.write("\u01fb\3\2\2\2\u01fd\u01fe\3\2\2\2\u01fe\u0094\3\2\2\2")
        buf.write("\u01ff\u01fd\3\2\2\2\u0200\u0202\t\t\2\2\u0201\u0200\3")
        buf.write("\2\2\2\u0202\u0203\3\2\2\2\u0203\u0201\3\2\2\2\u0203\u0204")
        buf.write("\3\2\2\2\u0204\u0205\3\2\2\2\u0205\u0206\bK\2\2\u0206")
        buf.write("\u0096\3\2\2\2\16\2\u0099\u00cb\u011f\u01c9\u01d4\u01e0")
        buf.write("\u01e8\u01f0\u01f6\u01fd\u0203\3\b\2\2")
        return buf.getvalue()


class CircomLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    SIGNAL_TYPE = 1
    LP = 2
    RP = 3
    LB = 4
    RB = 5
    LC = 6
    RC = 7
    SEMICOLON = 8
    DOT = 9
    COMMA = 10
    UNDERSCORE = 11
    TERNARY_CONDITION = 12
    TERNARY_ALTERNATIVE = 13
    EQ_CONSTRAINT = 14
    LEFT_CONSTRAINT = 15
    LEFT_ASSIGNMENT = 16
    RIGHT_CONSTRAINT = 17
    RIGHT_ASSIGNMENT = 18
    SELF_OP = 19
    NOT = 20
    BNOT = 21
    POW = 22
    MUL = 23
    DIV = 24
    QUO = 25
    MOD = 26
    ADD = 27
    SUB = 28
    SHL = 29
    SHR = 30
    BAND = 31
    BXOR = 32
    BOR = 33
    EQ = 34
    NEQ = 35
    GT = 36
    LT = 37
    LE = 38
    GE = 39
    AND = 40
    OR = 41
    ASSIGNMENT = 42
    ASSIGNMENT_WITH_OP = 43
    SIGNAL = 44
    INPUT = 45
    OUTPUT = 46
    PUBLIC = 47
    TEMPLATE = 48
    COMPONENT = 49
    VAR = 50
    FUNCTION = 51
    RETURN = 52
    IF = 53
    ELSE = 54
    FOR = 55
    WHILE = 56
    DO = 57
    LOG = 58
    ASSERT = 59
    INCLUDE = 60
    PARALLEL = 61
    PRAGMA = 62
    BUS = 63
    CIRCOM = 64
    CUSTOM_TEMPLATES = 65
    CUSTOM = 66
    MAIN = 67
    SINGLE_LINE_COMMENT = 68
    MULTI_LINES_COMMENT = 69
    STRING = 70
    NUMBER = 71
    HEXNUMBER = 72
    IDENTIFIER = 73
    WHITESPACE = 74

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'['", "']'", "'{'", "'}'", "';'", "'.'", "','", 
            "'_'", "'?'", "':'", "'==='", "'<=='", "'<--'", "'==>'", "'-->'", 
            "'!'", "'~'", "'**'", "'*'", "'/'", "'\\'", "'%'", "'+'", "'-'", 
            "'<<'", "'>>'", "'&'", "'^'", "'|'", "'=='", "'!='", "'>'", 
            "'<'", "'<='", "'>='", "'&&'", "'||'", "'='", "'signal'", "'input'", 
            "'output'", "'public'", "'template'", "'component'", "'var'", 
            "'function'", "'return'", "'if'", "'else'", "'for'", "'while'", 
            "'do'", "'log'", "'assert'", "'include'", "'parallel'", "'pragma'", 
            "'bus'", "'circom'", "'custom_templates'", "'custom'", "'main'" ]

    symbolicNames = [ "<INVALID>",
            "SIGNAL_TYPE", "LP", "RP", "LB", "RB", "LC", "RC", "SEMICOLON", 
            "DOT", "COMMA", "UNDERSCORE", "TERNARY_CONDITION", "TERNARY_ALTERNATIVE", 
            "EQ_CONSTRAINT", "LEFT_CONSTRAINT", "LEFT_ASSIGNMENT", "RIGHT_CONSTRAINT", 
            "RIGHT_ASSIGNMENT", "SELF_OP", "NOT", "BNOT", "POW", "MUL", 
            "DIV", "QUO", "MOD", "ADD", "SUB", "SHL", "SHR", "BAND", "BXOR", 
            "BOR", "EQ", "NEQ", "GT", "LT", "LE", "GE", "AND", "OR", "ASSIGNMENT", 
            "ASSIGNMENT_WITH_OP", "SIGNAL", "INPUT", "OUTPUT", "PUBLIC", 
            "TEMPLATE", "COMPONENT", "VAR", "FUNCTION", "RETURN", "IF", 
            "ELSE", "FOR", "WHILE", "DO", "LOG", "ASSERT", "INCLUDE", "PARALLEL", 
            "PRAGMA", "BUS", "CIRCOM", "CUSTOM_TEMPLATES", "CUSTOM", "MAIN", 
            "SINGLE_LINE_COMMENT", "MULTI_LINES_COMMENT", "STRING", "NUMBER", 
            "HEXNUMBER", "IDENTIFIER", "WHITESPACE" ]

    ruleNames = [ "SIGNAL_TYPE", "LP", "RP", "LB", "RB", "LC", "RC", "SEMICOLON", 
                  "DOT", "COMMA", "UNDERSCORE", "TERNARY_CONDITION", "TERNARY_ALTERNATIVE", 
                  "EQ_CONSTRAINT", "LEFT_CONSTRAINT", "LEFT_ASSIGNMENT", 
                  "RIGHT_CONSTRAINT", "RIGHT_ASSIGNMENT", "SELF_OP", "NOT", 
                  "BNOT", "POW", "MUL", "DIV", "QUO", "MOD", "ADD", "SUB", 
                  "SHL", "SHR", "BAND", "BXOR", "BOR", "EQ", "NEQ", "GT", 
                  "LT", "LE", "GE", "AND", "OR", "ASSIGNMENT", "ASSIGNMENT_WITH_OP", 
                  "SIGNAL", "INPUT", "OUTPUT", "PUBLIC", "TEMPLATE", "COMPONENT", 
                  "VAR", "FUNCTION", "RETURN", "IF", "ELSE", "FOR", "WHILE", 
                  "DO", "LOG", "ASSERT", "INCLUDE", "PARALLEL", "PRAGMA", 
                  "BUS", "CIRCOM", "CUSTOM_TEMPLATES", "CUSTOM", "MAIN", 
                  "SINGLE_LINE_COMMENT", "MULTI_LINES_COMMENT", "STRING", 
                  "NUMBER", "HEXNUMBER", "IDENTIFIER", "WHITESPACE" ]

    grammarFileName = "Circom.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None





