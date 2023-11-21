import allure
import requests
import json
import os

from dotenv import load_dotenv
from utils.get_data import get_data_from_json
from requests.exceptions import RequestException

def post_payment_request(step):
    """
    Creates a new payment request.

    Returns:
    dict: The response of the request.
    """
    # Load the token from the .env file
    load_dotenv()
    bearer_token = os.getenv("BEARER_TOKEN")

    # Set up the URL and headers
    endpoint = "https://api.sandbox.pagos360.com"
    service = "/payment-request"
    payment_url = (endpoint + service)
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/json"
    }

    # Get data from JSON
    params = get_data_from_json(step)

    # Attach the URL and body of the request to Allure
    allure.attach(payment_url, name='Request URL', attachment_type=allure.attachment_type.TEXT)
    allure.attach(json.dumps(params, indent=2), name='Request Body', attachment_type=allure.attachment_type.JSON)

    try:
        # Make the request
        response = requests.post(
            payment_url,
            json=params,
            headers=headers
        )
        response_payment = json.loads(response.text)
        with allure.step('Attach the response to Allure'):
            allure.attach(json.dumps(response_payment, indent=2), name='Response',
                          attachment_type=allure.attachment_type.JSON)
        return response, response_payment
    except RequestException as e:
        allure.attach(str(e), name='Error', attachment_type=allure.attachment_type.TEXT)
        raise Exception(f"Error in the request: {str(e)}")