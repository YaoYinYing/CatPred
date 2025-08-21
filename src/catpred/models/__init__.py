"""Model architectures provided by :mod:`catpred`.

The previous implementation eagerly imported many model classes to populate
``__all__``.  That approach introduced circular import problems and pulled in
heavy optional dependencies during package import.  The module now exposes a
lightweight namespace; users should import required classes directly from their
submodules, e.g. ``from catpred.models.mpn import MPN``.
"""

__all__: list[str] = []
