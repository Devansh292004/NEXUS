import os

class MakefileGenerator:
    """
    Section 10.1: Makefile Generator
    Automatic Dependency Tracking and Build Variants.
    """
    def generate(self, target="app", sources="main.c"):
        print("Generating Makefile with mandatory flags and variants...")
        base_flags = "-Wall -Wextra -Wvla -fPIC"
        libs = "-lpthread -lcrypto"

        makefile = f"""
CC=gcc
CFLAGS_BASE={base_flags}
LIBS={libs}
TARGET={target}
SOURCES={sources}

# Build Variants (Section 10.1)
DEBUG_FLAGS=-g -fsanitize=address -O0
RELEASE_FLAGS=-O3 -DNDEBUG
TEST_FLAGS=-g --coverage

.PHONY: all debug release test clean

all: debug

debug:
\t$(CC) $(CFLAGS_BASE) $(DEBUG_FLAGS) $(SOURCES) -o $(TARGET) $(LIBS)

release:
\t$(CC) $(CFLAGS_BASE) $(RELEASE_FLAGS) $(SOURCES) -o $(TARGET) $(LIBS)

test:
\t$(CC) $(CFLAGS_BASE) $(TEST_FLAGS) $(SOURCES) -o $(TARGET)_test $(LIBS)

clean:
\trm -f $(TARGET) $(TARGET)_test *.gcda *.gcno
"""
        return makefile

class CompilationBuildSystem:
    def __init__(self):
        self.generator = MakefileGenerator()

    def process(self, code_info, base_path="."):
        print(f"Starting Compilation & Build System stage in {base_path}...")
        makefile = self.generator.generate()

        # Write Makefile and code to the unique session directory
        try:
            os.makedirs(base_path, exist_ok=True)
            with open(os.path.join(base_path, "Makefile"), "w") as f:
                f.write(makefile)
            with open(os.path.join(base_path, "main.c"), "w") as f:
                f.write(code_info.get("code", ""))
        except Exception as e:
            print(f"Build System: Error writing files to {base_path}: {e}")

        return {"makefile": makefile, "status": f"Build artifacts generated in {base_path}", "variants": ["debug", "release", "test"]}
