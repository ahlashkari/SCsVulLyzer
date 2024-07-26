import json
from collections import Counter
import scipy.stats as ss
import solcx
import re

def compile_solidity_source(source_code):
    solcx.install_solc(version="0.4.24")
    solcx.set_solc_version("0.4.24")
    compiled_sol = solcx.compile_source(source_code, output_values=["ast", "bin", "opcodes"])
    contract_id, contract_interface = compiled_sol.popitem()
    bytecode = contract_interface['bin']
    ast = contract_interface['ast']
    opcodes = contract_interface['opcodes']
    return bytecode, ast, opcodes

def calculate_bytecode_entropy(bytecode):
    counter = Counter(bytecode)
    probabilities = [count / len(bytecode) for count in counter.values()]
    entropy = ss.entropy(probabilities, base=2)
    return entropy

def process_bytecode(source_code):
    bytecode  = compile_solidity_source(source_code)[0]
    bytecode_dic = {}
    bytecode_dic['bytecode_len'] = len(bytecode)
    char_count = Counter(bytecode)
    total_chars = sum(char_count.values())
    prefix = 'Weight bytecode_character_'
    weight_char_count = {prefix + key: value / total_chars for key, value in char_count.items()}
    bytecode_dic.update(weight_char_count)
    prefix = 'bytecode_character_'
    char_count = {prefix + key: value for key, value in char_count.items()}
    bytecode_dic.update(char_count)
    bytecode_dic['bytecode_entropy'] = calculate_bytecode_entropy(bytecode)
    return bytecode_dic


def process_ast(source_code):
    ast  = compile_solidity_source(source_code)[1]
    ast_dic = {}
    ast_dic['ast_len_exportedSymbols'] = len(ast['attributes'])
    ast_dic['ast_id'] = ast['id']
    ast_dic['ast_nodetype'] = ast['name']
    ast_dic['ast_src'] = ast['src']
    ast_dic['ast_len_nodes'] = len(ast['children'])
    return ast_dic

def process_opcode(source_code):
    opcode_frequency_dic = {}
    opcodes  = compile_solidity_source(source_code)[2].split(' ')
    opcode_count = Counter(opcodes)
    opcode_list = ['STOP', 'ADD', 'MUL', 'SUB', 'DIV', 'SDIV', 'MOD', 'SMOD', 'ADDMOD', 'MULMOD', 'EXP', 'SIGNEXTEND',                  
                 'LT', 'GT', 'SLT', 'SGT', 'EQ', 'ISZERO', 'AND', 'OR', 'XOR', 'NOT', 'BYTE', 'SHL', 'SHR', 'SAR',                  
                 'SHA3', 'ADDRESS', 'BALANCE', 'ORIGIN', 'CALLER', 'CALLVALUE', 'CALLDATALOAD', 'CALLDATASIZE',                  
                 'CALLDATACOPY', 'CODESIZE', 'CODECOPY', 'GASPRICE', 'EXTCODESIZE', 'EXTCODECOPY', 'RETURNDATASIZE',                  
                 'RETURNDATACOPY', 'BLOCKHASH', 'COINBASE', 'TIMESTAMP', 'NUMBER', 'DIFFICULTY', 'GASLIMIT', 'POP',                  
                 'MLOAD', 'MSTORE', 'MSTORE8', 'SLOAD', 'SSTORE', 'JUMP', 'JUMPI', 'PC', 'MSIZE', 'GAS', 'JUMPDEST',                  
                 'PUSH1', 'PUSH2', 'PUSH3', 'PUSH4', 'PUSH5', 'PUSH6', 'PUSH7', 'PUSH8', 'PUSH9', 'PUSH10', 'PUSH11',                  
                 'PUSH12', 'PUSH13', 'PUSH14', 'PUSH15', 'PUSH16', 'PUSH17', 'PUSH18', 'PUSH19', 'PUSH20', 'PUSH21',                  
                 'PUSH22', 'PUSH23', 'PUSH24', 'PUSH25', 'PUSH26', 'PUSH27', 'PUSH28', 'PUSH29', 'PUSH30', 'PUSH31',                  
                 'PUSH32', 'DUP1', 'DUP2', 'DUP3', 'DUP4', 'DUP5', 'DUP6', 'DUP7', 'DUP8', 'DUP9', 'DUP10', 'DUP11',                  
                 'DUP12', 'DUP13', 'DUP14', 'DUP15', 'DUP16', 'SWAP1', 'SWAP2', 'SWAP3', 'SWAP4', 'SWAP5', 'SWAP6',                  
                 'SWAP7', 'SWAP8', 'SWAP9', 'SWAP10', 'SWAP11', 'SWAP12', 'SWAP13', 'SWAP14', 'SWAP15', 'SWAP16',                  
                 'LOG0', 'LOG1', 'LOG2', 'LOG3', 'LOG4', 'CREATE', 'CALL', 'CALLCODE', 'RETURN', 'DELEGATECALL',                  
                 'STATICCALL', 'REVERT', 'INVALID', 'SELFDESTRUCT']
    # Remove items not in opcode_list
    keys_to_remove = set(opcode_count.keys()) - set(opcode_list)
    for key in keys_to_remove:
        opcode_count.pop(key)
    total_opcodes = sum(opcode_count.values())
    # Calculate frequency of each opcode
    for opcode in opcode_list:
        frequency = opcode_count.get(opcode, 0) / total_opcodes if total_opcodes > 0 else 0
        opcode_frequency_dic = {"Opcode weight " + opcode: opcode_count.get(opcode, 0) / total_opcodes if total_opcodes > 0 else 0 for opcode in opcode_list}
    return opcode_frequency_dic

def count_keywords_in_code(source_code):
    # Prepare a regex pattern to match whole words only, case-insensitive
    keywords_list = ['from', 'require', 'dev', 'internal', 'string', 'view', 'mapping', 'sub', 'emit', 'length','pure', 'will', 'not', 'approve', 'external', 'memory', 'eth', 'else', 'can', 'calls', 'data', 'q' , 'eth', 'else', 'can','calls', 'data', 'q' ]
    patterns = {keyword: re.compile(r'\b' + re.escape(keyword) + r'\b', re.IGNORECASE) for keyword in keywords_list}
    # Initialize a dictionary to store the count of each keyword
    keyword_counts = {keyword: 0 for keyword in keywords_list}
    # Count occurrences of each keyword using the prepared regex patterns
    for keyword, pattern in patterns.items():
        matches = pattern.findall(source_code)
        keyword_counts[keyword] = len(matches)
    # Return the dictionary with keyword counts
    return keyword_counts
