if ! conda -V > /dev/null 2>&1; then
    CONDA="Miniconda3-latest-Linux-x86_64.sh"
    if [ ! -f ${CONDA} ]; then
        wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
    fi
    chmod +x "./${CONDA}"
    echo "Installing conda."
    if ! ./"${CONDA}" -b -p ../conda > /dev/null 2>&1; then
        echo "Something went wrong with the installation."
        exit 1
    fi

    export PATH="../conda/bin:$PATH"
    SHELL="$(basename ${SHELL})"
    conda init ${SHELL}
fi

if ! conda activate base > /dev/null 2>&1; then
    SHELL="$(basename ${SHELL})"
    echo "Couldn't use `conda activate`. Re-sourcing ${HOME}/.${SHELL}rc"
    source "~/.${SHELL}rc"
    if ! coda activate base > /dev/null 2>&1; then
        echo "Can't use `conda activate`."
        exit 1
    fi
fi

for env in python36 python37 python38; do
    if ! conda activate "${env}" > /dev/null 2>&1; then
        conda env create -f "${env}.yml"
    else
        echo "`${env}` already created."
    fi
    conda deactivate
done