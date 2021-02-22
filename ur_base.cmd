1>2# : ^
"""
@echo off
rem Name:     UnRen.cmd
rem Purpose:  One click tool wrapper for the work on game engine files
rem Author:   github/madeddy
rem Revision: Feb 2021

echo Here is much space for endless speeches
echo Or not...




rem config
rem --------------------------------------------------------------------------------
setlocal enabledelayedexpansion
set "version=vers_placeholder"
rem for /f "skip=1 tokens=2 delims='" %%x in (
rem	'type _x_vers.py^|find "version"') do set version=%%x
title "UnRen for Windows v%version%"
mode con: cols=90 lines=50
rem set "PYTHONIOENCODING=UTF-8"
set "base_pth=%~dp0"

rem Script loc check
rem --------------------------------------------------------------------------------
:init
rem lets assume the ideal loc (script sits in the games base-dir)
if exist "game" if exist "lib" if exist "renpy" (
	goto :arch
)

rem or if one below we shorten the path
if exist "..\game" if exist "..\lib" if exist "..\renpy" (
    for %%X in ("%base_pth:~0,-1%") do set base_pth=%%~dpX
    goto :arch
) else goto :err_path

:arch
rem Python architecture paths
set "python32dir=%base_pth%lib\windows-i686\"
set "python64dir=%base_pth%lib\windows-x86_64\"

rem Future: On Renpy 8 (py3) we will have 64bit support for win
rem if "%processor_architecture%" equ "AMD64" (
rem     set "python_pth=%base_pth%lib\windows-x86_64\"
rem ) else (
rem     set "python_pth=%base_pth%lib\windows-i686\"
rem )

if exist "%python64dir%" (
    set "pythondir=%python64dir%"
    goto :set_paths
)

if exist "%python32dir%" (
    set "pythondir=%python32dir%"
    goto :set_paths
) else goto :err_py


rem py check
rem --------------------------------------------------------------------------------
:py_check
set "pyexe=%pythondir%python.exe"

if not exist "%pyexe%" (
	goto :err_py
)
goto :run_py


rem Script in wrong location error
rem --------------------------------------------------------------------------------
:err_path
echo    ! Error: The location of UnRen appears to be wrong. It should be
echo             in the game's root directory. 
echo             e.g. '.../{Here_Your_Games_Name}/'  <- here (directories
                 'game', 'lib', 'renpy' are present)
echo/
goto :term


rem Missing python error
rem --------------------------------------------------------------------------------
:err_py
echo    ! Error: Cannot locate python.exe, unable to continue.
echo             Check in directory "%pythondir%" for the executable.
echo/
goto :term


rem Bad end message after error
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


rem Here are the "Kingdom of Python" --- lets go
rem --------------------------------------------------------------------------------
:run_py
rem Works in 7 exit /b !errorlevel!
"%pyexe%" -xEO "%~f0" %* & goto :end
"""
batch_placeholder
