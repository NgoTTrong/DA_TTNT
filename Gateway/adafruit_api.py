from Adafruit_IO import MQTTClient
import sys
from uart import Uart
class Adafruit_API:
    def __init__(self,username,key,feed_id_list,port = "COM4"):
        self.username = username
        self.feed_id_list = feed_id_list
        self.key = key
        self.mqtt_client = None
        self.uart = None
        self.port = port
    def connected(self,client):
        print("Connected to server!")
        for feed_id in self.feed_id_list:
            client.subscribe(feed_id)
    def subscribe(self,client,userdata, mid , granted_qos):
        print("Subscribe successful!")
    def disconnected(client):
        print("Disconnect succcessful!")
        sys.exit(1)
    def message(self,client,feed_id,payload):
        print("Receive from " + feed_id + " : " + payload)
        self.uart.write_message("Receive from " + feed_id + " : " + payload)
    def publish(self,feed_id,data):
        print("Publish to " + feed_id + " : " + str(data))
        self.mqtt_client.publish(feed_id,data)
    def connect(self):
        self.mqtt_client = MQTTClient(self.username,self.key)
        self.mqtt_client.on_connect = self.connected
        self.mqtt_client.on_disconnect = self.disconnected
        self.mqtt_client.on_message = self.message
        self.mqtt_client.on_subscribe = self.subscribe
        self.mqtt_client.connect()
        self.uart = Uart(self.port,self)
        self.uart.init_connection()
        self.mqtt_client.loop_background()
    def read_serial(self):
        self.uart.read_serial()