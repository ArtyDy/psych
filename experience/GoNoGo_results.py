#%%
from ast import Break
import scipy.io
import numpy as np
import glob
from ast import Break
import os

sub='sub-test'

datapath= sub + '/'
data=dict()
datapos=dict()


idx=[]
mat=scipy.io.loadmat('C:/Users/mathi/OneDrive/Documents/GitHub/psych/experience/'+ 'results_GNG'+sub + '.mat')
# for file in glob.glob(datapath + 'results_gng_' + sub +'.mat'):
#     if os.path.basename(file)[-7]=='_':
#                 idx.append(os.path.basename(file)[-6:-4])
idx=sorted(idx)
# listecondition=['C', 'NG', 'C', 'NG', 'NG', 'C', 'C', 'NG', 'C', 'C', 'NG', 'NG', 'C', 'G', 'NG', 'NG', 'NG', 'NG', 'C', 'G', 'NG', 'C', 'C', 'C', 'G', 'NG', 'C', 'G', 'G', 'C', 'NG', 'NG', 'C', 'NG', 'NG', 'C', 'G', 'NG', 'NG', 'G', 'G', 'G', 'NG', 'NG', 'G', 'C', 'NG', 'NG', 'NG', 'NG', 'G', 'C', 'C', 'G', 'C', 'C', 'C', 'C', 'G', 'C', 'NG', 'C', 'G', 'NG', 'C', 'G', 'C', 'G', 'G', 'NG', 'C', 'C', 'G', 'G', 'NG', 'G', 'G', 'NG', 'C', 'C', 'G', 'G', 'G', 'G', 'NG', 'G', 'G', 'G', 'G', 'G']
# listecondition = ['NG', 'C', 'G', 'C', 'C', 'NG', 'NG', 'G', 'NG', 'G', 'NG', 'G', 'G', 'C', 'NG', 'G', 'NG', 'C', 'C', 'G', 'G', 'C', 'NG', 'C', 'C', 'G', 'C', 'NG', 'C', 'C', 'G', 'G', 'C', 'G', 'NG', 'C', 'NG', 'C', 'G', 'G', 'NG', 'G', 'NG', 'C', 'NG', 'C', 'NG', 'NG', 'G', 'NG', 'G', 'G', 'G', 'G', 'NG', 'NG', 'C', 'NG', 'C', 'G', 'NG', 'G', 'C', 'G', 'G', 'C', 'C', 'NG', 'C', 'NG', 'C', 'C', 'G', 'C', 'G', 'NG', 'C', 'NG', 'NG', 'NG', 'NG', 'C', 'G', 'G', 'C', 'NG', 'C', 'G', 'NG', 'G']
# # listecondition=['G', 'NG', 'G', 'NG', 'NG', 'C', 'G', 'G', 'NG', 'G', 'C', 'NG','NG', 'G', 'NG', 'C', 'C', 'G', 'G', 'NG', 'C', 'G', 'G', 'NG','NG', 'G', 'G', 'C', 'C', 'C', 'C', 'G', 'G', 'G', 'NG', 'G', 'C','G', 'G', 'C', 'G', 'NG', 'NG', 'NG', 'C', 'NG', 'C', 'G', 'G','C', 'C', 'C', 'NG', 'G', 'NG', 'C', 'C', 'C', 'G', 'C', 'NG', 'C','G', 'C', 'NG', 'G', 'NG', 'C', 'C', 'NG', 'C', 'C', 'G', 'NG',
# 'NG', 'G', 'NG', 'G', 'C', 'C', 'NG', 'C', 'G', 'C', 'G', 'C',
# 'NG', 'G', 'NG', 'C', 'G', 'G', 'G', 'G', 'C', 'G', 'NG', 'NG',
# 'NG', 'G', 'C', 'C', 'G', 'NG', 'NG', 'C', 'C', 'C', 'NG', 'C',
# 'C', 'C', 'NG', 'C', 'NG', 'C', 'G', 'C', 'G', 'C', 'G', 'NG', 'G',
# 'NG', 'NG', 'C', 'G', 'C', 'G', 'NG', 'C', 'NG', 'NG', 'NG', 'NG',
# 'G', 'C', 'G', 'G', 'NG', 'C', 'G', 'G', 'NG', 'NG', 'G', 'C', 'G',
# 'NG', 'G', 'C', 'NG', 'C', 'NG', 'NG', 'C', 'G', 'C', 'G', 'NG',
# 'NG', 'NG', 'C', 'G', 'C', 'G', 'NG', 'G', 'NG', 'NG', 'C', 'G',
# 'NG', 'NG', 'NG', 'G', 'NG', 'C', 'C', 'G']

