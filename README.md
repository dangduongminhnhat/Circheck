# Circheck: Detecting Semantic Vulnerabilities in Circom using Circuit Dependence Graphs

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.16741615.svg)](https://doi.org/10.5281/zenodo.16741615)
This repository contains the source code and evaluation framework for the research paper: **"Circheck: Detecting Semantic Vulnerabilities in Circom using Circuit Dependence Graphs"**.

## About

Circheck is a static analysis framework designed to automatically detect semantic vulnerabilities in Circom circuits. By constructing a Circuit Dependence Graph (CDG) to model signal and constraint dependencies, Circheck targets nine classes of common vulnerabilities that, while syntactically valid, can lead to invalid proofs or information leakage. Our evaluation demonstrates that Circheck achieves competitive, state-of-the-art performance, with a high recall of 96% and an F1-score of 0.83.

## Installation

To install Circheck, you can clone the repository and install the required dependencies:

```bash
git clone https://github.com/dangduongminhnhat/Circheck.git
cd Circheck
pip install -r requirements.txt
```

or you can install Circheck via pip, use the following command:

```bash
pip install circheck
```

## Reproducing Paper Results

To reproduce all quantitative results presented in our paper (specifically Tables III, IV, and V in Section VII), run the main evaluation script.

This script will execute Circheck on the 118 benchmark circuits. The final summary tables matching those in the paper will be printed to your console at the end of the execution. Detailed logs for each run will be saved to the following files:

- `src/test/log_per_project.txt`
- `src/test/log_per_file.txt`

To start the evaluation, run:

```bash
python src/test/test_cases.py
```

## Usage

Circheck is a static analysis tool designed to detect ZKP vulnerabilities in Circom circuits. You can use it via the command line interface (CLI) to analyze Circom code and generate reports.

### Command Line Arguments

- `input`: **Required** - The path to the Circom file you want to analyze.
- `--json`: **Optional** - If specified, the tool will output a JSON report to the given file. The output file must end with `.json`.

### Example Usage

1. **Basic Analysis:**
   To analyze a Circom file and print the report to the console:

   ```bash
   circheck path/to/your/file.circom
   ```

   This will run the analysis and display the results directly in the terminal.

2. **Generate JSON Report:**
   To analyze the Circom file and save the report in a JSON file:

   ```bash
   circheck path/to/your/file.circom --json path/to/output/report.json
   ```

   This will run the analysis and save the results in the specified JSON file.

## Features

Circheck detects a variety of potential issues in Circom circuits, including:

- **Unconstrained Output Signals**: Detects output signals that are not constrained by any constraints.
- **Unconstrained Component Inputs**: Identifies input signals to components that are not constrained and may accept unchecked values.
- **Data Flow Constraint Discrepancy**: Finds signals that depend on others via dataflow but lack corresponding constraint dependencies.
- **Unused Component Outputs**: Warns when outputs of components are not used or checked in the circuit.
- **Unused Signals**: Identifies signals that are declared but never used in any computation or constraint.
- **Type Mismatch**: Detects potential type mismatches, such as signals flowing into templates like `Num2Bits` without proper range checks.
- **Assignment Misuse**: Finds assignment misuse, where a variable is assigned using the wrong operator.
- **Divide by Zero**: Warns of potential divide-by-zero issues in the circuit.
- **Non-deterministic Data Flow**: Flags conditional assignments depending on signals, which may lead to non-deterministic data flows.

## How to Cite

If you use Circheck in your research, please cite our paper:

```
@article{dang2025circheck,
  author    = {Minh Nhat Dang-Duong and Cao Thang Trinh and Nhat Minh Pham and Khuong Nguyen-An},
  title     = {Circheck: Detecting Semantic Vulnerabilities in Circom using Circuit Dependence Graphs},
  journal   = {IEEE Transactions on Dependable and Secure Computing},
  year      = {2025},
  note      = {Submitted for review}
}
```

## License

Licensed under the [MIT License](LICENSE) © 2025 Dang Duong Minh Nhat.
