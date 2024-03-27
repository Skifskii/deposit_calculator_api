from calendar import monthrange
from datetime import datetime


def calculate_next_date(old_date: datetime, start_day: int) -> str:
    if old_date.month == 12:
        new_year = old_date.year + 1  # Инкремент года
    else:
        new_year = old_date.year
    new_month = old_date.month % 12 + 1  # Инкремент месяца
    new_day = min(start_day, monthrange(new_year, new_month)[1])  # Перерасчет дня

    new_date = datetime(new_year, new_month, new_day)
    return new_date


def calculate_deposit(amount: int, periods: int, rate: float, date: str) -> dict[str:float]:
    date_obj = datetime.strptime(date, "%d.%m.%Y")
    start_date_day = date_obj.day
    result = {}

    for _ in range(periods):
        amount = round(amount * (1 + rate / 100 / 12), 2)
        result[date_obj.strftime("%d.%m.%Y")] = amount
        date_obj = calculate_next_date(date_obj, start_date_day)

    return result
