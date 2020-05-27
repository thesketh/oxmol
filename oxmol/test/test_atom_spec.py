from oxmol.spec import AtomSpec
from oxmol.element import Element
from oxmol.parity import Parity


def test_contructor_variants():
    elements = ['C', 6, Element(6), Element.from_symbol('C')]

    for element in elements:
        a = AtomSpec(element)
        assert str(a.element) == 'PyElement::C'


def test_normal_atoms():
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
    atom = AtomSpec('C')
    assert atom.isotope is None


def test_no_parity():
    atom = AtomSpec(3)
    assert atom.parity is None


def test_positive_parity():
    atom = AtomSpec(3, parity=True)
    assert atom.parity == Parity(True)


def test_no_ion():
    atom = AtomSpec('H')
    assert atom.ion == 0


def test_no_hydrogens():
    atom = AtomSpec(5)
    assert atom.hydrogens == 0
    