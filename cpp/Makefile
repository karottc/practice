# Mac OS or linux
ifeq ($(shell uname),Linux)
	GCC = gcc
	G++ = g++
else
	GCC = /usr/local/Cellar/gcc/4.9.1/bin/gcc-4.9
	G++ = /usr/local/Cellar/gcc/4.9.1/bin/g++-4.9
endif

TARGET=timerExample read priority size

all: $(TARGET)

timerExample:
	$(GCC) timerExample.c -o timerExample -Wall -lrt

read:
	$(GCC) forkReadFile.c -o read -Wall -DFORK_READ

priority:
	$(G++) test_priority_queue.cc -o priority -Wall 

size:
	$(G++) testSizeof.cc -o size -Wall


clean:
	rm -rf $(TARGET)
