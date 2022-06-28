# Ezviz smart plug support for Home Assistant (docker)
Scripts that allows to use Ezviz smart WiFi plugs in dockerized Home Assistant.
## How it works?
1. Template switch in `template_switch.yaml` is defined to send mqtt message on `home/mqttr/control` topic.
2. Daemonized bash script `mqttr-receiver` executes `mosquitto_sub` which listens for /home/mqttr/# messages and pass payload to python script.
3. Python script `mqttr.py` is checking payload and sends it to a module given in `serve` variable (for now `ezviz-plug` only, but you can add more for your own purposes).
4. Python script `ezviz-plug.py` when executed from `mqttr.py` is changing the state of plug but when  executed from cron is updating Home Assistant sensors defined in `mqttr_sensor.yaml` by sending mqtt message to `home/plug/QXXXXXXXX`

## What do you need?
Linux server with Python 3.10+, Mosquitto server, pyEzviz, Home Assistant, MQTT integration in HA, smart plugs added to your Ezviz account.

## What to do?

1. Copy `mqttr` folder to `/usr/local/bin`.
2. Edit `mqttr.conf` and provide your mosquitto server user and password.
3. Edit and copy template switch and mqtt sensor definitions from `homeassistant/*.yaml`to HA configuration
4. Edit `inc/ezviz_config.py` and change your Ezviz account user, password and plugs device serial number list.
5. Use `mqttr-receiver` as systemd service to receive mqtt messages from HA
6. Use cron to execute `inc/ezviz-plug.py` to check plugs status.

Look into files and directories and you'll figure it out. ;)
