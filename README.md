# Ezviz smart plug support for Home Assistant (docker)
Scripts that allows to use Ezviz smart WiFi plugs in dockerized Home Assistant.
## How it works?
1. Template switch in `template_switch.yaml` is defined to send mqtt message on `home/mqttr/control` topic.
2. Daemonized bash script `mqttr-receiver` executes `mosquitto_sub` which listens for /home/mqttr/# messages and pass payload to python script.
3. Python script `mqttr.py` is checking payload and sends it to a module given in `serve` variable (for now `ezviz-plug` only, but you can add more for your own purposes).
4. Python script `ezviz-plug.py` when executed from `mqttr.py` is changing the state of plug but when  executed from cron is updating Home Assistant sensors defined in `mqttr_sensor.yaml` by sending mqtt message to `home/plug/QXXXXXXXX`

## What do you need?
Linux server with Python 3.10+, mosquitto, pyEzviz, Home Assistant, smart plugs on your Ezviz account.

More info later. Look into files and directories and you'll figure it out. ;)
