import paho.mqtt.client as mqtt

f = open("pass.py", "r")
lines = f.read().split("\n") 
_user = lines[0]
_pass = lines[1]
f.close() 

host="farmer.cloudmqtt.com"
port=10668
	# Callback fires when conected to MQTT broker.
def on_connect(client, userdata, flags, rc):
    print('Connected with result code {0}'.format(rc))
    # Subscribe (or renew if reconnect).
    client.subscribe("esp")

# Callback fires when a published message is received.
def on_message(client, userdata, msg):
	# Decode temperature and humidity values from binary message paylod.
    #t,h = [float(x) for x in msg.payload.decode("utf-8").split(',')]
    
    print(msg.payload)
    #display_data(t, h)  # Display data on OLED display.

client = mqtt.Client()
client.username_pw_set(username=_user, password=_pass)
client.on_connect = on_connect  # Specify on_connect callback
client.on_message = on_message  # Specify on_message callback
client.connect(host, port, 60)  # Connect to MQTT broker (also running on Pi).

# Processes MQTT network traffic, callbacks and reconnections. (Blocking)
client.loop_forever()