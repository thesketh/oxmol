"""
Atom and bond specifications, used to construct ``Molecule``

These are thin wrappers around the PyO3 classes: they call their
base class' ``__new__`` constructor and return an instance of the
base class.

At present, it doesn't seem to be possible to actually subclass
PyO3 classes from Python, so this is all we are able to do on the 
Python end.

In the case of these classes, we tweak the constructors a bit to allow
for some limited duck typing (this is harder to do in the PyO3 base
classes).

"""
from typing import Optional, Union, Type, TypeVar
from .oxmol import (
    PyAtomSpec,
    PyBondSpec,
    PyElement,
    PyParity,
    PyBondOrder
)

AS = TypeVar('AS', bound='AtomSpec')
BS = TypeVar('BS', bound='BondSpec')


class AtomSpec(PyAtomSpec):
    """
    An atom specification, used to create a Molecule instance.

    :param element: an ``Element``, ``int`` (atomic number), or\
    ``str`` (element symbol).
    :param hydrogens: an ``int``, the number of implicit hydrogen\
    atoms.
    :param ion: an optional ``int``, the formal charge on the atom.
    :param isotope: an optional ``int``, the isotope of the atom.
    :param parity: an optional ``Parity`` or ``bool``, the chirality.

    *Attributes*
    See Parameters.

    """
    def __new__(
            cls: Type[AS],
            element: Union[PyElement, int, str],
            hydrogens: int = 0,
            ion: int = 0,
            isotope: Optional[int] = None,
            parity: Optional[Union[PyParity, bool]] = None
    ) -> AS:
        if isinstance(element, PyElement):
            pass
        elif isinstance(element, int):
            element = PyElement(element)
        elif isinstance(element, str):
            element = PyElement.from_symbol(element)
        else:
            raise TypeError("Can't convert {} to PyElement".format(element))

        if isinstance(parity, bool):
            parity = PyParity(parity)

        instance = PyAtomSpec.__new__(
            cls,
            element,
            hydrogens,
            ion,
            isotope,
            parity
        )
        return instance


class BondSpec(PyBondSpec):
    """
    A bond specification, used to create a molecule instance.

    :param sid: an ``int``, the atom ID of the first atom in the bond.
    :param tid: an ``int``, the atom ID of the last atom in the bond.
    :param order: a ``BondOrder`` or an ``int``, the order of the bond.
    :param parity: an optional ``Parity`` or ``bool``, the \
    stereochemistry of the bond (only valid for double bonds).

    *Attributes*
    See Parameters.

    """
    def __new__(
            cls: Type[BS],
            sid: int,
            tid: int,
            order: Union[PyBondOrder, int],
            parity: Optional[Union[PyParity, bool]] = None
    ) -> BS:
        if isinstance(order, int):
            order = PyBondOrder(order)

        if isinstance(parity, bool):
            parity = PyParity(parity)

        instance = PyBondSpec.__new__(
            cls,
            sid,
            tid,
            order,
            parity
        )
        return instance
