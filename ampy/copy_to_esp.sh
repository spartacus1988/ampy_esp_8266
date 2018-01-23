#!/bin/sh
ampy -p /dev/ttyUSB0 put $HOME/ampy/ampy_esp_8266/ampy/boot.py  /boot.py
ampy -p /dev/ttyUSB0 put $HOME/ampy/ampy_esp_8266/ampy/HTTPsServer.py  /HTTPsServer.py
ampy -p /dev/ttyUSB0 put $HOME/ampy/ampy_esp_8266/ampy/connect.py  /connect.py
ampy -p /dev/ttyUSB0 put $HOME/ampy/ampy_esp_8266/ampy/extract_credential.py  /extract_credential.py
ampy -p /dev/ttyUSB0 put $HOME/ampy/ampy_esp_8266/ampy/credentials.txt  /credentials.txt

ampy -p /dev/ttyUSB0 mkdir lib
ampy -p /dev/ttyUSB0 mkdir /lib/uasyncio
ampy -p /dev/ttyUSB0 put $HOME/ampy/ampy_esp_8266/ampy/micropython-uasyncio/__init__.py  /lib/uasyncio/__init__.py
ampy -p /dev/ttyUSB0 put $HOME/ampy/ampy_esp_8266/ampy/micropython-uasyncio/core.mpy  /lib/uasyncio/core.mpy
echo "All files was copied successful"
