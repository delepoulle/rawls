"""Utils function for .rawls file
"""
#main imports
from os import listdir, name, makedirs, chdir, remove, rmdir
from os.path import isfile, join,exists
import csv
import glob
from posix import POSIX_FADV_WILLNEED
import pandas as pd
import shutil

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
    file_name_CSV = filepath.split('/')[-1] + "_" + str(x) + "_" + str(y)
    if not exists(out_filepath):
        makedirs(out_filepath)
    out_filepath += "/" + file_name_CSV + ".csv"
    with open(out_filepath, 'w', newline='') as file:
        writer = csv.writer(file,delimiter=',')
        row_title = [str(x) + "_" + str(y) + "_" + "R" , str(x) + "_" + str(y) + "_" + "G" , str(x) + "_" + str(y) + "_" + "B"]
        writer.writerow(row_title)
        writer.writerows(samplesPixel)

def create_CSV_zone(filepath, x1, y1, x2, y2, out_filepath):
    """create a CSV file with all the samples
    for a pixel specified by x an y coordinates

    Arguments:
        filepath : {str} -- repertory of the rawls samples
        x1 : {int} -- horizontal coordinate of the top left corner pixel
        y1 : {int} -- vertical coordinate of the top left corner pixel
        x2 : {int} -- horizontal coordinate of the bottom right corner pixel
        y2 : {int} -- vertical coordinate of the bottom right corner pixel
        out_filepath : {str} -- path where we want to save the CSV file

    Raises:
        Exception: Invalid coodinate
        Exception: Invalid input filepath, need at least one image rawls

    """

    if (x1>x2) or (y1>y2):
        raise Exception('Invalid coordinate')
    if filepath.endswith("/"):
        filepath = filepath[:-1]
    if out_filepath.endswith("/"):
        out_filepath = out_filepath[:-1]
    #create a temp repertory
    temp_out_filepath = out_filepath + "/" +  filepath.split('/')[-1]
    for j in range(y2-y1+1):
        for i in range(x2-x1+1):
            create_CSV(filepath,i+1,j+1,temp_out_filepath)
    chdir(temp_out_filepath)
    file_extension = '.csv'
    all_filenames = [i for i in glob.glob(f"*{file_extension}")]
    #combine all files in the list
    combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
    file_name_CSV = filepath.split('/')[-1] + "_" + str(x1) + "_" + str(y1) + "_to_" + str(x2) + "_" + str(y2)
    combined_csv.to_csv( file_name_CSV + ".csv", index=False, encoding='utf-8-sig')
    shutil.move(file_name_CSV + ".csv", "../" + file_name_CSV + ".csv")
    chdir("../")
    shutil.rmtree("./" + filepath.split('/')[-1])

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