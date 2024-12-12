import os
import scipy
from scipy import io
import time
import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# Initial sweep data (Au-ONT Conjugation 10/29)


# file name
filename1 = 'C:/Users/natal/Downloads/AuNP_ONT_conjugation_20241029/Plate Reader/Plate 1_AuNPs_spectra_20241029_.csv'
data_t0 = pd.read_csv(filename1)

# Extract wavelengths and sample data
wavelengths = data_t0.iloc[29:100, 0].to_numpy()  # First column for wavelengths
sample_data_t0 = data_t0.iloc[29:100, 1:35].to_numpy()  # Remaining columns for samples
samples_t0 = data_t0.iloc[28,1:35].to_numpy()

#extract flocculation data
flocculation_t0 = data_t0.iloc[76,1:35].to_numpy()

filename2 = 'C:/Users/natal/Downloads/AuNP_ONT_conjugation_20241029/Plate Reader/Plate 2_AuNPs_spectra_20241029_.csv'
data_t1h = pd.read_csv(filename2)

# Extract wavelengths and sample data
sample_data_t1h = data_t1h.iloc[29:100, 1:35].to_numpy()  # Remaining columns for samples
samples_t1h = data_t1h.iloc[28,1:35].to_numpy()

#extract flocculation data
flocculation_t1h = data_t1h.iloc[76,1:35].to_numpy()

filename3 = 'C:/Users/natal/Downloads/AuNP_ONT_conjugation_20241029/Plate Reader/Plate 3_AuNPs_spectra_20241029_.csv'
data_salt = pd.read_csv(filename3)

# Extract wavelengths and sample data
sample_data_salt = data_salt.iloc[29:100, 1:35].to_numpy()  # Remaining columns for samples
samples_salt = data_salt.iloc[28,1:35].to_numpy()

#extract flocculation data
flocculation_salt = data_salt.iloc[76,1:35].to_numpy()

# print(flocculation)
# print(samples)

# Create a list to store peak values and their corresponding wavelengths
peaks_t0 = []
peaks_t1h = []
peaks_salt = []
absorbance_t0 = []
absorbance_t1h = []
absorbance_salt = []
absorbance_buffer = []
absorbance_water = []
data_abs_t0 = []
data_abs_t1h = []
data_abs_salt = []
data_abs_buffer = []
data_abs_water = []

pH = [9.0, 9.2, 9.4, 9.6, 9.8, 10.0, 10.2, 10.4, 10.6, 10.8, 11.0]
print(f"Length of pH: {len(pH)}")

# Loop through each sample
for i in range(11):
    sample = sample_data_t0.T[i]  # Transpose to iterate over samples
    peak_value = np.max(sample)  # Get the maximum absorbance
    peak_index = np.argmax(sample)  # Get the index of the maximum absorbance
    peak_wavelength = wavelengths[peak_index]  # Corresponding wavelength
    data_abs_t0 = sample_data_t0[:,i]
    data_abs_t1h = sample_data_t1h[:,i]
    data_abs_salt = sample_data_salt[:,i]
    buffer_i = i + 22
    data_abs_buffer = sample_data_t0[:,buffer_i]
    data_abs_water = sample_data_t0[:,33]

    absorbance_t0 = [] # extract peak values for initial timepoint
    for x in data_abs_t0:
        try:
            absorbance_t0.append(float(x))
        except ValueError:
            print(f"Warning: '{x}' is not a valid number and will be ignored.")
    peak_value = np.max(absorbance_t0)
    absorbance_t0 = [x / peak_value for x in absorbance_t0]
    peaks_t0.append((peak_wavelength, peak_value))

    absorbance_t1h = [] # extract peak values for 1 hour timepoint
    for x in data_abs_t1h:
        try:
            absorbance_t1h.append(float(x))
        except ValueError:
            print(f"Warning: '{x}' is not a valid number and will be ignored.")
    absorbance_t1h = [x / peak_value for x in absorbance_t1h]
    # peaks_t1h.append((peak_wavelength, peak_value))

    absorbance_salt = [] # extract peak values after salt addition
    for x in data_abs_salt:
        try:
            absorbance_salt.append(float(x))
        except ValueError:
            print(f"Warning: '{x}' is not a valid number and will be ignored.")
    absorbance_salt = [x / peak_value for x in absorbance_salt]

    absorbance_buffer = [] # extract peak values for buffer controls
    for x in data_abs_buffer:
        try:
            absorbance_buffer.append(float(x))
        except ValueError:
            print(f"Warning: '{x}' is not a valid number and will be ignored.")
    absorbance_buffer = [x / peak_value for x in absorbance_buffer]

    absorbance_water = [] # extract peak values for water controls
    for x in data_abs_water:
        try:
            absorbance_water.append(float(x))
        except ValueError:
            print(f"Warning: '{x}' is not a valid number and will be ignored.")
    absorbance_water = [x / peak_value for x in absorbance_water]

    # Plotting the absorbance spectrum for each sample
    current_pH = pH[i]

    wavelengths = np.array(wavelengths)
    absorbance_t0 = np.array(absorbance_t0)
    absorbance_buffer = np.array(absorbance_buffer)
    absorbance_water = np.array(absorbance_water)
    wavelengths = pd.to_numeric(wavelengths, errors='coerce')
    data = pd.DataFrame({
    "wavelengths": np.tile(wavelengths, 3),  # Repeat wavelengths for each sample
    "absorbance": np.concatenate([absorbance_t0, absorbance_buffer, absorbance_water]),  # Concatenate absorbance values
    "Sample": ["IgG + AuNPs"] * len(wavelengths) + ["Buffer + AuNPs"] * len(wavelengths) + ["Water + AuNPs"] * len(wavelengths),  # Labels
    })

    # Set the theme
    sns.set_theme(style="white")
    sns.set_style("ticks")
    sns.color_palette("Blues", as_cmap=True)


    # Plot with viridis palette
    sns.lineplot(data=data, x="wavelengths", y="absorbance", hue="Sample", palette = "deep")
    plt.xlabel("Wavelengths / nm", fontweight = 'bold')
    plt.ylabel("Absorbance / normalized", fontweight = 'bold')
    plt.title(f'Absorbance Spectrum for pH {current_pH}', fontsize=16, fontweight='bold')
    specific_ticks = [350, 400, 450, 500, 550, 600, 650, 700] # Apply ticks and tick lines for specific values
    plt.xticks(ticks=specific_ticks, labels=[f"{tick}" for tick in specific_ticks])
    plt.tick_params(axis='x', which='both', length=5, width=1, direction='out', color='black') # tick parameters
    plt.show()


    i=0


