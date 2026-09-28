import datetime
today_date = datetime.date.today()
random_date = datetime.date(2023, 1, 1)  # Example random date
print(f'Days from today to {random_date}: {(random_date - today_date).days}')