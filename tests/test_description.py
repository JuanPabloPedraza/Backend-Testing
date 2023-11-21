import allure
import pytest

from services.payment_request import post_payment_request

@pytest.fixture(scope="session")
def response_payment():
    with allure.step('Make the payment request'):
        response, response_payment = post_payment_request('set_2')
        return response, response_payment

@allure.feature('Validation Status Code 400')
@allure.story('Verify the response status code is 400')
def test_TC_05_validate_status_code_400(response_payment):
    response, response_payment = response_payment
    with allure.step('Verify that status code is 400'):
        assert response.status_code == 400

@allure.feature('Validation Status Code 400')
@allure.story('Verify the message is "Validation Failed"')
def test_TC_06_validate_error_message(response_payment):
    response, response_payment = response_payment
    with allure.step('Verify that message is Validation Failed'):
        assert response_payment["message"] == "Validation Failed"

@allure.feature('Validation Status Code 400')
@allure.story('Verify specific errors in the description')
def test_TC_07_validate_description_errors(response_payment):
    response, response_payment = response_payment
    with allure.step('Verify text of errors'):
        errors = response_payment["errors"]["children"]["description"]["errors"]
        assert "Este valor es demasiado largo. Debería tener 500 caracteres o menos." in errors
