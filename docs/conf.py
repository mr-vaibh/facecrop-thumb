import os
import sys

# Add the project directory to the Python path
sys.path.insert(0, os.path.abspath('../..'))

# -- Project information -----------------------------------------------------

project = 'facecrop-thumb'
author = 'Vaibhav Shukla'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',      # Generate documentation from docstrings
    'sphinx.ext.viewcode',     # Add links to source code
    'sphinx.ext.napoleon',     # Support for Google and NumPy style docstrings
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'  # Choose a theme (e.g., 'sphinx_rtd_theme' for Read the Docs)

html_static_path = ['_static']

# -- Extension configuration -------------------------------------------------

# Add any additional configurations for extensions here

# -- Autodoc configuration ---------------------------------------------------

autodoc_member_order = 'bysource'  # Order members by source order
autodoc_default_options = {
    'members': True,              # Document class members
    'undoc-members': True,        # Document members with no docstring
    'show-inheritance': True,     # Show inheritance diagrams
}

# -- Napoleon extension configuration ----------------------------------------

napoleon_google_docstring = False  # Set to True if using Google style docstrings
napoleon_numpy_docstring = True     # Set to True if using NumPy style docstrings

# -- Other configurations ----------------------------------------------------

# Add any other custom configurations here
