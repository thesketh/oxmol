"""
Test suite for oxmol.spec.BondSpec / oxmol.oxmol.PyElement

"""
import pytest
from oxmol.spec import BondSpec
from oxmol.bond_order import BondOrder


def test_single_bond():
    """Test that single bonds are created normally."""
    bond = BondSpec(0, 1, 1)
    assert bond.order.as_int() == 1
    assert bond.order == BondOrder(1)
    bond = BondSpec(0, 1, BondOrder(1))
    assert bond.order.as_int() == 1


def test_double_bond():
    """Test that double bonds are created normally."""
    bond = BondSpec(4, 8, 2)
    assert bond.order == BondOrder(2)
    bond = BondSpec(0, 1, BondOrder(2))
    assert bond.order.as_int() == 2


def test_triple_bond():
    """Test that triple bonds are created normally."""
    bond = BondSpec(5, 7, 3)
    assert bond.order == BondOrder(3)
    bond = BondSpec(0, 1, BondOrder(3))
    assert bond.order.as_int() == 3


def test_quadruple_bond():
    """Test that quadruple bonds fail normally."""
    with pytest.raises(ValueError):
        BondSpec(0, 1, 4)
    with pytest.raises(ValueError):
        BondSpec(0, 1, BondOrder(4))
