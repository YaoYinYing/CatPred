# CatPred

CatPred is a framework for deep learning of in vitro enzyme kinetic parameters.

## Installation

```bash
pip install catpred
```

For development or to run the test suite:

```bash
pip install -e .[test,docs]
```

## Quickstart

```python
from catpred import InferenceRunner

runner = InferenceRunner({"checkpoint_paths": ["model.pt"]})
# runner.prepare()
# preds = runner.run([["CCO"]])
```

See the [examples](example/) directory for sample inputs.
