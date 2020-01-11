print("-------Connect.py------")

import network
from time import sleep
from machine import Pin
from machine import I2C
import sh1106

i2c = I2C(scl=Pin(22), sda=Pin(23), freq=400000)
display = sh1106.SH1106_I2C(128, 64, i2c, Pin(16), 0x3c)
display.sleep(False)
display.fill(0)
display.text('----Connect.py---', 0, 0, 1)
display.show()


station = network.WLAN(network.STA_IF)
station.active(True)
print('----1---')
display.text('----1---', 0, 20, 1)
display.show()
station.connect("Wifi_name", "pass")
print('----2---')
display.text('----2---', 0, 30, 1)
display.show()
sleep(4)
print('----3---')
display.text('----3---', 0, 40, 1)
display.show()
import program.py


