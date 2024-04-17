from rest_framework import status
from rest_framework.exceptions import APIException

class CategoryNotFoundException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'La categoría no existe'
    default_code = 'invalid'