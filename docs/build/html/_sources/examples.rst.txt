Examples
=====================================

Some examples are already available into documentation. You can find here some others and results of use of `rawls` package.

Processing example
--------------------

Read and save `.rawls` file:

.. code:: python
    
    from rawls.rawls import Rawls
    path = 'images/example_1.rawls'
    rawls_img = Rawls.load(path)
    rawls_img.to_png('output.png')

.. image:: _static/output.png
   :width: 120 px
   :align: center


Display rendering information:

.. code:: python
    
    from rawls.rawls import Rawls
    path = 'images/example_1.rawls'
    rawls_img = Rawls.load(path)
    print(rawls_img)

.. code:: bash

    --------------------------------------------------------
    Shape: 
            (100, 100, 3)
    Details: 
            Samples: 1000
            Filter: default
            Resolution: `image`
                    - [integer] xresolution: 100
                    - [integer] yresolution: 100
                    - [string] filename: p3d_bathroom.rawls
            Sampler: `random`
                    - [integer] pixelsamples: 64
            Accelerator: default
            Integrator: `path`
                    - [integer] maxdepth: 65
            Camera: `perspective`
                    - [float] fov: 55
                    - [float] focaldistance: 31
                    - [float] lensradius: 0.15000001
            LookAt: 
                    - eye: (0.0, 18.0, 30.0) 
                    - point: (10.2, 5.0, 0.0) 
                    - up: (0.0, 1.0, 0.0)
    Gamma converted: 
            False
    --------------------------------------------------------

Statistics extraction
---------------------

Extract statistics from multiples `.rawls` samples files:

.. code:: python

    from rawls.rawls import Rawls
    from rawls.stats import RawlsStats
    path_list = ['images/example_1.rawls', 'images/example_2.rawls']
    rawls_stats = RawlsStats.load(path_list)
    print(rawls_stats)

.. code:: bash

    --------------------------------------------------------
    nelements: 
        2
    Details: 
        Samples: 2000
        Filter: default
        Resolution: `image`
            - [integer] xresolution: 100
            - [integer] yresolution: 100
            - [string] filename: p3d_bathroom.rawls
        Sampler: `random`
            - [integer] pixelsamples: 64
        Accelerator: default
        Integrator: `path`
            - [integer] maxdepth: 65
        Camera: `perspective`
            - [float] fov: 55
            - [float] focaldistance: 31
            - [float] lensradius: 0.15000001
        LookAt: 
            - eye: (0.0, 18.0, 30.0) 
            - point: (10.2, 5.0, 0.0) 
            - up: (0.0, 1.0, 0.0)
    Mean samples per element: 
        1000.0
    Expected shape: 
        (100, 100, 3)
    --------------------------------------------------------

.. code:: python

    rawls_mean = rawls_stats.mean()
    rawls_mean.save('output_mean.png')

.. image:: _static/output_mean.png
   :width: 120 px
   :align: center


Store additionals data
----------------------

Add additionals comments into `.rawls` file before saving:

.. code:: python

    rawls_img = Rawls.load('images/example_1.rawls')
    rawls_img.add_comment('SceneVersion', 'v1.0.1')
    print(rawls_img)

.. code:: bash

    --------------------------------------------------------
    Shape: 
            (100, 100, 3)
    Details: 
            Samples: 1000
            Filter: default
            Film: `image`
                    - [integer] xresolution: 100
                    - [integer] yresolution: 100
                    - [string] filename: p3d_bathroom.rawls
            Sampler: `random`
                    - [integer] pixelsamples: 64
            Accelerator: default
            Integrator: `path`
                    - [integer] maxdepth: 65
            Camera: `perspective`
                    - [float] fov: 55
                    - [float] focaldistance: 31
                    - [float] lensradius: 0.15000001
            LookAt: 
                    - eye: (0.0, 18.0, 30.0) 
                    - point: (10.2, 5.0, 0.0) 
                    - up: (0.0, 1.0, 0.0)
    Additionnals:
            SceneVersion: v1.0.1
    Gamma converted: 
            False
    --------------------------------------------------------

.. code:: python

    rawls_img.save('images/example_additionals.rawls')