pragma circom 2.0.0;

include "../libs/circomlib/circuits/comparators.circom";
include "../libs/circomlib/circuits/gates.circom";
include "./utils/hashTable.circom";
include "./utils/utils.circom";

template INSERT(c,r) {
    signal input header[c];
    signal input table[r][c];
    signal input tableCommit;

    signal input insertValues[c];
    signal input argsCommit;
    
    signal output newTableCommit;
    signal modified[r+1][c];

    var i;
    var j;

    // Hash arguments
    component preImage = CalculateTotal(c);
    component argsHasher = Poseidon(1);

    for (i=0;i<c;i++) {
        preImage.nums[i] <== insertValues[i];
    }

    argsHasher.inputs[0] <== preImage.sum;
    argsHasher.out === argsCommit;


    // Hash table along with header
    component hasher = HashTable(c,r);

    for (i=0;i<c;i++) {
        hasher.header[i] <== header[i];
    }
    for (i=0;i<r;i++) {
        for (j=0;j<c;j++) {
            hasher.table[i][j] <== table[i][j];
        }
    }

    // Check that the table corresponds to commitment
    hasher.out === tableCommit;

    for (i=0; i<r; i++) {
        for (j=0; j<c; j++) {
            modified[i][j] <== table[i][j];
        }
    }

    for (j=0; j<c; j++) {
        modified[r][j] <== insertValues[j];
    }

    // Hash table and header again to produce new commitment.
    component newHasher = HashTable(c,r+1);

    for (i=0;i<c;i++) {
        newHasher.header[i] <== header[i];
    }

    for (i=0;i<r+1;i++) {
        for (j=0;j<c;j++) {
            newHasher.table[i][j] <== modified[i][j];
        }
    }

    newTableCommit <== newHasher.out;
}

component main {public [tableCommit, argsCommit]} = INSERT(5, 10);
