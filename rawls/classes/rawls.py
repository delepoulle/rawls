# main imports
import math
import numpy as np
import struct


class Rawls():
    """[Rawls class used to open `.rawls` path image]
    """

    def __init__(self, filepath):
        self.shape = None
        self.data = None
        self.comments = None
        self.__read(filepath)

    def __read(self, filepath):
        """[open data of rawls file]
        
        Arguments:
            filepath {[str]} -- [path of the .rawls file to open]
        """

        if '.rawls' not in filepath:
            raise Exception('filepath used is not valid')

        f = open(filepath, "rb")

        # finding data into files
        ihdr_line = 'IHDR'
        ihdr_found = False

        comments_line = 'COMMENTS'
        comments_found = False

        data_line = 'DATA'
        data_found = False

        # prepare rawls object data
        img_chanels = None
        img_width = None
        img_height = None

        comments = ""
        data = None

        # read first line
        line = f.readline()
        line = line.decode('utf-8')

        while not ihdr_found:

            if ihdr_line in line:
                ihdr_found = True

                # read info line
                f.readline()

                values = f.readline().strip().replace(b' ', b'')
                img_width, img_height, img_chanels = struct.unpack(
                    'III', values)

                data = np.empty((img_height, img_width, img_chanels))

        line = f.readline()
        line = line.decode('utf-8')

        while not comments_found:

            if comments_line in line:
                comments_found = True

        # get comments information
        while not data_found:

            line = f.readline()
            line = line.decode('utf-8')

            if data_line in line:
                data_found = True
            else:
                comments += line

        # default read data size
        line = f.readline()

        # read buffer image data (here samples)
        for y in range(img_height):
            for x in range(img_width):

                # read the float bytes
                line = f.read(4 * img_chanels)
                values = struct.unpack('fff', line)

                for c in range(img_chanels):
                    data[y][x][c] = values[c]

                # skip new line
                f.read(1)

        f.close()

        self.shape = data.shape
        self.comments = comments
        self.data = data

    def __clamp(self, n, smallest, largest):
        """[clamp number using two numbers]
        
        Arguments:
            n {[float]} -- [the number to clamp]
            smallest {[float]} -- [the smallest number interval]
            largest {[float]} -- [the larget number interval]
        
        Returns:
            [float] -- [the clamped value]
        """
        return max(smallest, min(n, largest))

    def __gamma_correct(self, value):
        """[correct gamma of luminance value]
        
        Arguments:
            value {[float]} -- [luminance value to correct]
        
        Returns:
            [float] -- [correct value with specific gamma]
        """
        if value <= 0.0031308:
            return 12.92 * value
        else:
            return 1.055 * math.pow(value, float(1. / 2.4)) - 0.055

    def __gamma_convert(self, value):
        """[correct gamma value and clamp it]
        
        Arguments:
            value {[float]} -- [luminance value to correct and clamp]
        
        Returns:
            [float] -- [final chanel value]
        """
        return self.__clamp(255. * self.__gamma_correct(value) + 0., 0., 255.)

    def gammaConvert(self):
        """[convert gamma of luminance chanel values of rawls image]
        
        Returns:
            [buffer] -- [image buffer with converted gamma values]
        """

        height, width, chanels = self.shape

        output = np.empty((height, width, chanels))

        for y in range(height):
            for x in range(width):
                for c in range(chanels):
                    output[y][x][c] = self.__gamma_convert(self.data[y][x][c])

        return output
