import pickle
import pandas as pd
import csv

from sigproc import iczt

sd = open('umbmid/fd_data_s11_emp.pickle', 'rb')
gd = pd.read_csv('umbmid.csv')

print(gd.keys())
