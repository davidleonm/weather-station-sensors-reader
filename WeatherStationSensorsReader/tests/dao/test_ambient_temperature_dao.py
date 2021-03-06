import unittest
from datetime import datetime
from unittest import mock

from dao.ambient_temperature_dao import AmbientTemperatureDao


class TestAmbientTemperatureDao(unittest.TestCase):
    test_server = 'test_server'
    test_database = 'test_database'
    test_user = 'test_user'
    test_password = 'test_password'

    def setUp(self):
        self.dao = AmbientTemperatureDao(server=self.test_server, database=self.test_database, user=self.test_user, password=self.test_password)

    def test_when_constructor_called_properties_should_be_passed_to_the_dao_correctly(self):
        self.assertEqual(self.dao.server, self.test_server)
        self.assertEqual(self.dao.database, self.test_database)
        self.assertEqual(self.dao.user, self.test_user)
        self.assertEqual(self.dao.password, self.test_password)

    def test_when_getting_query_expected_value_should_be_returned(self):
        self.assertEqual(self.dao.get_query(), self.dao.INSERT_QUERY)

    @mock.patch('dao.ambient_temperature_dao.datetime')
    def test_when_getting_parameters_expected_values_should_be_returned(self, mock_datetime):
        # arrange
        test_values = ['test_values', 'test2']
        expected_value = test_values[0]
        expected_time = datetime.now()
        mock_datetime.now.return_value = expected_time

        # act
        values, date = self.dao.get_parameters(values=test_values)

        # assert
        self.assertEqual(values, expected_value)
        self.assertEqual(date, expected_time)

        mock_datetime.now.assert_called_once()


if __name__ == '__main__':
    unittest.main()
