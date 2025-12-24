import paho.mqtt.client as mqtt
from dbconnection import getconnection

db = getconnection()
cursor = db.cursor()

pulse = None
spo2 = None

def send_alert(message):
    print(message)
    cursor.execute(
        "INSERT INTO patient_data (alert) VALUES (%s)",
        (message,)
    )
    db.commit()
    client.publish("health/alert", message)

def on_message(client, userdata, msg):
    global pulse, spo2

    value = int(msg.payload.decode())

    if msg.topic == "health/pulse":
        pulse = value
        print("Pulse:", pulse)

    elif msg.topic == "health/spo2":
        spo2 = value
        print("SpO2:", spo2)

    if pulse is not None and spo2 is not None:
        cursor.execute(
            "INSERT INTO patient_data (pulse, spo2) VALUES (%s, %s)",
            (pulse, spo2)
        )
        db.commit()

        if pulse < 60 or pulse > 100:
            send_alert(f"ALERT: Abnormal Pulse = {pulse} BPM")

        if spo2 < 95:
            send_alert(f"ALERT: Low SpO2 Level = {spo2}%")

        pulse = None
        spo2 = None

client = mqtt.Client()
client.connect("localhost", 1883, 60)

client.subscribe("health/pulse")
client.subscribe("health/spo2")
client.on_message = on_message

print("Healthcare Monitoring Subscriber Started...")
client.loop_forever()
