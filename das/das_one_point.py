import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import math

# figure details
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

# converting columns in csv to dataframe
columns = ['time', 'input', 'a1', 'a2']
df = pd.read_csv("ranging_data.csv", usecols=columns)

# distance between antennas s = 1.65 m (165 cm)
point = 0.6

time_delay_a1 = 4e-9
time_delay_a2 = 7e-9

samples_a1 = 1e13*4e-9
samples_a2 = 1e13*7e-9

print(samples_a1)
#new_a1 = []

new_a1 = df.a1.shift(periods=-40000, fill_value=0)
new_a2 = df.a2.shift(periods=-70000, fill_value=0)

#print(new_a1)

plt.plot(df.time, new_a1 + new_a2)
plt.plot(df.time, df.a1)
plt.plot(df.time, df.a2)
plt.show()
