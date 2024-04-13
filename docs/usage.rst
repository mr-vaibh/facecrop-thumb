Usage Guide
===========

This guide will walk you through the basic usage of the FaceCropThumb package.

Generating Thumbnails
----------------------

To generate a thumbnail of the detected face in an image, you can use the ``facecrop-thumb`` command followed by the path to the input image:

.. code-block:: bash

    facecrop-thumb input_image.jpg

By default, FaceCropThumb will detect the face in the input image and generate a thumbnail with the detected face cropped. The resulting thumbnail will be saved in the same directory as the input image.

Customizing Thumbnail Options
------------------------------

You can customize the behavior of FaceCropThumb using various options:

- **Margin Size**: Adjust the margin around the detected face using the ``-m`` or ``--margin`` option. For example:

  .. code-block:: bash

      facecrop-thumb input_image.jpg -m 50

- **Output Directory**: Specify a directory to store the output thumbnail using the ``-d`` or ``--dir`` option. For example:

  .. code-block:: bash

      facecrop-thumb input_image.jpg -d output_directory

- **Skip Face Detection**: You can skip face detection entirely and resize the whole image using the ``-S`` or ``--skip-face`` option. For example:

  .. code-block:: bash

      facecrop-thumb input_image.jpg -S

- **Skip Face Detection if No Face Detected**: You can skip face detection and resize the whole image if no face is detected using the ``-F`` or ``--no-face`` option. For example:

  .. code-block:: bash

      facecrop-thumb input_image.jpg -F

- **Version**: You can check the version of FaceCropThumb using the ``-v`` or ``--version`` option. For example:

  .. code-block:: bash

      facecrop-thumb -v

For more details on available options, you can use the ``--help`` option:

.. code-block:: bash

    facecrop-thumb --help

``facecrop-thumb`` supports various command-line options to customize the face detection and thumbnail generation process.

