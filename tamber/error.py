import sys

class TamberError(Exception):
    def __init__(self, message=None, is_timed_out_error=False):
        super(TamberError, self).__init__(message)
        self._message = message
        self.is_timed_out_error = is_timed_out_error
