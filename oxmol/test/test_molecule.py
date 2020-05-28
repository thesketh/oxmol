"""
Test suite for oxmol.molecule.Molecule / oxmol.oxmol.PyMolecule

"""
import pytest
from oxmol.parity import Parity
from oxmol.spec import AtomSpec, BondSpec
from oxmol.molecule import Molecule
from oxmol.bond_order import BondOrder


class TestFirstRow:
    """Test the first row of the periodic table."""
    @staticmethod
    def test_overionised_positive():
        """
        Test that atoms with too high a charge produce errors.

        """
        symbol_ion = [
            ('H', 2),
            ('Li', 2),
            ('Be', 3),
            ('B', 4),
            ('C', 5),
            # ('N', 4),
            # ('O', 3),
            # ('F', 2)
        ]
        for symbol, ion in symbol_ion:
            atom = AtomSpec(symbol, ion=ion)
            with pytest.raises(ValueError):
                Molecule([atom], [])

    @staticmethod
    @pytest.mark.xfail(reason="molecule.rs does not handle overly -ve ions.")
    def test_overionised_negative():
        """
        Test that atoms with too low a charge produce errors.

        """
        symbol_ion = [
            ('H', -2),
            ('Li', -8),
            ('Be', -7),
            ('B', -6),
            ('C', -5),
            ('N', -4),
            ('O', -3),
            ('F', -2)
        ]
        for symbol, ion in symbol_ion:
            atom = AtomSpec(symbol, ion=ion)
            with pytest.raises(ValueError):
                Molecule([atom], [])

    @staticmethod
    def test_oversaturated():
        """
        Test that oversaturated atoms produce errors.

        """
        symbol_hydrogens = [
            ('H', 2),
            ('Li', 2),
            ('Be', 3),
            ('B', 4),
            ('C', 5),
            # ('N', 4),
            # ('O', 3),
            # ('F', 2)
        ]

        for symbol, hydrogens in symbol_hydrogens:
            atom = AtomSpec(symbol, hydrogens)
            with pytest.raises(ValueError):
                Molecule([atom], [])

    @staticmethod
    def test_impossible_isotope():
        """
        Test that isotopes lower than atomic no. produce errors.

        """
        symbol_isotope = [
            ('H', 0),
            ('He', 1),
            ('Li', 2),
            ('Be', 3),
            ('B', 4),
            ('C', 5),
            ('N', 6),
            ('O', 7)
        ]
        for symbol, isotope in symbol_isotope:
            atom = AtomSpec(symbol, isotope=isotope)
            with pytest.raises(ValueError):
                Molecule([atom], [])


class TestIsolatedC:
    """Test an isolated carb atom."""
    @staticmethod
    def test_electrons():
        """Test the number of electrons."""
        molecule = Molecule([AtomSpec('C')], [])
        assert molecule.electrons(0) == 4

    @staticmethod
    def test_hydrogens():
        """Test the number of virtual hydrogens."""
        molecule = Molecule([AtomSpec('C')], [])
        assert molecule.hydrogens(0) == 0

    @staticmethod
    def test_charge():
        """Test the charge."""
        molecule = Molecule([AtomSpec('C')], [])
        assert molecule.charge(0) == 0

class TestMethylRadical:
    """Test a methyl radical."""
    @staticmethod
    def test_electrons():
        """Test the number of electrons."""
        molecule = Molecule([AtomSpec('C', 3)], [])
        assert molecule.electrons(0) == 1

    @staticmethod
    def test_hydrogens():
        """Test the number of virtual hydrogens."""
        molecule = Molecule([AtomSpec('C', 3)], [])
        assert molecule.hydrogens(0) == 3

    @staticmethod
    def test_charge():
        """Test the charge."""
        molecule = Molecule([AtomSpec('C', 3)], [])
        assert molecule.charge(0) == 0


