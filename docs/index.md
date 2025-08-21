# CatPred

Welcome to the CatPred documentation.

```{toctree}
:maxdepth: 2

api/catpred
```

## Quickstart

```python
from catpred import InferenceRunner

runner = InferenceRunner({"checkpoint_paths": ["model.pt"]})
# runner.prepare()  # load model
# predictions = runner.run([["CC"]])
```
