use pyo3::prelude::*;

mod exceptions;
mod element;
mod bond_order;
mod parity;
mod spec;
mod default_molecule;

#[pymodule]
fn oxmol(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<element::PyElement>()?;
    m.add_class::<parity::PyParity>()?;
    m.add_class::<bond_order::PyBondOrder>()?;
    m.add_class::<spec::PyAtomSpec>()?;
    m.add_class::<spec::PyBondSpec>()?;
    m.add_class::<default_molecule::PyDefaultMolecule>()?;
    Ok(())
}