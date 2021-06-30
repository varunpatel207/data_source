from rest_framework import status
from rest_framework.response import Response


def response_success(message='', data=None):
    return Response(status=status.HTTP_200_OK,
                    data={
                        'status': True,
                        'message': message,
                        'data': data,
                    })


def response_internal_error(message=None):
    return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    data={
                        'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                        'message': message if message else "Internal Error.",
                        'data': None
                    })


def response_already_exist(response_string, id=None):
    return Response(status=status.HTTP_200_OK,
                    data={
                        'status': False,
                        'message': str(
                            response_string) + " already exists.",
                        'data': id,
                    })


def method_not_allowed():
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED,
                    data={
                        'status': status.HTTP_405_METHOD_NOT_ALLOWED,
                        'message': "Method Not allowed.",
                        'data': None
                    })


def data_not_acceptable(message=''):
    return Response(status=status.HTTP_400_BAD_REQUEST,
                    data={
                        'status':
                            status.HTTP_400_BAD_REQUEST,
                        'message':
                            'Not allowed.' if message == '' else message,
                        'data': {}
                    })


def custom_response(status_code, status_bool, message='', data=None):
    return Response(status=status_code,
                    data={
                        'status': status_bool,
                        'message': message,
                        'data': data,
                    })
