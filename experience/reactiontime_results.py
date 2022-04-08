#%% RT
import scipy.io
import numpy as np
sub='sub-88VP'

datapath= 'results_RT_'+sub+'.mat'
conds=['H0.2', 'H0.5', 'H0.8','B0.2', 'B0.5', 'B0.8','G0.2', 'G0.5', 'G0.8','D0.2', 'D0.5', 'D0.8']
data=dict()
for k in conds:
    data[k]=dict()
    
# listecondition=['DF', 'DV', 'DV', 'GV', 'GV', 'DF', 'GF', 'DV', 'DF', 'DV', 'GV', 'DV', 'DV', 'DV', 'DF', 'DF', 'GV', 'GV', 'DV', 'GV', 'DV', 'DV', 'DV', 'DF', 'DV', 'DV', 'DF', 'GV', 'DV', 'DF', 'GV', 'DF', 'GV', 'GV', 'GV', 'GF', 'GV', 'GV', 'DV', 'DV', 'GF', 'GV', 'GV', 'DF', 'GV', 'GV', 'DF', 'GV', 'GF', 'GF', 'GV', 'GV', 'DV', 'DV', 'GF', 'DV', 'GV', 'DV', 'GV', 'GV', 'GV', 'DV', 'GV', 'DV', 'DV', 'GV', 'GV', 'GV', 'DV', 'GF', 'GV', 'DV', 'DF', 'DF', 'GV', 'DV', 'DV', 'GV', 'DV', 'GV', 'GV', 'DV', 'GV', 'DV', 'GV', 'DV', 'DF', 'DV', 'GV', 'DV', 'GV', 'DV', 'GF', 'GF', 'DV', 'DV', 'GV', 'DV', 'DV', 'GV', 'DV', 'GF', 'GV', 'GF', 'GV', 'DV', 'GV', 'DV', 'DV', 'DF', 'DF', 'GF', 'DV', 'GF', 'GV', 'GV', 'GF', 'GV', 'GF', 'DV', 'DV', 'DV', 'GV', 'GF', 'DF', 'GV', 'GF', 'GV', 'DV', 'GV', 'GV', 'DV', 'DF', 'DV', 'GV', 'DV', 'DV', 'GF', 'GV', 'DV', 'GV', 'GV', 'GV', 'DV', 'DV', 'GF', 'GV', 'DF', 'GV', 'GF', 'DF', 'DV', 'DV', 'GV', 'DV', 'GV', 'DV', 'DV', 'DV', 'GV']

