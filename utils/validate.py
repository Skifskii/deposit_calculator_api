from datetime import datetime


def validate_date(date_string: str) -> bool:
    try:
        datetime.strptime(date_string, "%d.%m.%Y")
        return True
    except ValueError:
        return False


def validate_data(amount: int, periods: int, rate: float, date: str) -> tuple[bool, str]:
    errors = []
    if not validate_date(date):
        errors.append("date" + ": " + "Incorrect date format (must be dd.mm.YYYY)")
    if (periods < 1) or (periods > 60):
        errors.append("periods" + ": " + "The number must be in the range from 1 to 60")
    if (amount < 10_000) or (amount > 3_000_000):
        errors.append("amount" + ": " + "The number must be in the range from 10 000 to 3 000 000")
    if (rate < 1.0) or (rate > 8.0):
        errors.append("rate" + ": " + "The number must be in the range from 1.0 to 8.0")
    if errors:
        answer = "; ".join(errors)
        return False, answer
    return True, ""
