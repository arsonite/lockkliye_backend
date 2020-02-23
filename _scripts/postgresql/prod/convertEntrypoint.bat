:: Turns off verbose-messages in command prompt
@ECHO OFF

:: Script that utilizes the dos2unix.exe on windows or the dos2unix command on linux
:: to convert the windows line endings of the entrypoint.*.sh file to linux

CALL dos2unix.exe ../../../entrypoint.prod.sh