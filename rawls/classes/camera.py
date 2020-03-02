class Camera():
    """Camera class which store camera information

    Attributes:
        name: {str} -- name of the camera
        fov: {float} -- field of view information
        focaldistance: {float} -- focal distance of camera
        lensradius: {float} -- lens radius of camera
    """

    def __init__(self, name, fov, focaldistance, lensradius):
        """Construct camera with all information
        
        Arguments:
            name: {str} -- name of the camera
            fov: {float} -- field of view information
            focaldistance: {float} -- focal distance information
            lensradius: {float} -- lens radius information
        """
        self.name = name
        self.fov = float(fov)
        self.focaldistance = float(focaldistance)
        self.lensradius = float(lensradius)

    def __str__(self):
        """Display Camera information
        
        Returns:
            {str} -- camera information
        """
        return "Camera: `{0}`, (fov: {1}, focaldistance: {2}, lensradius: {3})".format(
            self.name, self.fov, self.focaldistance, self.lensradius)
