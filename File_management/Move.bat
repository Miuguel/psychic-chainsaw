@echo off
setlocal enabledelayedexpansion

REM Defina o caminho da pasta de destino
set "destino=E:\Music"

REM Navegue até a pasta raiz onde estão as subpastas
cd /d "E:\Music"

REM Loop através de todas as subpastas
for /d %%a in (*) do (
    REM Mova todos os arquivos da subpasta para a pasta de destino
    move "%%a\*.*" "!destino!" >nul

    REM Loop através das sub-subpastas dentro desta subpasta
    for /d %%b in ("%%a\*") do (
        REM Mova os arquivos das sub-subpastas para a pasta de destino
        move "%%b\*.*" "!destino!" >nul

        REM Loop através das sub-sub-subpastas dentro desta sub-subpasta
        for /d %%c in ("%%b\*") do (
            REM Mova os arquivos das sub-sub-subpastas para a pasta de destino
            move "%%c\*.*" "!destino!" >nul
        )
    )
)

echo Arquivos movidos com sucesso!
pause
