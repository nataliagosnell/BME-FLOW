import sys
import seaborn
seaborn.set_theme()
import pandas
import openpyxl
import matplotlib.pyplot as plt
colors = {
    "Color 1": "#016FEB",  # Bright Blue 
    "Color 2": "#00326A",  # Deep Navy Blue
    "Color 3": "#749AFF",  # Light Sky Blue
    "Color 4": "#9AA5D8",  # Soft Lavender Blue
    "Color 5": "#827742",  # Olive Brown
    "Color 6": "#463F0F"   # Dark Olive Green
}

data = pandas.read_excel("/Users/raphaelschloubi/Desktop/Year 4/BME/AuNP_ONT_conjugation_20241029 2/DLS/20241029_measurment/Export_2024-10-29_11-34-40/Sample 5/Sample 5.xlsx")
data2 = pandas.read_excel("/Users/raphaelschloubi/Desktop/Year 4/BME/AuNP_ONT_conjugation_20241029 2/DLS/20241029_measurment/Export_2024-10-29_11-34-40/Sample 16/Sample 16.xlsx")

print(data2.columns)
plt.figure(figsize=(10, 6))
seaborn.set_theme(style="white")
seaborn.set_style("ticks")

seaborn.lineplot(data=data, x='Radius [nm]', y='Relative frequency [%]', color=colors["Color 1"])
seaborn.lineplot(data=data2, x='Radius [nm]', y='Relative frequency [%]', color=colors["Color 2"])


plt.xlabel("Radius / nm")
plt.ylabel("Relative frequency / %")
plt.title("Radius distribution at pH = 9.8") 
plt.xlim(0, 60)

plt.grid(False)

plt.show()
