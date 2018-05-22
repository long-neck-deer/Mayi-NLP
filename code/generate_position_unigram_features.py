import pandas as pd
from pandas import DataFrame
from math import sqrt
from config import isCase
path = './feature/'




def try_divide(x, y, val=0.0):
    """ 
        Try to divide two numbers
    """
    if y != 0.0:
        val = float(x) / y
    return val

def get_position_list(target, obs):
    """
        Get the list of positions of obs in target
    """
    pos_of_obs_in_target = [0]
    if len(obs) != 0:
        pos_of_obs_in_target = [j for j,w in enumerate(obs, start=1) if w in target]
        if len(pos_of_obs_in_target) == 0:
            pos_of_obs_in_target = [0]
    return pos_of_obs_in_target


def mean(x):
    return sum(x)/float(len(x))

def median(x):
    len_2 = int(len(x)/2)
    return x[len_2]

def std(x):
    mean_x = mean(x)
    s = 0.0
    for xx in x:
        s+=(xx-mean_x)**2
    s/=len(x)
    s = sqrt(s)
    return s



def prepare_position_index(path,out):
    data_input = pd.read_csv(path)
    data_ouput = DataFrame(columns=['min_pos_s1_in_s2',
                                    'max_pos_s1_in_s2',
                                    'mean_pos_s1_in_s2',
                                    'median_pos_s1_in_s2',
                                    'std_pos_s1_in_s2',
                                    'min_pos_s2_in_s1',
                                    'max_pos_s2_in_s1',
                                    'mean_pos_s2_in_s1',
                                    'median_pos_s2_in_s1',
                                    'std_pos_s2_in_s1'])
    for index,row in data_input.iterrows():
            s1 = str(row['sen1_unigram']).split(' ')
            s2 = str(row['sen2_unigram']).split(' ')

            pos_list = get_position_list(s1,s2)
            min_pos_s1_in_s2 = min(pos_list)
            max_pos_s1_in_s2 = max(pos_list)
            mean_pos_s1_in_s2 = mean(pos_list)
            median_pos_s1_in_s2 = median(pos_list)
            std_pos_s1_in_s2 = std(pos_list)

            pos_list = get_position_list(s2,s1)
            min_pos_s2_in_s1 = min(pos_list)
            max_pos_s2_in_s1 = max(pos_list)
            mean_pos_s2_in_s1 = mean(pos_list)
            median_pos_s2_in_s1 = median(pos_list)
            std_pos_s2_in_s1 = std(pos_list)
            data_ouput.loc[index] = [min_pos_s1_in_s2,
                                    max_pos_s1_in_s2,
                                    mean_pos_s1_in_s2,
                                    median_pos_s1_in_s2,
                                    std_pos_s1_in_s2,
                                    min_pos_s2_in_s1,
                                    max_pos_s2_in_s1,
                                    mean_pos_s2_in_s1,
                                    median_pos_s2_in_s1,
                                    std_pos_s2_in_s1]
    data_ouput.to_csv(out,index=False)


if isCase == False:
    prepare_position_index(path+'train_unigram.csv',path+'train_position_index.csv')
    prepare_position_index(path+'test_unigram.csv',path+'test_position_index.csv')
else:
    prepare_position_index(path+'case_unigram.csv',path+'case_position_index.csv')
