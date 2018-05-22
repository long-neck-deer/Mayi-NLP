from datetime import datetime
from csv import DictReader
from math import exp, log, sqrt
from random import random,shuffle
import pickle
import sys
import string
from config import isCase

path = './feature/'

'''
sen1_word+sen2_hash
sen2_word+sen1_hash
'''
def cooccurrence_terms(lst1, lst2, join_str="__"):
    lst1 = lst1.split(" ")
    lst2 = lst2.split(" ")
    terms = [""] * len(lst1) * len(lst2)
    cnt =  0
    for item1 in lst1:
        for item2 in lst2:
            terms[cnt] = item1 + join_str + item2
            cnt += 1
    res = " ".join(terms)
    return res

def prepare_cooccurrence(path1,path2,out):
    print path
    c = 0
    start = datetime.now()
    with open(out, 'w') as outfile:
        outfile.write('sen1_unigram_sen2_hash,sen1_hash_sen2_unigram\n')
        for row1, row2 in zip(DictReader(open(path1), delimiter=','),DictReader(open(path2), delimiter=',')): 
            if c%100000==0:
                print 'finished',c
            s1_unigram = str(row1['sen1_unigram'])
            s2_unigram = str(row1['sen2_unigram'])

            s1_hash = str(row2['sen1_hash'])
            s2_hash = str(row2['sen2_hash'])

            coo_terms1 = cooccurrence_terms(s1_unigram,s2_hash)
            coo_terms2 = cooccurrence_terms(s2_unigram,s1_hash)
            outfile.write('%s,%s\n' % (coo_terms1,coo_terms2))
            c+=1
        end = datetime.now()
    print 'times:',end-start
if isCase == False:
    prepare_cooccurrence(path+'train_unigram.csv',path+'train_hashed.csv',path+'train_cooccurrence_qid.csv')
    prepare_cooccurrence(path+'test_unigram.csv',path+'test_hashed.csv',path+'test_cooccurrence_qid.csv')
else:
    prepare_cooccurrence(path+'case_unigram.csv',path+'case_hashed.csv',path+'case_cooccurrence_qid.csv')