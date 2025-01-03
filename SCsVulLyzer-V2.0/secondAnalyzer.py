import re
from packaging import version
import solcx
from solcx.exceptions import SolcError, SolcInstallationError
import pandas as pd

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

def compile_with_correct_solidity_version(source_code):
    default_version = '0.4.24'

    try:
        match = re.search(r'pragma solidity (.*?);', source_code)
        if not match:
            version_str = default_version
        else:
            potential_versions = re.split(r'[^\d\.]+', match.group(1))
            version_str = next((v for v in potential_versions if re.fullmatch(r'\d+\.\d+\.\d+', v)), default_version)

            # Removing leading zeros from version components
            version_parts = version_str.split('.')
            version_str = '.'.join(str(int(part)) for part in version_parts)

            try:
                if version.parse(version_str) < version.parse("0.4.11"):
                    version_str = default_version
                elif "constructor" in source_code and version.parse(version_str) < version.parse("0.4.22"):
                    version_str = "0.4.22"
            except version.InvalidVersion:
                # print(f"Invalid version string: {version_str}. Falling back to {default_version}.")
                version_str = default_version

        installed_versions = solcx.get_installed_solc_versions()
        if version_str not in installed_versions:
            solcx.install_solc(version_str)

        solcx.set_solc_version(version_str)

        return solcx.compile_source(source_code)

    except (SolcError, SolcInstallationError) as e:
        # print(f"Error: {e}.")
        return None  # or handle the error as appropriate for your needs

def extract_ast_features(solidity_code):
    features = {}
    try:
        compiled_source = compile_with_correct_solidity_version(solidity_code)
        contract_name = list(compiled_source.keys())[0]
        ast = compiled_source[contract_name]["ast"]
        features['ast_len_exportedSymbols'] = len(ast.get('exportedSymbols', {}))  # Added check for 'exportedSymbols' key
        features['ast_id'] = ast['id']
        features['ast_nodetype'] = ast['nodeType']
        features['ast_src'] = ast['src']
        features['ast_len_nodes'] = len(ast['nodes'])
    except Exception as e:
        # print(f"An error occurred: {e}")
        features = {
            'ast_len_exportedSymbols': 0,
            'ast_id': 0,
            'ast_nodetype': 0,
            'ast_src': 0,
            'ast_len_nodes': 0,
        }
    return pd.Series(features)

def extract_abi_features(solidity_code):
    features = {}
    try:
        compiled_source = compile_with_correct_solidity_version(solidity_code)
        contract_name = list(compiled_source.keys())[0]
        abi = compiled_source[contract_name]["abi"]
        list_constact = []
        list_input = []
        list_name = []
        list_output = []
        list_payable = []
        list_stateMut = []
        list_type = []

        for item in abi:
            list_constact.append(item.get('constant'))
            list_name.append(item.get('name'))
            list_payable.append(item.get('payable'))
            list_stateMut.append(item.get('stateMutability'))
            list_type.append(item.get('type'))
            list_output.append(len(item.get('outputs')) if item.get('outputs') else 0)
            list_input.append(len(item.get('inputs')) if item.get('inputs') else 0)

        # Creating feature dictionary
        features['len_list_constant'] = len([i for i in list_constact if i is not None])
        features['len_list_name'] = len([i for i in list_name if i is not None])
        features['len_list_payable'] = len([i for i in list_payable if i is not None])
        features['len_list_stateMut'] = len([i for i in list_stateMut if i is not None])
        features['len_list_type'] = len([i for i in list_type if i is not None])
        features['len_non_zero_input'] = len([i for i in list_input if i != 0])
        features['len_list_input'] = sum(list_input)
        features['len_zero_input'] = sum(list_input) - len([i for i in list_input if i != 0])
        features['len_non_zero_output'] = len([i for i in list_output if i != 0])
        features['len_list_output'] = sum(list_output)
        features['len_zero_output'] = sum(list_output) - len([i for i in list_output if i != 0])

    except Exception as e:
        features['len_list_constant'] = 0
        features['len_list_name'] = 0
        features['len_list_payable'] = 0
        features['len_list_stateMut'] = 0
        features['len_list_type'] = 0
        features['len_non_zero_input'] = 0
        features['len_list_input'] = 0
        features['len_non_zero_output'] = 0
        features['len_list_output'] = 0
        features['len_zero_input'] = 0
        features['len_zero_output'] = 0
    return pd.Series(features)

def count_opcodes(solidity_code):
    opcode_count_features = {}
    try:
        compiled_source = compile_with_correct_solidity_version(solidity_code)
        contract_name = list(compiled_source.keys())[0]
        opcodes = compiled_source[contract_name]['opcodes'].split(' ')
        opcode_count = Counter(opcodes)
        # Update to include missing opcodes with a count of 0
        for opcode in opcode_list:
            opcode_count_features[opcode] = opcode_count.get(opcode, 0)

        return opcode_count_features
    except Exception as e:
        # print(f"Error compiling contract: {e}")
        # Return zeros for all opcodes
        return {opcode: 0 for opcode in opcode_list}

