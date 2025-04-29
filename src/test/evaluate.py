import csv
import json
import os
import pandas as pd


output_file = 'evaluation.csv'
results_dir = os.path.join(os.path.dirname(__file__), "results")
TP = TN = FP = FN = 0

output_rows = []
file = open("zkap.txt", "r")
data = file.readline()

file_not_check = [
    "ECDSAVerifyNoPubkeyCheck@circom-ecdsa@n=64@k=4.circom",
    "secp256k1ScalarMult@circom-ecdsa@n=64@k=4.circom",
    "mnist_convnet_test.circom",
    "mnist_test.circom",
    "Ark@poseidon.circom",
    "BabyPbk@babyjub.circom",
    "Bits2Point_Strict@pointbits.circom",
    "Poseidon@poseidon.circom",
    "Sigma@poseidon.circom",
    "CoreVerifyPubkeyG1@circom-pairing@n=55@k=7.circom",
    "batchverify.circom",
    "inversemodulo1.circom",
    "modulus0.circom",
    "modulus2.circom",
    "modulusq2.circom",
    "verify.circom",
    "test-decode-tx.circom",
    "test-fee-tx.circom",
    "test-hash-inputs.circom",
    "test-rollup-main-L1.circom",
    "test-rollup-tx-states.circom",
    "test-rollup-tx.circom",
    "test-withdraw.circom",
    "hydra-s1.circom",
    "verify-hydra-commitment.circom",
    "verify-merkle-path.circom",
    'auth.circom',
    'authTest.circom',
    'authWithRelayTest.circom',
    'credentialAtomicQueryMTP.circom',
    'credentialAtomicQueryMTPTest.circom',
    'credentialAtomicQueryMTPWithRelay.circom',
    'credentialAtomicQueryMTPWithRelayTest.circom',
    'micQueryMTPWithRelay.cicredentialAtomicQuerySig.circom',
    'credentialAtomicQuerySigTest.circom',
    'idOwnershipBySignatureWithRelayTest.circom',
    'poseidon.circom',
    'iden3-coreWithRelayTest.circom',
    'poseidon14.circom',
    'poseidon16.circom',
    'stateTransition.circom',
    'stateTransitionTest.circom',
    'utils_checkIdenStateMatchesRoots.circom',
    'utils_getClaimEcircom',
    'benchmaxpiration.circom',
    'utils_getClaimSubjectOtherIden.circom',
    'utils_getSubjectLocation.circom',
    'utils_GetValueByIndex.circom',
    'utils_isExpirable.circom',
    'utils_isUpdatabldatable.circom',
    'utils_verifyClaimSignature.circom',
    'utils_verifyCredentialSubject.circom',
    'utils_verifyExpirationTime.circom',
    "credentialAtomicQuerySig.circom",
    "idOwnershipBySignatureTest.circom",
    "utils_getClaimExpiration.circom",
    "utils_isUpdatable.circom",
    "Rotate@telepathy.circom",
    "absorb_test.circom",
    "final_test.circom",
    "keccakf_test.circom",
    "keccak_256_256_test.circom",
    "keccak_32_256_test.circom",
    "batchUpdateStateTree_32.circom",
    "batchUpdateStateTree_32_batch16.circom",
    "batchUpdateStateTree_32_batch256.circom",
    "batchUpdateStateTree_large.circom",
    "batchUpdateStateTree_medium.circom",
    "batchUpdateStateTree_small.circom",
    "batchUpdateStateTree_test.circom",
    "hasher11_test.circom",
    "hasher5_test.circom",
    "hashleftright_test.circom",
    "merkleTreeCheckRoot_test.circom",
    "merkleTreeInclusionProof_test.circom"
    "merkleTreeLeafExists_test.circom",
    "merkleTreeLeafExists_test.circom",
    "merkleTreeInclusionProof_test.circom",
    "performChecksBeforeUpdate_test.circom",
    "quadVoteTally_32.circom",
    "quadVoteTally_32_batch16.circom",
    "quadVoteTally_32_batch256.circom",
    "quadVoteTally_large.circom",
    "quadVoteTally_medium.circom",
    "quadVoteTally_small.circom",
    "quadVoteTally_test.circom",
    "quinGeneratePathIndices_test.circom",
    "quinSelector_test.circom",
    "quinTreeCheckRoot_test.circom",
    "quinTreeInclusionProof_test.circom",
    "quinTreeLeafExists_test.circom",
    "resultCommitmentVerifier_test.circom",
    "splicer_test.circom",
    "updateStateTree_test.circom",
    "verifySignature_test.circom",
    "semaphore.circom",
    "delete.circom",
    "insert.circom",
    "select.circom",
    "update.circom",
    "hashTable.circom",
    "utils.circom"
]

while data:
    col = data.split(",")
    name, project, groundtruth = col[0], col[1], col[2]
    if name in file_not_check:
        data = file.readline()
        continue
    name = name + "_report.json"
    if project == "circomlib":
        project = "circomlib-cff5ab6"
    if project == "iden3-core-56a08f20" or project == "iden3-core-56a08f24":
        project = "iden3-core-56a08f9"
    if "keccak256" in project:
        project = "keccak256-circom-af3e898"
    json_path = results_dir + "\\" + project + "\\" + name

    result = 'file not found'
    evaluation = 'Incorrect'

    if os.path.exists(json_path):
        with open(json_path, 'r', encoding='utf-8') as jf:
            try:
                data = json.load(jf)
                if data == {}:
                    result = 'safe'
                else:
                    result = 'unsafe'
            except json.JSONDecodeError:
                result = 'invalid json'

        if groundtruth == result:
            evaluation = 'Correct'
        else:
            evaluation = 'Incorrect'

        if groundtruth == "":
            if col[3] == col[4][:-1]:
                groundtruth = col[3]

        if groundtruth == 'unsafe' and result == 'unsafe':
            TP += 1
        elif groundtruth == 'safe' and result == 'safe':
            TN += 1
        elif groundtruth == 'safe' and result == 'unsafe':
            FP += 1
            print("false positive =", json_path)
        elif groundtruth == 'unsafe' and result == 'safe':
            FN += 1
            print("false negative =", json_path)

    output_rows.append({
        'Name': name,
        'Project': project,
        'Groundtruth': groundtruth,
        'Result': result,
        'Evaluation': evaluation
    })
    data = file.readline()


file.close()

total = TP + TN + FP + FN
accuracy = (TP + TN) / total if total > 0 else 0
precision = TP / (TP + FP) if (TP + FP) > 0 else 0
recall = TP / (TP + FN) if (TP + FN) > 0 else 0
f1_score = 2 * precision * recall / \
    (precision + recall) if (precision + recall) > 0 else 0

print("\n=== Evaluation Report ===")
print(f"Total Samples: {total}")
print(f"True Positive (TP): {TP}")
print(f"True Negative (TN): {TN}")
print(f"False Positive (FP): {FP}")
print(f"False Negative (FN): {FN}")
print(f"Accuracy: {accuracy:.4f}")
print(f"Precision (unsafe): {precision:.4f}")
print(f"Recall (unsafe): {recall:.4f}")
print(f"F1-Score (unsafe): {f1_score:.4f}")
