#!/usr/bin/env python3

import colorsys
import math
import time

import unicornhat as unicorn
from kubernetes import client, config
config.load_incluster_config()
v1 = client.CoreV1Api()


unicorn.set_layout(unicorn.HAT)
unicorn.rotation(0) # tested on pHAT/HAT with rotation 0, 90, 180 & 270
unicorn.brightness(1)
u_width,u_height=unicorn.get_shape()

def set_val(myval):
    unicorn.clear()
    unicorn.show()
    for w in range(0, u_width-1):
        for h in range(0, u_height-1):
            if myval > 0:
                myval = myval-1
                unicorn.set_pixel(w, h, 255, 255, 255)
    unicorn.show()

while True:
    ret = v1.list_pod_for_all_namespaces(watch=False)
    set_val(len(ret.items))
    time.sleep(2)

#
#import socket
#
#
#IP = '0.0.0.0'
#PORT = 2808
#
#s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#s.bind((IP, PORT))
#
#while True:
#    data, addr = s.recvfrom(5) # 1 byte for LED, 1 for R/G/B
#    ba = bytearray(data)
#    w = ba[0]
#    h = ba[1]
#    r = ba[2]
#    g = ba[3]
#    b = ba[4]
#    unicorn.set_pixel(w, h, r, g, b)
#    unicorn.show()
