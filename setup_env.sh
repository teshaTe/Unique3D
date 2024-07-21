#!/bin/bash

# Stop the script on any error
set -e

# Attempt to find Conda's base directory and source it (required for `conda activate`)
CONDA_BASE=$(conda info --base)

if [ -z "${CONDA_BASE}" ]; then
    echo "Conda is not installed or not in the PATH"
    exit 1
fi

PATH="${CONDA_BASE}/bin/":$PATH
source "${CONDA_BASE}/etc/profile.d/conda.sh"

# Create conda environment and activate it
conda env create -f conda_env.yml
conda activate unique-3d-env
conda info --env

CUDA_HOME=${CONDA_PREFIX}
pip install git+https://github.com/NVlabs/nvdiffrast.git
pip install git+https://github.com/facebookresearch/pytorch3d.git@stable
pip install onnxruntime-gpu==1.18.0 --extra-index-url https://aiinfra.pkgs.visualstudio.com/PublicPackages/_packaging/onnxruntime-cuda-12/pypi/simple/
pip install ort_nightly_gpu torch_scatter  nvidia-pyindex tensorrt-cu12==10.2.0.post1

# Store the path of the Conda interpreter
CONDA_INTERPRETER_PATH=$(which python)
