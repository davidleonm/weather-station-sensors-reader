import logging
from abc import ABC, abstractmethod

import psycopg2

from exceptions.dao_exception import DaoException


class Dao(ABC):
    """Base class for DAOs"""

    def __init__(self, server, database, user, password):
        self.server = server
        self.database = database
        self.user = user
        self.password = password

    def insert(self, values):
        if not self.server:
            logging.warning(msg='Database connection not configured, the data will not be stored anywhere.')
            return

        try:
            if not values:
                raise ValueError('values cannot be null or empty')

            sql_query = self.get_query()
            query_parameter_values = self.get_parameters(values=values)
            with psycopg2.connect(host=self.server,
                                  database=self.database,
                                  user=self.user,
                                  password=self.password) as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query=sql_query, vars=query_parameter_values)

                    logging.debug(f'Executed query "{sql_query}" with values {query_parameter_values}.')
        except ValueError:
            raise
        except Exception as e:
            raise DaoException(
                f'Error in DAO "{self.__class__.__name__} while executing the query "{sql_query}" with values {query_parameter_values}. ') from e

    @abstractmethod
    def get_query(self):
        raise NotImplementedError()

    @abstractmethod
    def get_parameters(self, values):
        raise NotImplementedError()

    def health_check(self):
        if not self.server:
            return

        sql_query = self.get_health_check_query()
        with psycopg2.connect(host=self.server,
                              database=self.database,
                              user=self.user,
                              password=self.password) as conn:
            with conn.cursor() as cursor:
                cursor.execute(query=sql_query)

    @abstractmethod
    def get_health_check_query(self):
        raise NotImplementedError()
