"""
Representation of bond order.

This is a thin wrapper around the PyO3 base class: it calls the
base class' ``__new__`` constructor and return an instance of the
base class.

At present, it doesn't seem to be possible to truly subclass
PyO3 classes from Python, so this is all we are able to do on the Python
end.

"""
from typing import Type, TypeVar
from .oxmol import PyBondOrder

BO = TypeVar('BO', bound='BondOrder')


class BondOrder(PyBondOrder):
    """
    A bond order. This is a Python class representing a Rust enum. The bond
    orders represented in ``molecule.rs`` are ``Zero``, ``Single``,
    ``Double`` and ``Triple``.

    :param order: an int in range(0, 4) representing the bond order as\
    an ``int``.

    """
    def __new__(cls: Type[BO], bond_order: int) -> BO:
        return PyBondOrder.__new__(cls, bond_order)

    def as_int(self) -> int:
        """Get the bond order as an integer in range(0, 4)."""
        self.super().as_int()
