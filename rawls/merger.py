# main imports
import os
import numpy as np

# image imports
from PIL import Image

# class import
from rawls.classes.rawls import Rawls
from rawls.converter import rawls_to_png, rawls_to_pil


def merge_mean_rawls(filepaths):
    """Merger `.rawls` samples images from list of files
    
    Arguments:
        filepaths: {[str]} image filepaths list
    
    Returns:
        new rawls object with mean data of rawls files
    """

    #
    rawls_images = []

    for filepath in filepaths:
        rawls_images.append(Rawls.fromfile(filepath))

    # getting and check shapes of images
    shapes = []

    for img in rawls_images:
        shapes.append(img.shape)

    if not shapes[1:] == shapes[:-1]:
        raise Exception('Input rawls images do not have same shapes')

    # compute merge values<
    height, width, chanels = rawls_images[0].shape
    merged_values = np.zeros((height, width, chanels))

    for img in rawls_images:

        for y in range(height):
            for x in range(width):
                for c in range(chanels):
                    merged_values[y][x][c] += img.data[y][x][c]

    nb_images = len(rawls_images)

    # compute mean of values
    for y in range(height):
        for x in range(width):
            for c in range(chanels):
                merged_values[y][x][c] /= nb_images

    # construct output data
    return Rawls(rawls_images[0].shape, merged_values,
                 rawls_images[0].comments)


def merge_mean_rawls_to_pil(filepaths):
    """Return mean merged image into PNG
    
    Arguments:
        filepaths: {[str]} image filepaths list
    
    Returns:
        PNG PIL mean merged image
    """
    merged_image = merge_mean_rawls(filepaths)
    return rawls_to_pil(merged_image)


def merge_mean_rawls_to_png(filepaths, outfile):
    """Return mean merged image into PNG
    
    Arguments:
        filepaths: {[str]} image filepaths list
        outfile: {str} output path of the .png image to save
    
    Returns:
        save mean merged image as png
    """
    merged_image = merge_mean_rawls(filepaths)
    return rawls_to_png(merged_image, outfile)
