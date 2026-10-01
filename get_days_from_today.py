import datetime
def get_days_from_today(date):
    try:
        converted_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        today_date = datetime.date.today()
        return (converted_date - today_date).days
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."
print(get_days_from_today("2023-01-01"))