import utils
from sensors.airpressure import AirPressureSensor
from sensors.gpsmodule import GPSModule

air_pressure_sensor = AirPressureSensor()
gps_module = GPSModule()


def send_data():
    # gather data from sensors

    position = gps_module.get_position()

    data = {
        "air_pressure": air_pressure_sensor.get_data(),
        "longiture": position.longitude,
        "latitude": position.latitude,
    }

    utils.send_data(data)


def main():
    utils.run_every_x_seconds(send_data, 0.5)


if __name__ == "__main__":
    main()
