from rest_framework.exceptions import APIException

class UsernameExists(APIException):
    status_code = 400
    default_detail = 'The requested username already exists.'
