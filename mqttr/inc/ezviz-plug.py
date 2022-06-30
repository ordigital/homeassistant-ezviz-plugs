#!/usr/bin/python
# EZVIZ SMART PLUGS

from pyezviz import client
import sys, subprocess, ezviz_config, ezviz_login

ezclient = ezviz_login.ezlogin()

# find plug
def find_plug(serial):
    global ezclient
    switches = ezclient._api_get_pagelist(
        page_filter="SWITCH", json_key="SWITCH"
    )
    return next((switches[device][1] for device in switches.keys() if device==serial), None)

# set plug state
def set_state(serial, state):
    state = int(state)
    plug = find_plug(serial)
    ezclient.switch_status(plug["deviceSerial"], 14, state)

# get plug state
def get_state(serial):
    plug = find_plug(serial)
    return plug["enable"]

# Change state of plug
def serve(payload):
    set_state(payload.deviceSerial, payload.enable)
    send(payload.deviceSerial,payload.enable)

# Check state of plug
def check():
    for serial in ezviz_config.plugs:
        state = get_state(serial)
        send(serial,state)

# Update state of plug
def send(serial,state):
    topic = "home/plug/" + serial
    cmd = "/usr/local/bin/mqtt " + topic + " {\"enable\":" + str(int(state)) + "}"
    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

# Check state by default
check()
