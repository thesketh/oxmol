"""
Representation of chemical element.

This is a thin wrapper around the PyO3 base class: it calls the
base class' ``__new__`` constructor and return an instance of the
base class.

At present, it doesn't seem to be possible to truly subclass
PyO3 classes from Python, so this is all we are able to do on the Python
end.

"""
from typing import Type, TypeVar
from .oxmol import PyElement

El = TypeVar('El', bound='Element')


class Element(PyElement):
    """
    A chemical element. Represented in ``chemcore::molecule`` as a Rust
    enum.

    :param atomic_number: an ``int``, the atomic number.

    """
    def __new__(cls: Type[El], atomic_number: int) -> El:
        return PyElement.__new__(cls, atomic_number)

    @classmethod
    def from_symbol(cls: Type[El], symbol: str) -> PyElement:
        """
        Create an element from its atomic symbol.
        """
        return PyElement.from_symbol(symbol)
