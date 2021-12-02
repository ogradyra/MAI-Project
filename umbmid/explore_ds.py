import pickle
import pandas as pd

# file containing the measured frequency-domain S11 parameters of all scans in that generation of the dataset, 
# after having performed empty-chamber reference subtraction

f1 = open('umbmid/td_cal_data.pickle', 'rb')
f2 = open('umbmid/fd_data_gen_two_s11.pickle', 'rb')
#infile = open('umbmid/geom_params.pickle','rb')
f3 = open('umbmid/metadata_gen_two.pickle', 'rb')

dict1 = pickle.load(f1)
dict2 = pickle.load(f2)
dict3 = pickle.load(f3)

f1.close()
f2.close()
f3.close()

#data = pd.read_pickle("umbmid/fd_data.pickle")
#print(data)

d1 = dict1['c2sf3cm']
d2 = dict2[989]
tar = dict2[989, :, :]
emp = dict2[993, :, :]
cal = tar - emp

#print("Scan with tumour: ", new_dict[989])
#print("Scan without tumour: ", new_dict[997])
#print(new_dict['c2sf3cm'])
#print("DAS data length: ", len(d1))
#print("UMBMID data length: ", len(d2))
#print(dict1['c2sf3cm'])
#print(dict2[989, 0, :])

#print("Num scans umbmid: ", len(dict2[0]))
#print("Num scans itDAS: ", len(dict1['c2sf3cm']))
#print("Num frequency points: ", len(dict2[0]))
#print("Num antenna points: ", len(dict2[0,0]))

print(dict3[989])

#print(dict1['c2sf3cm'])
#print(dict3)
#with open('./scan_990.pickle', 'wb') as handle:
#      pickle.dump(cal, handle, protocol=pickle.HIGHEST_PROTOCOL)