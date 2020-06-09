.. rawls documentation master file, created by
   sphinx-quickstart on Fri Jan  4 12:10:59 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

RAW Light Simulation image file
=====================================

.. image:: _static/rawls_logo.png
   :width: 450 px
   :align: center

What's `rawls` ?
=================

Global illumination methods based on stochastic techniques provide photo-realistic images. These methods are generally based on path tracing theory in which stochastic paths are generated from the camera point of view through each pixel toward the 3D scene. 

.. image:: _static/path_tracing.png
   :width: 450 px
   :align: center

`rawls` is a Python package developed during a thesis project. It enables to manage `.rawls` image file extension. The image extension `.rawls` is used to store all samples values of images obtained during rendering of synthesis images. 
This output extension is available in a custom version of pbrt-v3_ details.

.. _pbrt-v3: https://github.com/prise-3d/pbrt-v3

.. toctree::
   :maxdepth: 1
   :caption: Contents:

   description
   rawls
   examples
   contributing

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