class TestMethane:
    """Test methane."""
    @staticmethod
    def test_electrons_expl():
        """
        Test the number of electrons, constructed with explicit H.

        """
        carb = AtomSpec('C')
        hyd = AtomSpec('H')

        atoms = [carb, hyd, hyd, hyd, hyd]
        bonds = [
            BondSpec(0, 1, 1),
            BondSpec(0, 2, 1),
            BondSpec(0, 3, 1),
            BondSpec(0, 4, 1),
        ]

        molecule = Molecule(atoms, bonds)
        assert molecule.electrons(0) == 0

    @staticmethod
    def test_degree_expl():
        """Test the degree, constructed with explicit H."""
        carb = AtomSpec('C')
        hyd = AtomSpec('H')

        atoms = [carb, hyd, hyd, hyd, hyd]
        bonds = [
            BondSpec(0, 1, 1),
            BondSpec(0, 2, 1),
            BondSpec(0, 3, 1),
            BondSpec(0, 4, 1),
        ]

        molecule = Molecule(atoms, bonds)
        assert molecule.degree(0) == 4

    @staticmethod
    def test_neighbors_expl():
        """
        Test the number of neighbors, constructed with explicit H.

        """
        carb = AtomSpec('C')
        hyd = AtomSpec('H')

        atoms = [carb, hyd, hyd, hyd, hyd]
        bonds = [
            BondSpec(0, 1, 1),
            BondSpec(0, 2, 1),
            BondSpec(0, 3, 1),
            BondSpec(0, 4, 1),
        ]

        molecule = Molecule(atoms, bonds)
        assert len(molecule.neighbors(0)) == 4

    @staticmethod
    def test_electrons():
        """Test the number of electrons."""
        molecule = Molecule([AtomSpec('C', 4)], [])
        assert molecule.electrons(0) == 0

    @staticmethod
    def test_hydrogens():
        """Test the number of hydrogens."""
        molecule = Molecule([AtomSpec('C', 4)], [])
        assert molecule.hydrogens(0) == 4

    @staticmethod
    def test_charge():
        """Test the charge."""
        molecule = Molecule([AtomSpec('C', 4)], [])
        assert molecule.charge(0) == 0

    @staticmethod
    def test_parity():
        """Test the parity."""
        molecule = Molecule([AtomSpec('C', 4)], [])
        assert molecule.atom_parity(0) is None

    @staticmethod
    def test_given_parity():
        """Test a given parity."""
        molecule = Molecule([AtomSpec('C', 4, parity=False)], [])
        assert molecule.atom_parity(0) == Parity(False)

    @staticmethod
    def test_degree():
        """Test the degree."""
        molecule = Molecule([AtomSpec('C', 4)], [])
        assert molecule.degree(0) == 0

    @staticmethod
    def test_neighbors():
        """Test the number of neighbors."""
        molecule = Molecule([AtomSpec('C', 4)], [])
        assert not molecule.neighbors(0)

    @staticmethod
    def test_is_empty():
        """Test that methane is not empty."""
        molecule = Molecule([AtomSpec('C', 4)], [])
        assert molecule.is_empty() is False

    @staticmethod
    def test_size():
        """Test that methane's ``size`` is 0."""
        molecule = Molecule([AtomSpec('C', 4)], [])
        assert molecule.size() == 0

class TestMethylAnion:
    """Test a methyl anion."""
    @staticmethod
    def test_electrons():
        """Test the number of electrons."""
        molecule = Molecule([AtomSpec('C', 3, -1)], [])
        assert molecule.electrons(0) == 2

    @staticmethod
    def test_hydrogens():
        """Test the number of hydrogens."""
        molecule = Molecule([AtomSpec('C', 3, -1)], [])
        assert molecule.hydrogens(0) == 3

    @staticmethod
    def test_charge():
        """Test the charge."""
        molecule = Molecule([AtomSpec('C', 3, -1)], [])
        assert molecule.charge(0) == -1


class TestEthane:
    """Test ethane."""
    @staticmethod
    def test_electrons():
        """Test the number of electrons."""
        carb = AtomSpec('C')
        hyd = AtomSpec('H')

        atoms = [carb, hyd, hyd, hyd, carb, hyd, hyd, hyd]
        bonds = [
            BondSpec(0, 1, 1),
            BondSpec(0, 2, 1),
            BondSpec(0, 3, 1),
            BondSpec(0, 4, 1),
            BondSpec(4, 5, 1),
            BondSpec(4, 6, 1),
            BondSpec(4, 7, 1)
        ]

        molecule = Molecule(atoms, bonds)
        for node in molecule.nodes:
            assert molecule.electrons(node) == 0

    @staticmethod
    def test_bond_order():
        """Test the bond orders."""
        carb = AtomSpec(6)
        hyd = AtomSpec(1)

        atoms = [carb, hyd, hyd, hyd, carb, hyd, hyd, hyd]
        bonds = [
            BondSpec(0, 1, BondOrder(1)),
            BondSpec(0, 2, BondOrder(1)),
            BondSpec(0, 3, BondOrder(1)),
            BondSpec(0, 4, BondOrder(1)),
            BondSpec(4, 5, BondOrder(1)),
            BondSpec(4, 6, BondOrder(1)),
            BondSpec(4, 7, BondOrder(1))
        ]

        molecule = Molecule(atoms, bonds)
        assert molecule.bond_order(0, 4).as_int() == 1
        assert molecule.bond_order(3, 4).as_int() == 0


