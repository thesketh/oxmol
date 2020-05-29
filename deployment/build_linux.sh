if ! rustup -V /dev/null 2>&1; then
    if [ ! -d "${HOME}/.cargo" ]; then
        cd install_rust
        ./install_rust_linux.sh
        cd ../
    fi
    source "${HOME}/.profile"
fi

if ! conda -V > /dev/null 2>&1; then
    if [ ! -d "conda" ]; then
        cd conda_envs
        if ! ./setup_conda_linux.sh; then
            echo "Failed to install conda"
            cd ../
            exit 1
        fi
        cd ../
    fi
    export PATH="conda/bin:${PATH}"
fi

if ! conda activate base > /dev/null 2>&1; then
    SHELL=$(basename "${SHELL}")
    source "${HOME}/.${SHELL}rc"
fi

for env in python36 python37 python38; do
    conda activate $env
    cd ../
    maturin build -i $(which python3) --release
    if which pypy3 > /dev/null; then
        maturin build -i $(which pypy3) --release
    fi
    conda deactivate
    cd deployment
done
