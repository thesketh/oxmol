Installation
============

``oxmol`` is currently not listed in any package repos while deployment is 
worked out, but installation from source is fairly easy. Installation has 
only been tested on Linux (Ubuntu 18.04) and with Python 3.7, but should
be possible for any system compatible with PyO3_. This includes Windows,
macOS, Linux and BSD systems and both the Python and PyPy interpreters.

Toolchain
---------
The easiest way to build the Python wheels is to use Maturin_, which can be
installed via pip.

.. code-block:: bash

    pip install maturin

You will also need the `nightly Rust compiler`__. If you have not yet installed
the Rust toolchain, `see the instructions here`__. The nightly compiler can then
be installed and and enabled by running the following two commands:

.. code-block:: bash

    rustup install nightly
    rustup default nightly

To set the default compiler back to stable, run the following command:

.. code-block:: bash

    rustup default stable

If compiling on macOS, you will need to create a a file at ``~/.cargo/config``
with the following contents in order to set the linker options:

.. code-block:: toml

    [target.x86_64-apple-darwin]
    rustflags = [
    "-C", "link-arg=-undefined",
    "-C", "link-arg=dynamic_lookup",
    ]

Dependencies
------------
The Rust component of ``oxmol`` depends upon ``pyo3``, ``molecule`` and 
``gamma`` (a graph library) but these should be automatically fetched by Cargo 
when compiling so there are no dependencies to install manually.

Installation Steps
------------------
Clone the repo using git and move into the root folder:

.. code-block:: bash
   
    git clone https://github.com/thesketh/oxmol
    cd oxmol

Execute the following commands from the root of the repo, where
RELEVANT_VERSION is closest to your Python version:

.. code-block:: bash
    
    maturin build --release
    cd target/wheels
    pip install RELEVANT_VERSION

You should now be ready to start using ``oxmol``. If you are interested in 
compiling against additional versions of Python, the best place to start
is the Maturin_ docs.

.. _Maturin: https://github.com/PyO3/maturin
.. _PyO3: https://pyo3.rs/
__ https://doc.rust-lang.org/1.2.0/book/nightly-rust.html
__ https://www.rust-lang.org/learn/get-started