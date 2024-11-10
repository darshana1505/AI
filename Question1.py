# Question - 1
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 200)

y1 = 2 * x + 1
y2 = 2 * x + 2
y3 = 2 * x + 3

plt.figure(figsize=(10, 6))

plt.plot(x, y1, color="black", linestyle="solid", linewidth=1.5, label="y = 2x + 1")
plt.plot(x, y2, color="red", linestyle="dashed", linewidth=1.5, label="y = 2x + 2")
plt.plot(x, y3, color="green", linestyle="dotted", linewidth=1.5, label="y = 2x + 3")

plt.title("Graphs of the Lines y=2x+1, y=2x+2, y=2x+3")
plt.xlabel("x")
plt.ylabel("y")

plt.legend()

plt.grid(True)
plt.show()