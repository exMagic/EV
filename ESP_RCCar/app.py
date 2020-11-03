
import mysql.connector
import paho.mqtt.client as mqtt
import os, urlparse
from datetime import date

mydb = mysql.connector.connect(
  host="localhost",
  user="xxx",
  password="xxx",
  database="xxx"
)

mycursor = mydb.cursor()





# Define event callbacks
def on_connect(client, userdata, flags, rc):
    print("rc: " + str(rc))

def on_message(client, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    x = msg.payload.split(",")

    
    print(x)
    #print(type(x))
    #print(x[0])



    
    sql = "INSERT INTO car (voltage, amps) VALUES (%s, %s)"
    val = (x)
    print(sql)
    print(x)

    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "was inserted.")




def on_publish(client, obj, mid):
    print("mid: " + str(mid))

def on_subscribe(client, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(client, obj, level, string):
    print(string)

mqttc = mqtt.Client()
# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe

# Uncomment to enable debug messages
#mqttc.on_log = on_log

# Parse CLOUDMQTT_URL (or fallback to localhost)
url_str = os.environ.get('xxx', 'mqtt://localhost:xxx')
url = urlparse.urlparse(url_str)
topic = 'vc'

# Connect
mqttc.username_pw_set("xxx", "xxx")
mqttc.connect('xxx', xxx)

# Start subscribe, with QoS level 0
mqttc.subscribe(topic, 0)

# Publish a message
#mqttc.publish(topic, "my message")

# Continue the network loop, exit when an error occurs
rc = 0
while rc == 0:
    rc = mqttc.loop()
print("rc: " + str(rc))