# listecondition=['GB2', 'NGB8', 'NGD5', 'GD8', 'NGB2', 'NGH2', 'NGH2', 'GG5', 'NGH8', 'NGB5', 'NGH5', 'GB5', 'NGG5', 'GH2', 'GG8', 'NGD2', 'GD5', 'GG8', 'GH8', 'NGD8', 'GG8', 'GB2', 'NGD2', 'GD8', 'GB5', 'NGH8', 'NGG2', 'GH2', 'GH2', 'GB2', 'NGD8', 'NGG2', 'NGH8', 'GB2', 'NGG2', 'NGH5', 'GD8', 'GH5', 'NGG8', 'NGG5', 'GD2', 'GG2', 'NGH5', 'GG2', 'NGG2', 'NGD5', 'NGB5', 'NGD8', 'NGD5', 'NGH8', 'GH5', 'GD8', 'GD5', 'NGG5', 'GB5', 'GH8', 'NGB2', 'GG8', 'NGB8', 'GH2', 'GG2', 'GD2', 'GB2', 'NGH5', 'GB8', 'NGG2', 'NGB2', 'NGB5', 'NGH5', 'NGB8', 'GG2', 'GD5', 'NGH8', 'GB5', 'NGD2', 'NGD2', 'GG5', 'GG2', 'GB8', 'GD2', 'NGH2', 'GG5', 'GG8', 'GD2', 'NGG8', 'GH8', 'NGH8', 'GH8', 'GH8', 'GH8', 'GB2', 'NGD2', 'NGB8', 'NGH8', 'NGG8', 'NGG5', 'GD8', 'GH5', 'GD5', 'GG5', 'GB8', 'NGB5', 'NGD5', 'GH2', 'GG5', 'GH8', 'NGB8', 'NGG5', 'GH2', 'NGD2', 'NGG8', 'NGD8', 'NGD5', 'GD8', 'NGH2', 'GB8', 'GD5', 'NGG8', 'NGD8', 'GD2', 'NGB8', 'NGH2', 'NGD8', 'NGB2', 'NGG5', 'GG8', 'GB5', 'GG5', 'GH5', 'NGB5', 'NGB8', 'NGH5', 'NGB2', 'NGG2', 'NGD5', 'GH2', 'GD2', 'GB5', 'NGH5', 'NGB5', 'GB8', 'NGB2', 'GB5', 'NGG5', 'GH5', 'NGD5', 'NGB5', 'GD5', 'GG2', 'NGH2', 'NGG8', 'GD2', 'NGH2', 'GB2', 'NGD2', 'NGD8', 'GD8', 'GB8', 'NGB2', 'GH5', 'NGG2', 'GB8', 'GG2', 'GG5', 'GH5', 'GD5', 'GG8', 'NGG8']
listecondition=['GG2','NGG8','GD2','NGD8']
listecondition=['GB2', 'NGB8', 'NGD5', 'GD8']


# for k in range(60):
#     listecondition.remove('NG')
# listecond=['G','NG','C']
listecond=['GD2','GD5','GD8','GG2','GG5','GG8','GH2','GH5','GH8','GB2','GB5','GB8','NGD2','NGD5','NGD8','NGG2','NGG5','NGG8','NGH2','NGH5','NGH8','NGB2','NGB5','NGB8']

for i in listecond:
    data[i]=dict()
    datapos[i]=dict()

#mettre data['GO']['Essai13'][0000000001111100000000000000000]
# for cond, n, file in zip (listecondition, idx, (glob.glob(datapath + 'results_gng_' + sub +'*.mat'))):
#     mat=scipy.io.loadmat(file)
#     data[cond]['Essai'+str(n)]= mat['Buttons'][:,0]
#     datapos[cond]['Essai'+str(n)]= mat['Pos'][:,1]

