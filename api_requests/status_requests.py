import requests


def get_api_status_code():
    return requests.get('https://simple-books-api.glitch.me/status').status_code


def get_api_status_body():
    return requests.get('https://simple-books-api.glitch.me/status').json()


print("status code = ", get_api_status_body())
print("Api response body = ", get_api_status_code())
