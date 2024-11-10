# question - 3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("weight-height.csv")

height_inches = data['Height']
weight_pounds = data['Weight']

height_cm = height_inches * 2.54

weight_kg = weight_pounds * 0.453592

mean_height_cm = np.mean(height_cm)
mean_weight_kg = np.mean(weight_kg)

print(f"Mean Height (cm): {mean_height_cm}")
print(f"Mean Weight (kg): {mean_weight_kg}")

plt.figure(figsize=(8, 5))
plt.hist(height_cm, bins=20, color="skyblue", edgecolor="black")
plt.title("Histogram of Heights (in cm)")
plt.xlabel("Height (cm)")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()