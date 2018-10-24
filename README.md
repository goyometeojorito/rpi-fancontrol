# rpi-fancontrol
Script to control the fan of the Raspberry Pi2 / 3 using PWM and the internal temperature sensor

# How it's work

A transistor is used as a switch to turn the fan on and off quickly (PWM pulse) and so depending on how long it is turned on and how long off the fan speed can be regulated. A capacitor is used to "soften" the signal that receives the fan and thus makes less noise

The phython script make a PWM based on the temperature of the CPU, if the temperature is low, the fan will be off (0%), if the temperature starts to rise, a gentle pulse will be made and if the temperature is too high it will be set to the maximum (100%) in the script there is a table with the relationship between temperature and percentage values that can be changed

PWM example
```
50% of pulse
     ____      ____      ____     5v
    |    |    |    |    |    |
____|    |____|    |____|    |___ 0v

25% of pulse
     _         _         _        5v
    | |       | |       | |
____| |_______| |_______| |______ 0v

75% of pulse
     _______   _______   _______  5v
    |       | |       | |       |
____|       |_|       |_|       |_0v

```

# The electronic connection

Components:

- 1 NPN transistor (2n2222A) or compatible
- 1 Capacitor of 100nF or more (try with another values, low values the fan make noise)

## Circuit in protoboard
![Protoboard](https://github.com/goyometeojorito/rpi-fancontrol/raw/master/protoboard.png)

## Circuit in real
I use a female connector to put the cables to the RPi, (you can omit and connect directly)

![Circuit](https://github.com/goyometeojorito/rpi-fancontrol/raw/master/circuit.png)

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

edit the _runfancontrol.sh_ and fix the path to the _fancontrol.py_ with the path where you copied it

now open the crontab editor (for the sudo account)

```
sudo crontab -e
```

and write in bottom (don't forget the @ and change with your path):

```
@reboot sh /home/osmc/runfancontrol.sh
```

and all it's done.

If you can call the python script directly from the crontab without hanging the system, tell my how.
Currently the "sh" script launch the python in a separate process (with the "&" symbol).
