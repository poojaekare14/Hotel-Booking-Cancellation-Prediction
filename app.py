import streamlit as st
import pandas as pd
import pickle


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Hotel Booking Cancellation Prediction",
    page_icon="🏨",
    layout="wide"
)


# =========================================================
# LOAD MODEL
# =========================================================

@st.cache_resource
def load_model():

    with open("hotel_bagging_model.pkl", "rb") as file:
        model = pickle.load(file)

    return model


model = load_model()


# =========================================================
# DARK HOTEL BACKGROUND + CSS
# =========================================================

st.markdown("""
<style>

/* ========================================================
   HOTEL IMAGE BACKGROUND
   ======================================================== */

.stApp {

    background-image:
        linear-gradient(
            rgba(0, 0, 0, 0.78),
            rgba(0, 0, 0, 0.82)
        ),
        url("https://images.unsplash.com/photo-1566073771259-6a8506099945");

    background-size: cover;
    background-position: center;
    background-attachment: fixed;

    color: white;
}


/* ========================================================
   MAIN CONTENT
   ======================================================== */

.block-container {

    padding-top: 2rem;
    padding-bottom: 2rem;

}


/* ========================================================
   TITLE
   ======================================================== */

.title {

    text-align: center;

    color: #ff80ab;

    font-size: 42px;

    font-weight: bold;

    margin-bottom: 5px;

    text-shadow:
        0px 2px 10px rgba(0,0,0,0.8);

}


/* ========================================================
   SUBTITLE
   ======================================================== */

.subtitle {

    text-align: center;

    color: #ffffff;

    font-size: 18px;

    margin-bottom: 30px;

}


/* ========================================================
   SECTION HEADINGS
   ======================================================== */

.section-title {

    color: #ff80ab;

    font-size: 25px;

    font-weight: bold;

    margin-top: 15px;

    margin-bottom: 18px;

}


/* ========================================================
   INPUT LABELS
   ======================================================== */

.stSelectbox label,
.stNumberInput label {

    color: #ffffff !important;

    font-size: 16px !important;

    font-weight: bold !important;

}


/* ========================================================
   INPUT BOXES
   ======================================================== */

.stSelectbox > div > div,
.stNumberInput > div > div {

    background-color: rgba(30, 30, 30, 0.90) !important;

    color: white !important;

    border: 1px solid rgba(255, 128, 171, 0.7);

    border-radius: 8px;

}


/* Text inside inputs */

.stSelectbox div,
.stNumberInput input {

    color: white !important;

}


/* ========================================================
   NUMBER INPUT BUTTONS
   ======================================================== */

.stNumberInput button {

    color: #ff80ab !important;

    background-color: transparent !important;

}


/* ========================================================
   PREDICT BUTTON
   ======================================================== */

.stButton > button {

    width: 100%;

    height: 55px;

    background: linear-gradient(
        90deg,
        #c2185b,
        #ec407a
    );

    color: white;

    border: none;

    border-radius: 12px;

    font-size: 19px;

    font-weight: bold;

    box-shadow:
        0px 4px 15px rgba(0,0,0,0.5);

}


/* Button hover */

.stButton > button:hover {

    background: linear-gradient(
        90deg,
        #ad1457,
        #d81b60
    );

    color: white;

}


/* ========================================================
   DIVIDER
   ======================================================== */

hr {

    border-color: rgba(255, 128, 171, 0.5);

}


/* ========================================================
   SUCCESS RESULT
   ======================================================== */

.success-box {

    padding: 22px;

    border-radius: 15px;

    background: rgba(27, 94, 32, 0.90);

    border: 1px solid #66bb6a;

    color: white;

    text-align: center;

    font-size: 23px;

    font-weight: bold;

    box-shadow:
        0px 5px 20px rgba(0,0,0,0.5);

}


/* ========================================================
   CANCELLED RESULT
   ======================================================== */

.warning-box {

    padding: 22px;

    border-radius: 15px;

    background: rgba(183, 28, 28, 0.90);

    border: 1px solid #ef5350;

    color: white;

    text-align: center;

    font-size: 23px;

    font-weight: bold;

    box-shadow:
        0px 5px 20px rgba(0,0,0,0.5);

}


/* ========================================================
   FOOTER
   ======================================================== */

.footer {

    text-align: center;

    color: #cccccc;

    font-size: 14px;

}

</style>
""", unsafe_allow_html=True)


# =========================================================
# TITLE
# =========================================================

