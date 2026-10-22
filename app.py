
import streamlit as st

st.set_page_config(
    page_title="Harvest Rescue AI",
    page_icon="🌱",
    layout="wide"
)

st.title("🌱 Harvest Rescue AI")
st.subheader("Helping farmers recover from cancelled orders")

st.write(
    "When a buyer cancels an order, "
    "find alternative buyers before the produce goes to waste."
)

st.divider()

st.header("📦 Cancelled Order Details")

farmer_name = st.text_input("Farmer's name")
produce = st.selectbox(
    "Type of produce",
    ["Tomatoes", "Carrots", "Cabbage", "Potatoes"]
)

quantity = st.number_input(
    "Unsold quantity (kg)",
    min_value=1,
    value=120
)

minimum_price = st.number_input(
    "Farmer's minimum price per kg (LKR)",
    min_value=1,
    value=170
)

if st.button("Find Recovery Options"):
    st.success("Order details received!")

    st.write("Farmer:", farmer_name or "Demo Farmer")
    st.write("Produce:", produce)
    st.write("Unsold quantity:", quantity, "kg")
    st.write("Minimum price:", f"LKR {minimum_price} per kg")

    st.info(
        "Next, we will build the buyer-matching engine "
        "to find suitable alternative buyers."
    )
