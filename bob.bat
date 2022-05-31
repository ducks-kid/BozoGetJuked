@echo off
cls
echo Protecting NOT from crashes...
echo If you want to close srcds and this script, close the srcds window and type Y depending on your language followed by Enter.
title BossMan's Watchdog
:bob
echo (%time%) BOB started.
echo (%time%) Thanks for turning me on Daddy.
echo Jk it was a joke lol.

start /wait main.py

echo (%time%) WARNING: BOB closed or crashed, restarting.
goto bob 