peaks = []

for i, sample in enumerate(sample_data_t0.T):  # Transpose to iterate over samples
    peak_value = np.max(sample)  # Get the maximum absorbance
    peak_index = np.argmax(sample)  # Get the index of the maximum absorbance
    peak_wavelength = wavelengths[peak_index]  # Corresponding wavelength
    peaks.append((peak_wavelength, peak_value))

# print(peaks)
peaks_avg = []
peaks_std = []
for i in range(11):
    average1 = peaks[i][0]
    average1 = int(average1)
    average2 = peaks[i+11][0]
    average2 = int(average2)
    average = np.mean([average1, average2])
    stddev = np.std([average1, average2])
    peaks_std.append(stddev)
    peaks_avg.append(average)

flocc_avg_t0 = []
flocc_std_t0 = []
flocc_avg_t1h = []
flocc_std_t1h = []
flocc_avg_salt = []
flocc_std_salt = []
flocc_avg_buffer = []
flocc_std_buffer = []

# Calculate flocculation data

for i in range(11):
    average1 = flocculation_t0[i]
    average1 = float(average1)
    average2 = flocculation_t0[i+11]
    average2 = float(average2)
    average = np.mean([average1, average2])
    stddev = np.std([average1, average2])
    flocc_std_t0.append(stddev)
    flocc_avg_t0.append(average)

for i in range(11):
    average1 = flocculation_t1h[i]
    average1 = float(average1)
    average2 = flocculation_t1h[i+11]
    average2 = float(average2)
    average = np.mean([average1, average2])
    stddev = np.std([average1, average2])
    flocc_std_t1h.append(stddev)
    flocc_avg_t1h.append(average)

for i in range(11):
    average1 = flocculation_salt[i]
    average1 = float(average1)
    average2 = flocculation_salt[i+11]
    average2 = float(average2)
    average = np.mean([average1, average2])
    stddev = np.std([average1, average2])
    flocc_std_salt.append(stddev)
    flocc_avg_salt.append(average)

for i in range(11):
    average1 = flocculation_t0[i+22]
    average1 = float(average1)
    average = np.mean([average1, average1])
    stddev = np.std([average1, average1])
    flocc_std_buffer.append(stddev)
    flocc_avg_buffer.append(average)

flocc_avg_t0 = [float(value) for value in flocc_avg_t0]
# print(flocc_avg)
flocc_std_t0 = [float(value) for value in flocc_std_t0]
# print(flocc_std)

flocc_avg_t1h = [float(value) for value in flocc_avg_t1h]
flocc_std_t1h = [float(value) for value in flocc_std_t1h]
flocc_avg_salt = [float(value) for value in flocc_avg_salt]
flocc_std_salt = [float(value) for value in flocc_std_salt]
flocc_avg_buffer = [float(value) for value in flocc_avg_buffer]
flocc_std_buffer = [float(value) for value in flocc_std_buffer]

peaks_avg = [float(value) for value in peaks_avg]
# print(peaks_avg)
peaks_std = [float(value) for value in peaks_std]
# print(peaks_std)

# Plot peak wavelengths

sns.set_theme(style="white")
sns.set_style("ticks")
palette = sns.color_palette("viridis", as_cmap=True)

# Create the plot using scatterplot for points and plt.errorbar for error bars
plt.figure(figsize=(10, 6))
sns.scatterplot(x=pH, y=peaks_avg, s=100, color=palette(0.5), marker='o')  # Plot the points
plt.errorbar(pH, peaks_avg, yerr=peaks_std, fmt='none', ecolor=palette(0.5), capsize=5)  # Add error bars

# Labels and title
plt.xlabel('pH Values', fontweight = 'bold')
plt.ylabel('Peak Centre / nm', fontweight = 'bold')
plt.title('Peak Wavelength vs pH of IgG-AuNP Particles', fontsize=16, fontweight='bold')
plt.xticks(pH)

# Show grid and legend
plt.grid(False)
plt.show()

# Plot flocculation

sns.set_theme(style="white")
sns.set_style("ticks")
palette = sns.color_palette("viridis", as_cmap=True)

# Create the plot using scatterplot for points and plt.errorbar for error bars
plt.figure(figsize=(10, 6))
sns.scatterplot(x=pH, y=flocc_avg_salt, s=100, color=palette(0.5), marker='o')  # Plot the points
plt.errorbar(pH, flocc_avg_salt, yerr=flocc_std_salt, fmt='none', ecolor=palette(0.5), capsize=5)  # Add error bars

# Labels and title
plt.xlabel('pH Values', fontweight = 'bold')
plt.ylabel('Flocculation', fontweight = 'bold')
plt.title('Flocculation vs pH of IgG-AuNP Particles', fontsize=16, fontweight='bold')
plt.xticks(pH)

# Show grid and legend
plt.grid(False)
plt.show()

