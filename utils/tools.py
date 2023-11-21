import requests

def url_exists_and_valid(url):
    if url:
        try:
            response = requests.get(url)
            return response.status_code == 200
        except requests.RequestException as e:
            error_message = str(e)
            return {"url": url, "error_message": error_message}
    else:
        return {"url": None, "error_message": "URL not provided"}
