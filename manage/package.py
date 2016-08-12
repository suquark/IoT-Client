import os
import sys
from scripts.tar import uncompress, compress

def apply(path):

    os.system("python3 %s" % os.path.join(path, ""))
    sys.exit()