if ! conda -V; then
    CONDA="Miniconda3-latest-Linux-x86_64.sh"
    if [ ! -f ${CONDA} ]; then
        wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
    fi
    chmod +x "./${CONDA}"
    ./"${CONDA}" -b -p ../conda
    export PATH="../conda/bin:$PATH"
    SHELL="$(basename ${SHELL})"
    conda init ${SHELL}
    source "~/.${SHELL}rc"
fi

for env in python36 python37 python38; do
    if ! conda activate "${env}"; then
        conda env create -f "${env}.yml"
    else
        conda deactivate
    fi
done