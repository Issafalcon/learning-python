import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Helper functions
def custom_mean(data):
    return sum(data) / len(data)


def custom_median(sorted_data):
    num_elements = len(sorted_data)
    if num_elements % 2 == 0:
        return (sorted_data[(num_elements / 2) - 1] + sorted_data[num_elements / 2]) / 2
    else:
        return sorted_data[(num_elements - 1) / 2]


# Import data
height_weight = pd.read_csv("./500_Person_Gender_Height_Weight_Index.csv")
print(height_weight.head())

# Drop an unrequired column from the dataframe
height_weight.drop("Index", axis=1, inplace=True)
print(height_weight.shape)  # Show tuple of count of rows and count of columns

# Count missing values
print(height_weight.isnull().sum())

# Calculate range of height and weight and print them out
height_range = height_weight["Height"].max() - height_weight["Height"].min()
weight_range = height_weight["Weight"].max() - height_weight["Weight"].min()
print("Height range: " + str(height_range))
print("Weight range: " + str(weight_range))

# Extract weights to a separate Series
weights = height_weight["Weight"]
print(weights.head())

# Calculate median weight using existing helpers and custom helpers
sorted_weights = weights.sort_values().reset_index()
print(sorted_weights.head())
print(weights.median())
print(custom_median(sorted_weights["Weight"]))
print(weights.mean())
print(custom_mean(weights))

# Plot histogram of weights
plt.figure(figsize=(12, 8))
plt.hist(weights, bins=30)
plt.title("Weight Histogram")
plt.axvline(weights.mean(), color="red", label="Mean")
plt.axvline(weights.median(), color="green", label="Median")
plt.legend()
# plt.show()

# Introduce outlier series into dataframe
listOfSeries = [
    pd.Series(["Male", 205, 460], index=height_weight.columns),
    pd.Series(["Female", 202, 390], index=height_weight.columns),
    pd.Series(["Female", 199, 410], index=height_weight.columns),
    pd.Series(["Male", 202, 390], index=height_weight.columns),
    pd.Series(["Female", 199, 410], index=height_weight.columns),
    pd.Series(["Male", 200, 490], index=height_weight.columns),
]

height_weight_updated = height_weight._append(listOfSeries, ignore_index=True)
print(height_weight_updated.tail())

# Calculate mean and median of weight with outliers and print off
update_weight_mean = height_weight_updated["Weight"].mean()
update_weight_median = height_weight_updated["Weight"].median()
print("Mean with outliers:")
print(update_weight_mean)
print("Median with outliers:")
print(update_weight_median)

# Plot histogram of weights
plt.figure(figsize=(12, 8))
plt.hist(height_weight_updated['Weight'], bins=100)
plt.title("Weight Histogram With Outliers")
plt.axvline(update_weight_mean, color="red", label="Mean")
plt.axvline(update_weight_median, color="green", label="Median")
plt.legend()
# plt.show()

# Print the mode of the weight column
print(height_weight_updated['Weight'].mode())
