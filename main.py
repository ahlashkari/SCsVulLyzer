import argparse
from analyzer import count_keys, compile_solidity_source, calculate_bytecode_entropy, calculate_weights, calculate_opcode_sums, extract_keywords_from_source

def integrate_features_and_print(source_code):
    bytecode, ast, opcodes = compile_solidity_source(source_code)
    features = {
        'Bytecode_entropy': calculate_bytecode_entropy(bytecode),
        'AST_source_id': ast['id'],
        'AST_numberOf_exportedSymbols': count_keys(ast, 'exportedSymbols'),
        'AST_numberOf_nodes': count_keys(ast,'id'),
    }
    features.update(calculate_weights(bytecode))
    features.update(calculate_opcode_sums(opcodes))
    keywords_list = [
        'from', 'require', 'dev', 'internal', 'string', 'view', 'mapping', 'sub', 'emit', 'length','pure', 'will', 'not', 'approve', 'external', 'memory', 'eth', 'else', 'can', 'calls', 'data', 'q' , 'eth', 'else', 'can','calls', 'data', 'q' ]
    features.update(extract_keywords_from_source(source_code, keywords_list))
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