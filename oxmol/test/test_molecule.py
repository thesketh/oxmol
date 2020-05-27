import pytest
from oxmol.parity import Parity
from oxmol.spec import AtomSpec, BondSpec
from oxmol.molecule import Molecule
from oxmol.bond_order import BondOrder


def test_overionised():
    atom = AtomSpec('H', ion=2)
    with pytest.raises(ValueError):
        Molecule([atom], [])


def test_oversaturated():
    symbol_hydrogens = [
        ('H', 2),
        ('Li', 2),
        ('Be', 3),
        ('B', 4),
        ('C', 5),
    ]

    for symbol, hydrogens in symbol_hydrogens:
        atom = AtomSpec(symbol, hydrogens)
        with pytest.raises(ValueError):
            Molecule([atom], [])


def test_impossible_isotope():
    symbol_isotope = [
        ('H', 0),
        ('Li', 2),
        ('Be', 3),
        ('B', 4),
        ('C', 5),
    ]
    for symbol, isotope in symbol_isotope:
        atom = AtomSpec(symbol, isotope=isotope)
        with pytest.raises(ValueError):
            Molecule([atom], [])


def test_HD():
    H = AtomSpec('H', isotope=1)
    D = AtomSpec(1, isotope=2)

    molecule = Molecule([H, D], [BondSpec(0, 1, 1)])
    assert molecule.isotope(0) == 1
    assert molecule.isotope(1) == 2


def test_electrons_isolated_C():
    molecule = Molecule([AtomSpec('C')], [])
    assert molecule.electrons(0) == 4


def test_hydrogens_isolated_C():
    molecule = Molecule([AtomSpec('C')], [])
    assert molecule.hydrogens(0) == 0


def test_charge_isolated_C():
    molecule = Molecule([AtomSpec('C')], [])
    assert molecule.charge(0) == 0


def test_electrons_methyl_radical_C():
    molecule = Molecule([AtomSpec('C', 3)], [])
    assert molecule.electrons(0) == 1


def test_hydrogens_methyl_radical_C():
    molecule = Molecule([AtomSpec('C', 3)], [])
    assert molecule.hydrogens(0) == 3


def test_charge_methyl_radical_C():
    molecule = Molecule([AtomSpec('C', 3)], [])
    assert molecule.charge(0) == 0


def test_electrons_methane_explicit_H():
    C = AtomSpec('C')
    H = AtomSpec('H')

    atoms = [C, H, H, H, H]
    bonds = [
        BondSpec(0, 1, 1),
        BondSpec(0, 2, 1),
        BondSpec(0, 3, 1),
        BondSpec(0, 4, 1),
    ]

    molecule = Molecule(atoms, bonds)
    assert molecule.electrons(0) == 0


def test_degree_methane_explicit_H():
    C = AtomSpec('C')
    H = AtomSpec('H')

    atoms = [C, H, H, H, H]
    bonds = [
        BondSpec(0, 1, 1),
        BondSpec(0, 2, 1),
        BondSpec(0, 3, 1),
        BondSpec(0, 4, 1),
    ]

    molecule = Molecule(atoms, bonds)
    assert molecule.degree(0) == 4


def neighbors_methane_explicit_H():
    C = AtomSpec('C')
    H = AtomSpec('H')

    atoms = [C, H, H, H, H]
    bonds = [
        BondSpec(0, 1, 1),
        BondSpec(0, 2, 1),
        BondSpec(0, 3, 1),
        BondSpec(0, 4, 1),
    ]

    molecule = Molecule(atoms, bonds)
    assert len(molecule.neighbors(0)) == 4



def test_electrons_methane():
    molecule = Molecule([AtomSpec('C', 4)], [])
    assert molecule.electrons(0) == 0


def test_hydrogens_methane():
    molecule = Molecule([AtomSpec('C', 4)], [])
    assert molecule.hydrogens(0) == 4


def test_charge_methane():
    molecule = Molecule([AtomSpec('C', 4)], [])
    assert molecule.charge(0) == 0


def test_parity_methane():
    molecule = Molecule([AtomSpec('C', 4)], [])
    assert molecule.atom_parity(0) is None


def test_false_parity_methane():
    molecule = Molecule([AtomSpec('C', 4, parity=False)], [])
    assert molecule.atom_parity(0) == Parity(False)


def test_degree_methane():
    molecule = Molecule([AtomSpec('C', 4)], [])
    assert molecule.degree(0) == 0


def test_neighbors_methane():
    molecule = Molecule([AtomSpec('C', 4)], [])
    assert not molecule.neighbors(0)


