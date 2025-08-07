import pandas as pd

def load_subscriptions(path="data/subscriptions.csv"):
    try:
        return pd.read_csv(path)
    except FileNotFoundError:
        return pd.DataFrame(columns=["Name", "Email", "Phone", "StartDate", "Duration"])

def save_subscription(df, path="data/subscriptions.csv"):
    df.to_csv(path, index=False)