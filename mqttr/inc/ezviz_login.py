from pyezviz import client
import subprocess, ezviz_config

def ezlogin():
    ezclient = client.EzvizClient(ezviz_config.email, ezviz_config.password)
    token = ezclient.login()
    return ezclient
