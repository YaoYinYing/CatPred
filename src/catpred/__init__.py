"""CatPred package."""

from importlib import metadata

from catpred.runner import InferenceRunner

__all__ = ["InferenceRunner"]

try:  # pragma: no cover - version retrieval
    __version__ = metadata.version("catpred")
except metadata.PackageNotFoundError:  # pragma: no cover
    __version__ = "0.0.0"
