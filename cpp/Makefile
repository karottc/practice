# Mac OS or linux
ifeq ($(shell uname),Linux)
	GCC = gcc
	G++ = g++
else
	GCC = /usr/local/Cellar/gcc/4.9.1/bin/gcc-4.9
	G++ = /usr/local/Cellar/gcc/4.9.1/bin/g++-4.9
endif

TARGET=timerExample read priority size setTest mapTest vectorTest

all: $(TARGET)

timerExample:
	$(GCC) timerExample.c -o timerExample -Wall -lrt

read:
	$(GCC) forkReadFile.c -o read -Wall -DFORK_READ

priority:
	$(G++) test_priority_queue.cc -o priority -Wall 

size:
	$(G++) testSizeof.cc -o size -Wall

vectorTest:
	$(G++) vector-test.cpp -o vectorTest -Wall

mapTest:
	$(G++) map-test.cpp -o mapTest -Wall

setTest:
	$(G++) set-test.cpp -o setTest -Wall


clean:
	rm -rf $(TARGET)
