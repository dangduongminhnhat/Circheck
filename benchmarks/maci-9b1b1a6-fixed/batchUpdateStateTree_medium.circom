pragma circom 2.0.8;

include "../libs/maci-9b1b1a6-fixed/batchUpdateStateTree.circom";

// state_tree_depth,
// message_tree_depth,
// vote_options_tree_depth,
// batch_size

component main = BatchUpdateStateTree(9, 13, 3, 4);
