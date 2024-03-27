import requests

input_vector = {
    "date": "32.01.2021",
    "periods": -1,
    "amount": 1000,
    "rate": 15.0
}

res = requests.post("http://127.0.0.1:3000/calculate_deposit")
print(res.json())
