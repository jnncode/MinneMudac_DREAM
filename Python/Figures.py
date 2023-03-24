# Yearly Frequency - Value/Year > Average Attendance (December)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("GameLogsCSV/DateFormat.csv", index_col=["Date"])

# Convert index to Pandas timestamp objects
data.index = pd.to_datetime(data.index)

start_year = 2019 # First found 2019 of December in China
start_date = pd.to_datetime(str(start_year))
filtered_data = data[start_date:]

yearly_average = filtered_data.resample("Y").mean()

# Format the datetime objects as strings
x_labels = yearly_average.index.strftime("%b %Y")
plt.bar(x_labels, yearly_average["Attendance"], color="blue")

plt.xlabel("Month and Year")
plt.ylabel("Attendance")
plt.title("Yearly Average Attend From " + str(start_year))

plt.show()

# Conclusion:
# Lockdowns were established in early to mid 2020.
# Attendance was compiled all of 2019 which includes previous time before Covid-19 was initially detected