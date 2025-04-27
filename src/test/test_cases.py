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
    for root, dirs, files in os.walk(benchmarks_dir):
        if 'knownbugs' in dirs:
            dirs.remove('knownbugs')
        if 'libs' in dirs:
            dirs.remove('libs')

        subdir_name = os.path.basename(root)
        subdir_results_dir = os.path.join(results_dir, subdir_name)
        if not os.path.exists(subdir_results_dir):
            os.makedirs(subdir_results_dir)

        bug_files = [os.path.join(root, file)
                     for file in files if file.endswith(".circom")]

        for file_path in bug_files:
            print(f"[Info]       Running analysis for {file_path}")
            graphs, reports = detect(file_path)
            if graphs:
                report_to_file(graphs, reports, os.path.join(
                    subdir_results_dir, f"{os.path.basename(file_path)}_report.json"))
            print("---------------------------------------------")
            break
        count += 1
        if count == 2:
            break


if __name__ == "__main__":
    from circheck import detect, report_to_file

    # test_known_bugs()
    test_other_bugs()
