# oxmol

[![Documentation Status](https://readthedocs.org/projects/oxmol/badge/?version=latest)](https://oxmol.readthedocs.io/en/latest/?badge=latest)

`oxmol` is a Python wrapper, written using [PyO3](https://github.com/PyO3/pyo3), for the [minimal molecule implemented in Rust by Rich Apodaca](https://github.com/rapodaca/chemcore). This follows the 'minimal molecule API' [outlined by Apodaca in a blog post](https://depth-first.com/articles/2020/04/06/a-minimal-molecule-api/). Due to the PyO3 dependency, nightly Rust is required.

This package is currently a work in progress, it is missing some of the following key pieces:

- A fully-geatured SMILES parser/writer ([this work is in progress, but hasn't yet made it into oxmol](https://depth-first.com/articles/2020/05/25/lets-build-a-smiles-parser-in-rust/))
- Substructure matching
- Coordinate representations and embedding
- Descriptor generation

These will be expanded upon in future versions. At present, molecules can be instantiated and their 'minimal molecule' functionality works.

The API is not yet guaranteed to be stable, and is likely to break between releases.

## Installation

[The installation instructions can be found in the docs](https://oxmol.readthedocs.io/en/latest/installation.html). These cover installation of binaries and building from source.

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
