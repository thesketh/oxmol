"""
Test suite for oxmol.element.Element / oxmol.oxmol.PyElement

"""
import pytest
from oxmol.element import Element


def test_from_number():
    """Test making an element from its atomic number."""
    element = Element(6)
    assert str(element) == 'PyElement::C'


def test_from_symbol():
    """Test making an element from its atomic symbol."""
    element = Element.from_symbol('Li')
    assert str(element) == 'PyElement::Li'


def test_incorrect_case():
    """Test that symbols with the wrong case fail."""
    with pytest.raises(ValueError):
        Element.from_symbol('c')
    with pytest.raises(ValueError):
        Element.from_symbol('AG')


def test_fake_symbol():
    """Test that fake symbols fail."""
    with pytest.raises(ValueError):
        Element.from_symbol('A')


def test_outside_range():
    """Test that undiscovered elements fail."""
    with pytest.raises(ValueError):
        Element(119)


def test_negative():
    """Test that cursed negative elements fail."""
    with pytest.raises(OverflowError):
        Element(-1)
