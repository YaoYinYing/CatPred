"""Shared test fixtures."""

import pytest


class DummyDataset:
    """Minimal dataset providing atom and bond counts."""

    def __init__(self, atoms, bonds):
        self.number_of_atoms = atoms
        self.number_of_bonds = bonds

    def __len__(self):  # pragma: no cover - trivial
        return len(self.number_of_atoms)


@pytest.fixture
def dataset_factory():
    """Factory returning a :class:`DummyDataset`."""
    def factory(atoms, bonds):
        return DummyDataset(atoms, bonds)
    return factory
