
CC=gcc
CFLAGS=-Wall -Wextra -Wvla -fPIC -fsanitize=address
LIBS=-lpthread -lcrypto
TARGET=app
SOURCES=main.c

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) $(SOURCES) -o $(TARGET) $(LIBS)

clean:
	rm -f $(TARGET)
