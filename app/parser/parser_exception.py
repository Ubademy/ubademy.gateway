class InvalidMicroserviceError(Exception):
    message = "The microservice you specified is invalid."

    def __str__(self):
        return InvalidMicroserviceError.message
