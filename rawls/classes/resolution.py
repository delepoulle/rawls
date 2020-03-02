class Resolution():
    """Resolution screen information class
    
    Attributes:
        x: {int} -- x resolution
        y: {int} -- y resolution
    """

    def __init__(self, x, y):
        """Resolution construction with `x` and `y` information
        
        Arguments:
            x: {int} -- x resolution
            y: {int} -- y resolution
        """
        self.x = x
        self.y = y

    def __str__(self):
        """Display Resolution object representation
        
        Returns:
            {str} -- Resolution information
        """
        return "Resolution: {0} x {1}".format(self.x, self.y)