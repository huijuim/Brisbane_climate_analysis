import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/hj/Desktop/4. Project/1/brisbane_climate_2015_2024_final_1.csv")

df["Rainfall"] = df["Rainfall"].astype(str).str.replace(r"[^\d\.]", "", regex=True).astype(float)
df["AvgMaxTemp"] = df["AvgMaxTemp"].astype(str).str.replace(r"[^\d\.]", "", regex=True).astype(float)
df["AvgMinTemp"] = df["AvgMinTemp"].astype(str).str.replace(r"[^\d\.]", "", regex=True).astype(float)

yearly = df.groupby("Year").agg({
    "AvgMaxTemp": "mean",
    "AvgMinTemp": "mean",
    "Rainfall": "sum"
}).reset_index()

# Visualization of Yearly Average Temperatures
plt.figure(figsize=(10, 5))
plt.plot(yearly["Year"], yearly["AvgMaxTemp"], marker='o', label="Avg Max Temp")
plt.plot(yearly["Year"], yearly["AvgMinTemp"], marker='o', label="Avg Min Temp")
plt.title("Yearly Average Temperatures in Brisbane (2015–2024)")
plt.xlabel("Year")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Visualization of Yearly Total Rainfall
plt.figure(figsize=(10, 5))
plt.bar(yearly["Year"], yearly["Rainfall"])
plt.title("Yearly Total Rainfall in Brisbane (2015–2024)")
plt.xlabel("Year")
plt.ylabel("Rainfall (mm)")
plt.grid(True)
plt.tight_layout()
plt.show()

# Calculate Monthly Average Temperatures and Rainfall
monthly = df.groupby("Month").agg({
    "AvgMaxTemp": "mean",
    "AvgMinTemp": "mean",
    "Rainfall": "mean"
}).reset_index()

# Temperature Graph
plt.figure(figsize=(10, 5))
plt.plot(monthly["Month"], monthly["AvgMaxTemp"], marker='o', label="Avg Max Temp")
plt.plot(monthly["Month"], monthly["AvgMinTemp"], marker='o', label="Avg Min Temp")
plt.title("Monthly Average Temperatures in Brisbane (2015–2024)")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.xticks(range(1, 13))
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Rainfall graph
plt.figure(figsize=(10, 5))
plt.bar(monthly["Month"], monthly["Rainfall"])
plt.title("Monthly Average Rainfall in Brisbane (2015–2024)")
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.xticks(range(1, 13))
plt.grid(True)
plt.tight_layout()
plt.show()

# Check Top 3 Years with Highest Total Rainfall
yearly = df.groupby("Year").agg({
    "Rainfall": "sum"
}).reset_index()

top_rain = yearly.sort_values(by="Rainfall", ascending=False)
print(top_rain.head(3))  # View Top 3 Years

# Monthly Rainfall in 2022
rain_2022 = df[df["Year"] == 2022]

plt.figure(figsize=(10, 5))
plt.bar(rain_2022["Month"], rain_2022["Rainfall"])
plt.title("Monthly Rainfall in Brisbane (2022)")
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.xticks(range(1, 13))
plt.grid(True)
plt.tight_layout()
plt.show()

