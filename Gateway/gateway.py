from adafruit_api import Adafruit_API
import time
from random import randint
USERNAME = 'Heo_Rey'
KEY = 'aio_DvAe72T5LAeLseyTXzblB34JYhgI'

feed_id_list = ['auto_modify_btn']
feed_id = 'air_conditioner'

client = Adafruit_API(USERNAME, KEY, feed_id_list)
client.connect()

counter = 10
while(True):
    counter = counter - 1
    if (counter == 0):
        counter = 10
        data = {
            'status':'on',
            'temperature': randint(1,100)
        }
        client.publish(feed_id,data['temperature'])
    client.read_serial()
    time.sleep(1)