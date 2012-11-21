#! /usr/bin/env python

import os

for fname in os.listdir('.'):
    if fname.endswith('.py'):
        try:
            name, ending = fname.split('.')
            int(name)
            os.system('git mv %s %s.py' % (fname, name.zfill(3)))
        except:
            pass
