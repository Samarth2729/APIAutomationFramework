import allure
import pytest
import logging
from src.helpers.api_request_wrapper import post_request
from src.constants.api_constants import APIconstants
from src.helpers.payload_manager import payload_create_booking
from src.helpers.common_verification import * # star means import all of them
from src.utils.utils import Utils


class TestCreateBooking(object):
    LOGGER = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO)

    @pytest.mark.positive
    @allure.title("Verify that Create Booking Status and Booking ID shouldn't be null")
    @allure.description(
        "Creating a Booking from the paylaod and verfiy that booking id should not be null and status code should be 200 for the correct payload")
    def test_create_booking_positive(self):
        LOGGER = logging.getLogger(__name__)
        response = post_request(
            url=APIconstants().url_createbooking(),
            auth=None,
            headers= Utils().common_headers_json(),
            payload=payload_create_booking(),
            in_json=False
        )
        verify_http_status_code(response_data=response, expect_data=200)
        verify_json_key_for_not_null(response.json()["bookingid"])
        self.LOGGER.info(f"Booking ID: {response.json()['bookingid']}")

    @pytest.mark.negative
    @allure.title("Verify that Create Booking doesn't work with no payload")
    @allure.description(
        "Creating a Booking with no payload and verify that booking id")
    def test_create_booking_negative(self):
        LOGGER = logging.getLogger(__name__)
        response = post_request(
            url=APIconstants().url_createbooking(),
            auth=None,
            headers= Utils().common_headers_json(),
            payload={},
            in_json=False
        )
        verify_http_status_code(response_data=response, expect_data=500)