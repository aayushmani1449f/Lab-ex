$ErrorActionPreference="Stop"
$venv=".venv"
if (!(Test-Path $venv)) { python -m venv $venv }
& "$venv\Scripts\python.exe" -m pip install --upgrade pip
& "$venv\Scripts\python.exe" -m pip install -r "requirements.txt"
Write-Output "Environment ready. Run scripts with .venv\Scripts\python.exe."
