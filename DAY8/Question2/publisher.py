import paho.mqtt.client as mqtt

def on_publish(client, userdata, mid, reason_code, properties):
    print("Message published")

publisher = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
publisher.on_publish = on_publish
publisher.connect("localhost", 1883)
publisher.loop_start()

while True:
    print("\n1. Light ON")
    print("2. Light OFF")
    print("3. Fan ON")
    print("4. Fan OFF")
    print("5. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        publisher.publish("home/light", "ON")
    elif ch == "2":
        publisher.publish("home/light", "OFF")
    elif ch == "3":
        publisher.publish("home/fan", "ON")
    elif ch == "4":
        publisher.publish("home/fan", "OFF")
    elif ch == "5":
        break

publisher.loop_stop()
publisher.disconnect()
