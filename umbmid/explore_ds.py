import pickle
import pandas as pd

# file containing the measured frequency-domain S11 parameters of all scans in that generation of the dataset, 
# after having performed empty-chamber reference subtraction
infile = open('umbmid/metadata_gen_two.pickle', 'rb')
new_dict = pickle.load(infile)
infile.close()

#data = pd.read_pickle("metadata_gen_one.pickle")
#print(data)

print("Scan with tumour: ", new_dict[989])
print("Scan without tumour: ", new_dict[997])
