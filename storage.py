import requests

payload = {"input": "test", "model": "rwkv7-g1d"}
response = requests.post("http://127.0.0.1:65530/api/oai/v1/states", json=payload)
print(response)
