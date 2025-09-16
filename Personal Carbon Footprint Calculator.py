import streamlit as st
import csv
from datetime import datetime

st.title("🌱 Personal Carbon Footprint Calculator")

electricity = st.number_input("🔌 Electricity usage per day (kWh):", min_value=0.0)
travel_km = st.number_input("🚗 Distance traveled per day (km):", min_value=0.0)
meat_meals = st.number_input("🍖 Number of meat meals per day:", min_value=0)

if st.button("Calculate"):
    co2_electricity = electricity * 0.82
    co2_travel = travel_km * 0.121
    co2_meals = meat_meals * 5.0
    total_co2 = co2_electricity + co2_travel + co2_meals

    st.subheader("📊 Results")
    st.write(f"Electricity: {co2_electricity:.2f} kg CO₂")
    st.write(f"Travel: {co2_travel:.2f} kg CO₂")
    st.write(f"Food: {co2_meals:.2f} kg CO₂")
    st.success(f"🌎 Total: {total_co2:.2f} kg CO₂")

    st.info("💡 Eco-Tips:")
    if electricity > 5:
        st.write("- Switch to LED bulbs & turn off devices.")
    if travel_km > 10:
        st.write("- Try carpooling, cycling, or public transport.")
    if meat_meals > 1:
        st.write("- Try a plant-based meal once a day.")

    # Save results
    date_today = datetime.now().strftime("%Y-%m-%d")
    with open("carbon_log.csv", "a", newline="") as file:
        csv.writer(file).writerow([date_today, electricity, travel_km, meat_meals, total_co2])


