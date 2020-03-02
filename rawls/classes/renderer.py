# main imports
import re

# class imports
from .sampler import Sampler
from .integrator import Integrator
from .camera import Camera
from .resolution import Resolution
from .lookAt import LookAt
from .vector import Vector3f


class Renderer():
    """Rawls renderer information

    Attributes:
            resolution: {Resolution} -- x and y resolution of image
            sampler: {Sampler} -- sampler instance with information
            integrator: {Integrator} -- integrator instance with information
            camera: {Camera} -- camera instance with information
            lookAt: {LookAt} -- look at instance with eye, point and up vector
    """

    def __init__(self, resolution, samples, sampler, integrator, camera,
                 lookAt):
        """Renderer information used to rendering current image
        
        Arguments:
            resolution: {Resolution} -- x and y resolution of image
            sampler: {Sampler} -- sampler instance with information
            integrator: {Integrator} -- integrator instance with information
            camera {Camera} -- camera instance with information
            lookAt {LookAt} -- look at instance with eye, point and up information
        """
        self.resolution = resolution
        self.integrator = integrator
        self.sampler = sampler
        self.camera = camera
        self.lookAt = lookAt

    @classmethod
    def fromcomments(self, comments):
        """Instanciate Renderer object with all comments information
        
        Arguments:
            comments: {str} -- extracted comments data

        Returns:
            {Renderer} -- renderer information instance
        """
        comments_line = comments.split('\n')

        samples = None
        for index, line in enumerate(comments_line):

            if 'Film' in line:
                res = re.findall(r'\[\d*', comments_line[index + 1])
                del res[-1]  # remove name of outfile
                resolution = [int(r.replace('[', '')) for r in res]
                resolution = Resolution(resolution[0], resolution[1])

            if 'Samples' in line:
                samples = int(line.split(' ')[-1])

            if 'Sampler' in line:
                sampler_name = line.split(' ')[-1]

                if samples is None:
                    res = re.findall(r'\[\d*', comments_line[index + 1])
                    pixelsamples = int(res[0].replace('[', ''))
                    sampler = Sampler(sampler_name, pixelsamples)
                else:
                    sampler = Sampler(sampler_name, samples)

            if 'Integrator' in line:
                integrator_name = line.split(' ')[-1]
                res = re.findall(r'\[\d*', comments_line[index + 1])
                maxdepth = int(res[0].replace('[', ''))
                integrator = Integrator(integrator_name, maxdepth)

            if 'Camera' in line:
                camera_name = line.split(' ')[-1]
                res = re.findall(r'\[\d*', comments_line[index + 1])
                parsed_res = [float(r.replace('[', '')) for r in res]
                camera = Camera(camera_name, parsed_res[0], parsed_res[1],
                                parsed_res[2])

            if 'LookAt' in line:
                info = line.split()
                del info[0]
                info = [float(i) for i in info]

                eye = Vector3f(info[0], info[1], info[2])
                point = Vector3f(info[3], info[4], info[5])
                up = Vector3f(info[6], info[7], info[8])

                lookAt = LookAt(eye, point, up)

        return Renderer(resolution, samples, sampler, integrator, camera,
                        lookAt)

    def __str__(self):
        """Display Renderer object representation
        
        Returns:
            {str} -- renderer information
        """
        return '{0}\n{1}\n{2}\n{3}\n{4}'.format(self.resolution, self.sampler,
                                                self.integrator, self.camera,
                                                self.lookAt)
