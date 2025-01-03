![](https://github.com/ahlashkari/SCsVulLyzer/blob/main/bccc.jpg)

# Smart Contracts Vulnerabilities Analyzer (SCsVulLyzer V2.0)

As a featured installment of the Understanding Cybersecurity Series (UCS), SCsVulLyzer V2 is an advanced Python open-source project designed to enhance the profiling of Smart Contracts (SCs) for improved vulnerability detection. This release builds upon the foundations of its predecessor by introducing refined methodologies for feature extraction and analysis.

SCsVulLyzer operates as a comprehensive tool tailored for Ethereum smart contracts coded in Solidity. This version, also known as BCCC-SCsVulLyzer, distinguishes itself by categorizing features into two primary types: compiler-based and non-compiler-based. Such classification expands the scope of feature extraction and leverages a variety of functions to deeply analyze the contract's source code. This analysis includes compiling the code to extract bytecode, opcodes, the Abstract Syntax Tree (AST), the Application Binary Interface (ABI), along with detailed contract and Solidity-specific information.

A notable enhancement in this version is the introduction of 'bytecode entropy'—a measure of the randomness within the bytecode, which serves as an indicator of unpredictability and complexity. This metric is particularly valuable in fields like cryptography and anomaly detection. The entropy is calculated using Shannon's formula:

$$
H(X) = -\sum_{i=1}^n p(x_i) \log_2 p(x_i)
$$

Where <em>X</em> represents the set of bytes, <em>p(x<sub>i</sub>)</em> the probability of each byte occurring, calculated as the frequency of <em>x<sub>i</sub></em> divided by the total number of bytes. For a byte array <strong>d</strong> of length <em>N</em>, the entropy <em>H(d)</em> is:

$$
H(\mathbf{d}) = -\sum_{x \in \mathbf{d}} \left( \frac{\text{count}(x)}{N} \right) \log_2 \left( \frac{\text{count}(x)}{N} \right) 
$$

Features are further categorized based on their evaluation timing—pre or post-compilation. Compiler-based features include those processed post-compilation, like ABI and AST, whereas non-compiler-based features derive from existing NLP methodologies adapted to smart contracts, focusing on critical keywords. This version also introduces three innovative feature categories: Contract Information, Source Code Information, and Solidity Information. These categories are designed to quantify various elements of the code, such as function counts, statements, loops, and lines, enhancing the granularity of our analysis. 

# Table of Contents

- [Installation](#installation)
- [Extracted Features](#extracted-features)
  * [Definitions](#definitions)
  * [Statistical Information Calculation](#statistical-information-calculation)
- [Output](#output)
- [Copyright (c) 2023](#copyright-c-2023)
- [Contributing](#contributing)
- [Project Team Members](#project-team-members)
- [Acknowledgment](#acknowledgment)

# Installation

You must install the requirements in your system before you can begin installing or running anything. To do so, you can easily run this command:

```bash 
sudo pip3 install -r requirements.txt
```

You are now ready to execute SCsVulLyzer, run this command:

```bash
python main.py Path_to_the_Solidity_source_code_file_to_analyze.sol
```
Also, this project has been successfully tested on Windows10, Ubuntu 22.04.

# Extracted Features Categories and Description
SCsVulLyzer V2.0 extracts 193 unique features, categorized and described as follows. Please note that some features, such as the number of instructions in opcode and bytecode, are generally referred to as the number of instructions or characters in the table.
  
| Category             | Features name                       | Description                                                                              | Category                | Features name              | Description                                                                    |
|----------------------|-------------------------------------|------------------------------------------------------------------------------------------|-------------------------|----------------------------|--------------------------------------------------------------------------------|
| Bytecode             | Entropy                             | Measure of randomness or complexity in the program's compiled bytecode.                  | Contract Information    | Base Contract Information  | Details of a parent or primary contract from which a SC inherits features.     |
| Bytecode             | Number of Characters                | Count of unique character symbols in the program's compiled bytecode.                    | Source Code Information | Number of Events           | Count of distinct occurrences or actions within a system or application.       |
| Opcode               | Number of Instructions              | Total count of operational code (opcode) instructions, representing the execution steps. | Source Code Information | Number of Functions        | Count of distinct operations or procedures in a specific context.              |
| AST                  | Length of exportedSymbols           | Size or complexity measure of the exported symbols in the AST.                           | Source Code Information | Number of Public Functions | Count of externally accessible functions in a module or contract.              |
| AST                  | Source ID                           | Unique identifier for specific source code elements within the AST.                      | Source Code Information | Number of Loop Statements  | Count of repetitive control structures (e.g., "while", "for") in a code block. |
| AST                  | NodeType                            | Category or class of a node, indicating the syntax construct it represents.              | Source Code Information | Number of If Statements    | Count of conditional statements for decision-making in a code block.           |
| AST                  | Number of Children                  | Count of immediate descendant nodes within the AST structure.                            | Source Code Information | Number of External Calls   | Count of calls to external contracts or services in blockchain development.    |
| ABI                  | Length of Constant                  | Fixed size of a constant value in the ABI data representation.                           | Source Code Information | Total Code Lines           | Total lines of code, including comments and whitespace.                        |
| ABI                  | Length of Name                      | Number of characters or bytes for an identifier or name in the ABI.                      | Source Code Information | Comment Lines              | Lines containing comments or explanations in a codebase.                       |
| ABI                  | Length of Payable                   | Specifies if a function can receive Ether transactions (not a length measure).           | Source Code Information | Blank Lines                | Empty lines without code or comments in a codebase.                            |
| ABI                  | Length of StateMutability           | Number of characters describing the mutability type of a contract's state.               | Source Code Information | Duplicate Lines            | Identical lines of code appearing more than once in a codebase.                |
| ABI                  | Length of Type                      | Number of characters or bytes specifying an ABI element's type.                          | Solidity Information    | "delegatecall" Count       | Occurrences of the "delegatecall" instruction in SC code.                      |
| ABI                  | Length of Input                     | Number of parameters or size of data for a function or method call.                      | Solidity Information    | "callcode" Count           | Occurrences of the "callcode" instruction in SC code.                          |
| ABI                  | Length of Zero Values in Input      | Count or size of parameters set to zero in a function or method call.                    | Solidity Information    | "call" Count               | Occurrences of the "call" instruction in SC code.                              |
| ABI                  | Length of Non-Zero Values in Input  | Count or size of non-zero value parameters in a function or method call.                 | Solidity Information    | "send" Count               | Uses of the "send" function to transfer funds in SC code.                      |
| ABI                  | Length of Output                    | Number of return values or data size returned by a function or method.                   | Solidity Information    | "transfer" Count           | Uses of the "transfer" function to transfer funds in SC code.                  |
| ABI                  | Length of Zero Values in Output     | Count or size of return values set to zero by a function or method.                      | Solidity Information    | "selfdestruct" Count       | Occurrences of "selfdestruct" to remove contracts from the blockchain.         |
| ABI                  | Length of Non-Zero Values in Output | Count or size of non-zero value return values by a function or method.                   | Solidity Information    | "create" Count             | Uses of "create" to deploy new contract instances on the blockchain.           |
| Contract Information | Contract Name                       | Identifier or title for a specific SC in a blockchain network.                           | Solidity Information    | "create2" Count            | Uses of "create2" to deploy new contract instances on the blockchain.          |


# Output
Here is the output from analyzing one source code with SCsVulLyzer V2.0, returned as a dictionary:

{'length of contract_name': 10, 'length of base_contract': 0, 'Number of total_lines': 376, 'Number of code_lines': 230, 'Number of comment_lines': 0, 'Number of blank_lines': 146, 'Solidity Features_0': 0, 'Solidity delegatecall': 0, 'Solidity callcode': 0, 'Solidity call': 0, 'Solidity send': 6, 'Solidity transfer': 0, 'Solidity selfdestruct': 0, 'Solidity create': 0, 'Duplicate Lines Count': 8, 'Event Count': 4, 'Functional Features_0': 22, 'Functional Features_1': 8, 'Functional_Number of "public"': 3, 'Functional_Number of "if"': 0, 'Functional_Number of "while"': 0, 'AST Features_ast_len_exportedSymbols': 3, 'AST Features_ast_id': 908, 'AST Features_ast_nodetype': 'SourceUnit', 'AST Features_ast_src': '0:9177:0', 'AST Features_ast_len_nodes': 4, 'ABI Features_len_list_constant': 26, 'ABI Features_len_list_name': 30, 'ABI Features_len_list_payable': 28, 'ABI Features_len_list_stateMut': 28, 'ABI Features_len_list_type': 32, 'ABI Features_len_non_zero_input': 21, 'ABI Features_len_list_input': 29, 'ABI Features_len_zero_input': 8, 'ABI Features_len_non_zero_output': 16, 'ABI Features_len_list_output': 21, 'ABI Features_len_zero_output': 5, 'Opcode Count Features_STOP': 17, 'Opcode Count Features_ADD': 237, 'Opcode Count Features_MUL': 58, 'Opcode Count Features_SUB': 73, 'Opcode Count Features_DIV': 48, 'Opcode Count Features_SDIV': 0, 'Opcode Count Features_MOD': 1, 'Opcode Count Features_SMOD': 0, 'Opcode Count Features_ADDMOD': 0, 'Opcode Count Features_MULMOD': 0, 'Opcode Count Features_EXP': 55, 'Opcode Count Features_SIGNEXTEND': 0, 'Opcode Count Features_LT': 38, 'Opcode Count Features_GT': 15, 'Opcode Count Features_SLT': 0, 'Opcode Count Features_SGT': 0, 'Opcode Count Features_EQ': 52, 'Opcode Count Features_ISZERO': 240, 'Opcode Count Features_AND': 188, 'Opcode Count Features_OR': 13, 'Opcode Count Features_XOR': 0, 'Opcode Count Features_NOT': 16, 'Opcode Count Features_BYTE': 0, 'Opcode Count Features_SHL': 0, 'Opcode Count Features_SHR': 0, 'Opcode Count Features_SAR': 0, 'Opcode Count Features_SHA3': 0, 'Opcode Count Features_ADDRESS': 3, 'Opcode Count Features_BALANCE': 0, 'Opcode Count Features_ORIGIN': 0, 'Opcode Count Features_CALLER': 19, 'Opcode Count Features_CALLVALUE': 32, 'Opcode Count Features_CALLDATALOAD': 23, 'Opcode Count Features_CALLDATASIZE': 20, 'Opcode Count Features_CALLDATACOPY': 0, 'Opcode Count Features_CODESIZE': 0, 'Opcode Count Features_CODECOPY': 5, 'Opcode Count Features_GASPRICE': 0, 'Opcode Count Features_EXTCODESIZE': 16, 'Opcode Count Features_EXTCODECOPY': 0, 'Opcode Count Features_RETURNDATASIZE': 52, 'Opcode Count Features_RETURNDATACOPY': 18, 'Opcode Count Features_BLOCKHASH': 0, 'Opcode Count Features_COINBASE': 0, 'Opcode Count Features_TIMESTAMP': 1, 'Opcode Count Features_NUMBER': 0, 'Opcode Count Features_DIFFICULTY': 2, 'Opcode Count Features_GASLIMIT': 0, 'Opcode Count Features_POP': 438, 'Opcode Count Features_MLOAD': 138, 'Opcode Count Features_MSTORE': 120, 'Opcode Count Features_MSTORE8': 0, 'Opcode Count Features_SLOAD': 102, 'Opcode Count Features_SSTORE': 39, 'Opcode Count Features_JUMP': 100, 'Opcode Count Features_JUMPI': 177, 'Opcode Count Features_PC': 0, 'Opcode Count Features_MSIZE': 0, 'Opcode Count Features_GAS': 16, 'Opcode Count Features_JUMPDEST': 276, 'Opcode Count Features_PUSH1': 791, 'Opcode Count Features_PUSH2': 374, 'Opcode Count Features_PUSH3': 14, 'Opcode Count Features_PUSH4': 66, 'Opcode Count Features_PUSH5': 1, 'Opcode Count Features_PUSH6': 2, 'Opcode Count Features_PUSH7': 1, 'Opcode Count Features_PUSH8': 0, 'Opcode Count Features_PUSH9': 0, 'Opcode Count Features_PUSH10': 0, 'Opcode Count Features_PUSH11': 0, 'Opcode Count Features_PUSH12': 0, 'Opcode Count Features_PUSH13': 0, 'Opcode Count Features_PUSH14': 0, 'Opcode Count Features_PUSH15': 0, 'Opcode Count Features_PUSH16': 0, 'Opcode Count Features_PUSH17': 0, 'Opcode Count Features_PUSH18': 0, 'Opcode Count Features_PUSH19': 0, 'Opcode Count Features_PUSH20': 154, 'Opcode Count Features_PUSH21': 0, 'Opcode Count Features_PUSH22': 0, 'Opcode Count Features_PUSH23': 0, 'Opcode Count Features_PUSH24': 2, 'Opcode Count Features_PUSH25': 0, 'Opcode Count Features_PUSH26': 0, 'Opcode Count Features_PUSH27': 0, 'Opcode Count Features_PUSH28': 0, 'Opcode Count Features_PUSH29': 18, 'Opcode Count Features_PUSH30': 0, 'Opcode Count Features_PUSH31': 0, 'Opcode Count Features_PUSH32': 4, 'Opcode Count Features_DUP1': 471, 'Opcode Count Features_DUP2': 297, 'Opcode Count Features_DUP3': 85, 'Opcode Count Features_DUP4': 64, 'Opcode Count Features_DUP5': 11, 'Opcode Count Features_DUP6': 7, 'Opcode Count Features_DUP7': 3, 'Opcode Count Features_DUP8': 19, 'Opcode Count Features_DUP9': 5, 'Opcode Count Features_DUP10': 0, 'Opcode Count Features_DUP11': 0, 'Opcode Count Features_DUP12': 0, 'Opcode Count Features_DUP13': 0, 'Opcode Count Features_DUP14': 0, 'Opcode Count Features_DUP15': 0, 'Opcode Count Features_DUP16': 0, 'Opcode Count Features_SWAP1': 447, 'Opcode Count Features_SWAP2': 129, 'Opcode Count Features_SWAP3': 60, 'Opcode Count Features_SWAP4': 3, 'Opcode Count Features_SWAP5': 0, 'Opcode Count Features_SWAP6': 0, 'Opcode Count Features_SWAP7': 1, 'Opcode Count Features_SWAP8': 0, 'Opcode Count Features_SWAP9': 0, 'Opcode Count Features_SWAP10': 0, 'Opcode Count Features_SWAP11': 0, 'Opcode Count Features_SWAP12': 0, 'Opcode Count Features_SWAP13': 0, 'Opcode Count Features_SWAP14': 0, 'Opcode Count Features_SWAP15': 0, 'Opcode Count Features_SWAP16': 0, 'Opcode Count Features_LOG0': 0, 'Opcode Count Features_LOG1': 2, 'Opcode Count Features_LOG2': 4, 'Opcode Count Features_LOG3': 0, 'Opcode Count Features_LOG4': 0, 'Opcode Count Features_CREATE': 1, 'Opcode Count Features_CALL': 17, 'Opcode Count Features_CALLCODE': 0, 'Opcode Count Features_RETURN': 22, 'Opcode Count Features_DELEGATECALL': 0, 'Opcode Count Features_STATICCALL': 0, 'Opcode Count Features_REVERT': 111, 'Opcode Count Features_INVALID': 28, 'Opcode Count Features_SELFDESTRUCT': 0, 'Bytecode Length and Entropy_bytecode_len': 23076.0, 'Bytecode Length and Entropy_bytecode_entropy': 4.836557728439604, 'Bytecode Character Count_bytecode_character_6': 1678, 'Bytecode Character Count_bytecode_character_0': 5414, 'Bytecode Character Count_bytecode_character_8': 1104, 'Bytecode Character Count_bytecode_character_4': 526, 'Bytecode Character Count_bytecode_character_5': 1846, 'Bytecode Character Count_bytecode_character_2': 669, 'Bytecode Character Count_bytecode_character_9': 758, 'Bytecode Character Count_bytecode_character_3': 703, 'Bytecode Character Count_bytecode_character_1': 2070, 'Bytecode Character Count_bytecode_character_7': 537, 'Bytecode Character Count_bytecode_character_f': 6609, 'Bytecode Character Count_bytecode_character_d': 291, 'Bytecode Character Count_bytecode_character_b': 395, 'Bytecode Character Count_bytecode_character_a': 207, 'Bytecode Character Count_bytecode_character_e': 132, 'Bytecode Character Count_bytecode_character_c': 137}


Here are the first 10 rows of the CSV file after applying SCsVulLyzer V2.0 to the dataset:


# Copyright (c) 2024

For citation in your works and also understanding SCsVulLyzer-V2.0 completely, you can find below-published papers:

[Sepideh Hajihosseinkhani, Arash Habibi Lashkari, Ali Mizani, “Unveiling Smart Contracts Vulnerabilities: Toward Profiling Smart Contracts Vulnerabilities using Enhanced Genetic Algorithm and Generating Benchmark Dataset”, Blockchain: Research and Applications, December 2024, 100253](https://www.sciencedirect.com/science/article/pii/S2096720924000666)

For citation in your works and also understanding SCsVulLyzer-V1.0 completely, you can find below-published papers:

[Sepideh Hajihosseinkhani, Arash Habibi Lashkari, Ali Mizani, “Unveiling Vulnerable Smart Contracts: Toward Profiling Vulnerable Smart Contracts using Genetic Algorithm and Generating Benchmark Dataset”, Blockchain: Research and Applications, Vol. 4, December 2023](https://www.sciencedirect.com/science/article/pii/S2096720923000465?via%3Dihub)


### Project Team members 

* [**Arash Habibi Lashkari:**](http://ahlashkari.com/index.asp) Founder and Project Owner 

* [**Sepideh HajHosseinkhani:**](https://github.com/Sepid-99) Researcher and Developer 

### Acknowledgement 
This project has been made possible through funding from the Natural Sciences and Engineering Research Council of Canada — NSERC (#RGPIN-2020-04701) and Canada Research Chair (Tier II) - (#CRC-2021-00340) to Arash Habibi Lashkari.
