import requests

import config

sws_token = ""

authentication_request = [
    {"privilege": "write", "resourceType": "stream", "resource": "gbi_002/qbike/BikeInputStream"}
]


def authenticate():
    headers = {
        "authorization": "Basic {}".format(config.base_64_auth)
    }
    response = post("/1/authorization", authentication_request, headers)
    global sws_token
    sws_token = retrieve_sws_token(response)


def post(path, data, headers):
    print(get_url(path), data, headers)
    response = requests.post(get_url(path), headers=headers, json=data)
    print(response.status_code, response.reason, response.text)
    return response


last_request_unauthorized = False


def post_data(path, data):
    global last_request_unauthorized
    response = post(path, data, get_authorization_header())
    if response.status_code == 401:
        print("Request was unauthorized, authenticate and retry again...")
        # last_request_unauthorized = True
        authenticate()
        post_data(path, data)
    else:
        # last_request_unauthorized = False
        pass


def get_url(path):
    return config.sap_streaming_server_url + path


def retrieve_sws_token(response):
    return response.json()[0]["sws-token"]


def get_authorization_header():
    return {
        "authorization": "SWS-Token \"sws-token\"=\"{}\"".format(sws_token)
    }

# http://h86sds.ucc.in.tum.de:9093/1/workspaces/gbi_002/projects/stream2/streams/InputStream1
