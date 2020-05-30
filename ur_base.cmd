1>2# : ^
"""
@echo off
rem Name:     UnRen.cmd
rem Purpose:  One clock tool wrapper for the work on game engine files
rem Author:   github/madeddy
rem Revision: March 2020 - initial version

echo Here is much space for endless speeches
echo Or not...




rem config
rem --------------------------------------------------------------------------------
setlocal enabledelayedexpansion
set "version=0.12.1-alpha"
title "UnRen for Windows v%version%"
mode con: cols=90 lines=50
rem set "PYTHONIOENCODING=UTF-8"
set "base_pth=%~dp0"


rem path check
rem --------------------------------------------------------------------------------
:path_check
rem lets assume the ideal (script sits in the games base-dir)
if exist "game" if exist "lib" if exist "renpy" (
	goto :py_check
)

rem or if one below we shorten the path
if exist "..\game" if exist "..\lib" if exist "..\renpy" (
    for %%X in ("%base_pth:~0,-1%") do set base_pth=%%~dpX
	goto :py_check
) else goto :err_path


rem py check
rem --------------------------------------------------------------------------------
:py_check
set "python_pth=%base_pth%lib\windows-i686\"
set "pyexe=%python_pth%python.exe"

rem Future: On Renpy 8 (py3) we will have 64bit support for win
rem if "%processor_architecture%" equ "AMD64" (
rem     set "python_pth=%base_pth%lib\windows-x86_64\"
rem ) else (
rem     set "python_pth=%base_pth%lib\windows-i686\"
rem )

if not exist "%python_pth%python.exe" (
	goto :err_py
)
goto :run_py


rem Script in wrong location error
rem --------------------------------------------------------------------------------
:err_path
echo    ! Error: The location of UnRen appears to be wrong. It should
echo             be in the game's root directory.
echo             (dirs 'game', 'lib', 'renpy' are present)
echo/
goto :term


rem Missing python error
rem --------------------------------------------------------------------------------
:err_py
echo    ! Error: Cannot locate python.exe, unable to continue.
echo             Check in directory "%python_pth%" for the executable.
echo/
goto :term


rem Bad end after error
rem --------------------------------------------------------------------------------
:term
echo/
echo    Terminating.
echo    If a reason was stated try to correct the problem, if not try to
echo    check path and script for possible issues.
echo/
pause>nul|set/p=.            Press any key to exit...
exit 1


:end
endlocal
echo on
exit /b 0


rem Kingdom of python --- lets go
rem --------------------------------------------------------------------------------
:run_py
rem Works in 7 exit /b !errorlevel!
"%python_pth%python.exe" -xEO "%~f0" %* & goto :end
"""
batch_placeholder
