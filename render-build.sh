#!/usr/bin/env bash
# Salir si ocurre un error
set -o errexit
# Instalar dependencias
pip install --upgrade pip
pip install -r requirements.txt
