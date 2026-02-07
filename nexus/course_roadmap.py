ROADMAP_CONTENT = """
### Course Roadmap: Systems Programming Masterclass
*   **Week 1: The Machine Interface** – Bits, Bytes, Memory Addressing, and the C Compilation Pipeline.
*   **Week 2: Memory Mastery** – Pointers, Addresses, and Pointer Arithmetic.
*   **Week 3: Data Architecture** – Aggregate Types (Structs/Unions), Memory Alignment, and Bit Manipulation.
*   **Week 4: Persistence & Dynamics** – File Streams, Manual Memory Management (Heap), and Linked Lists.
*   **Week 5: Execution Control** – Function Pointers, Signals (Software Interrupts), and Low-Level I/O.
*   **Week 6: The Build Pipeline** – C Preprocessor, Linking, and Automating with Makefiles.
*   **Week 7: Process Management** – Virtual Memory and the `fork`/`exec` Life Cycle.
*   **Week 8: Inter-Process Communication (IPC)** – Pipes, Named Pipes, and Shared Memory.
*   **Week 9: Concurrency Foundations** – Introduction to Parallelism and POSIX Threads (Pthreads).
*   **Week 10: Synchronisation Mastery** – Mutexes, Semaphores, and Preventing Race Conditions.
*   **Week 11: Scalable Algorithms** – Recursive Parallelism and Divide-and-Conquer Templates.
*   **Week 12: Performance Engineering** – Amdahl’s Law, Load Balancing, and Cache Optimization.

---

### Week 1: Foundations — Bits, Bytes, and the Machine
**Learning Goals:** By the end of this week, you must be able to:
1.  Diagram the four stages of the C compilation pipeline.
2.  Explain the relationship between bits, bytes, and memory addresses.
3.  Write a C program that performs formatted input and output.
4.  Navigate a UNIX environment using basic BASH commands.

**Key Topics & Keywords:**
*   **Systems Programming**
*   **Bits and Bytes**
*   **Memory Addressing**
*   **The Compilation System** (Preprocessing, Compiling, Assembling, Linking)
*   **Standard I/O** (`printf`, `scanf`, `getchar`, `putchar`)
*   **The `main` Function**

---

#### Topic 1: Systems Programming
*   **Definition:** A discipline focused on managing a computer's fundamental resources—memory and processes—and facilitating their communication [Introduction].
*   **Intuition:** It is the "plumbing" of a computer; you aren't just using the machine, you are managing its internals [Introduction].
*   **Why it exists:** Higher-level languages (like Java) hide resource management, which prevents fine-grained control over hardware performance and security.
*   **How it works:** It involves using low-level languages like C to interact directly with the Operating System (OS) kernel via system calls.
*   **Dependencies:** Basic understanding of logic and Java-like syntax.
*   **Connections:** Week 1 sets the stage for manual memory control in Week 4 and process management in Week 7.
*   **Common Mistakes:** Treating C like Java (e.g., forgetting there is no automatic garbage collection).

---

#### Topic 2: Bits and Bytes
*   **Definition:** A **bit** is the smallest unit of data (0 or 1); 8 bits constitute 1 **byte**.
*   **Intuition:** If a bit is a light switch, a byte is a panel of eight switches.
*   **Why it exists:** Computers use binary logic at the hardware level; bytes are the standard unit of measurement for memory storage.
*   **How it works:** Every character or number is encoded as a sequence of bits. In ASCII, one text character equals one byte.
*   **Dependencies:** None.
*   **Connections:** Leads to hexadecimal notation and memory addresses.
*   **Micro-example:** `0x17` in hex represents 4 bits for `1` (`0001`) and 4 bits for `7` (`0111`), totaling one byte.

**Exam-Style Check:**
1.  (MCQ) How many bits are in 3 bytes? A) 8, B) 16, C) 24, D) 32. *(Answer: C)*
2.  (T/F) ASCII characters are typically represented by 4 bits. *(Answer: False, they are byte-sized)*.
3.  (Short Answer) Why does C use bytes rather than bits as the primary unit of memory management? *(Answer: Dealing with individual bits is too "messy" and complex for the OS)*.

---

#### Topic 3: The Compilation System
*   **Definition:** The four-stage process that transforms human-readable C source code into a binary executable: **Preprocessing**, **Compilation**, **Assembly**, and **Linking**.
*   **Intuition:** A factory assembly line where raw text is refined until it becomes a functional tool.
*   **Why it exists:** Computers cannot read text; they only understand machine-level instructions.
*   **How it works:**
    1.  **Preprocessing:** Handles `#` directives (e.g., `#include` copies header files) to produce a `.i` file.
    2.  **Compilation:** Translates `.i` into Assembly language (`.s`), describing low-level instructions.
    3.  **Assembly:** Converts Assembly into binary machine code (object files, `.o`).
    4.  **Linking:** Merges object files and libraries (like `printf`) into one final executable.
*   **Dependencies:** Understanding Bits/Bytes.
*   **Connections:** Leads to Week 6 (Makefiles and modular builds).
*   **Common Mistakes:** Thinking the compiler creates the executable directly; it only creates object files—the *linker* finishes the job.

**Exam-Style Check:**
1.  (MCQ) Which stage merges `printf.o` with your code? A) Preprocessing, B) Assembly, C) Linking. *(Answer: C)*.
2.  (T/F) The `.o` file can be read with a standard text editor. *(Answer: False, it is binary)*.
3.  (Short Answer) What is the purpose of the Preprocessor? *(Answer: To modify the code based on hash-prefixed directives before compilation starts)*.

---

#### Topic 4: The `main` Function and Standard I/O
*   **Definition:** `main` is the entry point of a C program; `printf` and `scanf` are standard library functions for output and input.
*   **Symbol-by-Symbol Breakdown:** `int main(int argc, char **argv)`
    *   `int`: The return type. A return of `0` means success.
    *   `main`: The specific name the OS looks for to start the process.
    *   `argc`: **Arg**ument **c**ount; the number of items typed in the terminal command.
    *   `char **argv`: An array of pointers to the actual strings (arguments).
*   **Intuition:** `main` is the "Start" button; `printf` is the computer talking, and `scanf` is the computer listening.
*   **Why it exists:** Programs need a defined starting point and a way to interact with users.
*   **How it works:** `printf` uses format codes (e.g., `%d` for integer, `%f` for float) to display data. `scanf` requires the **address** of a variable (using `&`) to store input.
*   **Dependencies:** You must know **Pointers** before you can fully understand *why* `scanf` needs the `&` symbol.
*   **Connections:** Prepares for Week 2 (Pointers) and Week 5 (Low-level file descriptors).

**Exam-Style Check:**
1.  (MCQ) What does `scanf("%d", &x)` require to work? A) The value of x, B) The address of x, C) The size of x. *(Answer: B)*.
2.  (T/F) `argc` includes the name of the program itself. *(Answer: True)*.
3.  (Short Answer) Explain the difference between `printf` and `putchar`. *(Answer: printf handles formatted strings/multiple types; putchar writes only a single character)*.

---

### Week 1 Recap
**Concept Map:**
**Machine Bits** $\rightarrow$ **Bytes** $\rightarrow$ **Memory Addresses** $\rightarrow$ **C Source Code** $\rightarrow$ **Compilation Pipeline** $\rightarrow$ **Running Process** (`main`).

**Week 1 Quiz:**
1.  How many bits are in a byte?
2.  What character terminates all strings in C?
3.  Which stage of compilation handles `#define`?
4.  What does a return code of `0` indicate?
5.  What is the difference between an address and a value?
6.  What header file is required for `printf`?
7.  What is the format code for a hexadecimal number?
8.  True or False: C has automatic garbage collection.
9.  Which UNIX command lists directory contents?
10. If `argc` is 3, how many user-provided arguments (excluding the program name) were given?

**Common Pitfalls Checklist:**
*   [ ] Forgetting the semicolon `;` at the end of statements.
*   [ ] Forgetting to use `&` in `scanf` (causes a crash).
*   [ ] Confusing the `=` (assignment) with `==` (equality test).
*   [ ] Assuming an uninitialized variable starts at zero (it contains junk data).
"""
