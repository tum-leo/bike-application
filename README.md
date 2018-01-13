# Python Bike-Application

### General usage

This application runs on a small device attached to a bike. The bike has to be equiped with sensors, which are connected to the application. In predefined intervals, the application will gather information provided by the sensors, and push the data to an IoT-server, which is responsible for handling and processing the data.

### Data simulation

As real sensors are not present in development phase, the application in this stage will produce randomized fake data for tire air pressure and its GPS location. In further development the data gathering has simply to be switched from the data simulator to the real sensors.

The simulated GPS data originates from the GPS representation of a bike trail around munich, which can be found here: https://www.radtourenchef.de/radwege/radlring-muenchen/gps-track.php