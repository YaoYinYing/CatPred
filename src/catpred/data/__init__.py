"""Data handling utilities for :mod:`catpred`.

Historically this module re-exported many helpers to simplify imports.  Those
implicit imports triggered circular dependencies and loaded heavy third-party
packages on initialization.  The namespace is now kept intentionally light;
consumers should import required utilities from their dedicated submodules, e.g.
``from catpred.data.data import MoleculeDataset``.
"""

__all__: list[str] = []
