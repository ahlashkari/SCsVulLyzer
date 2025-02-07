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
        "Bytecode Character Count": count_bytecode(solidity_code)
    }

    return flatten_analysis_result(analysis_result)
  
def rename_out(output):
    rename_map = {
        'Contract Information_0': "length of contract_name",
        'Contract Information_1': "length of base_contract",
        'Lines of Code_0':"Number of total_lines",
        'Lines of Code_1':"Number of code_lines",
        'Lines of Code_2':"Number of comment_lines",
        'Lines of Code_3':"Number of blank_lines",
        'Solidity Features_1': 'Solidity delegatecall',
        'Solidity Features_2': 'Solidity callcode',
        'Solidity Features_3': 'Solidity call',
        'Solidity Features_4': 'Solidity send',
        'Solidity Features_5': 'Solidity transfer',
        'Solidity Features_6': 'Solidity selfdestruct',
        'Solidity Features_7': 'Solidity create',
        'Functional Features_2': 'Functional_Number of "public"',
        'Functional Features_3': 'Functional_Number of "if"',
        'Functional Features_4': 'Functional_Number of "while"'
    }
    renamed_output = {rename_map.get(k, k): v for k, v in output.items()}
    
    return renamed_output

def main():
    parser = argparse.ArgumentParser(description='Analyze Solidity source code.')
    parser.add_argument('source_file', type=str, help='Path to the Solidity source code file to analyze')
    args = parser.parse_args()

    features = rename_out(analyze_solidity_contract(args.source_file))
    for feature, value in features.items():
        print(f'{feature}: {value}')

if __name__ == '__main__':
    main()
