.. oxmol documentation master file, created by
   sphinx-quickstart on Sun May 24 12:53:50 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

oxmol Documentation
===================

|rtd|

.. |rtd| image:: https://readthedocs.org/projects/oxmol/badge/?version=latest
    :target: https://oxmol.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

``oxmol`` is a Python wrapper, written using PyO3_, for the `minimal molecule`__
implemented in Rust by Rich Apodaca. This follows the 'minimal molecule API' 
`outlined by Apodaca in a blog post`__.

This package is currently a work in progress, it is missing some of the following 
key pieces:

- A SMILES parser/writer (`this is being worked on`__)
- Substructure matching
- Coordinate representations and embedding
- Descriptor generation

These will be expanded upon in future versions. At present, molecules can be
instantiated and their 'minimal molecule' functionality works.

`The project's GitHub repository can be found here.`__ New contributors are
welcome. Any bugs or significant frustrations can be reported in the
issue tracker.

.. code-block:: python
    
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
    print(mol)

    # Prints the following:
    #   PyElement::C Element::O
    #   PyBondOrder::Single
    #   PyElement::O Element::H
    #   PyBondOrder::Single
    #   PyElement::C Element::H
    #   PyBondOrder::Single
    #   PyElement::C Element::H
    #   PyBondOrder::Single
    #   PyElement::C Element::H
    #   PyBondOrder::Single
    #   PyMolecule with 6 atoms and 5 bonds.

.. toctree::
   :maxdepth: 3
   :caption: Contents:

   Home <self>
   Installation <installation>
   source/oxmol


.. _PyO3: https://pyo3.rs
__ https://github.com/rapodaca/molecule.rs
__ https://depth-first.com/articles/2020/04/06/a-minimal-molecule-api/
__ https://depth-first.com/articles/2020/05/25/lets-build-a-smiles-parser-in-rust/
__ https://github.com/thesketh/oxmol