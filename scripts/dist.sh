#!/bin/bash
echo "start to build..."
python setup.py sdist bdist_wheel
echo "build finished."

echo "start to upload to pypi..."
twine upload dist/*
echo "upload finished."
