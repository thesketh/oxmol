use pyo3::class::PyObjectProtocol;
use pyo3::prelude::*;

use molecule::spec::{Atom,Bond};

use crate::exceptions::get_ValueError;
use crate::element::PyElement;
use crate::bond_order::PyBondOrder;
use crate::parity::PyParity;


#[pyclass(name=AtomSpec)]
#[derive(Copy,Clone,Debug)]
pub struct PyAtom {
    pub element: PyElement,
    pub hydrogens: u8,
    pub ion: i8,
    pub isotope: Option<u16>,
    pub parity: Option<PyParity>
}

impl Into<Atom> for PyAtom {
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

impl From<Atom> for PyAtom {
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
impl PyAtom {
    #[new]
    fn new(element: PyElement, hydrogens: u8, ion: Option<i8>, isotope: Option<u16>, parity: Option<PyParity>) -> Self {
        let ion = match ion {
            Some(value) => value,
            None => 0,
        };
        Self {element, hydrogens, ion, isotope, parity}
    }

    #[getter]
    fn element(&self) -> PyResult<PyElement> {
        Ok(self.element)
    }

    #[getter]
    fn hydrogens(&self) -> PyResult<u8> {
        Ok(self.hydrogens)
    }

    #[getter]
    fn ion(&self) -> PyResult<i8> {
        Ok(self.ion)
    }

    fn isotope(&self) -> PyResult<Option<u16>> {
        Ok(self.isotope)
    }

    fn parity(&self) -> PyResult<Option<PyParity>> {
        Ok(self.parity)
    }
}

#[pyproto]
impl PyObjectProtocol for PyAtom {
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
            "Atom {{ {:?}, {} hydrogens, Charge: {}, Isotope: {}, Parity: {} }}", 
            self.element.element, self.hydrogens, self.ion, isotope, parity
        ))
    }
}


#[pyclass(name=BondSpec)]
#[derive(Copy,Clone,Debug)]
pub struct PyBond {
    pub sid: usize,
    pub tid: usize,
    pub order: PyBondOrder,
    pub parity: Option<PyParity>
}

impl From<Bond> for PyBond {
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

impl Into<Bond> for PyBond {
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
impl PyBond {
    #[new]
    fn new(sid: usize, tid: usize, order: PyBondOrder, parity: Option<PyParity>) -> PyResult<Self> {
        if sid == tid {
            return Err(get_ValueError("Can't bond atom to itself"));
        }

        Ok(PyBond{sid, tid, order, parity})
    }
}

#[pyproto]
impl PyObjectProtocol for PyBond {
    fn __repr__(&self) -> PyResult<String> {
        let parity = match self.parity {
            Some(parity) => format!("{:?}", parity.parity),
            None => "None".to_string()
        };

        Ok(format!(
            "Bond {{ Start: {}, End: {}, {:?}, Parity: {} }}", 
            self.sid, self.tid, self.order.bond_order, parity
        ))
    }
}