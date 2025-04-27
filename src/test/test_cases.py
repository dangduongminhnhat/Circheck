import os
import unittest
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
    if not p in sys.path:
        sys.path.append(p)
# sys.path.append(os.path.abspath(
#     os.path.join(os.path.dirname(__file__), "../..")))


class TestCircomAnalysis(unittest.TestCase):

    def setUp(self):
        self.results_dir = os.path.join(os.path.dirname(__file__), "results")
        if not os.path.exists(self.results_dir):
            os.makedirs(self.results_dir)

    def test_known_bugs(self):
        knownbugs_dir = "../../benchmarks/knownbugs"
        bug_files = [os.path.join(knownbugs_dir, file) for file in os.listdir(
            knownbugs_dir) if file.endswith(".circom")]

        for file_path in bug_files:
            print(f"[Info]       Running analysis for {file_path}")
            graphs, reports = detect(file_path)
            if graphs:
                report_to_file(graphs, reports, os.path.join(
                    self.results_dir, f"{os.path.basename(file_path)}_report.json"))


if __name__ == "__main__":
    from circheck import detect, report_to_file
    unittest.main()
