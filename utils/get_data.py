import json
from json import load

def get_data_from_json(set_name="set_1"):
    ruta = '../data/payments.json'
    with open(ruta) as content:
        data = load(content)
        print(json.dumps(data, indent=2))
        return {"payment_request": data.get("test_data", {}).get(set_name, {}).get("payment_request", {})}