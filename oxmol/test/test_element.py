"""
Test suite for oxmol.element.Element / oxmol.oxmol.PyElement

"""
import pytest
from oxmol.element import Element


def test_from_number():
    e = Element(6)
    assert str(e) == 'PyElement::C'


def test_from_symbol():
    e = Element.from_symbol('Li')
    assert str(e) == 'PyElement::Li'


def test_incorrect_case():
    with pytest.raises(ValueError):
        Element.from_symbol('c')        
    with pytest.raises(ValueError):
        Element.from_symbol('AG')


def test_fake_symbol():
    with pytest.raises(ValueError):
        Element.from_symbol('A')


def test_outside_range():
    with pytest.raises(ValueError):
        Element(119)


def test_negative():
    with pytest.raises(OverflowError):
        Element(-1)