import RPi.GPIO as GPIO
import time
import os

# tempStep is the temperature, speedSteps is the PWM percent for the same index of temperature 
tempSteps =  [0, 20, 30, 40, 45, 50, 55, 60, 65, 70,  75,  80,  90]
speedSteps = [0,  0,  0,  0,  0,  6,  8, 10, 15, 50, 100, 100, 100]

# speedSteps: 0 is Fan OFF, 100% is Fan at 100%, 45, 50, 55 degrees is the normal temperature, put the speed in low speed for low noise 

# pin for PWM signal
PIN_TO_PWM = 25

# configure the GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_TO_PWM, GPIO.OUT)

class FanControl():

    def getCPUtemp(self):
        # get the current temperature in 1000 = 1 degree (must be divided by 1000 to get number in degrees)
        cTemp = os.popen('cat /sys/class/thermal/thermal_zone0/temp').readline()
        return float(cTemp.replace("\n",""))/1000.0

    def run(self):
        # set the PWM frecuency to 300Hz, if change to lower value the Fan make noise in each pulse
        p = GPIO.PWM(PIN_TO_PWM, 300)

        # start PWM in 0% when read the temperature will be changed to correct value
        p.start(0)
        while True:
            # get the current temperature in degrees
            CPU_temp = self.getCPUtemp()

            # the cycle of PWM by default must be off
            cycle = 0

            # search the correct cycle, the values are iterated from the largest to find one that is greater than the current temperature
            for i in range(len(tempSteps)-1, 0, -1):
                if CPU_temp >= tempSteps[i]:
                    cycle = speedSteps[i]
                    break

            # change the DutyCycle to the correct value
            p.ChangeDutyCycle(cycle)

            # wait x seconds. To use less CPU use a longer time but 10 seconds between each reading is fine
            time.sleep(10)



print "Fan control started"
fancontrol = FanControl()
fancontrol.run()

