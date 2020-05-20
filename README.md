Oxmol is a Python wrapper, written using ![pyo3](https://github.com/PyO3/pyo3) for the ![minimal molecule](https://github.com/rapodaca/molecule.rs) implemented in Rust by Rich Apodaca.

This package is currently incomplete and requires nightly Rust to build (due to the pyo3 dependency). DefaultMolecules can be instantiated, but no functionality is implemented yet.

## Example Usage

Ensure liboxmol.so is in the $PYTHONPATH.

```python
from liboxmol import element, bond_order, spec, molecule

C = element.Element.from_symbol('C')
O = element.Element.from_symbol('O')
H = element.Element.from_symbol('H')

atoms = []
atoms.append(spec.AtomSpec(C, 0))
atoms.append(spec.AtomSpec(O, 0))
atoms.append(spec.AtomSpec(H, 0))
atoms.append(spec.AtomSpec(H, 0))
atoms.append(spec.AtomSpec(H, 0))
atoms.append(spec.AtomSpec(H, 0))

single_bond = bond_order.BondOrder(1)

bonds = []
bonds.append(spec.BondSpec(0, 1, single_bond))
bonds.append(spec.BondSpec(1, 2, single_bond))
bonds.append(spec.BondSpec(0, 3, single_bond))
bonds.append(spec.BondSpec(0, 4, single_bond))
bonds.append(spec.BondSpec(0, 5, single_bond))

mol = molecule.DefaultMolecule(atoms, bonds)

for (sid, tid) in mol.edges():
    print(mol.element(sid), mol.element(tid))
    print(mol.bond_order(sid, tid))

# Element::C Element::O
# BondOrder::Single
# Element::O Element::H
# BondOrder::Single
# Element::C Element::H
# BondOrder::Single
# Element::C Element::H
# BondOrder::Single
# Element::C Element::H
# BondOrder::Single

print(mol)
# Something like <DefaultMolecule object at 0x7f9f8f115390>
```
