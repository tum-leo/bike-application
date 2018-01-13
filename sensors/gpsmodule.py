from data import gpssimulator


class GPSModule(object):

    def get_position(self):
        return gpssimulator.next_position()
