import requests

input_vector = {
    "date": "31.01.2021",
    "periods": 3,
    "amount": 10_000,
    "rate": 6.0
}

res = requests.post("http://localhost:3000/calculate_deposit", json=input_vector)
print(res.json())
