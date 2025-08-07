import streamlit as st
from utils.validator import check_subscription
from utils.notifier import send_sms, send_email
from utils.storage import load_subscriptions, save_subscription
import pandas as pd

st.title("📅 Subscription Monitor")

with st.form("subscription_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    start_date = st.date_input("Subscription Start Date")
    duration = st.number_input("Duration (days)", min_value=1)
    submitted = st.form_submit_button("Check Subscription")

if submitted:
    status, expiry = check_subscription(str(start_date), int(duration))
    st.write(f"**Status:** {status}")
    st.write(f"**Expires on:** {expiry.date() if expiry else 'N/A'}")

    if status == "Expired":
        send_sms(phone, f"Hi {name}, your subscription expired on {expiry.date()}. Please renew.")
        send_email(email, "Subscription Expired", f"Dear {name}, your subscription expired on {expiry.date()}.")

    # Save to CSV
    df = load_subscriptions()
    new_entry = pd.DataFrame([[name, email, phone, start_date, duration]],
                             columns=["Name", "Email", "Phone", "StartDate", "Duration"])
    df = pd.concat([df, new_entry], ignore_index=True)
    save_subscription(df)
