#%%
from ast import Break
import scipy.io
import numpy as np
import glob
from ast import Break

sub='sub-00AD'

datapath= sub + '/'
data=dict()

listecondition=['C', 'NG', 'C', 'NG', 'NG', 'C', 'C', 'NG', 'C', 'C', 'NG', 'NG', 'C', 'G', 'NG', 'NG', 'NG', 'NG', 'C', 'G', 'NG', 'C', 'C', 'C', 'G', 'NG', 'C', 'G', 'G', 'C', 'NG', 'NG', 'C', 'NG', 'NG', 'C', 'G', 'NG', 'NG', 'G', 'G', 'G', 'NG', 'NG', 'G', 'C', 'NG', 'NG', 'NG', 'NG', 'G', 'C', 'C', 'G', 'C', 'C', 'C', 'C', 'G', 'C', 'NG', 'C', 'G', 'NG', 'C', 'G', 'C', 'G', 'G', 'NG', 'C', 'C', 'G', 'G', 'NG', 'G', 'G', 'NG', 'C', 'C', 'G', 'G', 'G', 'G', 'NG', 'G', 'G', 'G', 'G', 'G']
listecond=['G','NG','C']

for i in listecond:
    data[i]=dict()

#mettre data['GO']['Essai13'][0000000001111100000000000000000]
for cond, n, file in zip (listecondition, range (90), (glob.glob(datapath + 'results_gng_' + sub +'*.mat'))):
    mat=scipy.io.loadmat(file)
    data[cond]['Essai'+str(n)]= mat['Buttons'][:,0]

#liste de RT
listeRT = []
for d in data.keys():
    for e in data[d].keys():
        if 1 in data[d][e]:
            a=np.where(data[d][e]==1) #renvoi les indices où data[d][e]=1 dans un array
            listeRT.append(a[0][0]/60)

        else :
            listeRT.append('sansclique')
          
print (listeRT)

# %% Faire un excel
import csv

name = 'results_GNG_CLIQUE_'+ sub + '.csv'

with open(name, 'w', newline ='') as file2:
    writer=csv.writer(file2)
