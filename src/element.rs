use std::convert::TryFrom;

use crate::exceptions::{get_ValueError,get_NotImplementedError};

use molecule::element::Element;
use pyo3::class::{PyObjectProtocol, basic::CompareOp};
use pyo3::types::PyType;
use pyo3::prelude::*;

#[pyclass(name=Element)]
#[derive(Copy,Clone,Debug)]
pub struct PyElement {
    pub element: Element,
}

impl TryFrom<u16> for PyElement {
    type Error = &'static str;

    fn try_from(atomic_number: u16) -> Result<Self, Self::Error> {
        let element = match atomic_number {
            1   => Element::H,
            2   => Element::He,
            3   => Element::Li,
            4   => Element::Be,
            5   => Element::B,
            6   => Element::C,
            7   => Element::N,
            8   => Element::O,
            9   => Element::F,
            10  => Element::Ne,
            11  => Element::Na,
            12  => Element::Mg,
            13  => Element::Al,
            14  => Element::Si,
            15  => Element::P,
            16  => Element::S,
            17  => Element::Cl,
            18  => Element::Ar,
            19  => Element::K,
            20  => Element::Ca,
            21  => Element::Sc,
            22  => Element::Ti,
            23  => Element::V,
            24  => Element::Cr,
            25  => Element::Mn,
            26  => Element::Fe,
            27  => Element::Co,
            28  => Element::Ni,
            29  => Element::Cu,
            30  => Element::Zn,
            31  => Element::Ga,
            32  => Element::Ge,
            33  => Element::As,
            34  => Element::Se,
            35  => Element::Br,
            36  => Element::Kr,
            37  => Element::Rb,
            38  => Element::Sr,
            39  => Element::Y,
            40  => Element::Zr,
            41  => Element::Nb,
            42  => Element::Mo,
            43  => Element::Tc,
            44  => Element::Ru,
            45  => Element::Rh,
            46  => Element::Pd,
            47  => Element::Ag,
            48  => Element::Cd,
            49  => Element::In,
            50  => Element::Sn,
            51  => Element::Sb,
            52  => Element::Te,
            53  => Element::I,
            54  => Element::Xe,
            55  => Element::Cs,
            56  => Element::Ba,
            57  => Element::La,
            58  => Element::Ce,
            59  => Element::Pr,
            60  => Element::Nd,
            61  => Element::Pm,
            62  => Element::Sm,
            63  => Element::Eu,
            64  => Element::Gd,
            65  => Element::Tb,
            66  => Element::Dy,
            67  => Element::Ho,
            68  => Element::Er,
            69  => Element::Tm,
            70  => Element::Yb,
            71  => Element::Lu,
            72  => Element::Hf,
            73  => Element::Ta,
            74  => Element::W,
            75  => Element::Re,
            76  => Element::Os,
            77  => Element::Ir,
            78  => Element::Pt,
            79  => Element::Au,
            80  => Element::Hg,
            81  => Element::Tl,
            82  => Element::Pb,
            83  => Element::Bi,
            84  => Element::Po,
            85  => Element::At,
            86  => Element::Rn,
            87  => Element::Fr,
            88  => Element::Ra,
            89  => Element::Ac,
            90  => Element::Th,
            91  => Element::Pa,
            92  => Element::U,
            93  => Element::Np,
            94  => Element::Pu,
            95  => Element::Am,
            96  => Element::Cm,
            97  => Element::Bk,
            98  => Element::Cf,
            99  => Element::Es,
            100 => Element::Fm,
            101 => Element::Md,
            102 => Element::No,
            103 => Element::Lr,
            104 => Element::Rf,
            105 => Element::Db,
            106 => Element::Sg,
            107 => Element::Bh,
            108 => Element::Hs,
            109 => Element::Mt,
            110 => Element::Ds,
            111 => Element::Rg,
            112 => Element::Cn,
            113 => Element::Nh,
            114 => Element::Fl,
            115 => Element::Mc,
            116 => Element::Lv,
            117 => Element::Ts,
            118 => Element::Og,   
            _ => return Err("Atomic number outside of expected range [1, 118]")
        };
        Ok(PyElement{ element })
    }    
}

impl From<Element> for PyElement {
    fn from(element: Element) -> Self {
        Self{element}
    }
}

impl Into<Element> for PyElement {
    fn into(self) -> Element {
        self.element
    }
}

#[pymethods]
impl PyElement {
    #[new]
    fn new(atomic_number: u16) -> PyResult<Self> {
        match PyElement::try_from(atomic_number) {
            Ok(instance) => Ok(instance),
            Err(error_msg) => Err(get_ValueError(error_msg)),
        }
    }

