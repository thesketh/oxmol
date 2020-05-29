if ! rustup -V; then
    cd install_rust
    ./install_rust_linux.sh
    cd ../
fi

cd conda_envs
./setup_conda_linux.sh
cd ../

for env in python36 python37 python38; do
    conda activate $env
    cd ../
    maturin build -i $(which python3) --release
    if $(which pypy3); then
        maturin build -i $(which pypy3) --release
    fi
    conda deactivate
    cd development
done