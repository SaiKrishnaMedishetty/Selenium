import matplotlib.pyplot as plt
import numpy as np

# Line Plot
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

plt.plot(x, y)
plt.xlabel('x values')
plt.ylabel('sin(x)')
plt.title('Sine Wave')
plt.show()

# Scatter Plot
x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y, c='red', marker='o')
plt.xlabel('Random x values')
plt.ylabel('Random y values')
plt.title('Scatter Plot')
plt.show()

# Bar Chart
categories = ['A', 'B', 'C', 'D']
values = [23, 45, 56, 78]

plt.bar(categories, values)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart')
plt.show()

# Histogram
data = np.random.randn(1000)

plt.hist(data, bins=30, alpha=0.75)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()

# Subplots
fig, axs = plt.subplots(2, 2)

# Line Plot
axs[0, 0].plot(x, y)
axs[0, 0].set_title('Line Plot')

# Scatter Plot
axs[0, 1].scatter(x, y, c='red')
axs[0, 1].set_title('Scatter Plot')

# Bar Chart
axs[1, 0].bar(categories, values)
axs[1, 0].set_title('Bar Chart')

# Histogram
axs[1, 1].hist(data, bins=30, alpha=0.75)
axs[1, 1].set_title('Histogram')

# Adjust layout
plt.tight_layout()
plt.show()
