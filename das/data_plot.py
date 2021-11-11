
import pandas as pd
from matplotlib import pyplot as plt

# figure details
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

# converting columns in csv to dataframe
columns = ['time', 'input', 'a1', 'a2']
df = pd.read_csv("ranging_data.csv", usecols=columns)
print("Contents in csv file:\n", df)

# plotting input and antenna responses
plt.title('Transmitted Pulse with Two Antenna Responses')
plt.xlabel('Time [ns]')
plt.ylabel('Amplitude')

plt.plot(df.time, df.input)
plt.plot(df.time, df.a1)
plt.plot(df.time, df.a2)

plt.show()

