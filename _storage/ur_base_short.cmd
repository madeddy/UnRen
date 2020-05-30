1>2# : ^
"""
@echo off

echo Here is much space for endless speeches about this cool app
echo Or not...



rem Basic config
rem --------------------------------------------------------------------------------
setlocal enabledelayedexpansion
set "version=0.12.0-alpha"
title "UnRen for Windows v%version%"
mode con: cols=90 lines=50


rem Kingdom of python --- lets go
rem --------------------------------------------------------------------------------
"python" -xEO "%~f0" %* & exit /b !errorlevel!
"""
batch_placeholder
