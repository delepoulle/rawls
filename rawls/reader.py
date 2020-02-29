# main imports
from PIL import Image
import numpy as np
import struct

def read(filepath):
    """[open data of rawls file]
    
    Arguments:
        filepath {str} -- [path of the .rawls file to open]
    """
    f = open(filepath, "r")

    ihdr_line = 'IHDR'
    ihdr = False

    img_chanels = None
    img_width = None
    img_height = None

    line = f.readline()
    line = line.decode('utf-8')

    while not ihdr:

        if ihdr_line in line:
            ihdr = True
            
            # read info line
            f.readline()

            img_chanels, img_width, img_height = f.readline().replace(b'\n', '').split(b' ')

            img_chanels


    f.close()