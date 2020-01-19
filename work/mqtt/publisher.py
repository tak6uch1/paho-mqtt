import paho.mqtt.client as mqtt

HOST = '172.19.0.11'
PORT = 1883
KEEP_ALIVE = 60
TOPIC = 'test/message'
MESSAGE = 'hello'

if __name__ == '__main__':
    client = mqtt.Client(protocol=mqtt.MQTTv311)
    client.connect(HOST, port=PORT, keepalive=KEEP_ALIVE)

    client.publish(TOPIC, MESSAGE)
    client.disconnect()