def test_electrons_methyl_anion():
    molecule = Molecule([AtomSpec('C', 3, -1)], [])
    assert molecule.electrons(0) == 2


def test_hydrogens_methyl_anion():
    molecule = Molecule([AtomSpec('C', 3, -1)], [])
    assert molecule.hydrogens(0) == 3


def test_charge_methyl_anion():
    molecule = Molecule([AtomSpec('C', 3, -1)], [])
    assert molecule.charge(0) == -1


def test_charge_methyl_carbocation():
    molecule = Molecule([AtomSpec('C', 3, 1)], [])
    assert molecule.charge(0) == 1


def test_electrons_ethane():
    C = AtomSpec('C')
    H = AtomSpec('H')

    atoms = [C, H, H, H, C, H, H, H]
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


def test_bond_order_ethane():
    C = AtomSpec(6)
    H = AtomSpec(1)

    atoms = [C, H, H, H, C, H, H, H]
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


def test_electrons_ethyl_radical():
    C = AtomSpec('C')
    H = AtomSpec('H')

    atoms = [C, H, H, H, C, H, H]
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


def test_electrons_ethene():
    C = AtomSpec('C')
    H = AtomSpec('H')

    atoms = [C, H, H, C, H, H]
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


def test_has_edge_ethene():
    C = AtomSpec('C')
    H = AtomSpec('H')

    atoms = [C, H, H, C, H, H]
    bonds = [
        BondSpec(0, 1, 1),
        BondSpec(0, 2, 1),
        BondSpec(0, 3, 2),
        BondSpec(3, 4, 1),
        BondSpec(3, 5, 1)
    ]

    molecule = Molecule(atoms, bonds)
    assert molecule.has_edge(0, 3)


def test_bond_order_ethene():
    C = AtomSpec(6)
    H = AtomSpec(1)

    atoms = [C, H, H, C, H, H]
    bonds = [
        BondSpec(0, 1, BondOrder(1)),
        BondSpec(0, 2, BondOrder(1)),
        BondSpec(0, 3, BondOrder(2)),
        BondSpec(3, 4, BondOrder(1)),
        BondSpec(3, 5, BondOrder(1))
    ]

    molecule = Molecule(atoms, bonds)
    assert molecule.bond_order(0, 3).as_int() == 2


def test_bond_parity_ethene():
    C = AtomSpec(6)
    H = AtomSpec(1)

    atoms = [C, H, H, C, H, H]
    bonds = [
        BondSpec(0, 1, BondOrder(1)),
        BondSpec(0, 2, BondOrder(1)),
        BondSpec(0, 3, BondOrder(2)),
        BondSpec(3, 4, BondOrder(1)),
        BondSpec(3, 5, BondOrder(1))
    ]

    molecule = Molecule(atoms, bonds)
    assert molecule.bond_parity(0, 3) is None


def test_bond_parity_butene():
    C3 = AtomSpec(6, 3)
    C1 = AtomSpec(6, 1)

    atoms = [C3, C1, C1, C3]
    bonds = [
        BondSpec(0, 1, BondOrder(1)),
        BondSpec(1, 2, BondOrder(2), True),
        BondSpec(2, 3, BondOrder(1)),
    ]

    molecule = Molecule(atoms, bonds)
    assert molecule.bond_parity(1, 2) == Parity(True)


def test_electrons_vinyl_radical():
    C = AtomSpec('C')
    H = AtomSpec('H')

    atoms = [C, H, H, C, H]
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


def test_has_edge_vinyl_radical():
    C = AtomSpec('C')
    H = AtomSpec('H')

    atoms = [C, H, H, C, H]
    bonds = [
        BondSpec(0, 1, 1),
        BondSpec(0, 2, 1),
        BondSpec(0, 3, 2),
        BondSpec(3, 4, 1),
    ]

    molecule = Molecule(atoms, bonds)
    assert molecule.has_edge(0, 3)


def test_texas_carbon():
    with pytest.raises(ValueError):
        Molecule([AtomSpec(6, 5)], [])


def test_duplicate_bond():
    with pytest.raises(ValueError):
        C = AtomSpec(6, 3)
        Molecule([C, C], [BondSpec(0, 1, 1), BondSpec(0, 1, 1)])


def test_hypervalent_bond():
    with pytest.raises(ValueError):
        C = AtomSpec(6, 3)
        Molecule([C, C], [BondSpec(0, 1, 2)])


def test_bond_to_self():
    with pytest.raises(ValueError):
        C = AtomSpec(6, 3)
        Molecule([C, C], [BondSpec(0, 0, 1)])


def test_hydroborate_charge():
    B = AtomSpec(5, 4, -1)
    assert Molecule([B], []).charge(0) == -1