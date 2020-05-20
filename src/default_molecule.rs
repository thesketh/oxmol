// use pyo3::class::PyObjectProtocol;
use pyo3::prelude::*;

use molecule::default_molecule::DefaultMolecule;
use molecule::spec;

use crate::exceptions::exception_from_error;
use crate::spec::{PyAtom,PyBond};

#[pyclass(name=DefaultMolecule)]
pub struct PyDefaultMolecule {
    default_molecule: DefaultMolecule,
}

#[pymethods]
impl PyDefaultMolecule {
    #[new]
    fn new(py_atoms: Vec<PyAtom>, py_bonds: Vec<PyBond>) -> PyResult<Self> {
        let mut atoms = Vec::new();
        let mut bonds = Vec::new();

        for py_atom in py_atoms {
            let atom: molecule::spec::Atom = py_atom.into();
            atoms.push(atom);
        }

        for py_bond in py_bonds {
            let bond: molecule::spec::Bond = py_bond.into();
            bonds.push(bond);
        }

        let molecule = molecule::spec::Molecule{atoms, bonds};
        let default_molecule = match DefaultMolecule::build(molecule) {
            Ok(molecule) => molecule,
            Err(error_type) => return Err(exception_from_error(error_type))
        };
        Ok(PyDefaultMolecule{default_molecule})
    }
}