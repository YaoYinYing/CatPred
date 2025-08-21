import json

import pytest

from catpred.runner import InferenceRunner


@pytest.mark.serial
def test_runner(monkeypatch, tmp_path):
    def fake_load_model(args, generator=False):
        return args, None, [], [], 0, []

    def fake_make_predictions(args, smiles, model_objects):
        return [[0.1] * len(smiles[0])]

    monkeypatch.setattr("catpred.runner.load_model", fake_load_model)
    monkeypatch.setattr("catpred.runner.make_predictions", fake_make_predictions)

    config = {"checkpoint_paths": ["model.pt"]}
    runner = InferenceRunner(config)
    runner.prepare()
    outputs = runner.run([["CC"]])
    assert outputs == [[0.1]]

    out_file = tmp_path / "out.json"
    runner.save_results(outputs, out_file)
    assert json.loads(out_file.read_text()) == [[0.1]]
