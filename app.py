import streamlit as st
import pandas as pd
import pickle

# Page settings
st.set_page_config(
    page_title="Hotel Cancellation Prediction",
    page_icon="🏨",
    layout="wide"
)

# Load model
with open("ml_model1 (2).pkl", "rb") as file:
    model = pickle.load(file)

# Background
st.markdown("""
<style>
.stApp {
    background: linear-gradient(rgba(0,0,0,.55),rgba(0,0,0,.55)),
    url("https://images.unsplash.com/photo-1566073771259-6a8506099945");
    background-size: cover;
    background-attachment: fixed;
}

h1,h2,h3,label,p {
    color: white !important;
}

input {
    color: white !important;
}
</style>
""", unsafe_allow_html=True)


# Title
st.title("🏨 Hotel Booking Cancellation Prediction")

st.write("Enter the booking details below:")


# =====================================================
# NUMERICAL INPUTS
# =====================================================

lead_time = st.number_input(
    "Lead Time",
    min_value=0,
    value=100
)

arrival_date_year = st.number_input(
    "Arrival Year",
    min_value=2015,
    max_value=2030,
    value=2017
)

arrival_date_week_number = st.number_input(
    "Arrival Week Number",
    min_value=1,
    max_value=53,
    value=27
)

arrival_date_day_of_month = st.number_input(
    "Arrival Day",
    min_value=1,
    max_value=31,
    value=15
)

stays_in_weekend_nights = st.number_input(
    "Weekend Nights",
    min_value=0,
    value=1
)

stays_in_week_nights = st.number_input(
    "Week Nights",
    min_value=0,
    value=3
)

adults = st.number_input(
    "Adults",
    min_value=0,
    value=2
)

children = st.number_input(
    "Children",
    min_value=0,
    value=0
)

babies = st.number_input(
    "Babies",
    min_value=0,
    value=0
)

is_repeated_guest = st.selectbox(
    "Repeated Guest",
    [0, 1]
)

previous_cancellations = st.number_input(
    "Previous Cancellations",
    min_value=0,
    value=0
)

previous_bookings_not_canceled = st.number_input(
    "Previous Bookings Not Canceled",
    min_value=0,
    value=0
)

booking_changes = st.number_input(
    "Booking Changes",
    min_value=0,
    value=0
)

agent = st.number_input(
    "Agent",
    min_value=0,
    value=9
)

days_in_waiting_list = st.number_input(
    "Days in Waiting List",
    min_value=0,
    value=0
)

adr = st.number_input(
    "ADR (Average Daily Rate)",
    min_value=0.0,
    value=100.0
)

required_car_parking_spaces = st.number_input(
    "Required Car Parking Spaces",
    min_value=0,
    value=0
)

total_of_special_requests = st.number_input(
    "Total Special Requests",
    min_value=0,
    value=0
)


# =====================================================
# CATEGORICAL INPUTS
# =====================================================

hotel = st.selectbox(
    "Hotel",
    ["Resort Hotel", "City Hotel"]
)

arrival_date_month = st.selectbox(
    "Arrival Month",
    [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ]
)

meal = st.selectbox(
    "Meal",
    ["BB", "HB", "FB", "SC", "Undefined"]
)

country = st.text_input(
    "Country",
    "PRT"
)

market_segment = st.selectbox(
    "Market Segment",
    [
        "Direct",
        "Corporate",
        "Online TA",
        "Offline TA/TO",
        "Complementary",
        "Groups",
        "Aviation"
    ]
)

distribution_channel = st.selectbox(
    "Distribution Channel",
    [
        "Direct",
        "Corporate",
        "TA/TO",
        "Undefined",
        "GDS"
    ]
)

reserved_room_type = st.selectbox(
    "Reserved Room Type",
    list("ABCDEFGHLP")
)

assigned_room_type = st.selectbox(
    "Assigned Room Type",
    list("ABCDEFGHLP")
)

deposit_type = st.selectbox(
    "Deposit Type",
    ["No Deposit", "Refundable", "Non Refund"]
)

customer_type = st.selectbox(
    "Customer Type",
    [
        "Transient",
        "Contract",
        "Transient-Party",
        "Group"
    ]
)


# =====================================================
# CREATE INPUT DATAFRAME
# =====================================================

input_data = pd.DataFrame({
    "hotel": [hotel],
    "lead_time": [lead_time],
    "arrival_date_year": [arrival_date_year],
    "arrival_date_month": [arrival_date_month],
    "arrival_date_week_number": [arrival_date_week_number],
    "arrival_date_day_of_month": [arrival_date_day_of_month],
    "stays_in_weekend_nights": [stays_in_weekend_nights],
    "stays_in_week_nights": [stays_in_week_nights],
    "adults": [adults],
    "children": [children],
    "babies": [babies],
    "meal": [meal],
    "country": [country],
    "market_segment": [market_segment],
    "distribution_channel": [distribution_channel],
    "is_repeated_guest": [is_repeated_guest],
    "previous_cancellations": [previous_cancellations],
    "previous_bookings_not_canceled": [previous_bookings_not_canceled],
    "reserved_room_type": [reserved_room_type],
    "assigned_room_type": [assigned_room_type],
    "booking_changes": [booking_changes],
    "deposit_type": [deposit_type],
    "agent": [agent],
    "days_in_waiting_list": [days_in_waiting_list],
    "customer_type": [customer_type],
    "adr": [adr],
    "required_car_parking_spaces": [required_car_parking_spaces],
    "total_of_special_requests": [total_of_special_requests]
})


# =====================================================
# CREATE DERIVED FEATURES
# =====================================================

# Total number of guests
input_data["total_guests"] = (
    input_data["adults"]
    + input_data["children"]
    + input_data["babies"]
)

# Total number of nights
input_data["total_nights"] = (
    input_data["stays_in_weekend_nights"]
    + input_data["stays_in_week_nights"]
)


# =====================================================
# PREDICTION
# =====================================================

if st.button("🔮 Predict Cancellation"):

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("❌ Booking is likely to be CANCELLED")
    else:
        st.success("✅ Booking is likely to NOT be cancelled")
