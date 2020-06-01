from .params import Params

class Camera(Params):
    """Camera class which store Camera information    
    """

    def __init__(self, name, params_names, params_values, params_types):
        """Construct camera with all information
        
        Arguments:
            name: {str} -- name of the kind module used
            params_name: [{str}] -- parameters names of camera used
            params_values: [{str}] -- parameters values of camera used
            params_types: [{str}] -- parameters values of camera used
        """
        self.module = "Camera"
        self.name = name
        self.params_names = params_names
        self.params_values = params_values
        self.params_types = params_types
