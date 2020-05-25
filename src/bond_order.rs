use std::convert::TryFrom;

use pyo3::class::{PyObjectProtocol, basic::CompareOp};
use pyo3::prelude::*;

use molecule::bond_order::BondOrder;

use crate::exceptions::{get_ValueError, get_NotImplementedError};

#[pyclass(subclass)]
#[derive(Copy,Clone,Debug)]
pub struct PyBondOrder {
    pub bond_order: BondOrder,
}

impl TryFrom<u8> for PyBondOrder {
    type Error = &'static str;

    fn try_from(order: u8) -> Result<Self, Self::Error> {
        let bond_order = match order {
            0 => BondOrder::Zero,
            1 => BondOrder::Single,
            2 => BondOrder::Double,
            3 => BondOrder::Triple,
            _ => return Err("Order outside of expected range [0, 3]")
        };
        Ok(PyBondOrder{ bond_order })
    }    
}

impl From<BondOrder> for PyBondOrder {
    fn from(bond_order: BondOrder) -> Self {
        Self{bond_order}
    }
}

impl Into<BondOrder> for PyBondOrder {
    fn into(self) -> BondOrder {
        self.bond_order
    }
}

#[pymethods]
impl PyBondOrder {
    #[new]
    fn new(order: u8) -> PyResult<Self> {
        match PyBondOrder::try_from(order) {
            Ok(instance) => Ok(instance),
            Err(error_msg) => Err(get_ValueError(error_msg)),
        }
    }

    fn as_int(&self) -> PyResult<u8> {
        let order = match self.bond_order {
            BondOrder::Zero => 0,
            BondOrder::Single => 1,
            BondOrder::Double => 2,
            BondOrder::Triple => 3,
        };
        Ok(order)
    }
}

#[pyproto]
impl PyObjectProtocol for PyBondOrder {
    fn __repr__(&self) -> PyResult<String> {
        Ok(format!("PyBondOrder::{:?}", self.bond_order))
    }

    fn __bool__(&self) -> PyResult<bool> {
        let truthy = match self.bond_order {
            BondOrder::Zero => false,
            BondOrder::Single => true,
            BondOrder::Double => true,
            BondOrder::Triple => true,
        };
        Ok(truthy)
    }

    fn __hash__(&self) -> PyResult<isize> {
        Ok(self.as_int()? as isize)
    }

    fn __richcmp__(&self, other: Self, op: CompareOp) -> PyResult<bool> {
        let value = match op {
            CompareOp::Eq => self.bond_order == other.bond_order,
            CompareOp::Ne => self.bond_order != other.bond_order,
            _ => return Err(get_NotImplementedError("Operator not implemented."))
        };
        Ok(value)
    }
}