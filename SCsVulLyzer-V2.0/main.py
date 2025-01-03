import argparse
from secondAnalyzer import *

def analyze_solidity_contract(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            solidity_code = file.read()
    except UnicodeDecodeError:
        with open(file_path, 'r', encoding='latin-1') as file:
            solidity_code = file.read()

    analysis_result = {
        "Contract Information": extract_contract_info(solidity_code),
        "Lines of Code": calculate_loc(solidity_code),
        "Solidity Features": detect_solidity_features(solidity_code),
        "Duplicate Lines Count": detect_duplicates(solidity_code),
        "Event Count": extract_events(solidity_code),
        "Functional Features": extract_functional_features(solidity_code),
        "AST Features": extract_ast_features(solidity_code),
        "ABI Features": extract_abi_features(solidity_code),
        "Opcode Count Features": count_opcodes(solidity_code),
        "Bytecode Length and Entropy": extract_length_and_entropy(solidity_code),
        "Bytecode Character Count": extract_character_count(solidity_code)
    }

    return flatten_analysis_result(analysis_result)

def main():
    parser = argparse.ArgumentParser(description='Analyze Solidity source code.')
    parser.add_argument('source_file', type=str, help='Path to the Solidity source code file to analyze')
    args = parser.parse_args()

    features = analyze_solidity_contract(args.source_file)
    for feature, value in features.items():
        print(f'{feature}: {value}')

if __name__ == '__main__':
    main()