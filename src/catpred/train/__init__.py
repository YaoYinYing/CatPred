"""Training utilities for :mod:`catpred`.

The previous version of this module eagerly imported a large collection of
functions and exposed them via ``__all__``.  Besides inflating import time, this
pattern introduced circular dependencies between modules.  The package now
provides a minimal namespace; import training helpers directly from the relevant
submodules, e.g. ``from catpred.train.make_predictions import make_predictions``.
"""

__all__: list[str] = []
