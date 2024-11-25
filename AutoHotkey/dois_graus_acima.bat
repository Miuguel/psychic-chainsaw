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

    REM Agora, vamos percorrer as subpastas dentro desta subpasta
    for /d %%b in ("%%a\*") do (
        REM Mova os arquivos da sub-subpasta para a pasta de destino
        move "%%b\*.*" "!destino!" >nul
        
        REM Agora, vamos percorrer as subpastas dentro desta subpasta
        for /d %%b in ("%%a\*") do (
            REM Mova os arquivos da sub-subpasta para a pasta de destino
            move "%%b\*.*" "!destino!" >nul
    )
)

echo Arquivos movidos com sucesso!
pause
