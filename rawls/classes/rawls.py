# main imports
import numpy as np


class Rawls():

    def __init__(self):
        self.data = None
        self.comments = None
        self.shape = None    

    def get_comments(self):
        return self.comments

    def set_comments(self, comments):
        self.comments = comments

    def set_data(self, data):
        data = np.array(data)
        self.data = data
        self.data = data.shape

    def get_data(self):
        return self.data