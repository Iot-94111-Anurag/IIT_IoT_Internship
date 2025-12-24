import paho.mqtt.client as mqtt
from executequery import executeQuery

initialized = False

def on_message(client, userdata, message):
    global initialized

    status = message.payload.decode()
    topic = message.topic

    if not initialized:
        executeQuery("""
            INSERT IGNORE INTO status (id, light_status, fan_status)
            VALUES (1, 'OFF', 'OFF')
        """)
        initialized = True

    if topic == "home/light":
        executeQuery(f"UPDATE status SET light_status='{status}' WHERE id=1")
        print("Light:", status)

    elif topic == "home/fan":
        executeQuery(f"UPDATE status SET fan_status='{status}' WHERE id=1")
        print("Fan:", status)

subscriber = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
subscriber.on_message = on_message
subscriber.connect("localhost", 1883)

subscriber.subscribe("home/light")
subscriber.subscribe("home/fan")

subscriber.loop_forever()
