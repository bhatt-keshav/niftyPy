# A small python script that can be run in python terminal to tell where python is installed 
# Specially useful when working on a virtual env and you want to be sure that you are using the virtual-env py
# and not the python installed for the device
import os
import sys
os.path.dirname(sys.executable)
