from datetime import datetime

from dao.dao import Dao


class GroundTemperatureDao(Dao):
    """ Represents the ground temperature database access """

    INSERT_QUERY = 'INSERT INTO ground_temperatures(temperature, date_time) VALUES(%s, %s)'

    def get_query(self):
        return self.INSERT_QUERY

    def get_parameters(self, values):
        return values[0], datetime.now()
