from setuptools import setup
import setuptools.command.build_py

def readme():
    with open('README.rst') as f:
        return f.read()

class BuildTestCommand(setuptools.command.build_py.build_py):
    """Custom build command."""

    def run(self):

        # run tests using doctest
        import doctest
        
        # filters folder
        from rawls import converter
        from rawls import reader

        print("==============================")
        print("Runs test command...")

        # pass test using doctest
        doctest.testmod(converter)
        doctest.testmod(reader)

        setuptools.command.build_py.build_py.run(self)


setup(
    name='rawls',
    version='0.0.1',
    description='RAW Light Simulation file reader/converter package',
    long_description=readme(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Utilities'
    ],
    url='https://github.com/prise-3d/ipfml',
    author='Jérôme BUISINE',
    author_email='jerome.buisine@univ-littoral.fr',
    license='MIT',
    packages=['rawls', 'rawls.converter', 'rawls.reader'],
    install_requires=[
        'numpy',
        'Pillow',
    ],
    cmdclass={
        'build_py': BuildTestCommand,
    },
    zip_safe=False)
