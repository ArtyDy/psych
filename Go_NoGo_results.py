#%%
from ast import Break
import scipy.io
import numpy as np
import glob
from ast import Break
import os

sub='sub-22ML'

datapath= sub + '/'
data=dict()
datapos=dict()


idx=[]
for file in glob.glob(datapath + 'results_gng_' + sub +'*.mat'):
    if os.path.basename(file)[-7]=='_':
                idx.append(os.path.basename(file)[-6:-4])
idx=sorted(idx)
# listecondition=['C', 'NG', 'C', 'NG', 'NG', 'C', 'C', 'NG', 'C', 'C', 'NG', 'NG', 'C', 'G', 'NG', 'NG', 'NG', 'NG', 'C', 'G', 'NG', 'C', 'C', 'C', 'G', 'NG', 'C', 'G', 'G', 'C', 'NG', 'NG', 'C', 'NG', 'NG', 'C', 'G', 'NG', 'NG', 'G', 'G', 'G', 'NG', 'NG', 'G', 'C', 'NG', 'NG', 'NG', 'NG', 'G', 'C', 'C', 'G', 'C', 'C', 'C', 'C', 'G', 'C', 'NG', 'C', 'G', 'NG', 'C', 'G', 'C', 'G', 'G', 'NG', 'C', 'C', 'G', 'G', 'NG', 'G', 'G', 'NG', 'C', 'C', 'G', 'G', 'G', 'G', 'NG', 'G', 'G', 'G', 'G', 'G']
# listecondition = ['NG', 'C', 'G', 'C', 'C', 'NG', 'NG', 'G', 'NG', 'G', 'NG', 'G', 'G', 'C', 'NG', 'G', 'NG', 'C', 'C', 'G', 'G', 'C', 'NG', 'C', 'C', 'G', 'C', 'NG', 'C', 'C', 'G', 'G', 'C', 'G', 'NG', 'C', 'NG', 'C', 'G', 'G', 'NG', 'G', 'NG', 'C', 'NG', 'C', 'NG', 'NG', 'G', 'NG', 'G', 'G', 'G', 'G', 'NG', 'NG', 'C', 'NG', 'C', 'G', 'NG', 'G', 'C', 'G', 'G', 'C', 'C', 'NG', 'C', 'NG', 'C', 'C', 'G', 'C', 'G', 'NG', 'C', 'NG', 'NG', 'NG', 'NG', 'C', 'G', 'G', 'C', 'NG', 'C', 'G', 'NG', 'G']
listecondition=['G', 'NG', 'G', 'NG', 'NG', 'C', 'G', 'G', 'NG', 'G', 'C', 'NG','NG', 'G', 'NG', 'C', 'C', 'G', 'G', 'NG', 'C', 'G', 'G', 'NG','NG', 'G', 'G', 'C', 'C', 'C', 'C', 'G', 'G', 'G', 'NG', 'G', 'C','G', 'G', 'C', 'G', 'NG', 'NG', 'NG', 'C', 'NG', 'C', 'G', 'G','C', 'C', 'C', 'NG', 'G', 'NG', 'C', 'C', 'C', 'G', 'C', 'NG', 'C','G', 'C', 'NG', 'G', 'NG', 'C', 'C', 'NG', 'C', 'C', 'G', 'NG',
'NG', 'G', 'NG', 'G', 'C', 'C', 'NG', 'C', 'G', 'C', 'G', 'C',
'NG', 'G', 'NG', 'C', 'G', 'G', 'G', 'G', 'C', 'G', 'NG', 'NG',
'NG', 'G', 'C', 'C', 'G', 'NG', 'NG', 'C', 'C', 'C', 'NG', 'C',
'C', 'C', 'NG', 'C', 'NG', 'C', 'G', 'C', 'G', 'C', 'G', 'NG', 'G',
'NG', 'NG', 'C', 'G', 'C', 'G', 'NG', 'C', 'NG', 'NG', 'NG', 'NG',
'G', 'C', 'G', 'G', 'NG', 'C', 'G', 'G', 'NG', 'NG', 'G', 'C', 'G',
'NG', 'G', 'C', 'NG', 'C', 'NG', 'NG', 'C', 'G', 'C', 'G', 'NG',
'NG', 'NG', 'C', 'G', 'C', 'G', 'NG', 'G', 'NG', 'NG', 'C', 'G',
'NG', 'NG', 'NG', 'G', 'NG', 'C', 'C', 'G']
for k in range(60):
    listecondition.remove('NG')
listecond=['G','NG','C']

for i in listecond:
    data[i]=dict()
    datapos[i]=dict()

#mettre data['GO']['Essai13'][0000000001111100000000000000000]
for cond, n, file in zip (listecondition, idx, (glob.glob(datapath + 'results_gng_' + sub +'*.mat'))):
    mat=scipy.io.loadmat(file)
    data[cond]['Essai'+str(n)]= mat['Buttons'][:,0]
    datapos[cond]['Essai'+str(n)]= mat['Pos'][:,1]


#liste de RT : temps où clique / sansclique
listeRT = []
for d in data.keys():
    for e in data[d].keys():
        if 1 in data[d][e]:
            a=np.where(data[d][e]==1) #renvoi les indices où data[d][e]=1 dans un array
            listeRT.append(a[0][0]/60)

        else :
            listeRT.append('sansclique')
print (listeRT)

#dictionnaire de vitesses
vitesse=dict()
for co in datapos.keys():
    vitesse[co]=dict()
    for es in datapos[co].keys():
        vitesse[co][es]=dict()

for condition in datapos.keys():
    for essais in datapos[condition].keys():
        for pos in range (len(datapos[condition][essais])):
            if pos!=0:
                vitesse[condition][essais][pos]=abs(datapos[condition][essais][pos]- datapos[condition][essais][pos-1])*60
        
#dictionnaire de Vmax
vmax=dict()
for c in datapos.keys():
    vmax[c]=dict()

listevmax=[]
for c in datapos.keys():
    for e in datapos[c].keys():
        vmax[c][e]=np.max([vitesse[c][e][k]for k in vitesse[c][e]])
        listevmax.append(np.max([vitesse[c][e][k]for k in vitesse[c][e]]))




# %% Faire un excel des cliques
import csv

name = 'results_GNG_'+ sub + '.csv'

with open(name, 'w', newline ='') as file2:
    k=0
    writer=csv.writer(file2)
    writer.writerow(['Essai','GO','Vmax GO','Rest','Vmax Rest'])
    for nbessai in range (30):
        k=k+1
        c='Essai'+str(k)
        writer.writerow([ c,listeRT[nbessai],listevmax[nbessai],listeRT[nbessai+30],listevmax[nbessai+30]])



# %%
import matplotlib.pyplot as plt
plt.plot([vitesse['G']['Essai16'][k]for k in vitesse['G']['Essai16']])

# %%
# for q in datapos.keys():
for u in datapos['C'].keys():
    plt.plot(datapos['C'][u])
    plt.show()


# %%
