import allure
import pytest

# payloads

def payload_create_booking():
    payload = {
        "firstname": "Sam",
        "lastname": "Brown",
        "totalprice": 1111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    return payload


def payload_create_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    return payload


