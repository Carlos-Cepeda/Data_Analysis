import csv
from datetime import datetime

import matplotlib.pyplot as plt

# Read the csv file.
filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, high, and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')  # From string to date
        high = int(row[5])  # From string to integer
        low = int(row[6])  # From string to integer
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)  # plot each data set individually
ax.plot(dates, lows, c='blue', alpha=0.5)  # plot each data set individually
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)  # fill in between

# Format plot.
ax.set_title("Daily high and low temperatures - 2018", fontsize=18)
ax.set_xlabel('', fontsize=12)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (F)', fontsize=12)
ax.tick_params(axis='both', which='major', labelsize=12)

plt.show()


