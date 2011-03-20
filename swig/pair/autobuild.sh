swig -python -c++ pair.i
mv pair.h pair.h.bak
> pair.h
c++ -c pair_wrap.cxx -I/usr/include/python2.6
c++ -shared pair_wrap.o -o _pair.so
mv pair.h.bak pair.h
