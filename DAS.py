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
s = 165
# speed of light (cm/s)
c = 300000000000
points = np.random.randint(0, 165, size = 100)
#print(len(points))

time_delay_a1 = []
time_delay_a2 = []

# time  = distance / speed
for i in range(0,100):

    # Time taken for a wave to travel to a point and back for each antenna (values in secs)
    time_delay_a1.append((points[i] / c) * 2)
    time_delay_a2.append((165 - points[i] / c) * 2)

#print(time_delay_a1)

# delay a1 and a2 by the time delays above

#zero counts
zero_count_arr_a1 = []
count_a1 = 0
'''
for i in range(len(time_delay_a1)):

    count_a1 = 0

    for j in range(len(df.time)):

        if df.time[j] < time_delay_a1[i]:
            count_a1 = count_a1 + 1

    zero_count_arr_a1.append(count_a1)
'''

zero_count_arr_a2 = []
count_a2 = 0
'''
for i in range(len(time_delay_a2)):

    count_a2 = 0

    for j in range(len(df.time)):

        if df.time[j] < time_delay_a2[i]:
            count_a2 = count_a2 + 1

    zero_count_arr_a2.append(count_a2)
'''

print(zero_count_arr_a2)


new_a1 = df.a1.shift(periods=10000, fill_value=0)
new_a2 = df.a2.shift(periods=8000, fill_value=0)
print(len(new_a2))

#plt.plot(df.time, new_a1)
#plt.show()

# energy equation = square each point, add, square root

sum = 0

for n in range(len(df.time)):

    sum = sum + ((new_a1[n]+new_a2[n])**2)

e = math.sqrt(sum)**2
print(e)