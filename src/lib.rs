use pyo3::prelude::*;
use pyo3::wrap_pymodule;

mod exceptions;
mod element;
mod bond_order;
mod parity;
mod spec;
mod default_molecule;

#[pymodule]
pub fn element(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<element::PyElement>()?;
    Ok(())
}

#[pymodule]
pub fn bond_order(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<bond_order::PyBondOrder>()?;
    Ok(())
}

#[pymodule]
pub fn parity(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<parity::PyParity>()?;
    Ok(())
}

#[pymodule]
pub fn spec(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<spec::PyAtom>()?;
    m.add_class::<spec::PyBond>()?;
    Ok(())
}

#[pymodule]
pub fn molecule(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<default_molecule::PyDefaultMolecule>()?;
    Ok(())
}


#[pymodule]
fn liboxmol(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_wrapped(wrap_pymodule!(element))?;
    m.add_wrapped(wrap_pymodule!(bond_order))?;
    m.add_wrapped(wrap_pymodule!(parity))?;
    m.add_wrapped(wrap_pymodule!(spec))?;
    m.add_wrapped(wrap_pymodule!(molecule))?;
    Ok(())
}