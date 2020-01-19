# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt

HOST = '172.19.0.11'
PORT = 1883
KEEP_ALIVE = 60
TOPIC = 'test/message'

"""
接続を試みたときに実行
def on_connect(client, userdata, flags, respons_code):

* client
Clientクラスのインスタンス

* userdata
任意のタイプのデータで新たなClientクラスののインスタンスを作成するときに>設定することができる

* flags
応答フラグが含まれる辞書
クリーンセッションを0に設定しているユーザに有効。
セッションがまだ存在しているかどうかを判定する。
クリーンセッションが0のときは以前に接続したユーザに再接続する。

0 : セッションが存在していない
1 : セッションが存在している

* respons_code
レスポンスコードは接続が成功しているかどうかを示す。
0: 接続成功
1: 接続失敗 - incorrect protocol version
2: 接続失敗 - invalid client identifier
3: 接続失敗 - server unavailable
4: 接続失敗 - bad username or password
5: 接続失敗 - not authorised
"""
def on_connect(client, userdata, flags, respons_code):
    print('status {0}'.format(respons_code))
    client.subscribe(client.topic)

"""
def on_message(client, userdata, message):
topicを受信したときに実行する
"""
def on_message(client, userdata, message):
    print(message.topic + ' ' + str(message.payload))

if __name__ == '__main__':

    client = mqtt.Client(protocol=mqtt.MQTTv311)
    client.topic = TOPIC

    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(HOST, port=PORT, keepalive=KEEP_ALIVE)

    # ループ
    client.loop_forever()
