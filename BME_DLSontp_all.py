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
data = pd.read_excel("/Users/raphaelschloubi/Desktop/Year 4/BME/AuNP_ONT_conjugation_20241029 2/DLS/20241029_measurment/Export_2024-10-29_11-34-40/Data table.xlsx", skiprows=2, header=0)

# Initialize dictionaries to store radii values, errors, and Capillaries
radii = {}
error = {}
Capillaries = {}

# Iterate over the indices to extract data
for i in range(0, 22):  # Change to 22 to extract values
    radii[i] = data["⌀.1"][11*i]  # Store radius values
    error[i] = data["σ.1"][11*i]  # Store corresponding error values
    Capillaries[i] = data["Capillaries"][11*i]  # Store capillary values

# Sort the dictionaries based on Capillaries values
sorted_capillaries = sorted(Capillaries.items(), key=lambda x: x[1])

# Reorganize radii, error, and Capillaries based on sorted Capillaries
sorted_radii = [radii[i] for i, _ in sorted_capillaries]
sorted_error = [error[i] for i, _ in sorted_capillaries]
sorted_capillaries_values = [cap for _, cap in sorted_capillaries]

# Define the x-values (from 9.0 to 11.0 with a step of 0.2)
x_values = [9.0 + i*0.2 for i in range(11)]

# Group radii in pairs (1, 12), (2, 13), ..., (11, 22)
radii_pairs = [(sorted_radii[i], sorted_radii[i+11]) for i in range(11)]

# Separate the radii pairs into two lists: one for each value
radii_1 = [pair[0] for pair in radii_pairs]  # First radii in the pair
radii_2 = [pair[1] for pair in radii_pairs]  # Second radii in the pair

# Separate the error values into two lists: one for each radii value
error_1 = [sorted_error[i] for i in range(11)]  # First error in the pair
error_2 = [sorted_error[i+11] for i in range(11)]  # Second error in the pair

# Create a figure
fig, ax = plt.subplots()

# Use the "viridis" colormap
cmap = plt.get_cmap("viridis")

# Normalize the colormap to just have two colors (for two groups)
norm_1 = plt.Normalize(0, 1)  # For Group 1 (samples 1-11)
norm_2 = plt.Normalize(0, 1)  # For Group 2 (samples 12-22)

# Plot the radii for Group 1 (samples 1-11) with the first color from "viridis"
ax.errorbar(x_values, radii_1, yerr=error_1, fmt='o', capsize=5, linestyle='None', color=colors["Color 1"])

# Plot the radii for Group 2 (samples 12-22) with the second color from "viridis"
#ax.errorbar(x_values, radii_2, yerr=error_2, fmt='o', capsize=5, linestyle='None', color=cmap(0.8), label="Measurement 2")

# Label the axes
ax.set_xlabel('pH')
ax.set_ylabel('Radius / nm')

# Set the x-axis limits
ax.set_xlim(8.75, 11.25)

# Show a legend to distinguish between groups


# Show the plot
plt.show()