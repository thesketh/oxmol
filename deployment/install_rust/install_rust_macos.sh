#!/bin/sh
if ! rustup -V > /dev/null 2>&1; then
    if [ ! -f rustup-init ]; then
        wget https://static.rust-lang.org/rustup/dist/x86_64-apple-darwin/rustup-init
    fi
    chmod +x rustup-init
    ./rustup-init --default-toolchain nightly --profile minimal -y
    echo '[target.x86_64-apple-darwin]\nrustflags = [\n"-C", "link-arg=-undefined",\n"-C", "link-arg=dynamic_lookup",\n]\n' >> ~/.cargo/config
fi
