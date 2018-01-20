import json
import re
from pprint import pprint
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

__all__ = ['get_ngrok_url']


def get_ngrok_url(addr='127.0.0.1', port=4040):
    ngrokjson = ''
    try:
        ngrokpage = requests.get("http://{}:{}".format(addr, port)).text
    except:
        raise RuntimeError('Not able to connect to ngrok webui')
    for line in ngrokpage.split('\n'):
        if 'window.common = ' in line:
            ngrokjson = re.search('JSON.parse\(\"(.+)\"\)\;', line).group(1)
            ngrokjson = (ngrokjson.replace('\\', ''))
    ngrok_info = json.loads(ngrokjson)
    pprint(ngrok_info)
    url = ngrok_info['Session']['Tunnels']['command_line']['URL']
    return url
