"""
Test suite for oxmol.spec.AtomSpec / oxmol.oxmol.PyAtomSpec

"""
from oxmol.spec import AtomSpec
from oxmol.element import Element
from oxmol.parity import Parity


def test_contructor_variants():
    """Test variants on specifying the element."""
    elements = ['C', 6, Element(6), Element.from_symbol('C')]

    for element in elements:
        atom = AtomSpec(element)
        assert str(atom.element) == 'PyElement::C'


def test_normal_atoms():
    """Test some normal atoms."""
    # normal methane
    atom = AtomSpec('C', 4, 0, 12, None)

    # methyl carbocation
    atom = AtomSpec('C', 3, 1, 12, None)

    # C14
    atom = AtomSpec('C', 4, 1, 14, None)

    # chiral C
    atom = AtomSpec('C', 1, 0, None, True)
    assert atom.parity == Parity(True)
    atom = AtomSpec('C', 1, 0, None, False)
    assert atom.parity == Parity(False)
    atom = AtomSpec('C', 1, 0, None, Parity(True))
    assert atom.parity == Parity(True)
    atom = AtomSpec('C', 1, 0, None, Parity(False))
    assert atom.parity == Parity(False)


def test_no_isotope():
    """Test atom with no isotope."""
    atom = AtomSpec('C')
    assert atom.isotope is None


def test_no_parity():
    """Test atom with no parity."""
    atom = AtomSpec(3)
    assert atom.parity is None


def test_positive_parity():
    """Test atom with positive parity."""
    atom = AtomSpec(3, parity=True)
    assert atom.parity == Parity(True)


def test_no_ion():
    """Test atom with no ion."""
    atom = AtomSpec('H')
    assert atom.ion == 0


def test_no_hydrogens():
    """Test atom with no hydrogens."""
    atom = AtomSpec(5)
    assert atom.hydrogens == 0
    