import math

def calculate_entropy(bytecode):
    data = bytes.fromhex(bytecode)
    frequencies = [float(data.count(byte)) / len(data) for byte in set(data)]
    entropy = - sum([freq * math.log(freq) / math.log(2.0) for freq in frequencies])
    return entropy

def extract_length_and_entropy(solidity_code):
    features = {}
    try:
        compiled_source = compile_with_correct_solidity_version(solidity_code)
        contract_name = list(compiled_source.keys())[0]
        bytecode = compiled_source[contract_name]['bin']
        features['bytecode_len'] = len(bytecode)
        features['bytecode_entropy'] = calculate_entropy(bytecode)
    except Exception as e:
        features['bytecode_len'] = 0
        features['bytecode_entropy'] = 0

    return pd.Series(features)

from collections import Counter
a = 0
def extract_character_count(solidity_code):
    global a
    char_count_features = {}
    try:
        compiled_source = compile_with_correct_solidity_version(solidity_code)
        contract_name = list(compiled_source.keys())[0]
        bytecode = compiled_source[contract_name]['bin']
        char_count = Counter(bytecode)
        # print(char_count)
        prefix = 'bytecode_character_'
        char_count = {prefix + key: value for key, value in char_count.items()}
        char_count_features.update(char_count)
    except Exception as e:
        char_count_features = {f'bytecode_character_{i}': 0 for i in range(16)}
    a=a+1
    if a%100 == 0:
        print(a/100)
    return pd.Series(char_count_features)

def extract_contract_info(solidity_code):
    contract_match = re.search(r'contract\s+(\w+)', solidity_code)
    base_contract_match = re.search(r'is\s+(\w+)', solidity_code) if 'is' in solidity_code else None
    contract_name = contract_match.group(1) if contract_match else None
    base_contract = base_contract_match.group(1) if base_contract_match else None
    return len(contract_name) if contract_name else 0, len(base_contract) if base_contract else 0

def calculate_loc(solidity_code):
    solidity_code_lines = solidity_code.strip().split('\n')
    total_lines = len(solidity_code_lines)
    code_lines = len([line for line in solidity_code_lines if line.strip() != "" and not line.strip().startswith('//')])
    comment_lines = len([line for line in solidity_code_lines if line.strip().startswith('//')])
    blank_lines = total_lines - code_lines - comment_lines
    return total_lines, code_lines, comment_lines, blank_lines

def detect_solidity_features(solidity_code):
    delegatecall = len(re.findall(r'\.delegatecall\(', solidity_code))
    callcode = len(re.findall(r'\.callcode\(', solidity_code))
    call = len(re.findall(r'\.call\(', solidity_code))
    send = len(re.findall(r'\.send\(', solidity_code))
    transfer = len(re.findall(r'\.transfer\(', solidity_code))
    selfdestruct = len(re.findall(r'selfdestruct\(', solidity_code))
    create = len(re.findall(r'\.create\(', solidity_code))
    create2 = len(re.findall(r'\.create2\(', solidity_code))
    return delegatecall, callcode, call, send, transfer, selfdestruct, create, create2

def detect_duplicates(solidity_code):
    solidity_code_lines = solidity_code.strip().split('\n')
    duplicates = {}
    for line in solidity_code_lines:
        if line.strip() in duplicates:
            duplicates[line.strip()] += 1
        else:
            duplicates[line.strip()] = 1
    duplicates = {key: val for key, val in duplicates.items() if val > 1}
    return len(duplicates)

def extract_events(solidity_code):
    events = len(re.findall(r'event\s+(\w+)', solidity_code))
    return events

def extract_functional_features(solidity_code):
    num_functions = len(re.findall(r'function\s+\w+', solidity_code))
    num_public_functions = len(re.findall(r'function\s+\w+\s*\(.*\)\s*public', solidity_code))
    num_if_statements = len(re.findall(r'\bif\b', solidity_code))
    num_loops = len(re.findall(r'\bfor\b|\bwhile\b', solidity_code))
    num_external_calls = len(re.findall(r'\.call\(|\.callcode\(|\.delegatecall\(', solidity_code))
    return num_functions, num_public_functions, num_if_statements, num_loops, num_external_calls
def flatten_series_to_dict(series):
    return series.to_dict() if isinstance(series, pd.Series) else series

def flatten_analysis_result(result):
    flattened_result = {}
    for key, value in result.items():
        if isinstance(value, dict):
            flattened_result.update({f"{key}_{k}": v for k, v in value.items()})
        elif isinstance(value, tuple):
            for i, val in enumerate(value):
                flattened_result[f"{key}_{i}"] = val
        elif isinstance(value, pd.Series):
            flattened_result.update({f"{key}_{k}": v for k, v in flatten_series_to_dict(value).items()})
        else:
            flattened_result[key] = value
    return flattened_result

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
