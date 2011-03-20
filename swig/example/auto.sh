swig -python example.i
gcc -c example.c example_wrap.c -I /usr/include/python2.6/
ld -share example.o example_wrap.o -o _example.so
