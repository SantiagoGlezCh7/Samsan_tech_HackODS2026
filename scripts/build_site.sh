#!/usr/bin/env bash
set -euo pipefail

# Crear y activar un venv local para CI
PYTHON=python
VENV_DIR=.venv_ci
${PYTHON} -m venv ${VENV_DIR}
source ${VENV_DIR}/bin/activate
python -m pip install --upgrade pip

# Instalar herramientas mínimas para exportar notebooks
pip install nbconvert jupyter

# Instalar dependencias del proyecto si existen
if [ -f requirements.txt ]; then
  pip install -r requirements.txt
fi

# Asegurar carpeta de assets
mkdir -p dashboard/assets

# Exportar notebooks a HTML
python -m nbconvert --to html --output-dir dashboard/assets --output storytelling_outputs notebooks/storytelling.ipynb
python -m nbconvert --to html --output-dir dashboard/assets --output desempleo_outputs notebooks/01_desempleo.ipynb
python -m nbconvert --to html --output-dir dashboard/assets --output infraestructura_outputs notebooks/02_infraestructura.ipynb

# Renderizar sitio Quarto en la carpeta docs usando output-dir
quarto render dashboard --output-dir docs

echo "Build complete: docs/ generado con todos los notebooks."
