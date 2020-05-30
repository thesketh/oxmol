#!/bin/bash
if ! conda -V > /dev/null 2>&1; then
    if [ ! -d ../conda ]; then
        CONDA="Miniconda3-latest-Windows-x86_64.exe"
        if [ ! -f ${CONDA} ]; then
            curl "https://repo.anaconda.com/miniconda/${CONDA}" --output "${CONDA}"
        fi
        chmod +x "./${CONDA}"
        echo "Installing conda."
        if ! cmd //c run_conda_installer.bat > /dev/null 2>&1; then
            echo "Something went wrong with the installation."
            exit 1
        fi
        export PATH="../conda/condabin:$PATH"
        SHELL="$(basename ${SHELL})"
        conda.bat init ${SHELL}
    else
        export PATH="../conda/condabin:$PATH"
    fi
fi

if ! conda.bat activate base > /dev/null 2>&1; then
    SHELL="$(basename ${SHELL})"
    echo "Couldn't use conda activate. Re-sourcing ${HOME}/.${SHELL}rc"
    source "${HOME}/.${SHELL}rc"
    if ! conda activate base > /dev/null 2>&1; then
        echo "Can't use conda activate."
        exit 1
    fi
fi

for env in python36 python37 python38_windows; do
    if ! conda.bat activate "${env}" > /dev/null 2>&1; then
        conda.bat env create -f "${env}.yml"
    else
        echo "${env} already created."
    fi
    conda.bat deactivate
done
