@echo off
setlocal

echo ============================================
echo  Dead Cells Archipelago Installer - Build
echo ============================================
echo.

REM Vérifie que dotnet est disponible
where dotnet >nul 2>&1
if errorlevel 1 (
    echo [ERREUR] 'dotnet' introuvable. Installe le SDK .NET 8+ :
    echo   https://dotnet.microsoft.com/download
    pause
    exit /b 1
)

echo [1/2] Restauration des packages NuGet...
dotnet restore
if errorlevel 1 ( echo Echec de la restauration. & pause & exit /b 1 )

echo.
echo [2/2] Compilation en Release...
dotnet build -c Release -o publish\
if errorlevel 1 ( echo Echec de la compilation. & pause & exit /b 1 )

echo.
echo ============================================
echo  Build termine !
echo  Exe disponible dans : publish\DeadCellsInstaller.exe
echo ============================================
pause
