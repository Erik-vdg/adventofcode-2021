"""Sphinx configuration."""
from datetime import datetime


project = "Avent of Code 2021 - Python"
author = "Erik van der Goetz"
copyright = f"{datetime.now().year}, {author}"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "sphinx_rtd_theme",
]
autodoc_typehints = "description"
html_theme = "sphinx_rtd_theme"