class TestEthylRadical:
    """Test an ethyl radical."""
    @staticmethod
    def test_electrons():
        """Test the number of electrons."""
        carb = AtomSpec('C')
        hyd = AtomSpec('H')

        atoms = [carb, hyd, hyd, hyd, carb, hyd, hyd]
        bonds = [
            BondSpec(0, 1, 1),
            BondSpec(0, 2, 1),
            BondSpec(0, 3, 1),
            BondSpec(0, 4, 1),
            BondSpec(4, 5, 1),
            BondSpec(4, 6, 1),
        ]

        molecule = Molecule(atoms, bonds)
        for node in molecule.nodes:
            if node == 4:
                assert molecule.electrons(node) == 1
            else:
                assert molecule.electrons(node) == 0


class TestEthene:
    """Test ethene."""
    @staticmethod
    def test_electrons():
        """Test the number of electrons."""
        carb = AtomSpec('C')
        hyd = AtomSpec('H')

        atoms = [carb, hyd, hyd, carb, hyd, hyd]
        bonds = [
            BondSpec(0, 1, 1),
            BondSpec(0, 2, 1),
            BondSpec(0, 3, 2),
            BondSpec(3, 4, 1),
            BondSpec(3, 5, 1)
        ]

        molecule = Molecule(atoms, bonds)
        for node in molecule.nodes:
            assert molecule.electrons(node) == 0

    @staticmethod
    def test_has_edge():
        """Test that the right edges exist."""
        carb = AtomSpec('C')
        hyd = AtomSpec('H')

        atoms = [carb, hyd, hyd, carb, hyd, hyd]
        bonds = [
            BondSpec(0, 1, 1),
            BondSpec(0, 2, 1),
            BondSpec(0, 3, 2),
            BondSpec(3, 4, 1),
            BondSpec(3, 5, 1)
        ]

        molecule = Molecule(atoms, bonds)
        assert molecule.has_edge(0, 3)

    @staticmethod
    def test_bond_order():
        """Test the bond orders."""
        carb = AtomSpec(6)
        hyd = AtomSpec(1)

        atoms = [carb, hyd, hyd, carb, hyd, hyd]
        bonds = [
            BondSpec(0, 1, BondOrder(1)),
            BondSpec(0, 2, BondOrder(1)),
            BondSpec(0, 3, BondOrder(2)),
            BondSpec(3, 4, BondOrder(1)),
            BondSpec(3, 5, BondOrder(1))
        ]

        molecule = Molecule(atoms, bonds)
        assert molecule.bond_order(0, 3).as_int() == 2

    @staticmethod
    def test_bond_parity():
        """Test the bond parity."""
        carb = AtomSpec(6)
        hyd = AtomSpec(1)

        atoms = [carb, hyd, hyd, carb, hyd, hyd]
        bonds = [
            BondSpec(0, 1, BondOrder(1)),
            BondSpec(0, 2, BondOrder(1)),
            BondSpec(0, 3, BondOrder(2)),
            BondSpec(3, 4, BondOrder(1)),
            BondSpec(3, 5, BondOrder(1))
        ]

        molecule = Molecule(atoms, bonds)
        assert molecule.bond_parity(0, 3) is None

    @staticmethod
    def test_given_bond_parity():
        """Test a given bond parity."""
        carb = AtomSpec(6)
        hyd = AtomSpec(1)

        atoms = [carb, hyd, hyd, carb, hyd, hyd]
        bonds = [
            BondSpec(0, 1, BondOrder(1)),
            BondSpec(0, 2, BondOrder(1)),
            BondSpec(0, 3, BondOrder(2), True),
            BondSpec(3, 4, BondOrder(1)),
            BondSpec(3, 5, BondOrder(1))
        ]

        molecule = Molecule(atoms, bonds)
        assert molecule.bond_parity(0, 3) == Parity(True)


