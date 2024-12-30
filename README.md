![](https://github.com/ahlashkari/SCsVulLyzer/blob/main/bccc.jpg)

# Smart Contracts Vulnerability Analyzer (SCsVulLyzer-V1.0)


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

You are now ready to execute SCsVolLyzer, run this command:

```bash
python main.py path_to_solidity_source_file.sol
```
Also, this project has been successfully tested on Windows10, OS X. 


# Extracted Features
                
We have currenlty 70 features that are as follows:

| **Features name**                    | **Description**                                                                                                                                                                                          | **Features name**            | **Description**                                        |
|--------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------|--------------------------------------------------------|
| Bytecode_entropy                     | Counts the occurrences of each unique element calculates the probabilities of each element occurring and then computes the entropy of the sequence based on these probabilities using a base-2 logarithm | weight_sums_DIV              | Weight of DIV opcode instruction appears in the opcode |
| AST_source_id                        | Unique identifier for the source code                                                                                                                                                                    | weight_sums_EXP              | Weight of EXP opcode instruction appears in the opcode |
| weight_Bytecode_numberOf_character_0 | Weight of character 0 in the bytecode                                                                                                                                                                    | weight_sums_MUL              | Weight of MUL opcode instruction appears in the opcode |
| weight_Bytecode_numberOf_character_f | Weight of character f in the bytecode                                                                                                                                                                    | weight_sums_EQ               | Weight of EQ opcode instruction appears in the opcode  |
| weight_Bytecode_numberOf_character_5 | Weight of character 5 in the bytecode                                                                                                                                                                    | AST_numberOf_exportedSymbols | Number of exportedSymbols in abstract syntax tree      |
| weight_Bytecode_numberOf_character_6 | Weight of character 6 in the bytecode                                                                                                                                                                    | AST_numberOf_nodes           | Number of nodes/child in abstract syntax tree          |
| weight_Bytecode_numberOf_character_1 | Weight of character 1 in the bytecode                                                                                                                                                                    | weight_sums_NOT              | Weight of EXP opcode instruction appears in the opcode |
| weight_Bytecode_numberOf_character_2 | Weight of character 2 in the bytecode                                                                                                                                                                    | weight_sums_BYTE             | Weight of EXP opcode instruction appears in the opcode |
| weight_Bytecode_numberOf_character_8 | Weight of character 8 in the bytecode                                                                                                                                                                    | weight_sums_ADDRESS          | Weight of EXP opcode instruction appears in the opcode |
| weight_Bytecode_numberOf_character_9 | Weight of character 9 in the bytecode                                                                                                                                                                    | weight_sums_MSTORE8          | Weight of EXP opcode instruction appears in the opcode |
| weight_Bytecode_numberOf_character_4 | Weight of character 4 in the bytecode                                                                                                                                                                    | weight_sums_SSTORE           | Weight of EXP opcode instruction appears in the opcode |
| weight_sums_DUP                      | Weight of DUP opcode instruction appears in the opcode                                                                                                                                                   | weight_sums_INVALID          | Weight of EXP opcode instruction appears in the opcode |
| weight_Bytecode_numberOf_character_3 | Weight of character 3 in the bytecode                                                                                                                                                                    | from                         | Number of from repeated in the source code.            |
| weight_Bytecode_numberOf_character_7 | Weight of character 7 in the bytecode                                                                                                                                                                    | require                      | Number of require repeated in the source code.         |
| weight_sums_PUSH                     | Weight of PUSH opcode instruction appears in the opcode                                                                                                                                                  | dev                          | Number of dev repeated in the source code.             |
| weight_sums_SWAP                     | Weight of SWAP opcode instruction appears in the opcode                                                                                                                                                  | internal                     | Number of internal repeated in the source code.        |
| weight_Bytecode_numberOf_character_a | Weight of character a in the bytecode                                                                                                                                                                    | string                       | Number of string repeated in the source code.          |
| weight_Bytecode_numberOf_character_b | Weight of character b in the bytecode                                                                                                                                                                    | view                         | Number of view repeated in the source code.            |
| weight_Bytecode_numberOf_character_d | Weight of character d in the bytecode                                                                                                                                                                    | mapping                      | Number of mapping repeated in the source code.         |
| weight_Bytecode_numberOf_character_e | Weight of character e in the bytecode                                                                                                                                                                    | sub                          | Number of sub repeated in the source code.             |
| weight_Bytecode_numberOf_character_c | Weight of character c in the bytecode                                                                                                                                                                    | emit                         | Number of emit repeated in the source code.            |
| weight_sums_CALL                     | Weight of CALL opcode instruction appears in the opcode                                                                                                                                                  | length                       | Number of length repeated in the source code.          |
| weight_sums_ADD                      | Weight of ADD opcode instruction appears in the opcode                                                                                                                                                   | pure                         | Number of pure repeated in the source code.            |
| weight_sums_POP                      | Weight of POP opcode instruction appears in the opcode                                                                                                                                                   | will                         | Number of will repeated in the source code.            |
| weight_sums_JUMP                     | Weight of JUMP opcode instruction appears in the opcode                                                                                                                                                  | not                          | Number of not repeated in the source code.             |
| weight_sums_AND                      | Weight of AND opcode instruction appears in the opcode                                                                                                                                                   | approve                      | Number of approve repeated in the source code.         |
| weight_sums_OR                       | Weight of OR opcode instruction appears in the opcode                                                                                                                                                    | external                     | Number of external repeated in the source code.        |
| weight_sums_MSTORE                   | Weight of MSTORE opcode instruction appears in the opcode                                                                                                                                                | memory                       | Number of memory repeated in the source code.          |
| weight_sums_ISZERO                   | Weight of ISZERO opcode instruction appears in the opcode                                                                                                                                                | eth                          | Number of eth repeated in the source code.             |
| weight_sums_JUMPDEST                 | Weight of JUMPDEST opcode instruction appears in the opcode                                                                                                                                              | else                         | Number of else repeated in the source code.            |
| weight_sums_JUMPI                    | Weight of JUMPI opcode instruction appears in the opcode                                                                                                                                                 | can                          | Number of can repeated in the source code.             |
| weight_sums_SLOAD                    | Weight of SLOAD opcode instruction appears in the opcode                                                                                                                                                 | calls                        | Number of calls repeated in the source code.           |
| weight_sums_RETURN                   | Weight of RETURN opcode instruction appears in the opcode                                                                                                                                                | data                         | Number of data repeated in the source code.            |
| weight_sums_REVERT                   | Weight of REVERT opcode instruction appears in the opcode                                                                                                                                                | q                            | Number of q repeated in the source code.               |
| weight_sums_SUB                      | Weight of SUB opcode instruction appears in the opcode                                                                                                                                                   | hash_id                      | Unique ID for each source code                         |
| weight_sums_MLOAD                    | Weight of MLOAD opcode instruction appears in the opcode                                                                                                                                                 | label                        | label 0 --> secure / label 1 --> vulnerable            |

## Statistical Information Calculation

Only one mathematical functions is used to extract different features. You can see how those functions are calculated in the NLFlowLyzer below:

1. **calculate_bytecode_entropy()**
The function calculate_bytecode_entropy computes the entropy of a given bytecode sequence using Shannon's entropy formula. It first constructs a frequency distribution by counting the occurrences of each unique bytecode element, representing them as probabilities by dividing the count of each element by the total length of the sequence. These probabilities are then used as the probabilities of occurrence in the entropy calculation. Shannon's entropy, denoted as H(X), is defined as the sum of the negative of the product of each probability (p(x)) and its base-2 logarithm (-log2(p(x))), summed over all unique elements in the sequence. This formula, H(X) = -Σ(p(x) * log2(p(x))), quantifies the amount of uncertainty or information content in the bytecode sequence, where higher values imply greater randomness and lower values indicate more predictability in the sequence. ([https://www.analyticsvidhya.com/blog/2020/11/entropy-a-key-concept-for-all-data-science-beginners/#:~:text=Entropy%20measures%20the%20amount%20of,higher%20uncertainty%20have%20higher%20entropy.]) 

     

# Output

|   | Bytecode_entropy | AST_source_id | weight_Bytecode_numberOf_character_0 | weight_Bytecode_numberOf_character_f | weight_Bytecode_numberOf_character_5 | weight_Bytecode_numberOf_character_6 | weight_Bytecode_numberOf_character_1 | weight_Bytecode_numberOf_character_2 | weight_Bytecode_numberOf_character_8 | weight_Bytecode_numberOf_character_9 | weight_Bytecode_numberOf_character_4 | weight_sums_DUP | weight_Bytecode_numberOf_character_3 | weight_Bytecode_numberOf_character_7 | weight_sums_PUSH | weight_sums_SWAP | weight_Bytecode_numberOf_character_a | weight_Bytecode_numberOf_character_b | weight_Bytecode_numberOf_character_d | weight_Bytecode_numberOf_character_e | weight_Bytecode_numberOf_character_c | weight_sums_CALL | weight_sums_ADD | weight_sums_POP | weight_sums_JUMP | weight_sums_AND | weight_sums_OR | weight_sums_MSTORE | weight_sums_ISZERO | weight_sums_JUMPDEST | weight_sums_JUMPI | weight_sums_SLOAD | weight_sums_RETURN | weight_sums_REVERT | weight_sums_SUB | weight_sums_MLOAD | weight_sums_DIV | weight_sums_EXP | weight_sums_MUL | weight_sums_EQ | AST_numberOf_exportedSymbols | AST_numberOf_nodes | weight_Bytecode_numberOf_character_2.1 | weight_Bytecode_numberOf_character_c.1 | weight_sums_MUL.1 | weight_sums_DIV.1 | weight_sums_EXP.1 | weight_sums_AND.1 | weight_sums_OR.1 | weight_sums_NOT | weight_sums_BYTE | weight_sums_ADDRESS | weight_sums_MSTORE.1 | weight_sums_MSTORE8 | weight_sums_SLOAD.1 | weight_sums_SSTORE | weight_sums_JUMPI.1 | weight_sums_INVALID | from | require | dev | internal | string | view | mapping | sub | emit | length | pure | will | not | approve | external | memory | eth | else | can | calls | data | q | hash_id                                                          | label |
|---|------------------|---------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|-----------------|--------------------------------------|--------------------------------------|------------------|------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|------------------|-----------------|-----------------|------------------|-----------------|----------------|--------------------|--------------------|----------------------|-------------------|-------------------|--------------------|--------------------|-----------------|-------------------|-----------------|-----------------|-----------------|----------------|------------------------------|--------------------|----------------------------------------|----------------------------------------|-------------------|-------------------|-------------------|-------------------|------------------|-----------------|------------------|---------------------|----------------------|---------------------|---------------------|--------------------|---------------------|---------------------|------|---------|-----|----------|--------|------|---------|-----|------|--------|------|------|-----|---------|----------|--------|-----|------|-----|-------|------|---|------------------------------------------------------------------|-------|
| 0 | 5.118877         | 10928         | 0.284677                             | 0.186628                             | 0.079963                             | 0.094702                             | 0.101609                             | 0.041014                             | 0.048206                             | 0.042011                             | 0.028411                             | 0.141469        | 0.030333                             | 0.02243                              | 0.221327         | 0.111374         | 0.011108                             | 0.011962                             | 0.005127                             | 0.00648                              | 0.00534                              | 0.015403         | 0.050948        | 0.063033        | 0.056398         | 0.040284        | 0.04218        | 0.026303           | 0.031517           | 0.028199             | 0.015166          | 0.024645          | 0.00545            | 0.004502           | 0.011848        | 0.018009          | 0.012322        | 0.017773        | 0.015877        | 0.005924       | 1                            | 2                  | 0.041014                               | 0.00534                                | 0.015877          | 0.012322          | 0.017773          | 0.040284          | 0.04218          | 0.008057        | 0                | 0.000474            | 0.026303             | 0                   | 0.024645            | 0.009242           | 0.015166            | 0.001659            | 0    | 1       | 0   | 0        | 0      | 1    | 0       | 0   | 1    | 1      | 0    | 0    | 1   | 0       | 0        | 0      | 0   | 1    | 1   | 0     | 0    | 1 | 39fcd43b0f0aaa2cf8f084307d15e259d203843ba89845cb25e7ed2455679ffb | 0     |
| 1 | 4.845067         | 9686          | 0.225825                             | 0.273221                             | 0.080393                             | 0.075148                             | 0.095651                             | 0.048159                             | 0.055789                             | 0.036334                             | 0.02098                              | 0.168398        | 0.030422                             | 0.019073                             | 0.201763         | 0.10639          | 0.006103                             | 0.014591                             | 0.007438                             | 0.004482                             | 0.006389                             | 0.034309         | 0.055398        | 0.065471        | 0.06673          | 0.031791        | 0.041863       | 0.035883           | 0.022033           | 0.032735             | 0.019515          | 0.011646          | 0.00598            | 0.008499           | 0.018256        | 0.019515          | 0.005351        | 0.001889        | 0.005351        | 0.004721       | 2                            | 3                  | 0.048159                               | 0.006389                               | 0.005351          | 0.005351          | 0.001889          | 0.031791          | 0.041863         | 0.001889        | 0                | 0.000315            | 0.035883             | 0                   | 0.011646            | 0.005351           | 0.019515            | 0                   | 1    | 0       | 0   | 0        | 1      | 0    | 1       | 0   | 0    | 0      | 0    | 1    | 1   | 1       | 0        | 0      | 0   | 0    | 0   | 0     | 0    | 0 | 1a7db6c3aef23051792d765423481dc3834b0f0c040e538e6baf45682f7ae255 | 1     |
| 2 | 4.873377         | 10520         | 0.229925                             | 0.263822                             | 0.077666                             | 0.073058                             | 0.098398                             | 0.050241                             | 0.055507                             | 0.03993                              | 0.020075                             | 0.170438        | 0.033458                             | 0.019636                             | 0.195985         | 0.117883         | 0.005924                             | 0.014919                             | 0.006911                             | 0.005265                             | 0.005265                             | 0.033942         | 0.058759        | 0.067518        | 0.063504         | 0.032847        | 0.039416       | 0.033577           | 0.021533           | 0.031022             | 0.017883          | 0.009489          | 0.00438            | 0.005839           | 0.018978        | 0.023358          | 0.006569        | 0.00219         | 0.006204        | 0.004015       | 3                            | 4                  | 0.050241                               | 0.005265                               | 0.006204          | 0.006569          | 0.00219           | 0.032847          | 0.039416         | 0.00219         | 0                | 0.000365            | 0.033577             | 0                   | 0.009489            | 0.005109           | 0.017883            | 0                   | 1    | 1       | 0   | 0        | 1      | 0    | 1       | 0   | 0    | 0      | 0    | 0    | 1   | 1       | 0        | 0      | 1   | 0    | 0   | 1     | 0    | 1 | 4e9baf6ce5fefc2319ca9f0341d2010aba2656a711bb0f0c64cc64f911f3916f | 1     |
| 3 | 4.516593         | 10857         | 0.190564                             | 0.355227                             | 0.06938                              | 0.067993                             | 0.079093                             | 0.037465                             | 0.041628                             | 0.034228                             | 0.019426                             | 0.134752        | 0.037465                             | 0.021277                             | 0.214539         | 0.101064         | 0.007863                             | 0.015264                             | 0.012026                             | 0.004163                             | 0.006938                             | 0.056738         | 0.039007        | 0.058511        | 0.078014         | 0.037234        | 0.035461       | 0.031915           | 0.035461           | 0.039007             | 0.021277          | 0.008865          | 0.007092           | 0.012411           | 0.012411        | 0.014184          | 0.001773        | 0               | 0               | 0.007092       | 6                            | 7                  | 0.037465                               | 0.006938                               | 0                 | 0.001773          | 0                 | 0.037234          | 0.035461         | 0               | 0                | 0                   | 0.031915             | 0                   | 0.008865            | 0.003546           | 0.021277            | 0.003546            | 1    | 1       | 1   | 1        | 1      | 0    | 1       | 1   | 1    | 0      | 1    | 1    | 1   | 1       | 0        | 0      | 1   | 0    | 0   | 0     | 0    | 1 | 9c68294047c47e46f7808778f54e175e7d0f7437c9752ff4d041338bbc3b55eb | 0     |
| 4 | 4.797119         | 16119         | 0.196725                             | 0.317356                             | 0.081086                             | 0.072199                             | 0.09302                              | 0.037398                             | 0.047184                             | 0.0358                               | 0.02177                              | 0.139102        | 0.032754                             | 0.021919                             | 0.208043         | 0.103935         | 0.00694                              | 0.016028                             | 0.008738                             | 0.005343                             | 0.005742                             | 0.037953         | 0.038997        | 0.061978        | 0.077994         | 0.0336          | 0.030815       | 0.022284           | 0.043001           | 0.038997             | 0.022981          | 0.014972          | 0.008705           | 0.012187           | 0.009575        | 0.018454          | 0.005397        | 0.006442        | 0.009227        | 0.008008       | 6                            | 7                  | 0.037398                               | 0.005742                               | 0.009227          | 0.005397          | 0.006442          | 0.0336            | 0.030815         | 0.002437        | 0.000174         | 0.000348            | 0.022284             | 0                   | 0.014972            | 0.005745           | 0.022981            | 0.002786            | 1    | 1       | 0   | 1        | 1      | 0    | 1       | 1   | 0    | 1      | 1    | 0    | 0   | 1       | 1        | 0      | 1   | 0    | 1   | 0     | 1    | 1 | d4a4062767a37041cbe7c4433e06e3dbe0b5e4f89f10352e974a1ec4c8ba3a5f | 0     |
| 5 | 4.716128         | 11343         | 0.213761                             | 0.294013                             | 0.079622                             | 0.07416                              | 0.093172                             | 0.047689                             | 0.053782                             | 0.037815                             | 0.020273                             | 0.163605        | 0.031513                             | 0.017962                             | 0.201386         | 0.109185         | 0.004937                             | 0.015021                             | 0.008088                             | 0.003046                             | 0.005147                             | 0.036395         | 0.055459        | 0.066551        | 0.066205         | 0.032929        | 0.040208       | 0.033969           | 0.02669            | 0.032582             | 0.018371          | 0.012132          | 0.006239           | 0.007972           | 0.017331        | 0.018371          | 0.004853        | 0.002426        | 0.004853        | 0.004853       | 2                            | 3                  | 0.047689                               | 0.005147                               | 0.004853          | 0.004853          | 0.002426          | 0.032929          | 0.040208         | 0.001733        | 0                | 0.000347            | 0.033969             | 0                   | 0.012132            | 0.005546           | 0.018371            | 0.000347            | 1    | 1       | 0   | 1        | 1      | 0    | 1       | 0   | 1    | 0      | 0    | 1    | 1   | 1       | 1        | 0      | 0   | 0    | 1   | 0     | 0    | 1 | 880072718af126b7e38972393ea0cdbfb324c7c27277d6c402c3147ebd81e617 | 0     |
| 6 | 4.52828          | 10205         | 0.190918                             | 0.357275                             | 0.071826                             | 0.063948                             | 0.078313                             | 0.036145                             | 0.044949                             | 0.032901                             | 0.018072                             | 0.141844        | 0.036145                             | 0.023633                             | 0.203901         | 0.10461          | 0.007878                             | 0.015755                             | 0.010195                             | 0.005097                             | 0.006951                             | 0.053191         | 0.039007        | 0.060284        | 0.078014         | 0.037234        | 0.035461       | 0.031915           | 0.035461           | 0.039007             | 0.021277          | 0.008865          | 0.007092           | 0.012411           | 0.012411        | 0.014184          | 0.001773        | 0               | 0               | 0.007092       | 7                            | 8                  | 0.036145                               | 0.006951                               | 0                 | 0.001773          | 0                 | 0.037234          | 0.035461         | 0               | 0                | 0                   | 0.031915             | 0                   | 0.008865            | 0.003546           | 0.021277            | 0.003546            | 1    | 1       | 1   | 1        | 1      | 1    | 1       | 1   | 1    | 0      | 1    | 0    | 0   | 1       | 0        | 0      | 0   | 1    | 0   | 0     | 0    | 1 | a54f70b383cfc153e3cb2405c885e1a34d919ef8237b9179146acab1acd1c3c2 | 0     |
| 7 | 4.634054         | 15511         | 0.183803                             | 0.352871                             | 0.07351                              | 0.06896                              | 0.083207                             | 0.03792                              | 0.047562                             | 0.03467                              | 0.021343                             | 0.150117        | 0.032557                             | 0.020477                             | 0.205825         | 0.104378         | 0.008072                             | 0.014735                             | 0.009913                             | 0.004225                             | 0.006176                             | 0.042025         | 0.045739        | 0.062158        | 0.070172         | 0.036747        | 0.037138       | 0.028538           | 0.026974           | 0.034793             | 0.019547          | 0.016224          | 0.008014           | 0.009382           | 0.015442        | 0.017983          | 0.006841        | 0.005864        | 0.006059        | 0.007232       | 3                            | 4                  | 0.03792                                | 0.006176                               | 0.006059          | 0.006841          | 0.005864          | 0.036747          | 0.037138         | 0.001955        | 0                | 0.001368            | 0.028538             | 0                   | 0.016224            | 0.007037           | 0.019547            | 0.000586            | 1    | 1       | 0   | 1        | 1      | 0    | 1       | 1   | 0    | 0      | 0    | 1    | 1   | 1       | 0        | 0      | 1   | 1    | 1   | 0     | 0    | 1 | 49cdeb9e5efbc478d749949008fbf74a586fa938f288d6591a842d6ef8fd0c29 | 0     |
| 8 | 4.137519         | 7655          | 0.172643                             | 0.443559                             | 0.048473                             | 0.055113                             | 0.063081                             | 0.015936                             | 0.034529                             | 0.028552                             | 0.024568                             | 0.128205        | 0.034529                             | 0.024568                             | 0.221154         | 0.086538         | 0.013944                             | 0.018592                             | 0.011288                             | 0.004648                             | 0.005976                             | 0.057692         | 0.012821        | 0.035256        | 0.076923         | 0.054487        | 0.025641       | 0.012821           | 0.025641           | 0.038462             | 0.025641          | 0.016026          | 0.00641            | 0.019231           | 0.009615        | 0.012821          | 0.012821        | 0.016026        | 0.012821        | 0.012821       | 4                            | 5                  | 0.015936                               | 0.005976                               | 0.012821          | 0.012821          | 0.016026          | 0.054487          | 0.025641         | 0.009615        | 0                | 0                   | 0.012821             | 0                   | 0.016026            | 0.00641            | 0.025641            | 0                   | 0    | 1       | 1   | 1        | 0      | 0    | 0       | 1   | 1    | 0      | 1    | 0    | 0   | 0       | 0        | 0      | 0   | 0    | 0   | 0     | 0    | 1 | e681e677aec51451b01fb608d47c1daffd7cda6297cec705f198437d4181d41f | 0     |
| 9 | 4.145628         | 7655          | 0.173307                             | 0.444223                             | 0.047809                             | 0.057105                             | 0.064409                             | 0.0166                               | 0.030544                             | 0.02656                              | 0.024568                             | 0.119601        | 0.033865                             | 0.027888                             | 0.229236         | 0.086379         | 0.015936                             | 0.015272                             | 0.011952                             | 0.003984                             | 0.005976                             | 0.059801         | 0.009967        | 0.036545        | 0.079734         | 0.059801        | 0.023256       | 0.009967           | 0.026578           | 0.039867             | 0.026578          | 0.016611          | 0.006645           | 0.019934           | 0.009967        | 0.013289          | 0.013289        | 0.016611        | 0.013289        | 0.013289       | 4                            | 5                  | 0.0166                                 | 0.005976                               | 0.013289          | 0.013289          | 0.016611          | 0.059801          | 0.023256         | 0.006645        | 0                | 0                   | 0.009967             | 0                   | 0.016611            | 0.006645           | 0.026578            | 0                   | 0    | 1       | 1   | 1        | 0      | 0    | 0       | 1   | 1    | 0      | 1    | 0    | 0   | 0       | 0        | 0      | 0   | 0    | 0   | 0     | 0    | 1 | 1f6a2261b19c52cab0218ab286b6451b9d3bd5c789035b005886538628292493 | 0     |


# Copyright (c) 2023

SCsVulLyzer V1.0: For citation in your works and also understanding SCsVulLyzer V1.0 completely, you can find below-published papers:

[Sepideh Hajihosseinkhani, Arash Habibi Lashkari, Ali Mizani, “Unveiling Vulnerable Smart Contracts: Toward Profiling Vulnerable Smart Contracts using Genetic Algorithm and Generating Benchmark Dataset”, Blockchain: Research and Applications, Vol. 4, December 2023](https://www.sciencedirect.com/science/article/pii/S2096720923000465?via%3Dihub)


### Project Team members 

* [**Arash Habibi Lashkari:**](http://ahlashkari.com/index.asp) Founder and Project Owner 

* [**Sepideh HajHosseinkhani:**](https://github.com/Sepid-99) Researcher and Developer 

### Acknowledgement 
This project has been made possible through funding from the Natural Sciences and Engineering Research Council of Canada — NSERC (#RGPIN-2020-04701) and Canada Research Chair (Tier II) - (#CRC-2021-00340) to Arash Habibi Lashkari.
