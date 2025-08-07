from datetime import datetime, timedelta

def check_subscription(start_date_str, duration_days):
    try:
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        end_date = start_date + timedelta(days=duration_days)
        today = datetime.today()

        if today < start_date:
            return "Not started", end_date
        elif today <= end_date:
            return "Active", end_date
        else:
            return "Expired", end_date
    except ValueError:
        return "Invalid date format", None