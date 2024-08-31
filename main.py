import argparse
from analyzer import process_bytecode, process_ast, process_opcode, count_keywords_in_code

def integrate_features_and_print(source_code):
    features = {}
    features.update(process_bytecode(source_code) , process_ast(source_code) , 
                    process_opcode(source_code) , count_keywords_in_code(source_code))
    return features

def main():
    parser = argparse.ArgumentParser(description='Process some Solidity source code.')
    parser.add_argument('source_file', type=str, help='A file containing Solidity source code to analyze')
    args = parser.parse_args()

    with open(args.source_file, 'r') as file:
        source_code = file.read()

    features = integrate_features_and_print(source_code)
    for feature, value in features.items():
        print(f'{feature}: {value}')

if __name__ == '__main__':
    main()
