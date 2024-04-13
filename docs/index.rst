FaceCropThumb
=============

.. image:: https://img.shields.io/pypi/v/facecrop-thumb.svg
    :target: https://pypi.org/project/facecrop-thumb/
    :alt: PyPI Version

.. image:: https://img.shields.io/pypi/pyversions/facecrop-thumb.svg
    :target: https://pypi.org/project/facecrop-thumb/
    :alt: Python Versions

.. image:: https://img.shields.io/github/license/mr-vaibh/facecrop-thumb.svg
    :target: https://github.com/mr-vaibh/facecrop-thumb/blob/main/LICENSE
    :alt: License

.. image:: https://img.shields.io/pypi/dm/facecrop-thumb
   :target: https://pypistats.org/packages/facecrop-thumb
   :alt: PyPI - Downloads


Overview
--------

FaceCropThumb is a Python package for generating thumbnails of detected
faces in images. It utilizes the MTCNN (Multi-Task Cascaded
Convolutional Neural Network) for accurate face detection and OpenCV for
image processing.

.. include:: contents.rst

Features
--------

-  Detect faces in images using the MTCNN model
-  Crop detected faces with a configurable margin
-  Generate square thumbnails of detected faces
-  Option to resize the entire image if no face is detected or face
   detection is skipped
-  Command-line utility for easy usage

Quick Installation
------------------

You can install FaceCropThumb via pip:

``pip install facecropthumb``

Quick Usage
-----------

``facecropthumb <image_path> [-d/--dir <output_directory>] [-m/--margin <margin_size>] [-F/--no-face] [-S/--skip-face]``

-  ``<image_path>``: Path to the input image file.
-  ``-d/--dir <output_directory>``: Directory to store the output
   thumbnail. Default is the current directory.
-  ``-m/--margin <margin_size>``: Margin around the detected face.
   Default is 50 pixels.
-  ``-F/--no-face``: Skip face detection and resize the whole image if
   no face is detected.
-  ``-S/--skip-face``: Skip face detection and resize the whole image.
-  ``-v/--version``: Show installed version.
-  ``-h/--help``: Show help.

Example:

``facecropthumb input_image.jpg -d output_directory -m 30 -F``

This command will generate a thumbnail of the detected face in
``input_image.jpg``, with a margin of 30 pixels, and if no face is
detected, it will resize the whole image to a square of 74 x Y pixels
(~approx).

License
-------

This project is licensed under the MIT License - see the
`LICENSE <LICENSE>`__ file for details.

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`