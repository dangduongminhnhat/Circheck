pragma circom 2.0.2;

include "../libs/circom-ecdsa/circuits/secp256k1.circom";

component main {public [in]} = Secp256k1Double(64, 4);
