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

    from rawls.classes.rawls import Rawls
    path = 'images/example.rawls'
    rawls_img = Rawls.fromfile(path)
    rawls_img.to_png('output.png')


Modules
-------

This project contains modules.

- **converter** : *Converter functions in order to convert image into another*
- **merger** : *Merger functions which enables to merge `.rawls` image files*

All these modules will be enhanced during development of the package.

Documentation
-------------

For more information about package, documentation_ is available.

.. _documentation: https://prise-3d.github.io/rawls/

Contributing
------------

Please refer to the guidelines_ file if you want to contribute!

.. _guidelines: https://github.com/prise-3d/rawls/blob/master/CONTRIBUTING.md 
