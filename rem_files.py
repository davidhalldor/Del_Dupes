__author__ = 'davidhalldor'

import os
for dirpath, dirnames, filenames in os.walk(r'C:\Users\davidhalldor\Documents\Books'):
    print(dirpath)
    for fn in filenames:
        if fn.find('(00001)') is not -1:
            print ("   ", fn)
            os.remove(os.path.abspath(dirpath + os.sep + fn))