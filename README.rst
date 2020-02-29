RAW Light Simulation reader/converter package
=====================================

Installation
------------

```bash
pip install rawls
```

How to use ?
------------

To use, simply do :

.. code:: python

   from PIL import Image
   from ipfml.processing import transform
   img = Image.open('path/to/image.png')
   s = transform.get_LAB_L_SVD_s(img)


Modules
-------

This project contains modules.

- **reader** : *Reader functions which enables to read and load `.rawls` image file*
- **converter** : *Converter functions in order to convert image into another*

All these modules will be enhanced during development of the package.

Documentation
-------------

For more information about package, documentation_ is available.

.. _documentation: https://prise-3d.github.io/ipfml/

Contributing
------------

Please refer to the guidelines_ file if you want to contribute!

.. _guidelines: https://github.com/prise-3d/ipfml/blob/master/CONTRIBUTING.md 
