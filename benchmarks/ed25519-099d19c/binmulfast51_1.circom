pragma circom 2.0.0;

include "../libs/ed25519-099d19c-fixed/chunkedmul.circom";
component main = ChunkedMul(4, 4, 51);