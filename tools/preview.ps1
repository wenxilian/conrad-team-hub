# 项目内预览，不修改全局环境。
$ErrorActionPreference = 'Stop'
Set-Location (Split-Path $PSScriptRoot -Parent)
& ./.venv/Scripts/python.exe -m mkdocs serve -a 127.0.0.1:8000
