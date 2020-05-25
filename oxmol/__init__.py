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
# All this because mocking it's not possible to mock
# submodules in Sphinx...
import os
d, f = os.path.split(__file__)
# The fake Python submodule we make for building docs.
fake_py = os.path.join(d, 'oxmol.py')
if os.path.exists(fake_py):
    os.remove(fake_py)

__version__ = "0.1.0"

from oxmol.element import Element
from oxmol.parity import Parity
from oxmol.bond_order import BondOrder
from oxmol.spec import AtomSpec, BondSpec
from oxmol.molecule import Molecule
