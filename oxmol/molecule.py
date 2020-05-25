"""
Representation of a whole molecule.

This is a thin wrapper around the PyO3 base class: it calls the
base class' ``__new__`` constructor and return an instance of the
base class.

At present, it doesn't seem to be possible to truly subclass
PyO3 classes from Python, so this is all we are able to do on the Python
end.

"""
from typing import List, Optional, Type, TypeVar
from .oxmol import (
    PyAtomSpec,
    PyBondSpec,
    PyDefaultMolecule,
    PyElement,
    PyParity,
    PyBondOrder,
)

M = TypeVar('M', bound='Molecule')


class Molecule(PyDefaultMolecule):
    """
    A molecular representation. This class is ultimately a
    representation of ``molecule::default_molecule::DefaultMolecule``.

    :param atoms: a ``list`` of ``PyAtomSpec``
    :param bonds: a ``list`` of ``PyBondSpec``

    Attributes
    
    - ``nodes`` - a ``list`` of the atom indices
    - ``edges`` - a ``list`` of ``tuple`` of two atom indices,\
      representing the bonds

    """
    def __new__(
            cls: Type[M],
            atoms: List[PyAtomSpec],
            bonds: List[PyBondSpec]
    ) -> M:
        return PyDefaultMolecule.__new__(cls, atoms, bonds)

    def is_empty(self) -> bool:
        """Return whether the molecule contains atoms."""
        return self.super().is_empty()

    def order(self) -> int:
        """Return how many atoms are in the molecule."""
        return self.super().order()

    def size(self) -> int:
        """Return how many bonds are in the molecule."""
        return self.super().size()

    def has_node(self, atom_id: int) -> bool:
        """
        Given an atom ID, return a ``bool`` indicating whether the atom
        exists in the molecule.

        :param atom_id: the atom index
        :return: whether the atom exists in this molecule

        """
        return self.super().has_node(atom_id)

    def neighbors(self, atom_id: int) -> List[int]:
        """
        Given an atom ID, return the indices of the atom's neighbors.

        :param atom_id: the atom index
        :return: a ``list`` of indices of the atom's direct connections

        """
        return self.super().neighbors(atom_id)

    def has_edge(self, sid: int, tid: int) -> bool:
        """
        Given a start atom ID and target atom ID, return a bool indicating
        whether a bond exists between the two atoms.

        :param sid: the atom index of the start of the bond
        :param tid: the atom index of the target of the bond
        :return: whether the bond exists in the molecule

        """
        return self.super().has_edge(sid, tid)

    def degree(self, atom_id: int) -> int:
        """
        Given an atom ID, return the number of connections the atom
        has, including virtual hydrogens.

        :param atom_id: the atom index
        :return: the number of connections (including virtual) that\
        the atom has

        """
        return self.super().degree(atom_id)

    def hydrogens(self, atom_id: int) -> int:
        """
        Given an atom ID, return the number of virtual hydrogens the
        atom has.

        :param atom_id: the atom index
        :return: the number of virtual hydrogens on the atom

        """
        return self.super().hydrogens(atom_id)

    def element(self, atom_id: int) -> PyElement:
        """
        Given an atom ID, return the element of that atom.

        :param atom_id: the atom index
        :return: the element of the atom

        """
        return self.super().element(atom_id)

    def isotope(self, atom_id: int) -> Optional[int]:
        """
        Given an atom ID, return the isotope of that atom if it has
        been ascribed one. Otherwise, return ``None``.

        :param atom_id: the atom index
        :return: the isotope, if it has been set, otherwise ``None``

        """
        return self.super().isotope(atom_id)

    def electrons(self, atom_id: int) -> int:
        """
        Given an atom ID, return the number of nonbonding electrons the
        atom has in its valence shell.

        :param atom_id: the atom index
        :return: the number of nonbonding electrons in the atom's\
        valence shell

        """
        return self.super().electrons(atom_id)

    def charge(self, atom_id: int) -> int:
        """
        Given an atom ID, return the atom's formal charge.

        :param atom_id: the atom index
        :return: the atom's formal charge

        """
        return self.super().charge(atom_id)

    def atom_parity(self, atom_id: int) -> Optional[PyParity]:
        """
        Given an atom ID, return the atom's tetrahedral chirality.

        :param atom_id: the atom index
        :return: the tetrahedral chirality of the atom.

        """
        return self.super().atom_parity(atom_id)

    def bond_order(self, sid: int, tid: int) -> PyBondOrder:
        """
        Given a start atom ID and target atom ID, return the order of
        the bond between the two atoms.

        :param sid: the atom index of the start of the bond
        :param tid: the atom index of the target of the bond
        :return: the order of the bond between the atoms.

        """
        self.super().bond_order(sid, tid)

    def bond_parity(self, sid: int, tid: int) -> Optional[PyParity]:
        """
        Given a start atom ID and target atom ID, return the
        stereochemistry of the bond between the two atoms.

        :param sid: the atom index of the start of the bond
        :param tid: the atom index of the target of the bond
        :return: the stereochemistry of the bond between the atoms.

        """
        self.super().bond_parity(sid, tid)
