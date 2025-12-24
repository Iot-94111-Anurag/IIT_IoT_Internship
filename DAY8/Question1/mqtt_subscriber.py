import paho.mqtt.client as mqtt
from executequery import executeQuery

ldr_temp = None
ldr_intensity = None
lm35_temp = None
lm35_intensity = None

def on_message(client, userdata, msg):
    global ldr_temp, ldr_intensity, lm35_temp, lm35_intensity

    value = float(msg.payload.decode())
    print(f"{msg.topic} -> {value}")

    if msg.topic == "sensor/ldr/temp":
        ldr_temp = value
    elif msg.topic == "sensor/ldr/intensity":
        ldr_intensity = value
    elif msg.topic == "sensor/lm35/temp":
        lm35_temp = value
    elif msg.topic == "sensor/lm35/intensity":
        lm35_intensity = value

    if None not in (ldr_temp, ldr_intensity, lm35_temp, lm35_intensity):
        query = f"""
        INSERT INTO device_readings
        (ldr_temp, ldr_intensity, lm35_temp, lm35_intensity)
        VALUES ({ldr_temp}, {ldr_intensity}, {lm35_temp}, {lm35_intensity});
        """
        executeQuery(query)
        print("✅ Data inserted into database")

        ldr_temp = None
        ldr_intensity = None
        lm35_temp = None
        lm35_intensity = None


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_message = on_message

client.connect("localhost", 1883)

client.subscribe("sensor/ldr/temp")
client.subscribe("sensor/ldr/intensity")
client.subscribe("sensor/lm35/temp")
client.subscribe("sensor/lm35/intensity")

print("📡 Subscriber running...")
client.loop_forever()
