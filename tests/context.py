import os
import sys

try:
    import NYPDCompstatAPI
except ModuleNotFoundError:
    sys.path.insert(0, os.path.abspath('../'))
    os.chdir(os.path.abspath('../'))
    import NYPDCompstatAPI

