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
    unicorn.clear()
    for w in range(0, u_width):
        for h in range(0, u_height):
            if i < len(items):
                item = items[i]
                i += 1
                phase = item.status.phase
                elif phase == "Running":
                    #print("Setting {}/{} to green".format(w, h))
                    unicorn.set_pixel(w, h, 0, 255, 0)
                elif phase == "Pending":
                    #print("Setting {}/{} to yellow".format(w, h))
                    unicorn.set_pixel(w, h, 255, 255, 0)
                elif phase == "Failed":
                    #print("Setting {}/{} to red".format(w, h))
                    unicorn.set_pixel(w, h, 255, 0, 0)
                elif phase == "Unknown":
                    #print("Setting {}/{} to pink".format(w, h))
                    unicorn.set_pixel(w, h, 255, 0, 255)
                else:
                    print("Unknown Phase: {}".format(phase))
    unicorn.show()

while True:
    ret = v1.list_pod_for_all_namespaces(watch=False)
    set_val(ret.items)
    time.sleep(5)
