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
c = 3e11
# points on linear scale (100 evenly spaced points)
points = np.arange(0, 165, 1.65)
print("Number of points: ", len(points))

time_delay_a1 = []
time_delay_a2 = []

# time  = distance / speed
for i in range(0,100):

    # Time taken for a wave to travel to a point and back for each antenna (values in secs)
    time_delay_a1.append((points[i] / c) * 2)
    time_delay_a2.append(((165 - points[i]) / c) * 2)

#print(time_delay_a1)

# delay a1 and a2 by the time delays above

samples_a1 = []
samples_a2 = []

for i in range(len(time_delay_a1)):

    samples_a1.append(int(1e13*time_delay_a1[i]))
    samples_a2.append(int(1e13*time_delay_a2[i]))
    # round numbers 




new_a1 = []
new_a2 = []
comb = []
e = 0

#print(samples_a1)

for m in range(0,100):

    new_a1.append(df.a1.shift(periods=-samples_a1[m], fill_value=0))
    new_a2.append(df.a2.shift(periods=-samples_a2[m], fill_value=0))

    e = math.sqrt(sum((new_a1[m]+new_a2[m])**2))

    comb.append(e)


#print("Length of combined signal array: ", len(combo_a1_a2))
#print("Length of energy array: ", len(e))
print("Energy\n", comb)
plt.plot(points, comb)
plt.title("Energy Map for Antenna 1 and 2")
plt.xlabel("Distance (cm)")
plt.ylabel("Energy")
plt.show()

t = 105/3e11
#print(t)


#print(len(new_a2))

#plt.plot(df.time, new_a1)
#plt.plot(df.time, df.a1)
#plt.show()
# energy equation = square each point, add, square root