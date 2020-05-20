// use pyo3::class::PyObjectProtocol;
use std::convert::TryFrom;
use pyo3::prelude::*;

use molecule::default_molecule::DefaultMolecule;
use molecule::molecule::Molecule;

use gamma::graph::Graph;
use crate::exceptions::*;
use crate::spec::{PyAtom,PyBond};
use crate::element::PyElement;
use crate::parity::PyParity;
use crate::bond_order::PyBondOrder;

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

    fn is_empty(&self) -> PyResult<bool> {
        Ok(self.default_molecule.is_empty())
    }

    fn order(&self) -> PyResult<usize> {
        Ok(self.default_molecule.order())
    }

    fn size(&self) -> PyResult<usize> {
        Ok(self.default_molecule.size())
    }

    fn nodes(&self) -> PyResult<Vec<usize>> {
        let mut nodes = Vec::new();

        for item in self.default_molecule.nodes() {
            nodes.push(*item);
        };

        Ok(nodes)
    }

    fn edges(&self) -> PyResult<Vec<(usize, usize)>> {
        let mut edges = Vec::new();

        for (sid, tid) in self.default_molecule.edges() {
            edges.push((*sid, *tid));
        };

        Ok(edges)
    }

    fn has_node(&self, id: usize) -> PyResult<bool> {
        Ok(self.default_molecule.has_node(&id))
    }

    fn neighbors(&self, id: usize) -> PyResult<Vec<usize>> {
        let mut neighbors = Vec::new();

        let neighbour_iter = match self.default_molecule.neighbors(&id) {
            Ok(iterator) => iterator,
            Err(graph_error) => return Err(exception_from_graph_error(graph_error))
        };

        for neighbor_id in neighbour_iter {
            neighbors.push(*neighbor_id);
        }

        Ok(neighbors)
    }


    fn degree(&self, id: usize) -> PyResult<usize> {
        match self.default_molecule.degree(&id) {
            Ok(degree) => Ok(degree),
            Err(graph_error) => Err(exception_from_graph_error(graph_error))
        }
    }

    fn has_edge(&self, sid: usize, tid: usize) -> PyResult<bool> {
        match self.default_molecule.has_edge(&sid, &tid) {
            Ok(result) => Ok(result),
            Err(graph_error) => Err(exception_from_graph_error(graph_error))
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
