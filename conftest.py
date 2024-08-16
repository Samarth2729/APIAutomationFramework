import allure
import pytest

from src.helpers.api_request_wrapper import post_request
from src.constants.api_constants import APIconstants
from src.helpers.payload_manager import payload_create_token
from src.helpers.common_verification import * # star means import all of them
from src.utils.utils import Utils


@pytest.fixture(scope="session")
def create_token():
    response = post_request(
        url=APIconstants().auth_createtoken(),
        headers=Utils().common_headers_json(),
        auth=None,
        payload=payload_create_token,
        in_json=False,
    )
    verify_http_status_code(response_data=response, expect_data=200)
    verify_json_key_for_not_null_token(response.json()["token"])
    return response.json()["token"]


@pytest.fixture(scope="session")
def get_booking_id():
    response = post_request(url=APIconstants().url_createbooking(),
                            auth=None,
                            headers=Utils().common_headers_json(),
                            payload=payload_create_booking(),
                            in_json=False)

    booking_id = response.json()["bookingid"]

    verify_http_status_code(response_data=response, expect_data=200)
    verify_json_key_for_not_null(booking_id)
    return booking_id