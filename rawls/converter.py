# main imports
import os
import numpy as np

# image imports
from PIL import Image

# class import
from rawls.classes.rawls import Rawls


def rawls_to_pil(rawls_img):
    """Read and convert rawls image file into PIL image
    
    Arguments:
        rawls_img: {Rawls} .rawls image file loaded
    Returns:
        Pil RGB image

    Example:

    >>> import numpy as np
    >>> from rawls.converter import rawls_to_pil
    >>> path = 'images/example.rawls'
    >>> rawls_img = Rawls.fromfile(path)
    >>> rawls_pil_img = rawls_to_pil(rawls_img)
    >>> np.array(rawls_pil_img).shape
    (100, 100, 3)
    """
    gamma_converted = rawls_img.gammaConvert()

    return Image.fromarray(np.array(gamma_converted, 'uint8'))


def rawls_to_png(filepath, outfile):
    """Convert rawls image into PNG image
    
    Arguments:
        filepath: {str} path of the .rawls file to open
        outfile: {str} output path of the .png image to save
    """

    if '/' in outfile:
        folders = outfile.split('/')
        del folders[-1]

        output_path = ''
        for folder in folders:
            output_path = os.path.join(output_path, folder)

        if not os.path.exists(output_path):
            os.makedirs(output_path)

    if '.png' not in outfile:
        raise Exception('output filename is not `.png` format')

    rawls_to_pil(filepath).save(outfile)
