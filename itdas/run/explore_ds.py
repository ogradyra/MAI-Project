import pickle
import pandas as pd
import csv

from sigproc import iczt

# file containing the measured frequency-domain S11 parameters of all scans in that generation of the dataset, 
# after having performed empty-chamber reference subtraction

f1 = open('umbmid/td_cal_data.pickle', 'rb')
f2 = open('umbmid/fd_data_gen_two_s11.pickle', 'rb')
# f1 = open('umbmid/geom_params.pickle','rb')
f3 = open('umbmid/metadata_gen_two.pickle', 'rb')

itdas = pickle.load(f1)
gen2 = pickle.load(f2)
md_gen2 = pickle.load(f3)

# print(itdas.keys())

f1.close()
f2.close()
f3.close()

#data = pd.read_pickle("umbmid/fd_data.pickle")
#print(data)

# data from one of the itdas dataset scans
d1 = itdas['c1lf2cm']

# data from umbmid scan 990
d2 = gen2[989]

# phantom scan data 
tar = gen2[104, :, :]
# corresponding empty-chamber data for that scan
emp = gen2[109, :, :]
# calibrate the target measurements by subtracting the empty-chamber scan data
cal = tar - emp

cal_data = iczt(cal, ini_t=0, fin_t=6e-9, n_time_pts=1024, ini_f=1e9, fin_f=8e9)

print(d1.shape)
print(cal.shape)

#print("Scan with tumour: ", new_dict[989])
#print("Scan without tumour: ", new_dict[997])

#print("Num scans umbmid: ", len(dict2[0]))
#print("Num scans itDAS: ", len(dict1['c2sf3cm']))
#print("Num frequency points: ", len(dict2[0]))
#print("Num antenna points: ", len(dict2[0,0]))

# metadata for scan 990
# print(md_gen2[997].values())
# print(md_gen2[104])
#print(md_gen2[997])

# load scan data or metadata into a pickle file
with open('./scan_105.pickle', 'wb') as handle:
      pickle.dump(cal_data, handle, protocol=pickle.HIGHEST_PROTOCOL)


df = pd.DataFrame(md_gen2)
df.to_csv('md2.csv')