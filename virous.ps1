# $CODE = "
# import os
# os.mkdir('C:\\Users\\Pende\\Documents')
# "

# $SCRIPT = '
# @ECHO OFF
# PowerShell.exe -Command "%USERPROFILE%\AppData\Local\Temp\auto.bat"
# '

# Dynamically creates the files in TEMP
# New-Item -Path $env:TEMP -ItemType "file" -Name "athanee.py" -Value $CODE
# New-Item -Path $env:TEMP -ItemType "file" -Name "auto.bat" -Value $SCRIPT

# Path to execute the the virus
# $ATHANEE = Join-Path -Path $env:TEMP -ChildPath athanee.py

# Starts the process
Start-Process $ATHANEE

# Makes sure that the bin is emptied
# Start-Process -