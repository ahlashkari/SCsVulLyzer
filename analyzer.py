import json
from collections import Counter
import scipy.stats as ss
import solcx
import re

def count_keys(obj, key_to_count):
    count = 0
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key == key_to_count:
                count += 1
            count += count_keys(value, key_to_count)
    elif isinstance(obj, list):
        for item in obj:
            count += count_keys(item, key_to_count)
    return count

def compile_solidity_source(source_code):
    solcx.install_solc('0.4.24')
    compiled_sol = solcx.compile_source(source_code, output_values=["ast", "bin","opcodes"])
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

def calculate_weights(bytecode):
    counter = Counter(bytecode)
    total = len(bytecode)
    weights = {}
    for char in '0123456789abcdef':
        key = f'weight_Bytecode_numberOf_character_{char}'
        weights[key] = counter.get(char, 0) / total
    return weights

def calculate_opcode_sums(opcodes):
    opcode_list = ['CALL', 'ADD','POP','JUMP','AND','OR','MSTORE','ISZERO','JUMPDEST','JUMPI','SLOAD','RETURN','REVERT','SUB','MLOAD','DIV','EXP','MUL','EQ','MUL','DIV','EXP','AND','OR','NOT','BYTE','ADDRESS','MSTORE','MSTORE8','SLOAD','SSTORE','JUMPI', 'INVALID', 'DUP', 'PUSH','SWAP']
    weights = {}
    for op in opcode_list:
        weights[f'weight_sums_{op}'] = opcodes.count(op) * 1
    return weights

def extract_keywords_from_source(code, keywords):
    keywords_list = [
      'from', 'require', 'dev', 'internal', 'string', 'view', 'mapping', 'sub', 'emit', 'length',
      'pure', 'will', 'not', 'approve', 'external', 'memory', 'eth', 'else', 'can', 'calls', 'data', 'q'
    ]
    keyword_counts = dict.fromkeys(keywords, 0)
    words = re.split(r'\W+', code)
    for word in words:
        if word in keyword_counts:
            keyword_counts[word] += 1
    return keyword_counts