class TestButene:
    """Test butene."""
    @staticmethod
    def test_given_bond_parity():
        """Test a given bond parity."""
        carb_3 = AtomSpec(6, 3)
        carb_1 = AtomSpec(6, 1)

        atoms = [carb_3, carb_1, carb_1, carb_3]
        bonds = [
            BondSpec(0, 1, BondOrder(1)),
            BondSpec(1, 2, BondOrder(2), True),
            BondSpec(2, 3, BondOrder(1)),
        ]

        molecule = Molecule(atoms, bonds)
        assert molecule.bond_parity(1, 2) == Parity(True)

    @staticmethod
    def test_order():
        """Test that ``order`` is correct."""
        carb_3 = AtomSpec(6, 3)
        carb_1 = AtomSpec(6, 1)

        atoms = [carb_3, carb_1, carb_1, carb_3]
        bonds = [
            BondSpec(0, 1, BondOrder(1)),
            BondSpec(1, 2, BondOrder(2), True),
            BondSpec(2, 3, BondOrder(1)),
        ]

        molecule = Molecule(atoms, bonds)
        assert molecule.order() == 4

    @staticmethod
    def test_size():
        """Test that ``size`` is correct."""
        carb_3 = AtomSpec(6, 3)
        carb_1 = AtomSpec(6, 1)

        atoms = [carb_3, carb_1, carb_1, carb_3]
        bonds = [
            BondSpec(0, 1, BondOrder(1)),
            BondSpec(1, 2, BondOrder(2), True),
            BondSpec(2, 3, BondOrder(1)),
        ]

        molecule = Molecule(atoms, bonds)
        assert molecule.size() == 3


class TestVinylRadical:
    """Test a vinyl radical."""
    @staticmethod
    def test_electrons():
        """Test the number of electrons."""
        carb = AtomSpec('C')
        hyd = AtomSpec('H')

        atoms = [carb, hyd, hyd, carb, hyd]
        bonds = [
            BondSpec(0, 1, 1),
            BondSpec(0, 2, 1),
            BondSpec(0, 3, 2),
            BondSpec(3, 4, 1),
        ]

        molecule = Molecule(atoms, bonds)
        for node in molecule.nodes:
            if node == 3:
                assert molecule.electrons(node) == 1
            else:
                assert molecule.electrons(node) == 0

    @staticmethod
    def test_has_edge():
        """Test that the right edges exist."""
        carb = AtomSpec('C')
        hyd = AtomSpec('H')

        atoms = [carb, hyd, hyd, carb, hyd]
        bonds = [
            BondSpec(0, 1, 1),
            BondSpec(0, 2, 1),
            BondSpec(0, 3, 2),
            BondSpec(3, 4, 1),
        ]

        molecule = Molecule(atoms, bonds)
        assert molecule.has_edge(0, 3)


class TestBondingFailures:
    """Test failures in bonding."""
    @staticmethod
    def test_duplicate_bond():
        """Test a repeated bond."""
        carb = AtomSpec(6, 3)
        with pytest.raises(ValueError):
            Molecule([carb, carb], [BondSpec(0, 1, 1), BondSpec(0, 1, 1)])

    @staticmethod
    def test_hypervalent_bond():
        """Test a carb with 5 bonds."""
        carb = AtomSpec(6, 3)
        with pytest.raises(ValueError):
            Molecule([carb, carb], [BondSpec(0, 1, 2)])

    @staticmethod
    def test_bond_to_self():
        """Test bonding an atom to itself."""
        carb = AtomSpec(6, 3)
        with pytest.raises(ValueError):
            Molecule([carb, carb], [BondSpec(0, 0, 1)])

    @staticmethod
    def test_dangling_bond():
        """Test a dangling bond."""
        carb = AtomSpec(6, 3)
        with pytest.raises(ValueError):
            Molecule([carb], [BondSpec(0, 1, 1)])

        with pytest.raises(ValueError):
            Molecule([carb], [BondSpec(1, 0, 1)])


