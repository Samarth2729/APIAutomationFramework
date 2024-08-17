# Create Token
# Create Booking id
# Update the Booking(Put) - BookingID, Token
# Delete the Booking


# Verify that created booking id when we update we are able to update it and delete it also


import allure
import pytest

from src.constants.api_constants import APIconstants
from src.helpers.api_request_wrapper import put_requests, delete_requests
from src.helpers.common_verification import verify_response_key, verify_http_status_code, verify_response_delete
from src.helpers.payload_manager import payload_create_booking
from src.utils.utils import Utils


class TestCRUDbooking(object):
    @allure.title("Test CRUD operation Update(PUT).")
    @allure.description(
        "Verify that Full Update with the booking ID and Token is working.")
    def test_update_booking_id_token(self,create_token,get_booking_id):
        booking_id = get_booking_id
        token = create_token
        put_url = APIconstants.url_patch_put_delete(booking_id=booking_id)
        response = put_requests(
            url=put_url,
            headers=Utils().common_header_put_delete_patch_cookie(token=token),
            payload=payload_create_booking(),
            in_json = False
        )
        # Verification Here and more
        verify_response_key(response.json()["firstname"], expected_data="Sam")
        verify_response_key(response.json()["lastname"], expected_data="Brown")
        verify_http_status_code(response_data=response, expect_data=200)

        @allure.title("Test CRUD operation Delete(delete)")
        @allure.description(
            "Verify booking gets deleted with the booking ID and Token.")
        def test_delete_booking_id(self, create_token, get_booking_id):
            booking_id = get_booking_id
            token = create_token
            delete_url = APIconstants.url_patch_put_delete(booking_id=booking_id)
            response = delete_requests(
                url=delete_url,
                headers=Utils().common_header_put_delete_patch_cookie(token=token),
                auth=None,
                in_json=False
            )
            verify_response_delete(response=response.text)
            verify_http_status_code(response_data=response, expect_data=201)
