import allure
import pytest

from services.payment_request import post_payment_request
from utils.get_data import get_data_from_json
from datetime import datetime
from utils.tools import url_exists_and_valid

@pytest.fixture(scope="session")
def payment_request_data():
    with allure.step('Load the input data'):
        return get_data_from_json('set_1')
@pytest.fixture(scope="session")
def response_payment():
    with allure.step('Make the payment request'):
        response, response_payment = post_payment_request('set_1')
        return response, response_payment


@allure.feature('Payment Creation')
@allure.story('Create a payment successfully')
def test_TC_01_create_payment_success(response_payment, payment_request_data):
    response, response_payment = response_payment
    with allure.step('Verify that the payment is created successfully'):
        assert response.status_code == 201

@allure.feature('Payment Creation')
@allure.story('Input and Output Data Validation')
def test_TC_02_validate_input_output(response_payment, payment_request_data):
    response, response_payment = response_payment
    with allure.step('Verify the payment description matches the input'):
        assert response_payment['description'] == payment_request_data['payment_request']['description']

    with allure.step('Verify the due date is correctly formatted'):
        entered_date = payment_request_data['payment_request']['first_due_date']
        desired_date = datetime.strptime(entered_date, '%d-%m-%Y').strftime('%Y-%m-%dT00:00:00-03:00')
        assert response_payment['first_due_date'] == desired_date

    with allure.step('Verify other payment details'):
        assert response_payment['first_total'] == payment_request_data['payment_request']['first_total']
        assert response_payment['payer_name'] == payment_request_data['payment_request']['payer_name']

@allure.feature('Payment Creation')
@allure.story('Validation of the Request Status')
def test_TC_03_validate_payment_state(response_payment):
    response, response_payment = response_payment
    with allure.step('Verify that the request status is "pending"'):
        assert response_payment['state'] == 'pending'

@allure.feature('Payment Creation')
@allure.story('Validation of URLs in the Response')
def test_TC_04_validate_payment_urls(response_payment):
    response, response_payment = response_payment
    with allure.step('Verify the existence and validity of payment URLs'):
        checkout_url = response_payment['checkout_url']
        barcode_url = response_payment['barcode_url']
        pdf_url = response_payment['pdf_url']
        assert url_exists_and_valid(checkout_url)
        assert url_exists_and_valid(barcode_url)
        assert url_exists_and_valid(pdf_url)