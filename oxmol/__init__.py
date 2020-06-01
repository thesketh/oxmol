"""
``oxmol`` is a Python wrapper, written using PyO3_, for `ChemCore, a
cheminformatics library implemented in Rust by Rich Apodaca`__. This
follows the 'minimal molecule API' `outlined by Apodaca in a blog
post`__.

This package is currently a work in progress, it is missing some of the
following key pieces:

- A fully-featured SMILES parser (`this is being worked on, but isn't \
yet in oxmol`__)
- Substructure matching
- Coordinate representations and embedding
- Descriptor generation

These will be expanded upon in future versions. At present, molecules
can be instantiated and their 'minimal molecule' functionality works.

.. _PyO3: https://pyo3.rs
__ https://github.com/rapodaca/chemcore
__ https://depth-first.com/articles/2020/04/06/a-minimal-molecule-api/
__ https://depth-first.com/articles/2020/05/25/lets-build-a-smiles-parser-in-rust/

"""
# All this because it's not possible to mock subpackages in Sphinx...
import os as _os
_d, _ = _os.path.split(__file__)
# The fake Python submodule we make to build the docs.
_fake_py = _os.path.join(_d, 'oxmol.py')
if _os.path.exists(_fake_py):
    for _f in _os.listdir(_d):
        # If the real oxmol lib is there, remove the fake one
        _filename, _ext = _os.path.splitext(_f)
        if _filename.startswith('oxmol') and _ext == "so":
            _os.remove(_fake_py)
#####

__version__ = "0.1.0"

from oxmol.element import Element
from oxmol.parity import Parity
from oxmol.bond_order import BondOrder
from oxmol.spec import AtomSpec, BondSpec
from oxmol.molecule import Molecule
