pragma circom 2.0.3;

include "../libs/circomlib-matrix/circuits/outer.circom";

component main = outer(2,3);

/* INPUT = {
    "a": ["1","2"],
    "b": ["3","4","5"]
} */