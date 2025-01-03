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

Features are further categorized based on their evaluation timing—pre or post-compilation. Compiler-based features include those processed post-compilation, like ABI and AST, whereas non-compiler-based features derive from existing NLP methodologies adapted to smart contracts, focusing on critical keywords.

This version also introduces three innovative feature categories: Contract Information, Source Code Information, and Solidity Information. These categories are designed to quantify various elements of the code, such as function counts, statements, loops, and lines, enhancing the granularity of our analysis.

The integration of both compiler-based and non-compiler-based features in BCCC-SCsVulLyzer marks a significant step forward in the methodology of SC vulnerability detection, positioning the analyzer as a pivotal tool in the field.

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
