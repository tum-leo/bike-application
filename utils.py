import time
import requests

import config


def run_every_x_seconds(func, seconds):
    starttime = time.time()
    while True:
        func()
        waiting_time = seconds - ((time.time() - starttime) % seconds)
        time.sleep(waiting_time)


post_headers = {'content-type': 'application/json'}


def send_data(data):
    print(data)
    response = requests.post(config.sap_streaming_server_url, headers=post_headers, json=data)
