Examples
=====================================

Some examples are already available into documentation. You can find here some others and results of use of `rawls` package.

All examples below will use this picture.

Processing example
--------------------

.. code:: python
    
    from rawls.classes.rawls import Rawls
    path = 'images/example.rawls'
    rawls_img = Rawls.fromfile(path)
    rawls_img.to_png('output.png')

