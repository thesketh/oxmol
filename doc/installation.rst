Installation
============

Binary Releases
---------------

``oxmol`` is currently available on test PyPI whilst development is
likely to be erratic and API-breaking. Wheels have been compiled for the
following versions of Python:

- Python 3.6
- Python 3.7
- Python 3.8
- PyPy 7.3 (implementing Python 3.6)

These have been compiled against Linux, macOS and Windows, and are not
guaranteed to be bug free. These can be installed using the following command 
(with some exceptions for PyPy below):

.. code-block:: bash

    pip install --index-url https://test.pypi.org/simple/ oxmol

PyPy wheels for Linux currently aren't compatible with the ``manylinux`` tag, 
so these will have to be downloaded from the github releases and installed:

.. code-block:: bash

    RELEASE="oxmol-0.1.0-pp36-pypy36_pp73-linux_x86_64.whl"
    curl "https://github.com/thesketh/oxmol/releases/download/v0.1.0/${RELEASE}" --output "${RELEASE}"
    pip install "${RELEASE}"

PyPy doesn't currently support 64-bit Windows, so no Windows PyPy wheels are provided.

Compiling From Source 
---------------------

Toolchain
^^^^^^^^^
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
^^^^^^^^^^^^
The Rust component of ``oxmol`` depends upon ``pyo3``, ``molecule`` and 
``gamma`` (a graph library) but these should be automatically fetched by Cargo 
when compiling so there are no dependencies to install manually.

Compiling Against Python
^^^^^^^^^^^^^^^^^^^^^^^^
Clone the repo using git and move into the root folder:

.. code-block:: bash
   
    git clone https://github.com/thesketh/oxmol
    cd oxmol

Execute the following command from the root of the repo.

.. code-block:: bash
    
    maturin build --release

Maturin will compile the Rust component of the library and create a Python
wheel containing the Rust and Python components, which are placed in 
``./target/wheels``.

As Maturin will compile a wheel for each interpreter it finds (e.g. the
system Python and the interpreter from a Conda environment), there may be 
multiple versions. You will have to install the version most relevant to 
your version of Python (e.g. ``oxmol-0.1.0-cp36...`` for Python 3.6 and
``oxmol-0.1.0-cp37...`` for Python 3.7). The full name of the file
will vary depending on your platform.

cd into ``./target/wheels`` and use pip to install the most relevant wheel

.. code-block:: bash 

    cd ./target/wheels
    # Update the following command with the most relevant version.
    pip install ./oxmol-0.1.0-cp37-cp37m-manylinux1_x86_64.whl

You should now be ready to start using ``oxmol``. If you are interested in 
compiling against a specific version of Python, you can specify the path
to the interetreter using the ``-i`` flag for Maturin:

.. code-block:: bash

    maturin build -i $(which python3) --release

For information about other flags, use the Maturin_ docs.

Compiling Against PyPy
^^^^^^^^^^^^^^^^^^^^^^

This is mostly the same as the process for Python.

The latest version of PyPy changed the ABI string format and Maturin hasn't 
yet been updated, so you may have to rename the wheel file.

To compile oxmol against PyPy3, use the ``-i`` flag for Maturin:

.. code-block:: bash

    maturin build -i $(which pypy3) --release
    cd target/wheels

If you're using PyPy3 version >= 7.3.1 (where ``SYSTEM`` is e.g. ``linux_x86_64``):

.. code-block:: bash 

    mv oxmol-0.1.0-pp3pp73-pypy3_pp73-SYSTEM.whl oxmol-0.1.0-pp36-pypy36_pp73-SYSTEM.whl

Install using PyPy's pip:

.. code-block:: bash 

    pypy3 -m pip install oxmol-0.1.0-pp36-pypy36_pp73-SYSTEM.whl


Testing
-------

To run the tests, use ``pytest``:

.. code-block:: bash

    pip install pytest
    pytest --pyargs oxmol

If these pass, all is well! If not, please post an issue on GitHub.

.. _Maturin: https://github.com/PyO3/maturin
__ https://doc.rust-lang.org/1.2.0/book/nightly-rust.html
__ https://www.rust-lang.org/learn/get-started
