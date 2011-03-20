# -*- coding: utf-8 -*-
import sys
sys.path[0:0] = ["build/lib.linux-i686-2.6/"]
import cmmseg
#cmmseg.init('F:\\deps\\mmseg\\src\\win32')
cmmseg.init('/usr/local/coreseek/dict/')
rs = cmmseg.segment((u'中文分词').encode('utf-8'))
for i in rs:
    print i.decode('utf-8')
