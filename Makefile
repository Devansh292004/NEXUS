
CC=gcc
CFLAGS_BASE=-Wall -Wextra -Wvla -fPIC
LIBS=-lpthread -lcrypto
TARGET=app
SOURCES=main.c

# Build Variants (Section 10.1)
DEBUG_FLAGS=-g -fsanitize=address -O0
RELEASE_FLAGS=-O3 -DNDEBUG
TEST_FLAGS=-g --coverage

.PHONY: all debug release test clean

all: debug

debug:
	$(CC) $(CFLAGS_BASE) $(DEBUG_FLAGS) $(SOURCES) -o $(TARGET) $(LIBS)

release:
	$(CC) $(CFLAGS_BASE) $(RELEASE_FLAGS) $(SOURCES) -o $(TARGET) $(LIBS)

test:
	$(CC) $(CFLAGS_BASE) $(TEST_FLAGS) $(SOURCES) -o $(TARGET)_test $(LIBS)

clean:
	rm -f $(TARGET) $(TARGET)_test *.gcda *.gcno
