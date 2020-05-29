#!/bin/sh
if ! rustup -V > /dev/null 2>&1; then
    if [ ! -f rustup-init ]; then
        wget https://static.rust-lang.org/rustup/dist/x86_64-unknown-linux-gnu/rustup-init
    fi
    chmod +x rustup-init
    ./rustup-init --default-toolchain nightly --profile minimal -y
fi