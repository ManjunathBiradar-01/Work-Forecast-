import streamlit as st
import pandas as pd
import os

# Define the structure of the data
data_structure = {
    "BAL": {
        "Abhishek Shukla": {
            "Sep": ["Week 36", "Week 37", "Week 38", "Week 39"],
            "Oct": ["Week 40", "Week 41", "Week 42", "Week 43"],
            "Nov": ["Week 44", "Week 45", "Week 46", "Week 47", "Week 48"]
        },
        "Akshay Peddarajula": {
            "Sep": ["Week 36", "Week 37", "Week 38", "Week 39"],
            "Oct": ["Week 40", "Week 41", "Week 42", "Week 43"],
            "Nov": ["Week 44", "Week 45", "Week 46", "Week 47", "Week 48"]
        }
    }
}

# Create storage folder
storage_folder = "team_data"
os.makedirs(storage_folder, exist_ok=True)

st.title("Team Weekly Forecast and Actual Work Entry")

# Initialize session state to store inputs
if "entries" not in st.session_state:
    st.session_state.entries = []

# Display input table
for team, members in data_structure.items():
    for member, months in members.items():
        st.subheader(f"{team} - {member}")
        for month, weeks in months.items():
            st.markdown(f"**{month}**")
            for week in weeks:
                col1, col2 = st.columns(2)
                with col1:
                    forecast = st.number_input(f"{month} {week} Forecast", min_value=0.0, key=f"{team}_{member}_{month}_{week}_forecast")
                with col2:
                    actual = st.number_input(f"{month} {week} Actual", min_value=0.0, key=f"{team}_{member}_{month}_{week}_actual")
                st.session_state.entries.append({
                    "Team": team,
                    "Team Member": member,
                    "Month": month,
                    "Week": week,
                    "Forecast": forecast,
                    "Actual Work": actual
                })

# Save button
if st.button("Save All Data"):
    df = pd.DataFrame(st.session_state.entries)
    file_path = os.path.join(storage_folder, "BAL_team_data.xlsx")
    df.to_excel(file_path, index=False)
    st.success(f"Data saved successfully to {file_path}")

    
