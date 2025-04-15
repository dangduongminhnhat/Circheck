import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_200(self):
        input = """func main() {
            var i;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 200))

    def test_201(self):
        input = """func foo () {
            var i;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 201))

    def test_202(self):
        input = """func main({};"""
        expect = "Error on line 1 col 11: {"
        self.assertTrue(TestParser.checkParser(input, expect, 202))

    def test_203(self):
        input = """var int;"""
        expect = "Error on line 1 col 5: int"
        self.assertTrue(TestParser.checkParser(input, expect, 203))

    def test_204(self):
        input = """var i ;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 204))

    def test_205(self):
        input = "const Mn = 10.12;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 205))

    def test_206(self):
        input = "const Mn = [5][0]string{1, \"string\"};"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 206))

    def test_207(self):
        input = "const Mn = [5][5]string{1, \"string\", {1.21, \"nhat\"}, {3}};"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 207))

    def test_208(self):
        input = """ const Mn = [ID1][ID2]int{{1, \"string\", {21}}, {1.21, \"nhat\"}}; """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 208))

    def test_209(self):
        input = "const Mn = [ID1][ID2]ID3{1, \"string\", {1.21, \"nhat\"}};"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 209))

    def test_210(self):
        input = "const Mn = [10.]ID{2, 3};"
        expect = "Error on line 1 col 13: 10."
        self.assertTrue(TestParser.checkParser(input, expect, 210))

    def test_211(self):
        input = "const Mn = [true]ID{2, 3};"
        expect = "Error on line 1 col 13: true"
        self.assertTrue(TestParser.checkParser(input, expect, 211))

    def test_212(self):
        input = """const a = [1]int{1+1}"""
        expect = "Error on line 1 col 19: +"
        self.assertTrue(TestParser.checkParser(input, expect, 212))

    def test_213(self):
        input = "const Mn = [1+2+3]ID3{1, \"string\", {1.21, \"nhat\"}};"
        expect = "Error on line 1 col 14: +"
        self.assertTrue(TestParser.checkParser(input, expect, 213))

    def test_214(self):
        input = "const Mn = [14]float{};"
        expect = "Error on line 1 col 22: }"
        self.assertTrue(TestParser.checkParser(input, expect, 214))

    def test_215(self):
        input = "const Mn = [5][0]string{1 \"string\" 3};"
        expect = "Error on line 1 col 27: \"string\""
        self.assertTrue(TestParser.checkParser(input, expect, 215))

    def test_216(self):
        input = "const Mn = [5][0]string(1, \"string\", 3);"
        expect = "Error on line 1 col 24: ("
        self.assertTrue(TestParser.checkParser(input, expect, 216))

    def test_217(self):
        input = "const Mn = [5][0]{1, \"string\", 3};"
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.checkParser(input, expect, 217))

    def test_218(self):
        input = "const Mn = [5][0]{1, \"string\", 3;"
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.checkParser(input, expect, 218))

    def test_219(self):
        input = "const Mn = Person{name: \"Alice\", age: 30};"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 219))

    def test_220(self):
        input = "const Mn = MinhNhat{name: \"nhat\" age: 21};"
        expect = "Error on line 1 col 34: age"
        self.assertTrue(TestParser.checkParser(input, expect, 220))

    def test_221(self):
        input = "const Mn = MinhNhat{name: \"nhat\", age: 21, school: \"hcmut\",};"
        expect = "Error on line 1 col 60: }"
        self.assertTrue(TestParser.checkParser(input, expect, 221))

    def test_222(self):
        input = "const Mn = MinhNhat{name \"nhat\"};"
        expect = "Error on line 1 col 20: {"
        self.assertTrue(TestParser.checkParser(input, expect, 222))

    def test_223(self):
        input = "const Mn = MinhNhat{name: \"nhat\";"
        expect = "Error on line 1 col 33: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 223))

    def test_224(self):
        input = "const Mn = MinhNhat{};"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 224))

    def test_225(self):
        input = "const Mn = MinhNhat(name: , age: 21);"
        expect = "Error on line 1 col 25: :"
        self.assertTrue(TestParser.checkParser(input, expect, 225))

    def test_226(self):
        input = "const Mn = MinhNhat{name: };"
        expect = "Error on line 1 col 27: }"
        self.assertTrue(TestParser.checkParser(input, expect, 226))

    def test_227(self):
        input = "const Mn = MinhNhat{\"nhat\"};"
        expect = "Error on line 1 col 20: {"
        self.assertTrue(TestParser.checkParser(input, expect, 227))

    def test_228(self):
        input = "const Mn = int{\"nhat\"};"
        expect = "Error on line 1 col 12: int"
        self.assertTrue(TestParser.checkParser(input, expect, 228))

    def test_229(self):
        input = "const Mn = 2 + 2 - 2 * 2 / 2 % 2;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 229))

    def test_230(self):
        input = "const Mn = 2 == 2 != 2 > 2 < 2 >= 2 <= 2;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 230))

    def test_231(self):
        input = "const Mn = !3 && 3 || 3 && !!3 ;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 231))

    def test_232(self):
        input = "const Mn = a[3];"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 232))

    def test_233(self):
        input = "const Mn = a[3][2];"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 233))

    def test_234(self):
        input = "var z nhat = a[2][3][a + 2 / d && true];"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 201))

    def test_235(self):
        input = "var z nhat = a[2, 3]; "
        expect = "Error on line 1 col 15: ["
        self.assertTrue(TestParser.checkParser(input, expect, 235))

    def test_236(self):
        input = " var z Mn = nhat.name;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 236))

    def test_237(self):
        input = " var z Mn = nhat.name.first_name;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 237))

    def test_238(self):
        input = " var z Mn = nhat..name;"
        expect = "Error on line 1 col 17: ."
        self.assertTrue(TestParser.checkParser(input, expect, 238))

    def test_239(self):
        input = " var z Mn = nhat.1;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 239))

    def test_240(self):
        input = " var z Mn = add();"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 240))

    def test_241(self):
        input = " var z Mn = add(1+3, 2/4, a[3][2]);"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 241))

    def test_242(self):
        input = " var z Mn = add(3 a);"
        expect = "Error on line 1 col 19: a"
        self.assertTrue(TestParser.checkParser(input, expect, 242))

    def test_243(self):
        input = " var z Mn = add(a, c, 2);"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 243))

    def test_244(self):
        input = " var z Mn = add(3, a);"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 244))

    def test_245(self):
        input = " var z Mn = add();"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 245))

    def test_246(self):
        input = "const Mn = 1 || 2 && c + 3 / 2 - -1;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 246))

    def test_247(self):
        input = "const Mn = 1[2] + foo()[2] + ID[2].b.b;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 247))

    def test_248(self):
        input = "const Mn = ca.foo(132) + b.c[2];"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, "successful", 248))

    def test_249(self):
        input = "const Mn = a.a.foo();"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 249))

    def test_250(self):
        input = "var z TMn = ID {a: 2, b: 2 + 2 + ID {a: 2}};"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 250))

    def test_251(self):
        input = "var z nhat = a >= 2 <= \"string\" > a[2][3] < ID{A: 2} >= [2]S{2};"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 251))

    def test_252(self):
        input = "var z nhat = a.a.a[2].foo();"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 252))

    def test_253(self):
        input = "var z nhat = a.a.a[2].c[2].foo(1,);"
        expect = "Error on line 1 col 27: ."
        self.assertTrue(TestParser.checkParser(input, expect, 253))

    def test_254(self):
        input = "var z nhat = !a.a.a[2].c[2].foo(1, ID{A: 2});"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 254))

    def test_255(self):
        input = "var z nhat = nhat {name: NAME{firt_name: \"minh\", last_name: \"nhat\"}, age: a[2][3]};"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 255))

    def test_256(self):
        input = """
            var x int = foo() + 3 / 4;
            var y = "Hello" / 4
            var z str;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 256))

    def test_257(self):
        input = "const nhat = a.b() + 2;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 257))

    def test_258(self):
        input = """
            func (c c) Add(x, c int) {return ;}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 258))

    def test_259(self):
        input = "const nhat = a.b() + 2"
        expect = "Error on line 1 col 23: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 259))

    def test_260(self):
        input = "var y;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 260))

    def test_261(self):
        input = "var float;"
        expect = "Error on line 1 col 5: float"
        self.assertTrue(TestParser.checkParser(input, expect, 261))

    def test_262(self):
        input = """
        type Person struct {
            func (p Person) Greet() string {
                return "Hello, " + p.name
            }; c c;
            func (p Person) Greet() string {
                return "Hello, " + p.name
            } c c;
        }
"""
        expect = "Error on line 3 col 13: func"
        self.assertTrue(TestParser.checkParser(input, expect, 262))

    def test_263(self):
        input = """func foo () {
        };"""
        expect = "Error on line 2 col 9: }"
        self.assertTrue(TestParser.checkParser(input, expect, 263))

    def test_264(self):
        input = """func main({};"""
        expect = "Error on line 1 col 11: {"
        self.assertTrue(TestParser.checkParser(input, expect, 264))

    def test_265(self):
        input = """
            func nhat(x int, y int) int {}
            func nhat1() [2][3] ID {}
            func nhat2() {}
        """
        expect = "Error on line 2 col 42: }"
        self.assertTrue(TestParser.checkParser(input, expect, 265))

    def test_266(self):
        input = """
            func (c Calculator) nhat(x int) int {return;}
            func (c Calculator) nhat() ID {return;};
            func (c Calculator) nhat(x int, y [2]nhat) {return;}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 266))

    def test_267(self):
        input = """
            type nhat struct {
                nhat string ;
                nhat [1][3]nhat ;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 267))

    def test_268(self):
        input = """
            func nhat() {
                x  := foo() + 3 / 4;
                x.c[2][4] := 1 + 2;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 268))

    def test_269(self):
        input = """
            type Calculator interface {

                Add(x, y int) int;
                Subtract(a, b float, c int) [3]ID;
                Reset()

                SayHello(name string);

            }
            type nhat interface {}
        """
        expect = "Error on line 11 col 34: }"
        self.assertTrue(TestParser.checkParser(input, expect, 269))

    def test_270(self):
        input = """
            func nhat() {
                var x int = foo() + 3 / 4;
                var y = "Hello" / 4;
                var z str;

                const nhat = a.b() + 2;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 270))

    def test_271(self):
        input = """
            func nhat() {
                if (x > 10) {return;}
                if (x > 10) {
                  return;
                } else if (x == 10) {
                    var z str;
                } else {
                    var z ID;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 271))

    def test_272(self):
        input = """
            func nhat() {
                for i < 10 {return;}
                for i := 0; i < 10; i += 1 {return;}
                for index, value := range array {return;}
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 272))

    def test_273(self):
        input = """
            func nhat() {
                for i < 10 {break;}
                break;
                continue;
                return 1;
                return
                foo(2 + x, 4 / y); m.goo();
             }

        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 273))

    def test_274(self):
        input = """
            func Add(a) [2]id {}
        """
        expect = "Error on line 2 col 23: )"
        self.assertTrue(TestParser.checkParser(input, expect, 274))

    def test_275(self):
        input = """
            type Calculator interface {
                Add(x, y [2]ID) [2]int;
                Subtract(a, b float, c, e int);
                Reset()
                SayHello(name string)
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 275))

    def test_276(self):
        input = """
            type Calculator interface { Subtract(a int); }
            type Person struct {a int;}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 276))

    def test_277(self):
        input = """

            func (c c) Add(x int)  {return;}

            func Add(x int, y int) {return;}; var c int;

            var c int; type Calculator struct{a int;} type Calculator struct {} var c int;
        """
        expect = "Error on line 7 col 55: type"
        self.assertTrue(TestParser.checkParser(input, expect, 277))

    def test_278(self):
        input = """
            func Add(x int, y int) int  {return;};
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 278))

    def test_279(self):
        input = """
            func (c int) Add(x int) int {}
        """
        expect = "Error on line 2 col 21: int"
        self.assertTrue(TestParser.checkParser(input, expect, 279))

    def test_280(self):
        input = """
            func (c c) Add(x, c int) {}
        """
        expect = "Error on line 2 col 39: }"
        self.assertTrue(TestParser.checkParser(input, expect, 280))

    def test_281(self):
        input = """
            const a = 2 func (c c) Add(x int) {}
        """
        expect = "Error on line 2 col 25: func"
        self.assertTrue(TestParser.checkParser(input, expect, 281))

    def test_282(self):
        input = """
                func Add() {
                    const a = a[2].b
                    var a = a[2].b; var a = "s";
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 282))

    def test_283(self):
        input = """
                func Add() {
                    a += 2;
                    a -= a[2].b();
                    a /= 2
                    a *= 2
                    a %= 2;
                };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 283))

    def test_284(self):
        """Statement"""
        input = """
                                    func Add() {
                                        a[2].b := 2;
                                    };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 284))

    def test_285(self):
        input = """
                                    func Add() {
                                        a.foo() += 2;
                                    }"""
        expect = "Error on line 4 col 38: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 285))

    def test_286(self):
        input = """
                                    func Add() {
                                        2[1] + 2 += 2;
                                    }"""
        expect = "Error on line 3 col 50: +="
        self.assertTrue(TestParser.checkParser(input, expect, 286))

    def test_287(self):
        input = """
                                    func Add() {
                                       a[2+3&&2] += foo().b[2];
                                    };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 287))

    def test_288(self):
        input = """
                                    func Add() {
                                        if (x.foo().b[2]) {
                                            if (){}
                                        }
                                    };"""
        expect = "Error on line 4 col 49: )"
        self.assertTrue(TestParser.checkParser(input, expect, 288))

    def test_289(self):
        input = """
                                    func Add() {
                                        for var i = 0; i < 10; i += 1 {
                                            // loop body
                                            break;
                                        }
                                    };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 289))

    def test_290(self):
        input = """
                                    func Add() {
                                        for var i [2]int = 0; foo().a.b(); i[3] := 1 {
                                            // loop body
                                            break;
                                        }
                                    };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 290))

    def test_291(self):
        input = """
                                    func Add() {
                                        for index[2], value := range arr {
                                        // index: 0, 1, 2
                                        // value: 10, 20, 30
                                        }
                                    }"""
        expect = "Error on line 3 col 53: ,"
        self.assertTrue(TestParser.checkParser(input, expect, 291))

    def test_292(self):
        input = """
                                    func Add() {
                                        for index, value := range arr[2] {
                                            break;
                                        }
                                    };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 292))

    def test_293(self):
        input = """
                                    func Add() {
                                        for index, value := range 23 {
                                            break;
                                        }
                                    };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 293))

    def test_294(self):
        input = """
            func (p Person) Greet() string {
                for i := 0
                    i < 10
                    i += 1 {
                    return
                }
                for i := 0
                    i < 10
                    i += 1
                {
                    return
                }
            };
"""
        expect = "Error on line 10 col 27: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 294))

    def test_295(self):
        input = """
                                    func Add() {
                                        a[2][3].foo(2 + 3, a {a:2})
                                    };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 295))

    def test_296(self):
        input = """
                                    func Add() {
                                        return (2 + 3).b
                                        return -1.c
                                    }"""
        expect = "Error on line 4 col 51: c"
        self.assertTrue(TestParser.checkParser(input, expect, 296))

    def test_297(self):
        input = """
                                    func Add() {
                                        if (1) {return;}
                                        else if(2) {return string}
                                        else if(3) {reutrn int;}
                                    }"""
        expect = "Error on line 4 col 41: else"
        self.assertTrue(TestParser.checkParser(input, expect, 297))

    def test_298(self):
        input = """const a = (-1).c;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 298))

    def test_299(self):
        input = """
                                    func Add() {
                                        if (x.foo().b[2]) {
                                            if (1){return; } else {return; }

                                        } else if(2) {return;
                                        }
                                    };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 299))

    def test_extended(self):
        input = """
            func (p Person) Greet() string {
                if (1) {return;}
                else if (1)
                {}
            };