st.markdown(
    '<div class="title">'
    '🏨 Hotel Booking Cancellation Prediction'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Predict whether a hotel booking is likely to be cancelled'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# BOOKING INFORMATION
# =========================================================

st.markdown(
    '<div class="section-title">'
    '📋 Booking Information'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# TWO COLUMNS
# =========================================================

col1, col2 = st.columns(2)


# =========================================================
# LEFT COLUMN
# =========================================================

with col1:

    hotel = st.selectbox(
        "Hotel",
        [
            "Resort Hotel",
            "City Hotel"
        ]
    )


    lead_time = st.number_input(
        "Lead Time",
        min_value=0,
        value=100,
        step=1
    )


    arrival_date_month = st.selectbox(
        "Arrival Month",
        [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
        ]
    )


    stays_in_weekend_nights = st.number_input(
        "Weekend Nights",
        min_value=0,
        value=1,
        step=1
    )


    stays_in_week_nights = st.number_input(
        "Week Nights",
        min_value=0,
        value=2,
        step=1
    )


    adults = st.number_input(
        "Adults",
        min_value=0,
        value=2,
        step=1
    )


    children = st.number_input(
        "Children",
        min_value=0.0,
        value=0.0,
        step=1.0
    )


# =========================================================
# RIGHT COLUMN
# =========================================================

with col2:

    is_repeated_guest = st.selectbox(
        "Repeated Guest",
        [0, 1],

        format_func=lambda x:
            "No" if x == 0 else "Yes"
    )


    previous_cancellations = st.number_input(
        "Previous Cancellations",
        min_value=0,
        value=0,
        step=1
    )


    market_segment = st.selectbox(
        "Market Segment",
        [
            "Online TA",
            "Offline TA/TO",
            "Direct",
            "Groups",
            "Corporate",
            "Complementary",
            "Aviation"
        ]
    )


    deposit_type = st.selectbox(
        "Deposit Type",
        [
            "No Deposit",
            "Refundable",
            "Non Refund"
        ]
    )


    customer_type = st.selectbox(
        "Customer Type",
        [
            "Transient",
            "Transient-Party",
            "Contract",
            "Group"
        ]
    )


    adr = st.number_input(
        "Average Daily Rate (ADR)",
        min_value=0.0,
        value=100.0,
        step=1.0
    )


    total_of_special_requests = st.number_input(
        "Total Special Requests",
        min_value=0,
        value=0,
        step=1
    )


# =========================================================
# PREDICT BUTTON
# =========================================================

st.markdown("")

predict_button = st.button(
    "🔮 Predict Booking Cancellation",
    use_container_width=True
)


# =========================================================
# PREDICTION
# =========================================================

if predict_button:

    # -----------------------------------------------------
    # CREATE INPUT DATA
    # -----------------------------------------------------

    input_data = {

        "hotel": hotel,

        "lead_time": lead_time,

        "arrival_date_month":
            arrival_date_month,

        "stays_in_weekend_nights":
            stays_in_weekend_nights,

        "stays_in_week_nights":
            stays_in_week_nights,

        "adults":
            adults,

        "children":
            children,

        "is_repeated_guest":
            is_repeated_guest,

        "previous_cancellations":
            previous_cancellations,

        "market_segment":
            market_segment,

        "deposit_type":
            deposit_type,

        "customer_type":
            customer_type,

        "adr":
            adr,

        "total_of_special_requests":
            total_of_special_requests
    }


    # -----------------------------------------------------
    # DATAFRAME
    # -----------------------------------------------------

    input_df = pd.DataFrame(
        [input_data]
    )


    # -----------------------------------------------------
    # PREDICTION
    # -----------------------------------------------------

    prediction = model.predict(
        input_df
    )[0]


    # =====================================================
    # RESULT
    # =====================================================

    st.markdown("---")

    st.markdown(
        '<div class="section-title">'
        '📊 Prediction Result'
        '</div>',
        unsafe_allow_html=True
    )


    if prediction == 1:

        st.markdown(
            """
            <div class="warning-box">

            ⚠️ Booking is likely to be <b>CANCELLED</b>

            </div>
            """,
            unsafe_allow_html=True
        )


    else:

        st.markdown(
            """
            <div class="success-box">

            ✅ Booking is likely to be <b>NOT CANCELLED</b>

            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.markdown(
    """
    <div class="footer">

    Tuned Bagging Classifier |
    Accuracy: Approximately 85.09%

    </div>
    """,
    unsafe_allow_html=True
)