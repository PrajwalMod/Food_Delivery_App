class ValidationError(Exception):
    pass

class AuthenticationError(Exception):
    pass

class AuthorizationError(Exception):
    pass

class ResourceNotFoundError(Exception):
    pass
