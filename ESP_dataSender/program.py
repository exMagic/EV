print("-START program.py")

import os
import uos
from network import mDNS, ftp, telnet, STA_IF, WLAN
# import network, urequests, utime, machine
import urequests, utime, machine
from machine import RTC



from time import *
from umqtt.simple import MQTTClient
from machine import Pin, ADC, idle
from machine import I2C

import array as arr

import sh1106

# ///////// VARIABLES
Net = 0
# ///////// SETUP
print(" ///////// SETUP")
try:
    # start OLED

    # internal real time clock
    rtc = RTC()
    mdns = mDNS()
except Exception as e:
    print("--Exception: " + str(e))





# SaveEventLog( version , time)



# # //////// SAVE EVENT LOG
# def SaveEventLog(payload):
#     #save to sdcard

#     #send mq


#-----------------------------------------------------

# //////// CONNECT
print(" //////// CONNECT")
try:
    f = open("pass.py", "r")
    lines = f.read().split("\n") 
    _ssid = lines[0]
    _pass = lines[1]
    _ssid2 = lines[2]
    _pass2 = lines[3]
    f.close()   

    # station = network.WLAN(network.STA_IF)
    # station.active(True)
    print("_ssid : " + _ssid)
    print("_pass : " + _pass)

    print("_ssid2 : " + _ssid2)
    print("_pass2 : " + _pass2)

    _ssidString = "b'" + _ssid + "'"
    _ssid2String = "b'" + _ssid2 + "'"

    wlan = WLAN(STA_IF)
    wlan.active(True)
    nets = wlan.scan()
    
    update_time = utime.ticks_ms()

    for net in nets:
        ssid = str(net[0])        
        print(ssid)
        if ssid == _ssidString:
            print('try connecto to ' + ssid)        
            wlan.connect(_ssid, _pass)
            while not wlan.isconnected():
                # idle() # save power while waiting
                if utime.ticks_ms() - update_time > 15000:
                    print('timeout')        
                    
                    break
                    print('w1')     

            print('w2')
            if wlan.isconnected():
                Net = 1
                print('WLAN connection succeeded to : ' + ssid)
                print("Net = " + str(Net))                
                            
            print('a--92')
        
        print('a--94')
    print('a--96')


    if Net == 0:
        print('b--92')
        for net in nets:
            ssid = str(net[0])        
            print(ssid)

            if ssid == _ssid2String:
                print('try connecto to ' + ssid)        
                wlan.connect(_ssid2, _pass2)
                while not wlan.isconnected():
                    # idle() # save power while waiting
                    if utime.ticks_ms() - update_time > 15000:
                        print('timeout')        
                            
                        break
                        print('bw1')     
                print('bw2')
                if wlan.isconnected():
                    Net = 2
                    print('WLAN connection succeeded to : ' + ssid)
                    print("Net = " + str(Net))                
                    break        
                print('bw4')
                            
                # break            
            print('b--93')

    print('b--95')

    print("Final Net = " + str(Net))       
            

    # station.connect(_user, _pass)
    
    # update_time = utime.ticks_ms()
    
    
    # while not station.isconnected():
    #     #print(station.isconnected())
    #         # idle() # save power while waiting

    #     if utime.ticks_ms() - update_time > 15000:
    #         print("before brake")
    #         update_time = utime.ticks_ms()
    #         brake
    #         print("after brake")        
            
    # print('WLAN connection succeeded!')
    # Net = 1
except Exception as e:
    print("--Exception: " + str(e))
#try Wasiek


print('WENDDDD')
# while True:

#     print(station.isconnected())


#set Net = 1
#if not try Play
#set Net = 2
#if not 
#set Net = 0
#saveLog




# //////// CHECK VERSION
# if net = 1
# check version
# if version < globalVersion

# //////// UPDATE
# Run Update
# else

# //////// PROGRAM












# i2c = I2C(scl=Pin(22), sda=Pin(23), freq=400000)
# display = sh1106.SH1106_I2C(128, 64, i2c, Pin(16), 0x3c)
# display.sleep(False)
# display.fill(0)
# display.text('Program...', 0, 0, 1)
# display.show()

# # internal real time clock
# rtc = RTC()

# print('Program...1')
# sleep(4)

# pot = ADC(Pin(33))
# pot.atten(ADC.ATTN_11DB)   

# pot2 = ADC(Pin(34))
# pot2.atten(ADC.ATTN_11DB)   

# pot3 = ADC(Pin(39))
# pot3.atten(ADC.ATTN_11DB)   


# SERVER = 'farmer.cloudmqtt.com'  # MQTT Server Address (Change to the IP address of your Pi)
# CLIENT_ID = 'ESP32_DHT22_Sensor'
# TOPIC = b'esp'

