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