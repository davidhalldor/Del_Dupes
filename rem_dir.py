__author__ = 'davidhalldor'

import os, shutil
for dirpath, dirnames, filenames in os.walk(r'C:\Users\davidhalldor\Documents\Skolinn'):
    print(dirpath)
    if dirpath.find('.svn') is not -1:
        print ("   ", dir)
        shutil.rmtree(os.path.abspath(dirpath))