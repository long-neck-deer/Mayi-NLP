import pandas as pd
from pandas import DataFrame
from config import isCase
path = './feature/'

def prepare_hash_neighbour(paths,out):
    neighbour_dict = dict()
    for path in paths:
        data_in = pd.read_csv(path)
        for index,row in data_in.iterrows():
            s1 = str(row['sen1_hash'])
            s2 = str(row['sen2_hash'])
            l = neighbour_dict.get(s1,[])
            l.append(s2)
            neighbour_dict[s1] = l

            l = neighbour_dict.get(s2,[])
            l.append(s1)
            neighbour_dict[s2] = l
    data_out = DataFrame(columns=['sen','hashes'])
    c = 0
    for k in neighbour_dict.keys():
        data_out.loc[c] = [str(k),' '.join(neighbour_dict[k])]
        c += 1
    data_out.to_csv(out,index=False)

if isCase == False:
    prepare_hash_neighbour([path+'train_hashed.csv',path+'test_hashed.csv'],out=path+'neighbor.csv')
else:
    prepare_hash_neighbour([path+'case_hashed.csv',path+'case_hashed.csv'],out=path+'neighbor.csv')

