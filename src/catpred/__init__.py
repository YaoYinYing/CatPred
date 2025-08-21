"""CatPred package.

The top-level package previously re-exported :class:`catpred.runner.InferenceRunner`
on import which in turn pulled in a large portion of the training stack and could
trigger circular imports.  Only the version metadata is now resolved eagerly;
consumers should import :class:`InferenceRunner` from :mod:`catpred.runner`
directly when needed.
"""

from importlib import metadata

try:  # pragma: no cover - version retrieval
    __version__ = metadata.version("catpred")
except metadata.PackageNotFoundError:  # pragma: no cover
    __version__ = "0.0.0"

__all__: list[str] = []
