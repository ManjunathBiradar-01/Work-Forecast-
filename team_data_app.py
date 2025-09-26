
import streamlit as st
import pandas as pd
import os

# Load the Excel file and read the Forecast sheet
excel_file = "Work Forecast - Team Vice.xlsx"
df = pd.read_excel(excel_file, sheet_name="Forecast", engine="openpyxl")

# Create storage folder
storage_folder = "team_data"
os.makedirs(storage_folder, exist_ok=True)

st.title("Team Forecast and Actual Work Entry")

# Dropdown to select team
teams = sorted(df["Team"].dropna().unique())
selected_team = st.selectbox("Select Team", teams)

# Dropdown to select team member based on selected team
members = sorted(df[df["Team"] == selected_team]["Team Member"].dropna().unique())
selected_member = st.selectbox("Select Team Member", members)

# Filter data for selected team and member
filtered_data = df[(df["Team"] == selected_team) & (df["Team Member"] == selected_member)]

# Initialize list to collect updated entries
updated_entries = []

# Display input fields for each month and week
for _, row in filtered_data.iterrows():
    month = row["Month"]
    week = row["Week"]
    st.markdown(f"**{month} - {week}**")
    col1, col2 = st.columns(2)
    with col1:
        forecast = col1.number_input(
            f"{month} {week} Forecast",
            min_value=0.0,
            value=float(row["Forecast"]) if pd.notna(row["Forecast"]) else 0.0,
            key=f"{month}_{week}_forecast"
        )
    with col2:
        actual = col2.number_input(
            f"{month} {week} Actual Work",
            min_value=0.0,
            value=float(row["Actual Work"]) if pd.notna(row["Actual Work"]) else 0.0,
            key=f"{month}_{week}_actual"
        )
    updated_entries.append({
        "Team": selected_team,
        "Team Member": selected_member,
        "Month": month,
        "Week": week,
        "Forecast": forecast,
        "Actual Work": actual
    })

# Save button
if st.button("Save Data"):
    save_df = pd.DataFrame(updated_entries)
    file_path = os.path.join(storage_folder, f"{selected_team}_{selected_member}.xlsx")
    save_df.to_excel(file_path, index=False)
    st.success(f"Data saved successfully to {file_path}")