for cond, i in zip (listecondition, range(len(listecondition))):
    if mat[sub][0][i].size>0:
        data[cond]['essai'+str(i)]=mat[sub][0][i][0][1]
    else:
        data[cond]['essai'+str(i)]=[]


# #liste de RT : temps où clique / sansclique
# listeRT = []
# for d in data.keys():
#     for e in data[d].keys():
#         if 1 in data[d][e]:
#             a=np.where(data[d][e]==1) #renvoi les indices où data[d][e]=1 dans un array
#             listeRT.append(a[0][0]/60)

#         else :
#             listeRT.append('sansclique')
# print (listeRT)

# #dictionnaire de vitesses
# vitesse=dict()
# for co in datapos.keys():
#     vitesse[co]=dict()
#     for es in datapos[co].keys():
#         vitesse[co][es]=dict()

# for condition in datapos.keys():
#     for essais in datapos[condition].keys():
#         for pos in range (len(datapos[condition][essais])):
#             if pos!=0:
#                 vitesse[condition][essais][pos]=abs(datapos[condition][essais][pos]- datapos[condition][essais][pos-1])*60
        
#dictionnaire de Vmax
# vmax=dict()
# for c in datapos.keys():
#     vmax[c]=dict()

# listevmax=[]
# for c in datapos.keys():
#     for e in datapos[c].keys():
#         vmax[c][e]=np.max([vitesse[c][e][k]for k in vitesse[c][e]])
#         listevmax.append(np.max([vitesse[c][e][k]for k in vitesse[c][e]]))




# %% Faire un excel des cliques
import csv

name = 'results_GNG_'+ sub + '.csv'

with open(name, 'w', newline ='') as file2:
    k=0
    writer=csv.writer(file2)
    writer.writerow(['Essai','GD2','GD5','GD8','GG2','GG5','GG8','GH2','GH5','GH8','GB2','GB5','GB8','NGD2','NGD5','NGD8','NGG2','NGG5','NGG8','NGH2','NGH5','NGH8','NGB2','NGB5','NGB8'])

    for n in range (7):
        writer.writerow(['Essai'+str(n),data['GD2'][[key for key in data['GD2'].keys()][n]],data['GD5'][[key for key in data['GD5'].keys()][n]],data['GD8'][[key for key in data['GD8'].keys()][n]],data['GG2'][[key for key in data['GG2'].keys()][n]],data['GG5'][[key for key in data['GG5'].keys()][n]],data['GG8'][[key for key in data['GG8'].keys()][n]],data['GH2'][[key for key in data['GH2'].keys()][n]],data['GH5'][[key for key in data['GH5'].keys()][n]],data['GH8'][[key for key in data['GH8'].keys()][n]],data['GB2'][[key for key in data['GB2'].keys()][n]],data['GB5'][[key for key in data['GB5'].keys()][n]],data['GB8'][[key for key in data['GB8'].keys()][n]],data['NGD2'][[key for key in data['NGD2'].keys()][n]],data['NGD5'][[key for key in data['NGD5'].keys()][n]],data['NGD8'][[key for key in data['NGD8'].keys()][n]],data['NGG2'][[key for key in data['NGG2'].keys()][n]],data['NGG5'][[key for key in data['NGG5'].keys()][n]],data['NGG8'][[key for key in data['NGG8'].keys()][n]],data['NGH2'][[key for key in data['NGH2'].keys()][n]],data['NGH5'][[key for key in data['NGH5'].keys()][n]],data['NGH8'][[key for key in data['NGH8'].keys()][n]],data['NGB2'][[key for key in data['NGB2'].keys()][n]],data['NGB5'][[key for key in data['NGB5'].keys()][n]],data['NGB8'][[key for key in data['NGB8'].keys()][n]]])


# %%
import matplotlib.pyplot as plt
plt.plot([vitesse['G']['Essai16'][k]for k in vitesse['G']['Essai16']])

# %%
# for q in datapos.keys():
for u in datapos['C'].keys():
    plt.plot(datapos['C'][u])
    plt.show()


# %%