"""
        expect = "Error on line 4 col 17: else"
        self.assertTrue(TestParser.checkParser(input, expect, 2000))

        input = "const Mn = 1;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 2001))

        input = "const Mn = true;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 2002))

        input = "const Mn = false;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 2003))

        input = "const Mn = foo(1+1);"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 2004))

        input = "const Mn = 2 + 2 - 2 ** 2 // 2 % 2;"
        expect = "Error on line 1 col 23: *"
        self.assertTrue(TestParser.checkParser(input, expect, 2005))

        input = "const Mn = nil;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 2006))

        input = "const Mn = [ID1][ID2]int{1, \"string\", {1.21, \"nhat\"}};"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 2007))

        input = "const Mn = [nil]ID3{1, \"string\", {1.21, \"nhat\"}};"
        expect = "Error on line 1 col 13: nil"
        self.assertTrue(TestParser.checkParser(input, expect, 2008))

        input = """

            var x int = foo() + 3 / 4;

            var y = "Hello" / 4;   

            var z str;

        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 2009))

        input = """

            var x int = foo() + 3 / 4

            var y = "Hello" / 4;   

            var z NHAT;

        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 2010))

        input = """

                                    func Add() {

                                        (1+2).foo(2 + 3, a {a:2})

                                    }"""

        expect = "Error on line 7 col 38: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 2011))
