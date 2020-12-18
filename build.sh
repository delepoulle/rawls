#! bin/bash

# Format code
echo "Use of yapf package to format code.."
#yapf -ir -vv rawls

# Build rawls package
echo "Build package..."
python setup.py build

echo "Build documentation..."
rm -r docs/source/rawls
cd docs && make clean && make html