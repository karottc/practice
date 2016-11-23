# Mac OS or linux
ifeq ($(shell uname),Linux)
	GCC = gcc
	G++ = g++
else
	GCC = /usr/local/Cellar/gcc/4.9.1/bin/gcc-4.9
	G++ = /usr/local/Cellar/gcc/4.9.1/bin/g++-4.9
endif

FLAGS=-Wall
TARGET= server client

all: $(TARGET)

server:
	$(G++) $(FLAGS) -o server epoll-server-test1.cc

client:
	$(G++) $(FLAGS) -o client epoll-client-test1.cc

clean:
	rm -rf $(TARGET)
