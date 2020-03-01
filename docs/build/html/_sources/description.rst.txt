Description
=====================================

Installation
------------

Just install package using pip 

.. code:: bash
   
   pip install rawls


How to use ?
------------

To use, simply do :

.. code:: python
    
   from rawls.converter import rawls_to_png
   path = 'images/p3d_bathroom-S1-00000.rawls'
   rawls_to_png(path, 'test.png')