# client = MQTTClient(CLIENT_ID, SERVER,10668, 'hrrtilwc', 'DO4mpEZjrXUB')
# client.connect()   # Connect to MQTT broker

# print("-d2")



# lt = arr.array('i',[0,1, 2, 3, 4, 5,6,7,8,9])
# lc = arr.array('i',[0,1, 2, 3, 4, 5,6,7,8,9])
# lv = arr.array('i',[0,1, 2, 3, 4, 5,6,7,8,9])

# pot_value = pot.read()
# pot_value2 = pot2.read()
# pot_value3 = pot3.read()
# lt[0] = pot_value  
# lv[0] = pot_value2  
# lc[0] = pot_value3  
# print(lt)
# print(lc)

# maxv3 = pot_value3
# minv3 = pot_value3

# url = "http://worldtimeapi.org/api/timezone/Europe/Oslo"
# web_query_delay = 60000
# retry_delay = 5000
# update_time = utime.ticks_ms() - web_query_delay

# response = urequests.get(url)    
# if response.status_code == 200: # query success        
#     print("JSON response:\n", response.text)            
#     # parse JSON
#     parsed = response.json()
#     datetime_str = str(parsed["datetime"])
#     year = int(datetime_str[0:4])
#     month = int(datetime_str[5:7])
#     day = int(datetime_str[8:10])
#     hour = int(datetime_str[11:13])
#     minute = int(datetime_str[14:16])
#     second = int(datetime_str[17:19])
#     subsecond = int(round(int(datetime_str[20:26]) / 10000))
        
#     # update internal RTC
#     rtc.datetime((year, month, day, 0, hour, minute, second, subsecond))
#     update_time = utime.ticks_ms()
#     print("RTC updated\n")
   
# else: # query failed, retry retry_delay ms later
#     update_time = utime.ticks_ms() - web_query_delay + retry_delay

# while True:
#     pot_value = pot.read()
#     pot_value2 = pot2.read()
#     pot_value3 = pot3.read()

#     if pot_value3 > maxv3:
#         maxv3 = pot_value3
#     if pot_value3 < minv3:
#         minv3 = pot_value3

#     lt[9] = lt[8] 
#     lt[8] = lt[7] 
#     lt[7] = lt[6] 
#     lt[6] = lt[5] 
#     lt[5] = lt[4] 
#     lt[4] = lt[3] 
#     lt[3] = lt[2] 
#     lt[2] = lt[1] 
#     lt[1] = lt[0] 
#     lt[0] = pot_value  

#     lv[9] = lv[8] 
#     lv[8] = lv[7] 
#     lv[7] = lv[6] 
#     lv[6] = lv[5] 
#     lv[5] = lv[4] 
#     lv[4] = lv[3] 
#     lv[3] = lv[2] 
#     lv[2] = lv[1] 
#     lv[1] = lv[0] 
#     lv[0] = pot_value2  

#     lc[9] = lc[8] 
#     lc[8] = lc[7] 
#     lc[7] = lc[6] 
#     lc[6] = lc[5] 
#     lc[5] = lc[4] 
#     lc[4] = lc[3] 
#     lc[3] = lc[2] 
#     lc[2] = lc[1] 
#     lc[1] = lc[0] 
#     lc[0] = pot_value3  

#     temp = int((lt[0] + lt[1] + lt[2] + lt[3] + lt[4] + lt[5] + lt[6] + lt[7] + lt[8] + lt[9]) / 10)
#     volt = int((lv[0] + lv[1] + lv[2] + lv[3] + lv[4] + lv[5] + lv[6] + lv[7] + lv[8] + lv[9]) / 10)
#     amp = int((lc[0] + lc[1] + lc[2] + lc[3] + lc[4] + lc[5] + lc[6] + lc[7] + lc[8] + lc[9]) / 10)

#     date_str = "{1:02d}/{2:02d}/{0:4d}".format(*rtc.datetime())
#     time_str = "{4:02d}:{5:02d}:{6:02d}".format(*rtc.datetime())

#     if utime.ticks_ms() - update_time >= 1000:

#         #MQTT
#         msg =  date_str + ' ' + time_str + ' ' + str(temp) + ', ' + str(volt) + ', ' + str(amp)
#         client.publish(TOPIC, msg) 
#         #TERMINAL PI
#         print(msg)    

#         #DISPLAY
#         display.fill(0)
#         display.text('temp: ' + str(temp), 2, 0, 99)    
#         display.text('Volt: ' + str(volt), 2, 12, 99)
#         display.text('Aamp: ' + str(amp), 2, 24, 99)    
#         display.show()

#         update_time = utime.ticks_ms()