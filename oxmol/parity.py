"""
Representation of stereochemistry.

This is a thin wrapper around the PyO3 base class: it calls the
base class' ``__new__`` constructor and return an instance of the
base class.

At present, it doesn't seem to be possible to truly subclass
PyO3 classes from Python, so this is all we are able to do on the Python
end.

"""
from typing import Type, TypeVar
from .oxmol import PyParity

P = TypeVar('P', bound='Parity')


class Parity(PyParity):
    """
    A stereochemical atom or bond parity, represented using a Rust enum.
    `This parity is laid out in the minimal API description.`__

    The enum refers to 'Positive' or 'Negative', which are represented
    using Python's ``True`` and ``False`` respectively.

    For tetrahedral chirality:
    - ``True`` represents clockwise
    - ``False`` represents anticlockwise

    For E/Z double bond stereochemistry:
    - ``True`` represents syn
    - ``False`` represents anti

    :param parity: The atom or bond parity.

    __ https://depth-first.com/articles/2020/04/06/a-minimal-molecule-api/

    """
    def __new__(cls: Type[P], parity: bool) -> P:
        return PyParity.__new__(cls, parity)
