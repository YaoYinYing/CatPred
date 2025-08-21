"""High level inference runner for CatPred."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Mapping, Optional, Sequence, List, Tuple

from typing import TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover - typing helpers
    from catpred.args import PredictArgs  # noqa: F401


def load_model(*args, **kwargs):
    """Lazy loader for :func:`catpred.train.make_predictions.load_model`."""
    from catpred.train.make_predictions import load_model as _load_model

    return _load_model(*args, **kwargs)


def make_predictions(*args, **kwargs):
    """Lazy loader for :func:`catpred.train.make_predictions.make_predictions`."""
    from catpred.train.make_predictions import make_predictions as _make_predictions

    return _make_predictions(*args, **kwargs)


class InferenceRunner:
    """Execute inference using pre-trained CatPred models.

    Parameters
    ----------
    config:
        Mapping of configuration options compatible with
        :class:`catpred.args.PredictArgs`.
    n_jobs:
        Number of worker processes for data loading.
    verbose:
        Flag to control verbose output.
    """

    def __init__(self, config: Optional[Mapping] = None, *, n_jobs: int = 1, verbose: bool = False) -> None:
        self.config = dict(config or {})
        self.config.setdefault("num_workers", n_jobs)
        self.verbose = verbose
        self._model_objects: Optional[Tuple] = None

    @classmethod
    def from_config(cls, path: str) -> "InferenceRunner":
        """Create runner from a JSON configuration file."""
        with open(path, "r", encoding="utf8") as fh:
            config = json.load(fh)
        return cls(config)

    def load_model(self, path: str) -> None:
        """Load model checkpoint and prepare for inference."""
        self.config["checkpoint_paths"] = [path]
        self.prepare()

    def prepare(self) -> None:
        """Load model objects based on the current configuration."""
        try:
            from catpred.args import PredictArgs  # type: ignore
        except Exception:  # pragma: no cover - lightweight fallback
            class PredictArgs(dict):
                """Minimal stand-in used when full dependencies are unavailable."""

                def __init__(self, **kwargs):
                    self.__dict__.update(kwargs)

        args = PredictArgs(**self.config)
        self._model_objects = load_model(args, generator=False)

    def run(self, inputs: Sequence[Sequence[str]]) -> List[List[Optional[float]]]:
        """Run inference on a list of SMILES strings.

        Parameters
        ----------
        inputs:
            Sequence of SMILES sequences to evaluate.

        Returns
        -------
        list of list of float or None
            Predicted values for each input.
        """
        if self._model_objects is None:
            self.prepare()
        args = self._model_objects[0]
        return make_predictions(args=args, smiles=list(inputs), model_objects=self._model_objects)

    def save_results(self, outputs: Any, path: str) -> None:
        """Persist prediction results to a JSON file."""
        path_obj = Path(path)
        path_obj.parent.mkdir(parents=True, exist_ok=True)
        with path_obj.open("w", encoding="utf8") as fh:
            json.dump(outputs, fh)
