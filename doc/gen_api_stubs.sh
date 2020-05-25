#!/bin/bash
rm -rf source
cargo build --release
ln ../target/release/liboxmol.so ../oxmol/oxmol.so
sphinx-apidoc -e -M -o source ../oxmol ../oxmol/test ../oxmol/oxmol.so
rm source/modules.rst
sed -i "s/oxmol package/API Reference/g" source/oxmol.rst
