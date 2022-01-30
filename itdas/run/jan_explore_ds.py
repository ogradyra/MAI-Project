import pickle
import pandas as pd
import csv

from sigproc import iczt

f1 = open('umbmid/fd_data_s11_emp.pickle', 'rb')
f2 = open('umbmid/md_list_s11_emp.pickle', 'rb')
f3 = open('umbmid/td_cal_data.pickle', 'rb')
f4 = open('umbmid/geom_params.pickle','rb')

u_scan_data = pickle.load(f1)
u_meta_data = pickle.load(f2)
itdas_data = pickle.load(f3)
itdas_md = pickle.load(f4)

f1.close()
f2.close()
f3.close()
f4.close()

# one scan from 2nd gen clean umbmid file
fd_u_data = u_scan_data[919]
# convert scan data to time domain
td_u_data = iczt(fd_u_data, ini_t=0, fin_t=6e-9, n_time_pts=700, ini_f=1e9, fin_f=8e9)
td_i_data = itdas_data['c1lf2cm']

# metadata for scan being analysed
print("Metadata for scan of interest: ", u_meta_data[919])

# num frequency points: comparing umbmid and itdas data
print('Num freq points umbmid:', len(td_u_data))
print('Num freq points itdas:', len(td_i_data))

# load scan data or metadata into a pickle file
with open('./scan_1174.pickle', 'wb') as handle:
      pickle.dump(td_u_data, handle, protocol=pickle.HIGHEST_PROTOCOL)


# put all gen 2 clean scan data into a .csv file
# df = pd.DataFrame(u_meta_data)
# df.to_csv('umbmid.csv')