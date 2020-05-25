use pyo3::class::PyObjectProtocol;
use pyo3::prelude::*;

use molecule::spec::{Atom,Bond};

use crate::exceptions::get_ValueError;
use crate::element::PyElement;
use crate::bond_order::PyBondOrder;
use crate::parity::PyParity;


#[pyclass(subclass)]
#[derive(Copy,Clone,Debug)]
pub struct PyAtomSpec {
    #[pyo3(get)]
    pub element: PyElement,
    #[pyo3(get)]
    pub hydrogens: u8,
    #[pyo3(get)]
    pub ion: i8,
    #[pyo3(get)]
    pub isotope: Option<u16>,
    #[pyo3(get)]
    pub parity: Option<PyParity>
}

impl Into<Atom> for PyAtomSpec {
    fn into(self) -> Atom {
        Atom {
            element: self.element.element,
            hydrogens: self.hydrogens,
            ion: self.ion,
            isotope: self.isotope,
            parity: match self.parity {
                Some(parity) => Some(parity.parity),
                None => None
            }
        }
    }
}

impl From<Atom> for PyAtomSpec {
    fn from(atom: Atom) -> Self {
        Self {
            element: PyElement::from(atom.element),
            hydrogens: atom.hydrogens,
            ion: atom.ion,
            isotope: atom.isotope,
            parity: match atom.parity {
                Some(parity) => Some(PyParity::from(parity)),
                None => None,
            }
        }
    }
}

#[pymethods]
impl PyAtomSpec {
    #[new]
    fn new(element: PyElement, hydrogens: u8, ion: i8, isotope: Option<u16>, parity: Option<PyParity>) -> Self {
        Self {element, hydrogens, ion, isotope, parity}
    }
}

#[pyproto]
impl PyObjectProtocol for PyAtomSpec {
    fn __repr__(&self) -> PyResult<String> {
        let parity = match self.parity {
            Some(parity) => format!("{:?}", parity.parity),
            None => "None".to_string()
        };

        let isotope = match self.isotope {
            Some(isotope) => isotope.to_string(),
            None => "None".to_string()
        };

        Ok(format!(
            "PyAtomSpec {{ {:?}, {} hydrogens, Charge: {}, Isotope: {}, Parity: {} }}", 
            self.element.element, self.hydrogens, self.ion, isotope, parity
        ))
    }
}


#[pyclass(subclass)]
#[derive(Copy,Clone,Debug)]
pub struct PyBondSpec {
    #[pyo3(get)]
    pub sid: usize,
    #[pyo3(get)]
    pub tid: usize,
    #[pyo3(get)]
    pub order: PyBondOrder,
    #[pyo3(get)]
    pub parity: Option<PyParity>
}

impl From<Bond> for PyBondSpec {
    fn from(bond: Bond) -> Self {
        Self {
            sid: bond.sid,
            tid: bond.tid,
            order: PyBondOrder::from(bond.order),
            parity: match bond.parity {
                Some(parity) => Some(PyParity::from(parity)),
                None => None
            }
        }
    }
}

impl Into<Bond> for PyBondSpec {
    fn into(self) -> Bond {
        Bond {
            sid: self.sid,
            tid: self.tid,
            order: self.order.into(),
            parity: match self.parity {
                Some(parity) => Some(parity.into()),
                None => None
            }
        }
    }
}

#[pymethods]
impl PyBondSpec {
    #[new]
    fn new(sid: usize, tid: usize, order: PyBondOrder, parity: Option<PyParity>) -> PyResult<Self> {
        if sid == tid {
            return Err(get_ValueError("Can't bond atom to itself"));
        }

        Ok(PyBondSpec{sid, tid, order, parity})
    }
}

#[pyproto]
impl PyObjectProtocol for PyBondSpec {
    fn __repr__(&self) -> PyResult<String> {
        let parity = match self.parity {
            Some(parity) => format!("{:?}", parity.parity),
            None => "None".to_string()
        };

        Ok(format!(
            "PyBondSpec {{ Start: {}, End: {}, {:?}, Parity: {} }}", 
            self.sid, self.tid, self.order.bond_order, parity
        ))
    }
}