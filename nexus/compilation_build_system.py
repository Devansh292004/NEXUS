class MakefileGenerator:
    def generate(self, target="app", sources="main.c"):
        print("Generating Makefile with mandatory flags...")
        flags = "-Wall -Wextra -Wvla -fPIC -fsanitize=address"
        libs = "-lpthread -lcrypto"
        makefile = f"""
CC=gcc
CFLAGS={flags}
LIBS={libs}
TARGET={target}
SOURCES={sources}

all: $(TARGET)

$(TARGET): $(SOURCES)
\t$(CC) $(CFLAGS) $(SOURCES) -o $(TARGET) $(LIBS)

clean:
\trm -f $(TARGET)
"""
        return makefile

class CompilationBuildSystem:
    def __init__(self):
        self.generator = MakefileGenerator()

    def process(self, code_info):
        print("Starting Compilation & Build System stage...")
        makefile = self.generator.generate()

        # Write Makefile and code to disk for actual compilation capability
        with open("Makefile", "w") as f:
            f.write(makefile)
        with open("main.c", "w") as f:
            f.write(code_info.get("code", ""))

        return {"makefile": makefile, "status": "Build artifacts generated on disk"}
