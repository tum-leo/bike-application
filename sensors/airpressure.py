from data import airpressuresimulator as simulator


class AirPressureSensor(object):

    def get_data(self):
        return simulator.get_simulated_airpressure()
