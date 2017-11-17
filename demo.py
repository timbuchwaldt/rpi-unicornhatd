#!/usr/bin/env python3

import colorsys
import math
import time

import unicornhat as unicorn
from kubernetes import client, config
config.load_incluster_config()
v1 = client.CoreV1Api()


unicorn.set_layout(unicorn.HAT)
unicorn.rotation(0)
unicorn.brightness(0.3)
u_width,u_height=unicorn.get_shape()
unicorn.clear()

def set_val(items):
    i = 0
    for w in range(0, u_width):
        for h in range(0, u_height):
            if i < len(items):
                item = items[i]
                i += 1
                phase = item.status.phase
                print(phase)
                if phase == "Running":
                    print("Setting {}/{} to green".format(w, h))
                    unicorn.set_pixel(w, h, 0, 255, 0)
                if phase == "Pending":
                    print("Setting {}/{} to yellow".format(w, h))
                    unicorn.set_pixel(w, h, 255, 255, 0)
                if phase == "Failed":
                    print("Setting {}/{} to red".format(w, h))
                    unicorn.set_pixel(w, h, 255, 0, 0)
                if phase == "Failed":
                    print("Setting {}/{} to pink".format(w, h))
                    unicorn.set_pixel(w, h, 255, 0, 255)
    unicorn.show()

while True:
    ret = v1.list_pod_for_all_namespaces(watch=False)
    set_val(ret.items)
    time.sleep(5)

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
