Description
=====================================

.. image:: _static/rawls_logo.png
   :width: 350 px
   :align: center
   
Installation
------------

Just install package using pip 

.. code:: bash
   
   pip install rawls


How to use ?
------------

To use, simply do :

.. code:: python
    
    from rawls.classes.rawls import Rawls
    path = 'images/example.rawls'
    rawls_img = Rawls.fromfile(path)
    rawls_img.to_png('output.png')
