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
s = 1.65
# speed of light (cm/s)
c = 3e8
# points on linear scale (100 evenly spaced points)
points = np.arange(0, 1.65, 0.0165)
print("Number of points: ", len(points))

time_delay_a1 = []
time_delay_a2 = []

# time  = distance / speed
for i in range(0,100):

    # Time taken for a wave to travel to a point and back for each antenna (values in secs)
    time_delay_a1.append((points[i] / c) * 2)
    time_delay_a2.append(((1.65 - points[i]) / c) * 2)

#print(time_delay_a1)

# delay a1 and a2 by the time delays above

samples_a1 = []
samples_a2 = []

for i in range(len(time_delay_a1)):

    # count the number of smaples needed to delay the antenna responses at each point
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

    # calculate energy of the combined signals at each point
    # energy equation = square each point, add, square root
    e = math.sqrt(sum((new_a1[m]+new_a2[m])**2))
    comb.append(e) 


plt.plot(points, comb)
plt.title("Energy Map")
plt.xlabel("Distance (m)")
plt.ylabel("Energy")
plt.show()
