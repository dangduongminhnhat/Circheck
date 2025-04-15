import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_100(self):
        self.assertTrue(TestLexer.checkLexeme("abc", "abc,<EOF>", 100))

    def test_101(self):
        self.assertTrue(TestLexer.checkLexeme(
            "ab?sVN", "ab,ErrorToken ?", 101))

    def test_102(self):
        self.assertTrue(TestLexer.checkLexeme(
            "var abc int ;", "var,abc,int,;,<EOF>", 102))

    def test_103(self):
        self.assertTrue(TestLexer.checkLexeme(
            """func abc ( ) """, """func,abc,(,),<EOF>""", 103))

    def test_104(self):
        input = """if () {}"""
        expect = "if,(,),{,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 104))

    def test_105(self):
        input = "if () {} else if () {} else"
        expect = "if,(,),{,},else,if,(,),{,},else,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 105))

    def test_106(self):
        input = "var abc"
        expect = "var,abc,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 106))

    def test_107(self):
        input = "func abc "
        expect = "func,abc,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 107))

    def test_108(self):
        input = "for()"
        expect = "for,(,),<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 108))

    def test_109(self):
        input = "{return 123} "
        expect = "{,return,123,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 109))

    def test_110(self):
        input = "type Person struct"
        expect = "type,Person,struct,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 110))

    def test_111(self):
        input = "type Calculator interface"
        expect = "type,Calculator,interface,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 111))

    def test_112(self):
        input = "const a "
        expect = "const,a,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 112))

    def test_113(self):
        input = "int float string boolean "
        expect = "int,float,string,boolean,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 113))

    def test_114(self):
        input = "v = nil "
        expect = "v,=,nil,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 114))

    def test_115(self):
        input = "{continue}; "
        expect = "{,continue,},;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 115))

    def test_116(self):
        input = "{break;} "
        expect = "{,break,;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 116))

    def test_117(self):
        input = "(true) {something}(false) {something} "
        expect = "(,true,),{,something,},(,false,),{,something,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 117))

    def test_118(self):
        input = "range array(){} "
        expect = "range,array,(,),{,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 118))

    def test_119(self):
        input = "a - c < b && !(a - b > c) || a != b && a != c"
        expect = "a,-,c,<,b,&&,!,(,a,-,b,>,c,),||,a,!=,b,&&,a,!=,c,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 119))

    def test_120(self):
        input = "a := c; a += 3; b -= c;"
        expect = "a,:=,c,;,a,+=,3,;,b,-=,c,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 120))

    def test_121(self):
        input = "a *= 2; b /= 6; c %= 5"
        expect = "a,*=,2,;,b,/=,6,;,c,%=,5,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 121))

    def test_122(self):
        input = "a := op; c ++= 20; d --= 30 "
        expect = "a,:=,op,;,c,+,+=,20,;,d,-,-=,30,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 122))

    def test_123(self):
        input = "a.b == 3 || c === d || c +== a || b -=== a"
        expect = "a,.,b,==,3,||,c,==,=,d,||,c,+=,=,a,||,b,-=,==,a,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 123))

    def test_124(self):
        input = "a ** b ; a ^ b;"
        expect = "a,*,*,b,;,a,ErrorToken ^"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 124))

    def test_125(self):
        input = "()[]{},;"
        expect = "(,),[,],{,},,,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 125))

    def test_126(self):
        input = "()''[]"
        expect = "(,),ErrorToken '"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 126))

    def test_127(self):
        input = "123 -470 +999197"
        expect = "123,-,470,+,999197,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 127))

    def test_128(self):
        input = "0 012 0046"
        expect = "0,0,12,0,0,46,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 128))

    def test_129(self):
        input = "0b110 0B1011"
        expect = "0b110,0B1011,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 129))

    def test_130(self):
        input = "0b000 0b011 0b0010"
        expect = "0b000,0b011,0b0010,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 130))

    def test_131(self):
        input = "0b108"
        expect = "0b10,8,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 131))

    def test_132(self):
        input = "0b210"
        expect = "0,b210,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 132))

    def test_133(self):
        input = "0o123 0O456"
        expect = "0o123,0O456,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 133))

    def test_134(self):
        input = "0o0000 0o0046"
        expect = "0o0000,0o0046,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 134))

    def test_135(self):
        input = "0o679"
        expect = "0o67,9,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 135))

    def test_136(self):
        input = "0o975"
        expect = "0,o975,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 136))

    def test_137(self):
        input = "0x123 0X123"
        expect = "0x123,0X123,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 137))

    def test_138(self):
        input = "0x12ab 0x12AB 0x12Ab"
        expect = "0x12ab,0x12AB,0x12Ab,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 138))

    def test_139(self):
        input = "0x000 0x0034"
        expect = "0x000,0x0034,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 139))

    def test_140(self):
        input = "0xEFG"
        expect = "0xEF,G,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 140))

    def test_141(self):
        input = "3.14 5.12"
        expect = "3.14,5.12,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 141))

    def test_142(self):
        input = "0. 12."
        expect = "0.,12.,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 142))

    def test_143(self):
        input = "2.0e10 2.0e+10 2.0e-10"
        expect = "2.0e10,2.0e+10,2.0e-10,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 143))

    def test_144(self):
        input = "10.e5"
        expect = "10.e5,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 144))

    def test_145(self):
        input = "10e5"
        expect = "10,e5,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 145))

    def test_146(self):
        input = "e5 e+5 e-5"
        expect = "e5,e,+,5,e,-,5,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 146))

    def test_147(self):
        input = "00.012 00.e013 00.00e00"
        expect = "00.012,00.e013,00.00e00,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 147))

    def test_148(self):
        input = ".15 .e20"
        expect = ".,15,.,e20,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 148))

    def test_149(self):
        input = "+30.12 -30.12"
        expect = "+,30.12,-,30.12,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 149))

    def test_150(self):
        input = "20.0e12.3"
        expect = "20.0e12,.,3,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 150))

    def test_151(self):
        input = """ "hello 123" """
        expect = """\"hello 123\",<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 151))

    def test_152(self):
        input = """ "This is a string with escaped: \\n \\t \\r \\\" \\\\" """
        expect = "\"This is a string with escaped: \\n \\t \\r \\\" \\\\\",<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 152))

    def test_153(self):
        input = """ "This \' #? \' string" """
        expect = "\"This ' #? ' string\",<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 153))

    def test_154(self):
        input = """ "This \" ?# \" string" """
        expect = "\"This \",ErrorToken ?"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 154))

    def test_155(self):
        input = """ "This \" is \" string" """
        expect = "\"This \",is,\" string\",<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 155))

    def test_156(self):
        input = """ "This \\ is \\ string" """
        expect = "Illegal escape in string: \"This \ "
        self.assertTrue(TestLexer.checkLexeme(input, expect, 156))

    def test_157(self):
        input = """ "This \\f is \\f string" """
        expect = "Illegal escape in string: \"This \\f"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 157))

    def test_158(self):
        input = """ "This is a string \n"  """
        expect = "Unclosed string: \"This is a string "
        self.assertTrue(TestLexer.checkLexeme(input, expect, 158))

    def test_159(self):
        input = """ "This is 
                    a string"  """
        expect = "Unclosed string: \"This is "
        self.assertTrue(TestLexer.checkLexeme(input, expect, 159))

    def test_160(self):
        input = """ "This is a string  """
        expect = "Unclosed string: \"This is a string  "
        self.assertTrue(TestLexer.checkLexeme(input, expect, 160))

    def test_161(self):
        input = "23main"
        expect = "23,main,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 161))

    def test_162(self):
        input = "main23"
        expect = "main23,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 162))

    def test_163(self):
        input = "main MAIN maIN"
        expect = "main,MAIN,maIN,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 163))

    def test_164(self):
        input = "_main ma_in"
        expect = "_main,ma_in,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 164))

    def test_165(self):
        input = "main-23"
        expect = "main,-,23,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 165))

    def test_166(self):
        input = """ // This is a comment main"""
        expect = "<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 166))

    def test_167(self):
        input = """ //This is first comment
                    //This is second comment
                    main
                """
        expect = "main,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 167))

    def test_168(self):
        input = """ /* Multi line comment
                    This is first comment
                    This is second comment */
                """
        expect = "<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 168))

    def test_169(self):
        input = """ /*This is global comment
                        /* This is nest comment*/
                    This is global comment*/ main """
        expect = "main,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 169))

    def test_170(self):
        input = """ /*This is multi
                    line comment*/ multi
                // This is single line comment
                single
                """
        expect = "multi,;,single,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 170))

    def test_171(self):
        input = """tong \t duy \r nhat \f"""
        expect = "tong,duy,nhat,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 171))

    def test_172(self):
        input = """func main() {};"""
        expect = "func,main,(,),{,},;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 172))

    def test_173(self):
        input = """func foo () {
        };"""
        expect = "func,foo,(,),{,},;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 173))

    def test_174(self):
        input = "const MN = [5][0]string{1, \"string\"};"
        expect = "const,MN,=,[,5,],[,0,],string,{,1,,,\"string\",},;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 174))

    def test_175(self):
        input = "const MN = Person{}"
        expect = "const,MN,=,Person,{,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 175))

    def test_176(self):
        input = "const MN = 1 || 2 && c"
        expect = "const,MN,=,1,||,2,&&,c,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 176))

    def test_177(self):
        input = "const MN = main()[0] + bc[2].b.b;"
        expect = "const,MN,=,main,(,),[,0,],+,bc,[,2,],.,b,.,b,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 177))

    def test_178(self):
        input = "const MN = ca.main(12) + b.c[23];"
        expect = "const,MN,=,ca,.,main,(,12,),+,b,.,c,[,23,],;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 178))

    def test_179(self):
        input = """
            var x int = main() + 4 / 4;
            var y = "abc" / 4;
            var z str;
        """
        expect = "var,x,int,=,main,(,),+,4,/,4,;,var,y,=,\"abc\",/,4,;,var,z,str,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 179))

    def test_180(self):
        input = """
            func main(x int, y int) int {}
            func main1() [2][6] ID {}
            func main2() {abc;}
        """
        expect = "func,main,(,x,int,,,y,int,),int,{,},;,func,main1,(,),[,2,],[,6,],ID,{,},;,func,main2,(,),{,abc,;,},;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 180))

    def test_181(self):
        input = """
            func (c Calculator) nhat() ID {}
            func (c Calculator) nhat(x float, y [2]nhat) {}
        """
        expect = "func,(,c,Calculator,),nhat,(,),ID,{,},;,func,(,c,Calculator,),nhat,(,x,float,,,y,[,2,],nhat,),{,},;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 181))

    def test_182(self):
        input = """
            type nhat struct {
                nhat string ;
                nhat [5][4]ID ;
            }
            """
        expect = "type,nhat,struct,{,nhat,string,;,nhat,[,5,],[,4,],ID,;,},;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 182))

    def test_183(self):
        input = """
            type Calculator interface {
                Add(x, y int) int;
                Subtract(a, b float, c int) [3]ID;
                Reset()
                Show(name string);
            }"""
        expect = "type,Calculator,interface,{,Add,(,x,,,y,int,),int,;,Subtract,(,a,,,b,float,,,c,int,),[,3,],ID,;,Reset,(,),;,Show,(,name,string,),;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 183))

    def test_184(self):
        input = """
            func nhat() {
                var z str;
                const nhat = a.b() + 2;
            }"""
        expect = "func,nhat,(,),{,var,z,str,;,const,nhat,=,a,.,b,(,),+,2,;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 184))

    def test_185(self):
        input = """ func nhat() {
                x  := foo() + 3 / 4;
                x.c[2][4] := 1 + 2;
            }"""
        expect = "func,nhat,(,),{,x,:=,foo,(,),+,3,/,4,;,x,.,c,[,2,],[,4,],:=,1,+,2,;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 185))

    def test_186(self):
        input = """ if (x > 10) {} """
        expect = "if,(,x,>,10,),{,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 186))

    def test_187(self):
        input = """ if (x > 10) {

                } else if (x == 10) {
                    var z str;
                } else {
                    var z ID;
                }"""
        expect = "if,(,x,>,10,),{,},else,if,(,x,==,10,),{,var,z,str,;,},else,{,var,z,ID,;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 187))

    def test_188(self):
        input = """ for i < 10 {}"""
        expect = "for,i,<,10,{,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 188))

    def test_189(self):
        input = """ for i := 0; i < 10; i += 1 {} """
        expect = "for,i,:=,0,;,i,<,10,;,i,+=,1,{,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 189))

    def test_190(self):
        input = """ for index, value := range array {}"""
        expect = "for,index,,,value,:=,range,array,{,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 190))

    def test_191(self):
        input = """ var c int; type Calculator struct{} type Calculator struct {} var c int;"""
        expect = "var,c,int,;,type,Calculator,struct,{,},type,Calculator,struct,{,},var,c,int,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 191))

    def test_192(self):
        input = """
                if (x.foo().b[2])
                {
                    if (){}
                }"""
        expect = "if,(,x,.,foo,(,),.,b,[,2,],),;,{,if,(,),{,},;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 192))

    def test_193(self):
        input = """
                func Add() {
                    return (2 + 3).b
                    return -1.c
                }"""
        expect = "func,Add,(,),{,return,(,2,+,3,),.,b,;,return,-,1.,c,;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 193))

    def test_194(self):
        input = """
                    if (1) {}
                    else if(2) {return string}
                    else if(3) {reutrn int;}"""
        expect = "if,(,1,),{,},;,else,if,(,2,),{,return,string,},;,else,if,(,3,),{,reutrn,int,;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 194))

    def test_195(self):
        input = """
                    for var i [2]int = 0; foo().a.b(); i[3] := 1 {
                        // loop body
                    }
        """
        expect = "for,var,i,[,2,],int,=,0,;,foo,(,),.,a,.,b,(,),;,i,[,3,],:=,1,{,},;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 195))

    def test_196(self):
        input = """ for var i = 0; i < 10; i += 1 {
                        // loop body
                    }"""
        expect = "for,var,i,=,0,;,i,<,10,;,i,+=,1,{,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 196))

    def test_197(self):
        input = """ a[2+3&&2] += foo().b[2];"""
        expect = "a,[,2,+,3,&&,2,],+=,foo,(,),.,b,[,2,],;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 197))

    def test_198(self):
        input = """
                    func Add() {
                        a += 2;
                        a /= 2
                        a *= 2
                        a %= 2;
                        return a
                    }"""
        expect = "func,Add,(,),{,a,+=,2,;,a,/=,2,;,a,*=,2,;,a,%=,2,;,return,a,;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 198))

    def test_199(self):
        input = """ var z nhat = a[2, 5];"""
        expect = "var,z,nhat,=,a,[,2,,,5,],;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 199))

    def test_extended(self):
        self.assertTrue(TestLexer.checkLexeme(
            "ab?sVN", "ab,ErrorToken ?", 1000))

        input = "1+2-5*4/7%3++8--9"
        expect = "1,+,2,-,5,*,4,/,7,%,3,+,+,8,-,-,9,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 1001))

        input = "1 + 3 * 2 && true || false "
        expect = "1,+,3,*,2,&&,true,||,false,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 1002))

        input = "1 + 3 >= 2 && 23 - 90 <= 6 || 5 == 6"
        expect = "1,+,3,>=,2,&&,23,-,90,<=,6,||,5,==,6,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 1003))

        self.assertTrue(TestLexer.checkLexeme("if", "if,<EOF>", 1004))

        self.assertTrue(TestLexer.checkLexeme("+", "+,<EOF>", 1005))

        self.assertTrue(TestLexer.checkLexeme("[]", "[,],<EOF>", 1006))

        self.assertTrue(TestLexer.checkLexeme("_MNhat", "_MNhat,<EOF>", 1007))

        self.assertTrue(TestLexer.checkLexeme("12", "12,<EOF>", 1008))

        self.assertTrue(TestLexer.checkLexeme("0x11", "0x11,<EOF>", 1009))

        self.assertTrue(TestLexer.checkLexeme("12.e-8", "12.e-8,<EOF>", 1010))

        self.assertTrue(TestLexer.checkLexeme(
            """ "MNHAT \\r" """, "\"MNHAT \\r\",<EOF>", 1011))

        self.assertTrue(TestLexer.checkLexeme("// MNHAT", "<EOF>", 1012))

        self.assertTrue(TestLexer.checkLexeme(
            "/* MINH /* /*NHAT*/ */ SHIBA", "SHIBA,<EOF>", 1013))

        self.assertTrue(TestLexer.checkLexeme("^", "ErrorToken ^", 1014))

        self.assertTrue(TestLexer.checkLexeme(
            """ "MNHAT\n" """, "Unclosed string: \"MNHAT", 1015))

        self.assertTrue(TestLexer.checkLexeme(
            """ "MNHAT\\f" """, "Illegal escape in string: \"MNHAT\\f", 1016))

        self.assertTrue(TestLexer.checkLexeme("""
            const a = 2;
""", "const,a,=,2,;,<EOF>", 1017))

        self.assertTrue(TestLexer.checkLexeme("0452.", "0452.,<EOF>", 1018))

        self.assertTrue(TestLexer.checkLexeme(
            "09.e-002", "09.e-002,<EOF>", 1019))

        self.assertTrue(TestLexer.checkLexeme(""" // /*
                                       */""", "*,/,<EOF>", 1020))
