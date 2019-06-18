from Grammars import US_PHONE_GRAMMAR, extend_grammar, opts
from subprocess import Popen, PIPE
import time
import paho.mqtt.client as paho
import argparse
import sys
import random
import os
import scapy.all as scapy





class mqtt_entry():
    x= 12.5
    y= 159753
    s= "asdfghjkl0"

radamsa_bin = "radamsa\\"
stdin = -1
stdout = -1



# Radamsa
'''
def mutate(payload):
    try:
        radamsa = [radamsa_bin, '-n', '1', '-']
        p = Popen(radamsa, stdin=-1, stdout=-2)
        mutated_data = p.communicate(payload)[0]
    except:
        print "Could not execute 'radamsa'."
        #sys.exit(1)

    return mutated_data '''

from Grammars import US_PHONE_GRAMMAR, extend_grammar, opts
def pick_area_code():
    return random.choice(['555', '554', '553'])
PICKED_US_PHONE_GRAMMAR = extend_grammar(US_PHONE_GRAMMAR,
{
    "<area>": [("<lead-digit><digit><digit>", opts(pre=pick_area_code))]
})

pick_area_code()
broker="127.0.0.1"
#broker="iot.eclipse.org"
#define callback
def on_message(client, userdata, message):
    time.sleep(1)
    print("received message 1=",str(message.payload.decode("utf-8")))

client= paho.Client("client-001") #create client object client1.on_publish = on_publish #assign function to callback client1.connect(broker,port) #establish connection client1.publish("house/bulb1","on")
######Bind function to callback
client.on_message=on_message
#####
print("connecting to broker ",broker)
client.connect(broker)#connect
client.loop_start() #start loop to process received messages
print("subscribing ")
client.subscribe("karim")#subscribe
time.sleep(2)
print("publishing ")
client.publish("karim",)#publish
time.sleep(4)
client.disconnect() #disconnect
client.loop_stop() #stop loop