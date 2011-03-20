from distutils.core import setup, Extension

setup(name="test",
        version="1.0",
        ext_modules=[Extension("_example", ["example.i", "example.c"], 
                    #           swig_opts=["-I/usr/include/python2.6"]
                              )
                    ],


        )
