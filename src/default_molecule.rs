// use pyo3::class::PyObjectProtocol;
use std::convert::TryFrom;
use pyo3::prelude::*;
use pyo3::class::PyObjectProtocol;

use molecule::default_molecule::DefaultMolecule;
use molecule::molecule::Molecule;

use gamma::graph::Graph;
use crate::exceptions::*;
use crate::spec::{PyAtomSpec,PyBondSpec};
use crate::element::PyElement;
use crate::parity::PyParity;
use crate::bond_order::PyBondOrder;

#[pyclass(subclass)]
pub struct PyDefaultMolecule {
    default_molecule: DefaultMolecule,
    #[pyo3(get)]
    nodes: Vec<usize>,
    #[pyo3(get)]
    edges: Vec<(usize, usize)>,
}

#[pymethods]
impl PyDefaultMolecule {
    #[new]
    fn new(py_atoms: Vec<PyAtomSpec>, py_bonds: Vec<PyBondSpec>) -> PyResult<Self> {
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

        let nodes = (0..atoms.len()).collect();

        let molecule = molecule::spec::Molecule{atoms, bonds};
        let default_molecule = match DefaultMolecule::build(molecule) {
            Ok(molecule) => molecule,
            Err(error_type) => return Err(exception_from_error(error_type))
        };

        let mut edges = Vec::new();
        for (sid, tid) in default_molecule.edges() {
            let edge = (*sid, *tid);
            edges.push(edge);
        }
        Ok(PyDefaultMolecule{ default_molecule, edges, nodes })
    }

    fn is_empty(&self) -> PyResult<bool> {
        Ok(self.nodes.is_empty())
    }

    fn order(&self) -> PyResult<usize> {
        Ok(self.nodes.len())
    }

    fn size(&self) -> PyResult<usize> {
        Ok(self.edges.len())
    }

    fn has_node(&self, id: usize) -> PyResult<bool> {
        match self.nodes.get(id) {
            Some(_) => Ok(true),
            None => Ok(false),
        }
    }

    fn has_edge(&self, sid: usize, tid: usize) -> PyResult<bool> {
        match self.default_molecule.has_edge(&sid, &tid) {
            Ok(result) => Ok(result),
            Err(graph_error) => Err(exception_from_graph_error(graph_error))
        }
    }

    fn neighbors(&self, id: usize) -> PyResult<Vec<usize>> {
        let mut neighbors = Vec::with_capacity(6);

        match self.default_molecule.neighbors(&id) {
            Ok(iterator) => {
                for neighbor_id in iterator {
                    neighbors.push(*neighbor_id);
                }
                Ok(neighbors)
            },
            Err(graph_error) => {
                let error = exception_from_graph_error(graph_error);
                Err(error)
            }
        }
    }

    fn degree(&self, id: usize) -> PyResult<usize> {
        match self.default_molecule.degree(&id) {
            Ok(degree) => Ok(degree),
            Err(graph_error) => Err(generic_exception(graph_error))
        }
    }

    fn element(&self, id: usize) -> PyResult<PyElement> {
        match self.default_molecule.element(&id) {
            Ok(element) => Ok(PyElement::from(element)),
            Err(graph_error) => Err(exception_from_graph_error(graph_error))
        }
    }

    fn isotope(&self, id: usize) -> PyResult<Option<u16>> {
        match self.default_molecule.isotope(&id) {
            Ok(isotope) => Ok(isotope),
            Err(graph_error) => Err(exception_from_graph_error(graph_error))
        }
    }

    fn electrons(&self, id: usize) -> PyResult<u8> {
        match self.default_molecule.electrons(&id) {
            Ok(electrons) => Ok(electrons),
            Err(graph_error) => Err(exception_from_graph_error(graph_error))
        }
    }

    fn hydrogens(&self, id: usize) -> PyResult<u8> {
        match self.default_molecule.hydrogens(&id) {
            Ok(hydrogens) => Ok(hydrogens),
            Err(graph_error) => Err(exception_from_graph_error(graph_error))
        }
    }

    fn charge(&self, id: usize) -> PyResult<i8> {
        match self.default_molecule.charge(&id) {
            Ok(charge) => Ok(charge),
            Err(graph_error) => Err(exception_from_graph_error(graph_error))
        }
    }

    fn atom_parity(&self, id: usize) -> PyResult<Option<PyParity>> {
        match self.default_molecule.atom_parity(&id) {
            Ok(parity) => {
                match parity {
                    Some(parity) => Ok(Some(PyParity::from(parity))),
                    None => Ok(None)
                }
            },
            Err(graph_error) => Err(exception_from_graph_error(graph_error))
        }
    }

    fn bond_order(&self, sid: usize, tid: usize) -> PyResult<PyBondOrder> {
        match self.default_molecule.bond_order(&sid, &tid) {
            Ok(bond_order) => {
                match PyBondOrder::try_from(bond_order) {
                    Ok(bond_order) => Ok(bond_order),
                    Err(error_message) => Err(get_ValueError(error_message))
                }
            }
            Err(graph_error) => Err(exception_from_graph_error(graph_error))
        }
    }

    fn bond_parity(&self, sid: usize, tid: usize) -> PyResult<Option<PyParity>> {
        match self.default_molecule.bond_parity(&sid, &tid) {
            Ok(parity) => {
                match parity {
                    Some(parity) => Ok(Some(PyParity::from(parity))),
                    None => Ok(None)
                }
            }
            Err(graph_error) => Err(exception_from_graph_error(graph_error))
        }
    }
}

#[pyproto]
impl PyObjectProtocol for PyDefaultMolecule {
    fn __repr__(&self) -> PyResult<String> {
        let n_atoms = self.nodes.len();
        let n_bonds = self.edges.len();

        Ok(format!(
            "PyDefaultMolecule with {} atoms, {} bonds.", 
            n_atoms, 
            n_bonds
        ))
    }
}