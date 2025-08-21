import numpy as np
import pytest

from catpred.multitask_utils import reshape_values


@pytest.mark.parametrize(
    "atoms,bonds,values,natom,nbond,expected",
    [
        (
            [[1], [2]],
            [[0], [0]],
            [np.array([[1], [2], [3]])],
            1,
            0,
            [[[1]], [[2, 3]]],
        ),
        (
            [[2], [1]],
            [[1], [1]],
            [np.array([[1], [2], [3]]), np.array([[4], [5]])],
            1,
            1,
            [[[1, 2], [4]], [[3], [5]]],
        ),
    ],
)
def test_reshape_values(dataset_factory, atoms, bonds, values, natom, nbond, expected):
    dataset = dataset_factory(atoms, bonds)
    result = reshape_values(values, dataset, natom, nbond, natom + nbond)
    converted = [[list(v) for v in row] for row in result]
    assert converted == expected
