from machine import Pin
from time import sleep
from s2pico_oled import OLED
from machine import Pin, I2C
from thermocouple import MAX6675

led1 = Pin(7, Pin.OUT)
led2 = Pin(6, Pin.OUT)

i2c = I2C(0, sda=Pin(8), scl=Pin(9))
oled = OLED(i2c, Pin(18))

rsteak = Pin(15, Pin.IN, Pin.PULL_UP)
mrsteak = Pin(16, Pin.IN, Pin.PULL_UP)
msteak = Pin(17, Pin.IN, Pin.PULL_UP)
wdsteak = Pin(21, Pin.IN, Pin.PULL_UP)
cancel = Pin(14, Pin.IN, Pin.PULL_UP)

therm = MAX6675(cs=Pin(2), sck=Pin(1), so=Pin(3))

temp = therm.read()

def display_temp(CurrentTemp, Temp):
    oled.fill(0)
    oled.text(CurrentTemp, 0, 10, 1)
    oled.text(str(Temp), 0, 20, 1)
    oled.show()

while True:
    temp = therm.read()
    if rsteak.value() == 0:
        while True:
            temp = therm.read()
            display_temp("Current Temp:", temp)
            oled.text("Cook: Rare", 0, 0, 1)
            oled.show()
            print(temp)
            sleep(1)
            if temp >= 48.8:
                oled.fill(0)
                oled.text("Rare steak ready", 0, 0, 1)
                oled.show()
                led1.on()
                led2.on()
                print("Rare steak ready")
                sleep(30)
                break
            elif cancel.value() == 0:
                break
                
    elif mrsteak.value() == 0:
        while True:
            temp = therm.read()
            display_temp("Current Temp:", temp)
            oled.text("Cook: Med-Rare", 0, 0, 1)
            oled.show()
            print(temp)
            sleep(1)
            if temp >= 54.4:
                oled.fill(0)
                oled.text("Medium rare", 0, 0, 1)
                oled.text("steak ready", 0, 10, 1)
                oled.show()
                led1.on()
                led2.on()
                print("Medium rare steak ready")
                sleep(30)
                break
            elif cancel.value() == 0:
                break
    elif msteak.value() == 0:
        while True:
            temp = therm.read()
            display_temp("Current Temp:", temp)
            oled.text("Cook: Medium", 0, 0, 1)
            oled.show()
            print(temp)
            sleep(1)
            if temp >= 57.2:
                oled.fill(0)
                oled.text("Medium steak", 0, 0, 1)
                oled.text("ready", 0, 10, 1)
                oled.show()
                led1.on()
                led2.on()
                print("Medium steak ready")
                sleep(30)
                break
            elif cancel.value() == 0:
                break
    elif wdsteak.value() == 0:
        while True:
            temp = therm.read()
            display_temp("Current Temp:", temp)
            oled.text("Cook: Well Done", 0, 0, 1)
            oled.show()
            print(temp)
            sleep(1)
            if temp >= 65.5:
                oled.fill(0)
                oled.text("Well done steak", 0, 0, 1)
                oled.text("ready", 0, 10, 1)
                oled.show()
                led1.on()
                led2.on()
                print("Well done steak ready")
                sleep(30)
                break
            elif cancel.value() == 0:
                break
    else:
        oled.fill(0)
        oled.text("Select desired", 0, 0, 1)
        oled.text("cook:WD M MR R", 0, 10, 1)
        oled.text("CANCEL", 35, 24, 1)
        oled.show()
        led1.off()
        led2.off()
        print("Select desired cook")
        sleep(1)
        