use crate::exceptions::get_NotImplementedError;

use molecule::parity::Parity;
use pyo3::class::{PyObjectProtocol, basic::CompareOp};
use pyo3::prelude::*;

#[pyclass(subclass)]
#[derive(Copy,Clone,Debug)]
pub struct PyParity {
    pub parity: Parity,
}

impl From<bool> for PyParity {
    fn from(value: bool) -> Self {
        let parity = match value {
            true => Parity::Positive,
            false => Parity::Negative,
        };

        Self{parity}
    }
}

impl From<Parity> for PyParity {
    fn from(parity: Parity) -> Self {
        Self{parity}
    }
}

impl Into<Parity> for PyParity {
    fn into(self) -> Parity {
        self.parity
    }
}

#[pymethods]
impl PyParity {
    #[new]
    fn new(value: bool) -> Self {
        Self::from(value)
    }
}

#[pyproto]
impl PyObjectProtocol for PyParity {
    fn __repr__(&self) -> PyResult<String> {
        Ok(format!("Parity::{:?}", self.parity))
    }

    fn __hash__(&self) -> PyResult<isize> {
        match self.parity {
            Parity::Positive => Ok(1),
            Parity::Negative => Ok(-1),
        }
    }

    fn __richcmp__(&self, other: Self, op: CompareOp) -> PyResult<bool> {
        let value = match op {
            CompareOp::Eq => self.parity == other.parity,
            CompareOp::Ne => self.parity != other.parity,
            _ => return Err(get_NotImplementedError("Operator not implemented."))
        };
        Ok(value)
    }
}