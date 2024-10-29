@echo off
REM Script para configurar y ejecutar el proyecto en Windows

REM Crear un entorno virtual llamado "venv"
echo Creando el entorno virtual...
python -m venv venv

REM Activar el entorno virtual
echo Activando el entorno virtual...
call venv\Scripts\activate

REM Instalar los requerimientos
echo Instalando dependencias desde requirements.txt...
pip install -r requirements.txt