import os
import sys

locpath = [
    '../../src/main/Circom/parser/',
    '../../src/main/Circom/astgen/',
    '../../src/main/Circom/typecheck/',
    '../../src/main/Circom/utils/',
    '../../src/main/Circom/cdggen/',
    '../../src/main/Circom/detect/',
    '../../target/',
    '../../'
]

for p in locpath:
    if p not in sys.path:
        sys.path.append(p)


def test_known_bugs():
    knownbugs_dir = "../../benchmarks/knownbugs"
    results_dir = os.path.join(os.path.dirname(__file__), "results")
    knownbugs_results_dir = os.path.join(results_dir, "knownbugs")

    if not os.path.exists(knownbugs_results_dir):
        os.makedirs(knownbugs_results_dir)

    bug_files = [os.path.join(knownbugs_dir, file) for file in os.listdir(
        knownbugs_dir) if file.endswith(".circom")]

    for file_path in bug_files:
        print(f"[Info]       Running analysis for {file_path}")
        graphs, reports = detect(file_path)
        if graphs:
            report_to_file(graphs, reports, os.path.join(
                knownbugs_results_dir, f"{os.path.basename(file_path)}_report.json"))
        print("---------------------------------------------")


def test_other_bugs():
    benchmarks_dir = "../../benchmarks"
    results_dir = os.path.join(os.path.dirname(__file__), "results")

    count = 0

    # checked already
    done_dir = [
        "aes-circom",
        "circom-ecdsa",
        "circom-matrix",
        "circom-ml",
        "circom-pairing",
        "circomlib-cff5ab6",
        "darkforest-eth-9033eaf",
        "ed25519-099d19c",
        "hermez-network-9a696e3-fixed",
        "hydra-2010a65",
        "iden3-core-56a08f9",
        "internal"
    ]

    # Because it's cause time out.
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
        "Rotate@telepathy.circom"
    ]

    for root, dirs, files in os.walk(benchmarks_dir):
        if 'libs' in dirs:
            dirs.remove('libs')

        subdir_name = os.path.basename(root)
        if subdir_name in done_dir:
            continue
        subdir_results_dir = os.path.join(results_dir, subdir_name)
        if not os.path.exists(subdir_results_dir):
            os.makedirs(subdir_results_dir)

        bug_files = [os.path.join(root, file)for file in files if file.endswith(
            ".circom") and file not in file_not_check]
        fails = []
        for file_path in bug_files:
            # tests = [
            #     '../../benchmarks\\hermez-network-9a696e3-fixed\\']
            # if file_path not in tests:
            #     continue
            # if file_path != tests[0]:
            #     continue
            print(f"[Info]       Running analysis for {file_path}")
            graphs, reports = detect(file_path)
            if graphs:
                report_to_file(graphs, reports, os.path.join(
                    subdir_results_dir, f"{os.path.basename(file_path)}_report.json"))
            else:
                fails.append(file_path)
            print("---------------------------------------------")
        count += 1
        print(fails)
        if count == 2:
            break


if __name__ == "__main__":
    from circheck import detect, report_to_file

    # test_known_bugs()
    test_other_bugs()
