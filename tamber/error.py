import sys


class TamberError(Exception):

    def __init__(self, message=None):
        super(TamberError, self).__init__(message)
        self._message = message
