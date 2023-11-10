# Smart Contracts Volnerability Analyzer (SCsVolLyzer)


As part of the Understanding Cybersecurity Series (UCS), SCsVolLyzer is a Python open-source project to extract features to profile Smart Contracts (SCs) for vulnerability detection.   

The SCsVolLyzer is a Python-based tool designed to analyze and extract key metrics from Ethereum smart contracts written in Solidity. It employs a suite of functions to dissect the contract's source code, compiling it to obtain its abstract syntax tree (AST), bytecode, and opcodes. The analyzer calculates entropy of the bytecode to assess its randomness and security, determines the frequency of certain opcodes to understand the contract's complexity, and evaluates the usage of key Solidity keywords to gauge coding patterns. This modular and extensible tool provides a comprehensive snapshot of a smart contract's structure and behavior, facilitating developers and auditors in optimizing and securing Ethereum blockchain applications.


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

You are now ready to install SCsVolLyzer. In order to do so, you should run this command, which will install the SCsVolLyzer package in your system:

```bash
sudo python3 setup.py install
```

Finally, to execute the program, run this command:

```bash
python main.py path_to_solidity_source_file.sol
```
Also, this project has been successfully tested on Windows10, OS X. 


# Extracted Features
                
We have currenlty 70 features that are as follows:

1. 'Bytecode_entropy'
1. 'AST_source_id'
1. 'AST_numberOf_exportedSymbols'
1. 'AST_numberOf_nodes'
1. 'weight_Bytecode_numberOf_character_0'
1. 'weight_Bytecode_numberOf_character_1'
1. 'weight_Bytecode_numberOf_character_2'
1. 'weight_Bytecode_numberOf_character_3'
...


## Definitions


## Statistical Information Calculation

We use differnet libraries to calculate various mathematical equations. Below you can see the libraries and their brief definition based on their documentations:

+ [**statistics**](https://docs.python.org/3/library/statistics.html)

     This module provides functions for calculating mathematical statistics of numeric (Real-valued) data.

     The module is not intended to be a competitor to third-party libraries such as NumPy, SciPy, or proprietary full-featured statistics packages aimed at professional statisticians such as Minitab, SAS and Matlab. It is aimed at the level of graphing and scientific calculators.


Only one mathematical functions is used to extract different features. You can see how those functions are calculated in the NLFlowLyzer below:

1. entropy??? I create the function!


     
     

# Output

| Bytecode_entropy | AST_source_id | weight_Bytecode_numberOf_character_0 | weight_Bytecode_numberOf_character_f | weight_Bytecode_numberOf_character_5 | weight_Bytecode_numberOf_character_6 | weight_Bytecode_numberOf_character_1 | weight_Bytecode_numberOf_character_2 | weight_Bytecode_numberOf_character_8 | weight_Bytecode_numberOf_character_9 | weight_Bytecode_numberOf_character_4 | weight_sums_DUP | weight_Bytecode_numberOf_character_3 | weight_Bytecode_numberOf_character_7 | weight_sums_PUSH | weight_sums_SWAP | weight_Bytecode_numberOf_character_a | weight_Bytecode_numberOf_character_b | weight_Bytecode_numberOf_character_d | weight_Bytecode_numberOf_character_e | weight_Bytecode_numberOf_character_c | weight_sums_CALL | weight_sums_ADD | weight_sums_POP | weight_sums_JUMP | weight_sums_AND | weight_sums_OR | weight_sums_MSTORE | weight_sums_ISZERO | weight_sums_JUMPDEST | weight_sums_JUMPI | weight_sums_SLOAD | weight_sums_RETURN | weight_sums_REVERT | weight_sums_SUB | weight_sums_MLOAD | weight_sums_DIV | weight_sums_EXP | weight_sums_MUL | weight_sums_EQ | AST_numberOf_exportedSymbols | AST_numberOf_nodes | weight_Bytecode_numberOf_character_2 | weight_Bytecode_numberOf_character_c | weight_sums_MUL | weight_sums_DIV | weight_sums_EXP | weight_sums_AND | weight_sums_OR | weight_sums_NOT | weight_sums_BYTE | weight_sums_ADDRESS | weight_sums_MSTORE | weight_sums_MSTORE8 | weight_sums_SLOAD | weight_sums_SSTORE | weight_sums_JUMPI | weight_sums_INVALID | from | require | dev | internal | string | view | mapping | sub | emit | length | pure | will | not | approve | external | memory | eth | else | can | calls | data | q |

| :----------------: | :-----------: | :------------------------------: | :--------------------------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: |
----


# Copyright (c) 2023

SCsVolLyzer V1.0: For citation in your works and also understanding SCsVolLyzer-V1.0 completely, you can find below published papers:

Sepideh Hajihosseinkhani, Arash Habibi Lashkari, Ali Mizani, “Unveiling Vulnerable Smart Contracts: Toward Profiling Vulnerable Smart Contracts using Genetic Algorithm and Generating Benchmark Dataset”, Blockchain: Research and Applications, Vol. , Page: , December 2023


### Project Team members 

* [**Arash Habibi Lashkari:**](http://ahlashkari.com/index.asp) Founder and Project Owner 

* [**Sepideh HajHosseinkhani:**](https://github.com/Sepid-99) Researcher and Developer 

### Acknowledgement 
This project has been made possible through funding from the Natural Sciences and Engineering Research Council of Canada — NSERC (#RGPIN-2020-04701) and Canada Research Chair (Tier II) - (#CRC-2021-00340) to Arash Habibi Lashkari.