# listecondition=['H', 'B', 'D', 'G', 'D', 'H', 'D', 'B', 'H', 'B', 'G', 'B', 'G', 'B', 'G', 'H', 'D', 'D', 'G', 'D', 'G', 'B', 'B', 'B', 'D', 'H', 'B', 'B', 'D', 'B', 'G', 'B', 'H', 'H', 'B', 'H', 'H', 'B', 'G', 'H', 'D', 'B', 'H', 'B', 'G', 'D', 'H', 'H', 'G', 'H', 'B', 'D', 'D', 'B', 'D', 'G', 'G', 'H', 'G', 'D', 'G', 'D', 'B', 'H', 'G', 'G', 'B', 'B', 'D', 'D', 'G', 'B', 'D', 'H', 'G', 'G', 'B', 'D', 'B', 'D', 'B', 'H', 'G', 'H', 'B', 'D', 'G', 'H', 'G', 'B', 'D', 'H', 'D', 'D', 'G', 'H', 'H', 'G', 'G', 'H', 'H', 'D', 'H', 'G', 'D', 'G', 'H', 'G', 'B', 'D', 'B', 'B', 'H', 'D', 'D', 'H', 'H', 'G', 'D', 'G']
# listetemps=[0.2, 0.5, 0.2, 0.5, 0.8, 0.5, 0.8, 0.5, 0.8, 0.8, 0.8, 0.8, 0.2, 0.2, 0.8, 0.5, 0.2, 0.2, 0.5, 0.5, 0.8, 0.8, 0.8, 0.2, 0.5, 0.2, 0.8, 0.5, 0.8, 0.2, 0.2, 0.8, 0.8, 0.5, 0.8, 0.5, 0.2, 0.5, 0.8, 0.8, 0.8, 0.2, 0.8, 0.8, 0.2, 0.5, 0.2, 0.2, 0.5, 0.2, 0.2, 0.8, 0.2, 0.2, 0.8, 0.8, 0.5, 0.2, 0.8, 0.2, 0.8, 0.5, 0.5, 0.8, 0.8, 0.2, 0.2, 0.2, 0.2, 0.8, 0.8, 0.5, 0.8, 0.8, 0.2, 0.5, 0.5, 0.8, 0.8, 0.2, 0.5, 0.5, 0.2, 0.8, 0.5, 0.5, 0.5, 0.5, 0.2, 0.5, 0.8, 0.5, 0.5, 0.2, 0.5, 0.8, 0.8, 0.5, 0.5, 0.5, 0.5, 0.5, 0.2, 0.8, 0.2, 0.5, 0.2, 0.2, 0.8, 0.5, 0.2, 0.2, 0.5, 0.5, 0.5, 0.2, 0.8, 0.2, 0.2, 0.2]
listecondition = ['H0.2', 'B0.5', 'D0.2', 'G0.5', 'D0.8', 'H0.5', 'D0.8', 'B0.5', 'H0.8', 'B0.8', 'G0.8', 'B0.8', 'G0.2', 'B0.2', 'G0.8', 'H0.5', 'D0.2', 'D0.2', 'G0.5', 'D0.5', 'G0.8', 'B0.8', 'B0.8', 'B0.2', 'D0.5', 'H0.2', 'B0.8', 'B0.5', 'D0.8', 'B0.2', 'G0.2', 'B0.8', 'H0.8', 'H0.5', 'B0.8', 'H0.5', 'H0.2', 'B0.5', 'G0.8', 'H0.8', 'D0.8', 'B0.2', 'H0.8', 'B0.8', 'G0.2', 'D0.5', 'H0.2', 'H0.2', 'G0.5', 'H0.2', 'B0.2', 'D0.8', 'D0.2', 'B0.2', 'D0.8', 'G0.8', 'G0.5', 'H0.2', 'G0.8', 'D0.2', 'G0.8', 'D0.5', 'B0.5', 'H0.8', 'G0.8', 'G0.2', 'B0.2', 'B0.2', 'D0.2', 'D0.8', 'G0.8', 'B0.5', 'D0.8', 'H0.8', 'G0.2', 'G0.5', 'B0.5', 'D0.8', 'B0.8', 'D0.2', 'B0.5', 'H0.5', 'G0.2', 'H0.8', 'B0.5', 'D0.5', 'G0.5', 'H0.5', 'G0.2', 'B0.5', 'D0.8', 'H0.5', 'D0.5', 'D0.2', 'G0.5', 'H0.8', 'H0.8', 'G0.5', 'G0.5', 'H0.5', 'H0.5', 'D0.5', 'H0.2', 'G0.8', 'D0.2', 'G0.5', 'H0.2', 'G0.2', 'B0.8', 'D0.5', 'B0.2', 'B0.2', 'H0.5', 'D0.5', 'D0.5', 'H0.2', 'H0.8', 'G0.2', 'D0.2', 'G0.2']
# listecondition=['D0.2','G0.5','H0.8','B0.2']
mat=scipy.io.loadmat(datapath)

for k, cond in zip(range(160), listecondition):
    data[cond]['Essai'+str(k)]=mat['Essai'+str(k)][0][0]



#%%


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


# %% Excel
import csv 

