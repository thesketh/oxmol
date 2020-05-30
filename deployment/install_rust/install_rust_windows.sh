#!/bin/sh
if ! rustup -V > /dev/null 2>&1; then
    if [ ! -f rustup-init ]; then
        curl "https://static.rust-lang.org/rustup/dist/x86_64-pc-windows-gnu/rustup-init.exe" --output "rustup-init.exe"
    fi
    chmod +x ./rustup-init.exe
    ./rustup-init.exe --default-toolchain nightly --profile minimal -y
fi