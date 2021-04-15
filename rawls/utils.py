"""Utils function for .rawls file
"""
#main imports
from os import listdir, name, makedirs
from os.path import isfile, join,exists
import csv

#modules imports
from .rawls import Rawls
# utils functions
def create_CSV(filepath, x, y, out_filepath):
    """create a CSV file with all the samples
    for a pixel specified by x an y coordinates

    Arguments:
        filepath : {str} -- repertory of the rawls samples
        x : {int} -- horizontal coordinate of the pixel
        y : {int} -- vertical coordinate of the pixel
        out_filepath : {str} -- path where we want to save the CSV file

    Raises:
        Exception: Invalid input filepath, need at least one image rawls

    """
    files = []
    for f in listdir(filepath):
        if '.rawls' in f:
            files.append(filepath + "/" + f)
    if(len(files)==0):
        raise Exception('Unvalid input filepath images, need .rawls image')
    samplesPixel = []
    for file in files:
        samplesPixel.append(Rawls.load_pix(file,x,y))
    if filepath.endswith("/"):
        filepath = filepath[:-1]
    name_file_CSV = filepath.split('/')[-1] + "_" + str(x) + "_" + str(y)
    if not exists(out_filepath):
        makedirs(out_filepath)
    out_filepath += "/" + name_file_CSV + ".csv"
    with open(out_filepath, 'w', newline='') as file:
        writer = csv.writer(file,delimiter=',')
        writer.writerows(samplesPixel)

def check_file_paths(filepaths):
    """check filepaths input extension
    
    Arguments:
        filepaths: {[str]} -- image filepaths list
    
    Raises:
        Exception: Invalid input filepaths extension
    """

    if isinstance(filepaths, list):
        for p in filepaths:
            check_file_paths(p)
    else:
        if not '.rawls' in filepaths:
            raise Exception('Unvalid input filepath images, need .rawls image')