from flask import Flask
from pydantic import BaseModel
from flask_pydantic import validate, ValidationError

from utils.scripts import calculate_deposit
from utils.validate import validate_data


class Body(BaseModel):
    date: str
    periods: int
    amount: int
    rate: float


app = Flask(__name__)

app.config["FLASK_PYDANTIC_VALIDATION_ERROR_RAISE"] = True
app.json.sort_keys = False


@app.errorhandler(ValidationError)
def handle_validation_error(e):
    try:
        errors = []
        for error in e.body_params:
            errors.append(error["loc"][0] + ": " + error["msg"])
        answer = "; ".join(errors)
    except Exception as _:
        answer = "ValidationError"
    return {"error": answer}, 400


@app.route("/calculate_deposit", methods=["POST"])
@validate()
def get_calculated_deposit(body: Body):
    validation_result, message = validate_data(**body.__dict__)
    if not validation_result:
        return {"error": message}, 400

    calculation_result = calculate_deposit(**body.__dict__)
    return calculation_result


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=3000)
