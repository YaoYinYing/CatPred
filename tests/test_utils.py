import os
from pathlib import Path

import pytest

from catpred.utils import makedirs


@pytest.mark.parametrize("isfile", [False, True])
def test_makedirs(tmp_path, isfile):
    target = tmp_path / ("file.txt" if isfile else "dir")
    makedirs(str(target), isfile=isfile)
    path = target.parent if isfile else target
    assert path.exists()
