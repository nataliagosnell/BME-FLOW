import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
colors = {
    "Color 1": "#016FEB",  # Bright Blue 
    "Color 2": "#00326A",  # Deep Navy Blue
    "Color 3": "#749AFF",  # Light Sky Blue
    "Color 4": "#9AA5D8",  # Soft Lavender Blue
    "Color 5": "#827742",  # Olive Brown
    "Color 6": "#463F0F"   # Dark Olive Green
}



# Load data from the Excel file
data = pd.read_excel("/Users/raphaelschloubi/Desktop/Year 4/BME/bme_AuNPs_DLS_sAv_2024-11-26_12-09-21/Data table.xlsx", skiprows=2, header=0)
data['Capillaries'] = pd.to_numeric(data['Capillaries'], errors='coerce')  # Converts non-numeric values to NaN if any

# Initialize dictionaries to store radii values, errors, and Capillaries
radii = {}
error = {}
capillaries = {}

# Iterate over the indices to extract data
for i in range(0, 28):  # Change to 28 to extract values
    radii[i] = data["⌀.1"][11*i]  # Store radius values
    error[i] = data["σ.1"][11*i]  # Store corresponding error values
    capillaries[i] = data["Capillaries"][11*i]  # Store capillary values
df = pd.DataFrame({
    'Radii': radii,
    'Error': error,
    'Capillaries': capillaries
})
x_values = [4.5, 5.0, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.6, 10, 10.6, 11]
# Sort the dictionaries based on Capillaries values
# Sort the DataFrame by Capillaries
df_sorted = df.sort_values(by='Capillaries')

# Extract sorted values
sorted_radii = df_sorted['Radii'].values
sorted_error = df_sorted['Error'].values
sorted_radii[14] = 50
sorted_radii[15] = 50
sorted_radii[24] = 50
sorted_radii[25] = 50
sorted_radii[27] = 50
sorted_radii[26] = 50
sorted_radii[23] = 50

# Group radii in pairs (1, 12), (2, 13), ..., (11, 22)
radii_pairs = [(sorted_radii[i], sorted_radii[i+14]) for i in range(14)]

# Separate the radii pairs into two lists: one for each value
radii_1 = [pair[0] for pair in radii_pairs]  # First radii in the pair
#radii_2 = [pair[1] for pair in radii_pairs]  # Second radii in the pair

# Separate the error values into two lists: one for each radii value
error_1 = [sorted_error[i] for i in range(14)]  # First error in the pair
#error_2 = [sorted_error[i+14] for i in range(14)]  # Second error in the pair

# Create a figure
fig, ax = plt.subplots()

# Use the "viridis" colormap
cmap = plt.get_cmap("viridis")

# Normalize the colormap to just have two colors (for two groups)
norm_1 = plt.Normalize(0, 1)  # For Group 1 (samples 1-11)
norm_2 = plt.Normalize(0, 1)  # For Group 2 (samples 12-22)

# Plot the radii for Group 1 (samples 1-11) with the first color from "viridis"
ax.errorbar(x_values[0], radii_1[0], yerr=error_1[0], fmt='o', capsize=5, linestyle='None', color=colors["Color 1"])

ax.errorbar(x_values[2:], radii_1[2:], yerr=error_1[2:], fmt='o', capsize=5, linestyle='None', color=colors["Color 1"])

# Plot the radii for Group 2 (samples 12-22) with the second color from "viridis"
#ax.errorbar(x_values, radii_2, yerr=error_2, fmt='o', capsize=5, linestyle='None', color=cmap(0.8), label="Buffer")

# Label the axes
ax.set_xlabel('pH')
ax.set_ylabel('Radius / nm')

# Set the x-axis limits
ax.set_xlim(4.4, 11.1)

# Show a legend to distinguish between groups
#ax.legend()

# Show the plot
plt.show()