    #[classmethod]
    fn from_symbol(_cls: &PyType, symbol: String) -> PyResult<Self> {
        let element = match symbol.as_str() {
            "H"  => Element::H,
            "He" => Element::He,
            "Li" => Element::Li,
            "Be" => Element::Be,
            "B"  => Element::B,
            "C"  => Element::C,
            "N"  => Element::N,
            "O"  => Element::O,
            "F"  => Element::F,
            "Ne" => Element::Ne,
            "Na" => Element::Na,
            "Mg" => Element::Mg,
            "Al" => Element::Al,
            "Si" => Element::Si,
            "P"  => Element::P,
            "S"  => Element::S,
            "Cl" => Element::Cl,
            "Ar" => Element::Ar,
            "K"  => Element::K,
            "Ca" => Element::Ca,
            "Sc" => Element::Sc,
            "Ti" => Element::Ti,
            "V"  => Element::V,
            "Cr" => Element::Cr,
            "Mn" => Element::Mn,
            "Fe" => Element::Fe,
            "Co" => Element::Co,
            "Ni" => Element::Ni,
            "Cu" => Element::Cu,
            "Zn" => Element::Zn,
            "Ga" => Element::Ga,
            "Ge" => Element::Ge,
            "As" => Element::As,
            "Se" => Element::Se,
            "Br" => Element::Br,
            "Kr" => Element::Kr,
            "Rb" => Element::Rb,
            "Sr" => Element::Sr,
            "Y"  => Element::Y,
            "Zr" => Element::Zr,
            "Nb" => Element::Nb,
            "Mo" => Element::Mo,
            "Tc" => Element::Tc,
            "Ru" => Element::Ru,
            "Rh" => Element::Rh,
            "Pd" => Element::Pd,
            "Ag" => Element::Ag,
            "Cd" => Element::Cd,
            "In" => Element::In,
            "Sn" => Element::Sn,
            "Sb" => Element::Sb,
            "Te" => Element::Te,
            "I"  => Element::I,
            "Xe" => Element::Xe,
            "Cs" => Element::Cs,
            "Ba" => Element::Ba,
            "La" => Element::La,
            "Ce" => Element::Ce,
            "Pr" => Element::Pr,
            "Nd" => Element::Nd,
            "Pm" => Element::Pm,
            "Sm" => Element::Sm,
            "Eu" => Element::Eu,
            "Gd" => Element::Gd,
            "Tb" => Element::Tb,
            "Dy" => Element::Dy,
            "Ho" => Element::Ho,
            "Er" => Element::Er,
            "Tm" => Element::Tm,
            "Yb" => Element::Yb,
            "Lu" => Element::Lu,
            "Hf" => Element::Hf,
            "Ta" => Element::Ta,
            "W"  => Element::W,
            "Re" => Element::Re,
            "Os" => Element::Os,
            "Ir" => Element::Ir,
            "Pt" => Element::Pt,
            "Au" => Element::Au,
            "Hg" => Element::Hg,
            "Tl" => Element::Tl,
            "Pb" => Element::Pb,
            "Bi" => Element::Bi,
            "Po" => Element::Po,
            "At" => Element::At,
            "Rn" => Element::Rn,
            "Fr" => Element::Fr,
            "Ra" => Element::Ra,
            "Ac" => Element::Ac,
            "Th" => Element::Th,
            "Pa" => Element::Pa,
            "U"  => Element::U,
            "Np" => Element::Np,
            "Pu" => Element::Pu,
            "Am" => Element::Am,
            "Cm" => Element::Cm,
            "Bk" => Element::Bk,
            "Cf" => Element::Cf,
            "Es" => Element::Es,
            "Fm" => Element::Fm,
            "Md" => Element::Md,
            "No" => Element::No,
            "Lr" => Element::Lr,
            "Rf" => Element::Rf,
            "Db" => Element::Db,
            "Sg" => Element::Sg,
            "Bh" => Element::Bh,
            "Hs" => Element::Hs,
            "Mt" => Element::Mt,
            "Ds" => Element::Ds,
            "Rg" => Element::Rg,
            "Cn" => Element::Cn,
            "Nh" => Element::Nh,
            "Fl" => Element::Fl,
            "Mc" => Element::Mc,
            "Lv" => Element::Lv,
            "Ts" => Element::Ts,
            "Og" => Element::Og,            
            _    => return Err(get_ValueError("Not an element"))
        };

        Ok(Self{ element })
    }

    fn valence_electrons(&self) -> u8 {
        self.element.valence_electrons()
    }

    fn atomic_number(&self) -> u16 {
        self.element.atomic_number()
    }

}

#[pyproto]
impl PyObjectProtocol for PyElement {
    fn __repr__(&self) -> PyResult<String> {
        Ok(format!("Element::{:?}", self.element))
    }

    fn __hash__(&self) -> PyResult<isize> {
        Ok(self.atomic_number() as isize)
    }

    fn __richcmp__(&self, other: Self, op: CompareOp) -> PyResult<bool> {
        let value = match op {
            CompareOp::Eq => self.element == other.element,
            CompareOp::Ne => self.element != other.element,
            _ => return Err(get_NotImplementedError("Operator not implemented."))
        };
        Ok(value)
    }
}