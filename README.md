# oxmol

[![Documentation Status](https://readthedocs.org/projects/oxmol/badge/?version=latest)](https://oxmol.readthedocs.io/en/latest/?badge=latest)

`oxmol` is a Python wrapper, written using [PyO3](https://github.com/PyO3/pyo3), for the [minimal molecule](https://github.com/rapodaca/molecule.rs) implemented in Rust by Rich Apodaca. This follows the 'minimal molecule API' [outlined by Apodaca in a blog post](https://depth-first.com/articles/2020/04/06/a-minimal-molecule-api/). Due to the PyO3 dependency, nightly Rust is required.

This package is currently a work in progress, it is missing some of the following key pieces:

- A SMILES parser/writer ([this is being worked on](https://depth-first.com/articles/2020/05/25/lets-build-a-smiles-parser-in-rust/))
- Substructure matching
- Coordinate representations and embedding
- Descriptor generation

These will be expanded upon in future versions.

## Building

[The installation instructions can be found in the docs](https://oxmol.readthedocs.io/en/latest/installation.html)

## Example Usage

```python
from oxmol import AtomSpec, BondSpec, Molecule

C, H, O = AtomSpec('C'), AtomSpec('H'), AtomSpec('O')
atoms = [C, O, H, H, H, H]

bond_indices = [(0, 1), (1, 2), (0, 3), (0, 4), (0, 5)]
bonds = [BondSpec(sid, tid, 1) for (sid, tid) in bond_indices]

mol = Molecule(atoms, bonds)
print(mol)
# PyMolecule with 6 atoms and 5 bonds.

for (sid, tid) in mol.edges:
    print(mol.element(sid), mol.element(tid))
    print(mol.bond_order(sid, tid))
# PyElement::C Element::O
# PyBondOrder::Single
# PyElement::O Element::H
# PyBondOrder::Single
# PyElement::C Element::H
# PyBondOrder::Single
# PyElement::C Element::H
# PyBondOrder::Single
# PyElement::C Element::H
# PyBondOrder::Single
```
