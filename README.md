# NEXUS: Universal Systems Programming Assignment Solver

NEXUS (Neural EXecution and Understanding System) is an autonomous AI-powered framework designed to solve complex systems programming assignments in C with high correctness. It integrates formal verification, symbolic execution, and LLM-guided code synthesis.

## Prerequisites

- **Python 3.8+**
- **GCC** (for compiling generated C code)
- **Make** (for build management)

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/Devansh292004/NEXUS.git
cd NEXUS
```

### 2. Run the Framework
You can run the framework using the provided `main.py` entry point.

**Using a string specification:**
```bash
python3 main.py --spec "REQ: Implement a concurrent queue. REQ: Must be fast."
```

**Using a specification file:**
```bash
python3 main.py --file path/to/assignment.txt
```

**Default run (sample specification):**
```bash
python3 main.py
```

## Generated Outputs

After a successful run, the framework produces:
- `main.c`: The synthesized C source code.
- `Makefile`: A professional Makefile with Debug/Release/Test variants.
- Documentation (accessible via the `OutputGuarantees` module):
    - System Architecture Diagrams (Mermaid.js)
    - API Documentation
    - Formal Proof of Correctness
    - Comprehensive README

## Running Tests

To verify the framework's internal logic and pipeline integrity, run the comprehensive test suite:

```bash
export PYTHONPATH=$PYTHONPATH:.
python3 -m unittest discover tests
```

## Architecture

The framework follows a 12-stage pipeline:
1.  **Multi-Stage Analysis**: Requirement decomposition and constraint extraction.
2.  **Domain Planning**: Specialized strategies for Memory, Concurrency, and Networking.
3.  **Formal Verification**: Path exploration (KLEE) and SMT solving (Z3).
4.  **Code Synthesis**: Multi-agent LLM-guided C code generation.
5.  **Intelligent Testing**: Property-based, metamorphic, and mutation testing.
6.  **Compliance Checking**: Static analysis for forbidden functions and code style.
7.  **Build System**: Automatic Makefile generation.
8.  **Output Guarantees**: Certification and documentation.
