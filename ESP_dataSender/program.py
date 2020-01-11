print("-START program.py")

from time import sleep
from umqtt.simple import MQTTClient
from machine import Pin, ADC
from machine import I2C

import array as arr

import sh1106

i2c = I2C(scl=Pin(22), sda=Pin(23), freq=400000)
display = sh1106.SH1106_I2C(128, 64, i2c, Pin(16), 0x3c)
display.sleep(False)
display.fill(0)
display.text('Program...', 0, 0, 1)
display.show()



print('Program...1')
sleep(4)

pot = ADC(Pin(33))
pot.atten(ADC.ATTN_11DB)   

pot2 = ADC(Pin(34))
pot2.atten(ADC.ATTN_11DB)   

pot3 = ADC(Pin(39))
pot3.atten(ADC.ATTN_11DB)   


SERVER = '192.168.1.220'  # MQTT Server Address (Change to the IP address of your Pi)
CLIENT_ID = 'ESP32_DHT22_Sensor'
TOPIC = b'temp_humidity'

client = MQTTClient(CLIENT_ID, SERVER)
client.connect()   # Connect to MQTT broker

print("-d2")



lt = arr.array('i',[0,1, 2, 3, 4, 5,6,7,8,9])
lc = arr.array('i',[0,1, 2, 3, 4, 5,6,7,8,9])
lv = arr.array('i',[0,1, 2, 3, 4, 5,6,7,8,9])

pot_value = pot.read()
pot_value2 = pot2.read()
pot_value3 = pot3.read()
lt[0] = pot_value  
lv[0] = pot_value2  
lc[0] = pot_value3  
print(lt)
print(lc)

maxv3 = pot_value3
minv3 = pot_value3

while True:
    pot_value = pot.read()
    pot_value2 = pot2.read()
    pot_value3 = pot3.read()

    if pot_value3 > maxv3:
        maxv3 = pot_value3
    if pot_value3 < minv3:
        minv3 = pot_value3




    lt[9] = lt[8] 
    lt[8] = lt[7] 
    lt[7] = lt[6] 
    lt[6] = lt[5] 
    lt[5] = lt[4] 
    lt[4] = lt[3] 
    lt[3] = lt[2] 
    lt[2] = lt[1] 
    lt[1] = lt[0] 
    lt[0] = pot_value  


    lv[9] = lv[8] 
    lv[8] = lv[7] 
    lv[7] = lv[6] 
    lv[6] = lv[5] 
    lv[5] = lv[4] 
    lv[4] = lv[3] 
    lv[3] = lv[2] 
    lv[2] = lv[1] 
    lv[1] = lv[0] 
    lv[0] = pot_value2  

    lc[9] = lc[8] 
    lc[8] = lc[7] 
    lc[7] = lc[6] 
    lc[6] = lc[5] 
    lc[5] = lc[4] 
    lc[4] = lc[3] 
    lc[3] = lc[2] 
    lc[2] = lc[1] 
    lc[1] = lc[0] 
    lc[0] = pot_value3  


    temp = int((lt[0] + lt[1] + lt[2] + lt[3] + lt[4] + lt[5] + lt[6] + lt[7] + lt[8] + lt[9]) / 10)
    volt = int((lv[0] + lv[1] + lv[2] + lv[3] + lv[4] + lv[5] + lv[6] + lv[7] + lv[8] + lv[9]) / 10)
    amp = int((lc[0] + lc[1] + lc[2] + lc[3] + lc[4] + lc[5] + lc[6] + lc[7] + lc[8] + lc[9]) / 10)

    print("temp: " + str(temp) + "  |  volt: " + str(volt) + "  |  amp: " + str(amp) + " | maxc: " + str(maxv3)+ " | minc: " + str(minv3))

    # sleep(1)

    # mv1 = pot_value / 4096
    # mv2 = mv1 * 3.3
    # mv3 = mv2 -0.5
    

    # ct = mv3 * 100

    # mv = pot_value * (3300/4096)

    # ct = (mv - 500) /10

    # msg = str(pot_value)
    # client.publish(TOPIC, msg)  # Publish sensor data to MQTT topic
    # print(msg)
    display.fill(0)
    display.text('temp: ' + str(temp), 2, 0, 99)
    
    display.text('Volt: ' + str(volt), 2, 12, 99)
    display.text('Aamp: ' + str(amp), 2, 24, 99)
    display.text('Magda & Kamil', 2, 36, 99)
    # display.text('mv3: ' + str(mv3), 2, 36, 99)
    
    display.show()
    #sleep(1)





