"""Sphinx configuration for CatPred."""

from __future__ import annotations

import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.abspath("../src"))

project = "CatPred"
author = "CatPred Developers"
current_year = datetime.utcnow().year
copyright = f"{current_year}, CatPred"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "myst_parser",
]

autodoc_typehints = "description"
html_theme = "furo"
