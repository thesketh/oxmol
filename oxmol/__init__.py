"""
``oxmol`` is a wrapper around ``molcule.rs``, `a Rust cheminformatics
library written by Richard Apodaca.`__ ``oxmol`` is implemented in Rust
(using PyO3) and Python, and is currently in the alpha stage.

``molecule.rs`` is based on a minimal molecule API set out by Apodaca
in the following blog posts:

- `Initial minimial molecule discussion`__
- `Rust implementation of the minimal molecule`__

Future development will likely be discussed on the blog. At present,
there is a useful molecule representation, but some critical
components are currently missing:

- A SMILES parser/writer (`this is being worked on`__)
- Substructure matching
- Coordinate representations and embedding
- Descriptor generation.

These will be expanded upon in future versions.

__ https://github.com/rapodaca/molecule.rs
__ https://depth-first.com/articles/2020/04/06/a-minimal-molecule-api/
__ https://depth-first.com/articles/2020/05/11/cheminformatics-in-rust-implementing-a-minimal-molecule-api/
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
