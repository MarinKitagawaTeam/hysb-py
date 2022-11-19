class HyPyError(Exception):
    pass


class InvalidApiKey(HyPyError):
    """Raised when the Api-Key is invalid"""
    pass
