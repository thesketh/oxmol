use pyo3::exceptions;
use pyo3::PyErr;
use molecule::error::Error;

#[allow(non_snake_case)]
pub fn get_ValueError(error_message: &'static str) -> PyErr {
    exceptions::ValueError::py_err(error_message)
}

#[allow(non_snake_case)]
pub fn get_NotImplementedError(error_message: &'static str) -> PyErr {
    exceptions::NotImplementedError::py_err(error_message)
}

pub fn exception_from_error(error: Error) -> PyErr {
    let error_message = match error {
        Error::HypervalentAtom => "Hypervalent atom encountered",
        Error::DuplicateBond => "Duplicate bond encountered",
        Error::MisplacedBond => "Misplaced bond encountered",
        Error::ImpossibleIsotope => "Impossible isotope encountered"
    };

    get_ValueError(error_message)
}