name = 'resultats_RT_'+ sub + '.csv'
with open(name, 'w', newline ='') as file2:
    writer=csv.writer(file2)
    # writer.writerow(['','MDDV','MDDF','MDGV', 'MDGF', 'VMDV', 'VMDF', 'VMGV', 'VMGF', 'RTDV', 'RTDF', 'RTGV', 'RTGF'])
    writer.writerow(['Essai','Haut 0.2', 'Haut 0.5', 'Haut 0.8','Bas 0.2', 'Bas 0.5', 'Bas 0.8','Gauche 0.2', 'Gauche 0.5', 'Gauche 0.8','Droite 0.2', 'Droite 0.5', 'Droite 0.8'])
    
    for k in range(10):
        writer.writerow(['essai' + str (k), data['H0.2'][[key for key in data['H0.2'].keys()][k]],data['H0.5'][[key for key in data['H0.5'].keys()][k]],data['H0.8'][[key for key in data['H0.8'].keys()][k]],data['B0.2'][[key for key in data['B0.2'].keys()][k]],data['B0.5'][[key for key in data['B0.5'].keys()][k]],data['B0.8'][[key for key in data['B0.8'].keys()][k]],data['D0.2'][[key for key in data['D0.2'].keys()][k]],data['D0.5'][[key for key in data['D0.5'].keys()][k]],data['D0.8'][[key for key in data['D0.8'].keys()][k]],data['G0.2'][[key for key in data['G0.2'].keys()][k]],data['G0.5'][[key for key in data['G0.5'].keys()][k]],data['G0.8'][[key for key in data['G0.8'].keys()][k]]])

        # if k<=19:
        #     writer.writerow([ 'Essai'+str(k), MD['DV'][list(MD['DV'].keys())[k]] , MD['DF'][list(MD['DF'].keys())[k]], MD['GV'][list(MD['GV'].keys())[k]] , MD['GF'][list(MD['GF'].keys())[k]] , Vmax['DV'][list(MD['DV'].keys())[k]] , Vmax['DF'][list(MD['DF'].keys())[k]], Vmax['GV'][list(MD['GV'].keys())[k]] , Vmax['GF'][list(MD['GF'].keys())[k]] , RT['DV'][list(MD['DV'].keys())[k]] , RT['DF'][list(MD['DF'].keys())[k]] , RT['GV'][list(MD['GV'].keys())[k]] , RT['GF'][list(MD['GF'].keys())[k]] ])
        # else:
        #     writer.writerow([ 'Essai'+str(k), MD['DV'][list(MD['DV'].keys())[k]] , '', MD['GV'][list(MD['GV'].keys())[k]] , '' , Vmax['DV'][list(MD['DV'].keys())[k]] , '', Vmax['GV'][list(MD['GV'].keys())[k]] , '' , RT['DV'][list(MD['DV'].keys())[k]] , '' , RT['GV'][list(MD['GV'].keys())[k]] , '' ])



# %%
listecondition=['H', 'B', 'D', 'G', 'D', 'H', 'D', 'B', 'H', 'B', 'G', 'B', 'G', 'B', 'G', 'H', 'D', 'D', 'G', 'D', 'G', 'B', 'B', 'B', 'D', 'H', 'B', 'B', 'D', 'B', 'G', 'B', 'H', 'H', 'B', 'H', 'H', 'B', 'G', 'H', 'D', 'B', 'H', 'B', 'G', 'D', 'H', 'H', 'G', 'H', 'B', 'D', 'D', 'B', 'D', 'G', 'G', 'H', 'G', 'D', 'G', 'D', 'B', 'H', 'G', 'G', 'B', 'B', 'D', 'D', 'G', 'B', 'D', 'H', 'G', 'G', 'B', 'D', 'B', 'D', 'B', 'H', 'G', 'H', 'B', 'D', 'G', 'H', 'G', 'B', 'D', 'H', 'D', 'D', 'G', 'H', 'H', 'G', 'G', 'H', 'H', 'D', 'H', 'G', 'D', 'G', 'H', 'G', 'B', 'D', 'B', 'B', 'H', 'D', 'D', 'H', 'H', 'G', 'D', 'G']
listetemps=[0.2, 0.5, 0.2, 0.5, 0.8, 0.5, 0.8, 0.5, 0.8, 0.8, 0.8, 0.8, 0.2, 0.2, 0.8, 0.5, 0.2, 0.2, 0.5, 0.5, 0.8, 0.8, 0.8, 0.2, 0.5, 0.2, 0.8, 0.5, 0.8, 0.2, 0.2, 0.8, 0.8, 0.5, 0.8, 0.5, 0.2, 0.5, 0.8, 0.8, 0.8, 0.2, 0.8, 0.8, 0.2, 0.5, 0.2, 0.2, 0.5, 0.2, 0.2, 0.8, 0.2, 0.2, 0.8, 0.8, 0.5, 0.2, 0.8, 0.2, 0.8, 0.5, 0.5, 0.8, 0.8, 0.2, 0.2, 0.2, 0.2, 0.8, 0.8, 0.5, 0.8, 0.8, 0.2, 0.5, 0.5, 0.8, 0.8, 0.2, 0.5, 0.5, 0.2, 0.8, 0.5, 0.5, 0.5, 0.5, 0.2, 0.5, 0.8, 0.5, 0.5, 0.2, 0.5, 0.8, 0.8, 0.5, 0.5, 0.5, 0.5, 0.5, 0.2, 0.8, 0.2, 0.5, 0.2, 0.2, 0.8, 0.5, 0.2, 0.2, 0.5, 0.5, 0.5, 0.2, 0.8, 0.2, 0.2, 0.2]
liste=[]
for i in range (120):
    liste.append(listecondition[i]+str(listetemps[i]))
print(liste)



# %%

#%% GNG

#%%

import scipy.io



# %% Excel
import matplotlib.pyplot as plt

plt.plot(Vitesse['DV']['Essai158'])