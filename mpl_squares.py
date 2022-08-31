import matplotlib.pyplot as plt
"""Print square numbers"""

input_values = [1, 2, 3, 4, 5]  # X coordinate
squares = [1, 4, 9, 16, 25]  # Y coordinate

plt.style.use('seaborn')  # Use a specific style: seaborn, classic, dark_background
fig, ax = plt.subplots()  # ax -> instance of plt
ax.plot(input_values, squares, linewidth=3)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)

plt.show()