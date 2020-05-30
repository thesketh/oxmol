if ! rustup.exe -V > /dev/null 2>&1; then
    if [ ! -d "${HOME}/.cargo" ]; then
        cd install_rust
        ./install_rust_windows.sh
        cd ../
    fi
    export PATH="${PATH}:${HOME}/.cargo/bin"
fi

if [ ! -d "conda" ]; then
    cd conda_envs
    if ! ./setup_conda_windows.sh; then
        echo "Failed to install conda"
        cd ../
        exit 1
    fi
    cd ../
fi

if ! conda activate base > /dev/null 2>&1; then
    SHELL=$(basename "${SHELL}")
    source "${HOME}/.${SHELL}_profile"
fi

for env in python36 python37 python38; do
    conda activate $env
    cd ../
    maturin build -i "$(which python)" --release
    # PyPy3 not supported on 64-bit Windows.
    # if which pypy3 > /dev/null; then
    #     maturin build -i "$(which pypy3)" --release
    # fi
    conda deactivate
    cd deployment
done
