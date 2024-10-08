# VErify status code

# def verify_http_status_code(response_data,expect_data):
#     assert response_data.status_code == expect_data, "Failed ER!=AR"
def verify_http_status_code(response_data, expect_data):
    assert response_data.status_code == expect_data, (
        f"Failed: Expected status code {expect_data}, but got {response_data.status_code}"
    )


#def verify_response_key(key,expected_data):
    #assert key == expected_data
def verify_response_key(actual_data, expected_data):
    print(f"Expected: {expected_data}, Actual: {actual_data}")
    assert actual_data == expected_data, f"Assertion Failed: Expected {expected_data}, but got {actual_data}"

def verify_json_key_for_not_null(key):
    assert key != 0, "Failed - Key is non Empty" + key
    assert key > 0, "Failed - Key is grater than zero"


def verify_json_key_for_not_null_token(key):
    assert key != 0, "Failed - Key is non Empty" + key


def verify_response_key_should_not_be_none(key):
    assert key is not None


def verify_response_delete(response):
    assert "Created" in response