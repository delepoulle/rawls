Description
=====================================

.. image:: _static/rawls_logo.png
   :width: 350 px
   :align: center


Context
------------

Global illumination methods based on stochastic techniques provide photo-realistic images. These methods are generally based on path tracing theory in which stochastic paths are generated from the camera point of view through each pixel toward the 3D scene. 

.. image:: _static/path_tracing.png
   :width: 450 px
   :align: center


The Monte Carlo theory based on the Kajiya rendering equation ensures that this process will converge to the correct image when the number of paths grows. However, they are prone to stochastic perceptual noise that can be reduced by increasing the number of paths as proved by Monte Carlo theory but requires a lot of time to generate such image.

.. image:: _static/noise_overview.png
   :width: 550 px
   :align: center


Installation
------------

Just install package using `pip` Python package manager: 

.. code:: bash
   
   pip install rawls


How to use ?
------------

To use, simply do:

.. code:: python
    
    from rawls.rawls import Rawls
    path = 'images/example_1.rawls'
    rawls_img = Rawls.load(path)
    rawls_img.save('output.png')