class TestInvalidAccess:
    """Test getting properties for nonexisting atoms."""
    @staticmethod
    def test_element_given_invalid():
        """Test that invalid atoms raise error when calling element."""
        carb = AtomSpec(6, 4)
        molecule = Molecule([carb], [])
        with pytest.raises(ValueError):
            molecule.element(1)

    @staticmethod
    def test_electrons_given_invalid():
        """
        Test that invalid atoms raise error when calling electrons.

        """
        carb = AtomSpec(6, 4)
        molecule = Molecule([carb], [])
        with pytest.raises(ValueError):
            molecule.electrons(1)

    @staticmethod
    def test_hydrogens_given_invalid():
        """
        Test that invalid atoms raise error when calling hydrogens.

        """
        carb = AtomSpec(6, 4)
        molecule = Molecule([carb], [])
        with pytest.raises(ValueError):
            molecule.hydrogens(1)

    @staticmethod
    def test_charge_given_invalid():
        """Test that invalid atoms raise error when calling charge."""
        carb = AtomSpec(6, 4)
        molecule = Molecule([carb], [])
        with pytest.raises(ValueError):
            molecule.charge(1)

    @staticmethod
    def test_isotope_given_invalid():
        """
        Test that invalid atoms raise error when calling isotope.

        """
        carb = AtomSpec(6, 4)
        molecule = Molecule([carb], [])
        with pytest.raises(ValueError):
            molecule.isotope(1)

    @staticmethod
    def test_atom_parity_given_invalid():
        """Test that invalid atoms raise error when calling parity."""
        carb = AtomSpec(6, 4)
        molecule = Molecule([carb], [])
        with pytest.raises(ValueError):
            molecule.atom_parity(1)

    @staticmethod
    def test_bond_parity_given_invalid():
        """
        Test that invalid bonds raise error when calling bond_parity.

        """
        carb_3 = AtomSpec(6, 3)
        bond = BondSpec(0, 1, 1)
        molecule = Molecule([carb_3, carb_3], [bond])
        with pytest.raises(ValueError):
            molecule.bond_parity(1, 2)
        with pytest.raises(ValueError):
            molecule.bond_parity(2, 0)

    @staticmethod
    def test_bond_order_given_invalid():
        """
        Test that invalid bonds raise error when calling bond_order.

        """
        carb_3 = AtomSpec(6, 3)
        bond = BondSpec(0, 1, 1)
        molecule = Molecule([carb_3, carb_3], [bond])
        with pytest.raises(ValueError):
            molecule.bond_order(1, 2)
        with pytest.raises(ValueError):
            molecule.bond_order(2, 0)

    @staticmethod
    def test_neighbors_given_invalid():
        """
        Test that invalid atoms raise error when calling neighbors.

        """
        carb = AtomSpec(6, 4)
        molecule = Molecule([carb], [])
        with pytest.raises(ValueError):
            molecule.neighbors(1)


class TestEmptyMolecule:
    """Tests for an empty molecule."""
    @staticmethod
    def test_is_empty():
        """Test that ``is_empty`` returns the correct result."""
        molecule = Molecule([], [])
        assert molecule.is_empty() is True

    @staticmethod
    def test_size():
        """Test that ``size`` returns the correct result."""
        molecule = Molecule([], [])
        assert molecule.size() == 0

    @staticmethod
    def test_order():
        """Test that ``order`` returns the correct result."""
        molecule = Molecule([], [])
        assert molecule.order() == 0

    @staticmethod
    def test_has_node():
        """Test that ``has_node`` returns the correct result."""
        molecule = Molecule([], [])
        assert molecule.has_node(0) is False

    @staticmethod
    def test_has_edge():
        """Test that ``has_edge`` returns the correct result."""
        molecule = Molecule([], [])
        with pytest.raises(ValueError):
            molecule.has_edge(0, 1)

class TestMisc:
    """Miscellaneous tests."""
    @staticmethod
    def test_texas_carbon():
        """Test a carb with 5 Hs."""
        with pytest.raises(ValueError):
            Molecule([AtomSpec(6, 5)], [])

    @staticmethod
    def test_hydroborate_charge():
        """Test the charge of a hydroborate."""
        boron = AtomSpec(5, 4, -1)
        assert Molecule([boron], []).charge(0) == -1

    @staticmethod
    def test_hyd_deut():
        """Test that isotopes are set correctly."""
        hyd = AtomSpec('H', isotope=1)
        deut = AtomSpec(1, isotope=2)

        molecule = Molecule([hyd, deut], [BondSpec(0, 1, 1)])
        assert molecule.isotope(0) == 1
        assert molecule.isotope(1) == 2

    @staticmethod
    def test_charge_methyl_carbocation():
        """Test the charge."""
        molecule = Molecule([AtomSpec('C', 3, 1)], [])
        assert molecule.charge(0) == 1
