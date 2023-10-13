CC=clang++
CFLAGS=-c -Wall

all: processes

processes: processes.o
	$(CC) processes.o -o processes

processes.o: processes.cpp
	$(CC) $(CFLAGS) processes.cpp

clean:
	rm -rf *o processes
