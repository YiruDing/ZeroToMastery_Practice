import sys
import os
# The OS module in Python provides functions for interacting with the operating system. OS comes under Python's standard utility modules. This module provides a portable way of using operating system-dependent functionality. The *os* and *os. path* modules include many functions to interact with the file system.
from PIL import Image
# https://github.com/aneagoie/pokedex/blob/master/JPGtoPNGconverter.py

# 1.Grab 1st and 2nd argument
path = sys.argv[1]
# 212 2:23 the first folder
directory = sys.argv[2]
# 212 the second folder created

# 2.check is new/exists, if not, create one.
if not os.path.exists(directory):
    os.makedirs(directory)

# 3.Loop through Pokedex,convert images to png, and save to the new folder
for filename in os.listdir(path):
    clean_name = os.path.splitext(filename)[0]
    img = Image.open(f'{path}{filename}')
    #added the / in case user doesn't enter it. You may want to check for this and add or remover it.
    img.save(f'{directory}/{clean_name}.png', 'png')
    # convert to png
    print('all done!')