class MakefileGenerator:
    def generate(self, target="app", sources="main.c"):
        print("Generating Makefile with mandatory flags...")
        flags = "-Wall -Wextra -Wvla -fPIC -fsanitize=address"
        makefile = f"""
CC=gcc
CFLAGS={flags}
TARGET={target}
SOURCES={sources}

all: $(TARGET)

$(TARGET): $(SOURCES)
\t$(CC) $(CFLAGS) $(SOURCES) -o $(TARGET)

clean:
\trm -f $(TARGET)
"""
        return makefile

class CompilationBuildSystem:
    def __init__(self):
        self.generator = MakefileGenerator()

    def process(self, code):
        print("Starting Compilation & Build System stage...")
        makefile = self.generator.generate()
        return {"makefile": makefile}
