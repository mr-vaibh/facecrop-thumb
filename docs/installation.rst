Installation
============

You can install facecrop-thumb using pip, the Python package manager. It is recommended to install facecrop-thumb within a virtual environment to avoid potential conflicts with other Python packages.

Prerequisites
-------------

Before installing facecrop-thumb, make sure you have Python and pip installed on your system. You can download Python from the [official Python website](https://www.python.org/downloads/).

Installation Steps
------------------

1. **Create a Virtual Environment**: Although optional, it's recommended to create a virtual environment to isolate the installation of facecrop-thumb. You can create a virtual environment using the following command:

   .. code-block:: shell

      python -m venv myenv

   Replace `myenv` with the name you prefer for your virtual environment.

2. **Activate the Virtual Environment**: Activate the virtual environment by running the appropriate command based on your operating system:

   - On Windows:

     .. code-block:: shell

        myenv\Scripts\activate

   - On Unix or MacOS:

     .. code-block:: shell

        source myenv/bin/activate

3. **Install facecrop-thumb**: Once the virtual environment is activated, you can install facecrop-thumb using pip:

   .. code-block:: shell

      pip install facecrop-thumb

   This will download and install the latest version of facecrop-thumb along with its dependencies.

4. **Verify Installation**: To verify that facecrop-thumb has been installed successfully, you can run the following command:

   .. code-block:: shell

      facecrop-thumb --version

   If installed correctly, this command should display the installed version of facecrop-thumb.

Congratulations! You have successfully installed facecrop-thumb on your system. You're now ready to start generating thumbnails of detected faces in images.
