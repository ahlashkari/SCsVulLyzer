from collections import Counter
import scipy.stats as ss
import solcx
import re

def compile_solidity_source(source_code, version="0.4.24"):
    """Compile Solidity source code to bytecode, AST, and opcodes."""
    solcx.install_solc(version=version)
    solcx.set_solc_version(version)
    compiled_sol = solcx.compile_source(source_code, output_values=["ast", "bin", "opcodes"])
    contract_id, contract_interface = compiled_sol.popitem()
    return {
        'bytecode': contract_interface['bin'],
        'ast': contract_interface['ast'],
        'opcodes': contract_interface['opcodes']
    }

def calculate_bytecode_entropy(bytecode):
    """Calculate the entropy of the bytecode."""
    counter = Counter(bytecode)
    probabilities = [count / len(bytecode) for count in counter.values()]
    return ss.entropy(probabilities, base=2)

def process_bytecode(source_code):
    """Process bytecode to extract statistics and entropy."""
    compiled = compile_solidity_source(source_code)
    bytecode = compiled['bytecode']
    
    bytecode_dic = {
        'bytecode_len': len(bytecode),
        'bytecode_entropy': calculate_bytecode_entropy(bytecode)
    }
    
    char_count = Counter(bytecode)
    total_chars = len(bytecode)
    
    bytecode_chars = [
        '6', '0', '8', '4', '5', '2', '1', 'a', '7', '3', 'f', '9', 'b', 'c', 'd', 'e', '_', '<', 's', 't', 'i', 'n', '>',
        ':', 'S', 'l', 'L', 'M', 'h', 'E', 'C', 'R', 'o', 'v', 'r', 'y', 'O', 'z', 'B', 'T', 'D', 'A', 'u', 'k', 'P', 'g',
        'I', 'm', 'x'
    ]
    
    for char in bytecode_chars:
        bytecode_dic[f'Weight_bytecode_character_{char}'] = char_count.get(char, 0) / total_chars
        bytecode_dic[f'bytecode_character_{char}'] = char_count.get(char, 0)
    
    return bytecode_dic

def process_ast(source_code):
    """Process the AST of the Solidity source code."""
    compiled = compile_solidity_source(source_code)
    ast = compiled['ast']
    
    return {
        'ast_len_exportedSymbols': len(ast.get('attributes', [])),
        'ast_id': ast.get('id', ''),
        'ast_nodetype': ast.get('name', ''),
        'ast_src': ast.get('src', ''),
        'ast_len_nodes': len(ast.get('children', []))
    }

def process_opcodes(source_code):
    """Process opcodes to extract frequency statistics."""
    compiled = compile_solidity_source(source_code)
    opcodes = compiled['opcodes'].split(' ')
    
    opcode_list = [
        'STOP', 'ADD', 'MUL', 'SUB', 'DIV', 'SDIV', 'MOD', 'SMOD', 'ADDMOD', 'MULMOD', 'EXP', 'SIGNEXTEND',
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
        'STATICCALL', 'REVERT', 'INVALID', 'SELFDESTRUCT'
    ]
    
    opcode_count = Counter(opcodes)
    opcode_frequency_dic = {
        f"Opcode_weight_{opcode}": opcode_count.get(opcode, 0) / sum(opcode_count.values()) if sum(opcode_count.values()) > 0 else 0
        for opcode in opcode_list
    }
    
    return opcode_frequency_dic

def count_keywords_in_code(source_code):
    """Count occurrences of specific keywords in the source code."""
    keywords_list = [
        'from', 'require', 'dev', 'internal', 'string', 'view', 'mapping', 'sub', 'emit', 'length', 'pure',
        'will', 'not', 'approve', 'external', 'memory', 'eth', 'else', 'can', 'calls', 'data', 'q'
    ]
    
    patterns = {keyword: re.compile(r'\b' + re.escape(keyword) + r'\b', re.IGNORECASE) for keyword in keywords_list}
    keyword_counts = {keyword: len(pattern.findall(source_code)) for keyword, pattern in patterns.items()}
    
    return keyword_counts
