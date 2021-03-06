from statistics import mean

from devices.anemometer import Anemometer
from devices.vane import Vane
from sensors.sensor import Sensor


class WindMeasurementSensor(Sensor):
    """Represents the sensor which measures wind speed, wind direction and wind gust"""

    def __init__(self, anemometer_port_number):
        self.anemometer = Anemometer(anemometer_port_number=anemometer_port_number)
        self.vane = Vane()

    def read_values(self):
        return [self.vane.get_sample(), self.anemometer.get_sample()]

    def get_averages(self, reads):
        transposed_matrix = list(zip(*reads))

        return [self.vane.get_direction_average(direction_angles=transposed_matrix[0]),
                mean(data=transposed_matrix[1]),
                max(transposed_matrix[1])]
