# oxmol

[![Documentation Status](https://readthedocs.org/projects/oxmol/badge/?version=latest)](https://oxmol.readthedocs.io/en/latest/?badge=latest)

`oxmol` is a Python wrapper, written using ![PyO3](https://github.com/PyO3/pyo3), for the ![minimal molecule](https://github.com/rapodaca/molecule.rs) implemented in Rust by Rich Apodaca. This follows the 'minimal molecule API' ![outlined by Apodaca in a blog post](https://depth-first.com/articles/2020/04/06/a-minimal-molecule-api/). Due to the PyO3 dependency, nightly Rust is required.

This package is currently a work in progress, it is missing some of the following key pieces:

- A SMILES parser/writer (![this is being worked on](https://depth-first.com/articles/2020/05/25/lets-build-a-smiles-parser-in-rust/))
- Substructure matching
- Coordinate representations and embedding
- Descriptor generation

These will be expanded upon in future versions.

## Building

1. Ensure that the Rust toolchain is installed
2. Set the nightly compiler as the default (`rustup default nightly`)
3. Ensure that ![Maturin](https://github.com/PyO3/maturin) is intalled (`pip install maturin`)
4. Clone the repo and `cd` into the root.
5. Build the Python wheels (`maturin build --release`)
6. `cd` into `target/wheels`
7. Install the relevant wheel using `pip`. 

## Example Usage

```python
from oxmol import Element, BondOrder, AtomSpec, BondSpec, Molecule

C = Element.from_symbol('C')
O = Element.from_symbol('O')
H = Element.from_symbol('H')

atoms = []
atoms.append(AtomSpec(C, 0))
atoms.append(AtomSpec(O, 0))
atoms.append(AtomSpec(H, 0))
atoms.append(AtomSpec(H, 0))
atoms.append(AtomSpec(H, 0))
atoms.append(AtomSpec(H, 0))

single_bond = BondOrder(1)

bonds = []
bonds.append(BondSpec(0, 1, single_bond))
bonds.append(BondSpec(1, 2, single_bond))
bonds.append(BondSpec(0, 3, single_bond))
bonds.append(BondSpec(0, 4, single_bond))
bonds.append(BondSpec(0, 5, single_bond))

mol = Molecule(atoms, bonds)

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

print(mol)
# PyMolecule with 6 atoms and 5 bonds.
```
