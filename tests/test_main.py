from main import app


def test_get_calculated_deposit():
    with app.test_client() as c:
        input_vector = {
            "date": "31.01.2021",
            "periods": 3,
            "amount": 10_000,
            "rate": 6.0
        }
        response = c.post(
            "http://127.0.0.1:3000/calculate_deposit",
            json=input_vector
        )
        assert response.status_code == 200
        assert response.get_json() == {
            '31.01.2021': 10050.0,
            '28.02.2021': 10100.25,
            '31.03.2021': 10150.75
        }


def test_get_calculated_deposit_with_empty_json():
    with app.test_client() as c:
        input_vector = {}
        response = c.post(
            "http://127.0.0.1:3000/calculate_deposit",
            json=input_vector
        )
        assert response.status_code == 400
        assert response.get_json() == {
            'error': 'date: Field required; periods: Field required; amount: Field required; rate: Field required'
        }


def test_get_calculated_deposit_wrong_types():
    with app.test_client() as c:
        input_vector = {
            "date": True,
            "periods": 3.5,
            "amount": "some",
            "rate": "qwerty"
        }
        response = c.post(
            "http://127.0.0.1:3000/calculate_deposit",
            json=input_vector
        )
        assert response.status_code == 400
        assert response.get_json() == {
            'error': 'date: Input should be a valid string; periods: Input should be a valid integer, got a number with a fractional part; amount: Input should be a valid integer, unable to parse string as an integer; rate: Input should be a valid number, unable to parse string as a number'
        }


def test_get_calculated_deposit_wrong_data():
    with app.test_client() as c:
        input_vector = {
            "date": "32.01.2021",
            "periods": -1,
            "amount": 1000,
            "rate": 15.0
        }
        response = c.post(
            "http://127.0.0.1:3000/calculate_deposit",
            json=input_vector
        )
        assert response.status_code == 400
        assert response.get_json() == {
            'error': 'date: Incorrect date format (must be dd.mm.YYYY); periods: The number must be in the range from 1 to 60; amount: The number must be in the range from 10 000 to 3 000 000; rate: The number must be in the range from 1.0 to 8.0'
        }
