@echo off
:: SISTEMA DE DESPLIEGUE AUTOMATIZADO - TERRENCE.M V4.2
:: Script de un solo clic para inicialización de entorno
echo [1/4] Iniciando Servidor...
start cmd /k "python app.py"

echo [2/4] Verificando Base de Datos...
python -c "from inventario.bd import db; db.create_all(); print('BD Creada')"

echo [3/4] Sincronizando repositorio local...
git add .
git commit -m "AUTOSYNC_SISTEMA_MIGRATORIO"
git push origin main

echo [4/4] Sistema Terrence.m operativo.
pause
