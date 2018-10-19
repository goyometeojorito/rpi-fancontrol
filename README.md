# rpi-fancontrol
Script to control the fan of the Raspberry Pi2 / 3 using PWM and the internal temperature sensor

# Instalation guide

## Pre-requisites
You need python and the library RPi.GPIO (for python)
and crontab (for automatic start on poweron)

## Instalation
Copy the files in you Raspberry Pi. Remember the path

in the shell, type the commands:

```
sudo chmod 775 fancontrol.py
sudo chown root fancontrol.py

sudo chmod 775 runfancontrol.sh
sudo chown root runfancontrol.sh
```

now open the crontab editor (for the sudo account)

```
sudo crontab -e
```

and write in bottom (don't forget the @):

```
@reboot sh /home/osmc/runfancontrol.sh
```

and all it's done
