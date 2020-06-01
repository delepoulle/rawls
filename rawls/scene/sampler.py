from .params import Params

class Sampler(Params):
    """Sampler class which store Sampler information    
    """

    def __init__(self, name, params_names, params_values, params_types):
        """Construct sampler with all information
        
        Arguments:
            name: {str} -- name of the kind module used
            params_name: [{str}] -- parameters names of sampler used
            params_values: [{str}] -- parameters values of sampler used
            params_types: [{str}] -- parameters values of sampler used
        """
        self.module = "Sampler"
        self.name = name
        self.params_names = params_names
        self.params_values = params_values
        self.params_types = params_types
