![](https://github.com/ahlashkari/SCsVulLyzer/blob/main/bccc.jpg)

# Smart Contracts Vulnerabilities Analyzer (SCsVulLyzer V2.0)


As a featured installment of the Understanding Cybersecurity Series (UCS), SCsVulLyzer V2 is an advanced Python open-source project designed to enhance the profiling of Smart Contracts (SCs) for improved vulnerability detection. This release builds upon the foundations of its predecessor by introducing refined methodologies for feature extraction and analysis.
SCsVulLyzer operates as a comprehensive tool tailored for Ethereum smart contracts coded in Solidity. This version, also known as BCCC-SCsVulLyzer, distinguishes itself by categorizing features into two primary types: compiler-based and non-compiler-based. Such classification expands the scope of feature extraction and leverages a variety of functions to deeply analyze the contract's source code. This analysis includes compiling the code to extract bytecode, opcodes, the Abstract Syntax Tree (AST), the Application Binary Interface (ABI), along with detailed contract and Solidity-specific information.
A notable enhancement in this version is the introduction of 'bytecode entropy'—a measure of the randomness within the bytecode, which serves as an indicator of unpredictability and complexity. This metric is particularly valuable in fields like cryptography and anomaly detection. The entropy is calculated using Shannon's formula:



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
