import os
import sys

sys.path.insert(0, os.path.abspath("../../dynamic_model/"))
sys.path.insert(0, os.path.abspath("../../GroupExperiment/"))
# sys.path.insert(0, os.path.abspath('../../dynamic_model'))
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

extensions = [
    "sphinx.ext.autodoc",  # Core autodoc
    "sphinx.ext.napoleon",  # Enable Google/NumPy style parsing
    "sphinx.ext.viewcode",  # Add source links
    "sphinx.ext.intersphinx",  # Cross-reference other projects
    "sphinx_autodoc_typehints",  # Render type hints nicely
]

# -- Napoleon settings -------------------------------------------------------
# Enable Google-style docstring parsing
napoleon_google_docstring = True
napoleon_numpy_docstring = False  # Disable NumPy style if you only want Google
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_use_keyword = True
napoleon_custom_sections = ["Returns", "Examples", "Notes", "See Also"]

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ["_templates"]
exclude_patterns = []

language = "english"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
