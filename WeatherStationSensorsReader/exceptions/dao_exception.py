class DaoException(Exception):
    """Represents an exception occurred in the DAO classes."""

    def __init__(self, class_name, message):
        super().__init__(message)

        self.class_name = class_name
