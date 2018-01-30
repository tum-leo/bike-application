import random

# configuration
import math

min_value = 0
max_value = 4
probability_failure_high = 0.05
probability_failure_low = 0.1

pressure_is_decreasing = False

# generated configuration
random_min = (max_value - min_value) * 0.4
random_bike_state = random.triangular(random_min, max_value)

print("The bike's current airpressure mid-value is {}".format(random_bike_state))


def get_simulated_airpressure():

    global random_bike_state

    if pressure_is_decreasing:
        random_bike_state = max(0, random_bike_state - 0.08)

    probability = random.random()
    if probability < probability_failure_low:
        print("Oh no! Sensor returns no value...")
        return 0
    if probability > 1 - probability_failure_high:
        print("Oh no! Sensor value too high")
        return max_value + random.random() * 5

    return max(0, random.gauss(random_bike_state, 2))

