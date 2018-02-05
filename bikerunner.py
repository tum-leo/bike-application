import time

import datetime

import config
import utils
from connection import connector
from sensors.airpressure import AirPressureSensor
from sensors.gpsmodule import GPSModule

air_pressure_sensor = AirPressureSensor()
gps_module = GPSModule()


def send_data():
    # gather data from sensors

    position = gps_module.get_position()

    data = [{
        "ESP_OPS": "i",
        "bike_id": 2,
        "sensor": 1,
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000"),
        "air_pressure": air_pressure_sensor.get_data(),
        # "longiture": position.longitude,
        # "latitude": position.latitude,
    }]

    connector.post_data(config.data_streaming_url, data)


def send_dummy():
    data = [{
        "ESP_OPS": "i",
        "entity": 1,
        "value": 50
    }]
    connector.post_data(config.data_streaming_url, data)


def main():
    utils.run_every_x_seconds(send_data, 1)

    # utils.run_every_x_seconds(send_dummy, 1)


if __name__ == "__main__":
    main()
