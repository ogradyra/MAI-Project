import pickle
import pandas as pd

# file containing the measured frequency-domain S11 parameters of all scans in that generation of the dataset, 
# after having performed empty-chamber reference subtraction

f1 = open('umbmid/fd_data.pickle', 'rb')
f2 = open('umbmid/fd_data_gen_two_s11.pickle', 'rb')
#infile = open('umbmid/geom_params.pickle','rb')

dict1 = pickle.load(f1)
dict2 = pickle.load(f2)

f1.close()
f2.close()

#data = pd.read_pickle("umbmid/fd_data.pickle")
#print(data)

d1 = dict1['c2sf3cm']
d2 = dict2[989]

#print("Scan with tumour: ", new_dict[989])
#print("Scan without tumour: ", new_dict[997])
#print(new_dict['c2sf3cm'])
#print("DAS data length: ", len(d1))
#print("UMBMID data length: ", len(d2))

#print(dict1['c2sf3cm'])
#print(dict2[989, 0, :])

print("Num scans: ", len(dict2))
print("Num frequencies: ", len(dict2[0]))
print("Num channels: ", len(dict2[0,0]))
