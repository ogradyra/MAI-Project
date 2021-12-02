import pickle
import pandas as pd

# file containing the measured frequency-domain S11 parameters of all scans in that generation of the dataset, 
# after having performed empty-chamber reference subtraction

f1 = open('umbmid/td_cal_data.pickle', 'rb')
f2 = open('umbmid/fd_data_gen_two_s11.pickle', 'rb')
#f4 = open('umbmid/geom_params.pickle','rb')
f3 = open('umbmid/metadata_gen_two.pickle', 'rb')

itdas = pickle.load(f1)
gen2 = pickle.load(f2)
md_gen2 = pickle.load(f3)

f1.close()
f2.close()
f3.close()

#data = pd.read_pickle("umbmid/fd_data.pickle")
#print(data)

# data from one of the itdas dataset scans
d1 = itdas['c2sf3cm']

# data from umbmid scan 990
d2 = gen2[989]

# phantom scan data 
tar = gen2[997, :, :]
# corresponding empty-chamber data for that scan
emp = gen2[993, :, :]
# calibrate the target measurements by subtracting the empty-chamber scan data
cal = tar - emp

#print("Scan with tumour: ", new_dict[989])
#print("Scan without tumour: ", new_dict[997])

#print("Num scans umbmid: ", len(dict2[0]))
#print("Num scans itDAS: ", len(dict1['c2sf3cm']))
#print("Num frequency points: ", len(dict2[0]))
#print("Num antenna points: ", len(dict2[0,0]))

# metadata for scan 990
print(md_gen2[997])

# load scan data or metadata into a pickle file
with open('./scan_998.pickle', 'wb') as handle:
      pickle.dump(cal, handle, protocol=pickle.HIGHEST_PROTOCOL)