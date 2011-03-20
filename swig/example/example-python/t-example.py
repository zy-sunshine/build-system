import sys
sys.path.insert(0, "build/lib.linux-i686-2.6/")
import example
cmds = ["example.fact(5)",
        "example.my_mod(7, 3)",
        "example.get_time()",
        ]
for cmd in cmds:
    print "%s: %s" % (cmd, eval(cmd))

