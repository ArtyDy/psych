#%% RT
import scipy.io
import numpy as np
sub='sub-00AD'

datapath= sub + '/' + 'results_RT_' + sub+ '.mat'
conds=['GV', 'GF', 'DV', 'DF']
data=dict()
for k in conds:
    data[k]=dict()
listecondition=['DF', 'DV', 'DV', 'GV', 'GV', 'DF', 'GF', 'DV', 'DF', 'DV', 'GV', 'DV', 'DV', 'DV', 'DF', 'DF', 'GV', 'GV', 'DV', 'GV', 'DV', 'DV', 'DV', 'DF', 'DV', 'DV', 'DF', 'GV', 'DV', 'DF', 'GV', 'DF', 'GV', 'GV', 'GV', 'GF', 'GV', 'GV', 'DV', 'DV', 'GF', 'GV', 'GV', 'DF', 'GV', 'GV', 'DF', 'GV', 'GF', 'GF', 'GV', 'GV', 'DV', 'DV', 'GF', 'DV', 'GV', 'DV', 'GV', 'GV', 'GV', 'DV', 'GV', 'DV', 'DV', 'GV', 'GV', 'GV', 'DV', 'GF', 'GV', 'DV', 'DF', 'DF', 'GV', 'DV', 'DV', 'GV', 'DV', 'GV', 'GV', 'DV', 'GV', 'DV', 'GV', 'DV', 'DF', 'DV', 'GV', 'DV', 'GV', 'DV', 'GF', 'GF', 'DV', 'DV', 'GV', 'DV', 'DV', 'GV', 'DV', 'GF', 'GV', 'GF', 'GV', 'DV', 'GV', 'DV', 'DV', 'DF', 'DF', 'GF', 'DV', 'GF', 'GV', 'GV', 'GF', 'GV', 'GF', 'DV', 'DV', 'DV', 'GV', 'GF', 'DF', 'GV', 'GF', 'GV', 'DV', 'GV', 'GV', 'DV', 'DF', 'DV', 'GV', 'DV', 'DV', 'GF', 'GV', 'DV', 'GV', 'GV', 'GV', 'DV', 'DV', 'GF', 'GV', 'DF', 'GV', 'GF', 'DF', 'DV', 'DV', 'GV', 'DV', 'GV', 'DV', 'DV', 'DV', 'GV']

mat=scipy.io.loadmat(datapath)

for k, cond in zip(range(160), listecondition):
    
    data[cond]['Essai'+str(k)]=mat['Essai'+str(k)][:,0]

MD=dict()
Vitesse=dict()
Vmax=dict()
RT=dict()
for k in conds:
    MD[k]=dict()
    Vitesse[k]=dict()
    Vmax[k]=dict()
    RT[k]=dict()
    for l in data[k].keys():
        MD[k][l]=len(data[k][l])/60
        Vitesse[k][l]=dict()
        Vitesse[k][l]=np.zeros(len(data[k][l]))

        for j in range(len(data[k][l])):
            if j!=0:
                Vitesse[k][l][j]=abs(data[k][l][j]- data[k][l][j-1])*60
        
        Vmax[k][l]=np.max(Vitesse[k][l])
        seuil=0.05*Vmax[k][l]
        m=0
        while Vitesse[k][l][m]<seuil:
            m=m+1
        RT[k][l]=m/60

#%% GNG

#%%

import scipy.io



# %% Excel
import matplotlib.pyplot as plt

plt.plot(Vitesse['DV']['Essai158'])
# %%
import csv 

name = 'psych_RT_'+ sub + '.csv'
with open(name, 'w', newline ='') as file2:
    writer=csv.writer(file2)
    writer.writerow(['','MDDV','MDDF','MDGV', 'MDGF', 'VMDV', 'VMDF', 'VMGV', 'VMGF', 'RTDV', 'RTDF', 'RTGV', 'RTGF'])
    
    
    for k in range(60):
        if k<=19:
            writer.writerow([ 'Essai'+str(k), MD['DV'][list(MD['DV'].keys())[k]] , MD['DF'][list(MD['DF'].keys())[k]], MD['GV'][list(MD['GV'].keys())[k]] , MD['GF'][list(MD['GF'].keys())[k]] , Vmax['DV'][list(MD['DV'].keys())[k]] , Vmax['DF'][list(MD['DF'].keys())[k]], Vmax['GV'][list(MD['GV'].keys())[k]] , Vmax['GF'][list(MD['GF'].keys())[k]] , RT['DV'][list(MD['DV'].keys())[k]] , RT['DF'][list(MD['DF'].keys())[k]] , RT['GV'][list(MD['GV'].keys())[k]] , RT['GF'][list(MD['GF'].keys())[k]] ])
        else:
            writer.writerow([ 'Essai'+str(k), MD['DV'][list(MD['DV'].keys())[k]] , '', MD['GV'][list(MD['GV'].keys())[k]] , '' , Vmax['DV'][list(MD['DV'].keys())[k]] , '', Vmax['GV'][list(MD['GV'].keys())[k]] , '' , RT['DV'][list(MD['DV'].keys())[k]] , '' , RT['GV'][list(MD['GV'].keys())[k]] , '' ])

# %%
