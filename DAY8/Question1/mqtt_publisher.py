# pip install paho-mqtt

import paho.mqtt.client as mqtt
import random

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect("localhost", 1883)

client.publish("sensor/ldr/temp", round(random.uniform(20, 30), 2))
client.publish("sensor/ldr/intensity", random.randint(400, 800))
client.publish("sensor/lm35/temp", round(random.uniform(25, 40), 2))
client.publish("sensor/lm35/intensity", random.randint(500, 900))

client.disconnect()
print("✅ Data published successfully")
