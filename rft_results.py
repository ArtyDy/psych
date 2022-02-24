#%%
#%%
import scipy.io
import numpy as np


sub='sub-00AD'

datapath= sub + '/' + 'results_RFT_' + sub+'_.mat'
mat=scipy.io.loadmat(datapath)

listeligne=[-7, -4, -2, -1, 0, 1, 2, 4, 7,-7, -4, -2, -1, 0, 1, 2, 4, 7]
listecarre=[-45, -40,-35,-30,-25,-20,-15,-10,-5,0,5,10,15,20,25,30,35,40]
listecondition=[15,4,  1, 13, 14, 12, 10,  4, 12,  7, 16,  5, 11,  6,  3, 12, 17,6,  9, 14,  5, 11, 16,  4, 11,  2,  6, 10,  3,  3, 14, 14, 15,  0,9,  5,  7,  7, 14,  2,  9,  2,  2,  9,  5,  9, 10, 11,  8,  6,  8,7, 17,  7, 12, 17, 12,  8, 10, 14,  8, 16, 14, 13, 15,  1,  2,  0,13, 10, 17,  7, 17,  5, 11, 13, 11, 14,  9,  7,  9, 10,  5,  7,  7,4, 17,  7,  7,  3, 13, 16, 16, 17,  8,  0,  3, 17,  1, 17,  8, 14,8,  3,  1,  4, 16,  5,  4,  3, 11,  1, 13,  9,  3, 10,  5, 16, 17,15, 10,  2,  1, 10, 10, 11, 15,  4,  4,  4, 13,  4,  0,  1,  0,  7,6,  6, 17,  0,  4,  3,  2, 16, 15, 15, 10, 15,  6,  8, 11,  8,  6, 11,  1, 10, 15, 13,  9,  6, 14, 16, 12,  5, 15, 16,  9,  9,  1, 13, 11,  9,  6, 12,  0,  6, 17, 11,  8, 15, 12, 14,  5, 12, 12, 13, 13, 2,  1, 12,  5,  5,  0,  0,  0,  4,  2, 16,  6, 12,  2,  9,  1,  8, 5, 16, 15, 17,  8, 15,  2,  4,  1,  2, 14,  7,  8,  3,  3,  2,  3,11, 16,  3, 13,  0,  6, 14, 10,  1, 13, 12,  0,  0]

#définition taille du cictionnaire
data=dict()
data2=dict()
for i in range (18):
    data[i]=dict()
    data2[i]=dict()

#enregistrement de data[4][essai8][faux]
for l, cond in zip(range(234), listecondition):
    data[cond]['Essai'+str(l)]=mat['keys_pressed'][l]
    data2[cond]['Essai'+str(l)]=mat['RT'][0][l]



print('ok')


# %% Faire un plot
import matplotlib.pyplot as plt

#prend le vecteur des éléments de data2[0]
plt.plot([data2[0][k] for k in data2[0].keys()])


#%% Faire un excel de Right Left
import csv

name = 'psych_RFT_RT'+ sub + '.csv'
nbcondition=0
nbessai=0

with open(name, 'w', newline ='') as file2:
    k=0
    writer=csv.writer(file2)
    writer.writerow(['Essai','Cond_0 -7/-45', 'Cond_1 -4/-40', 'Cond_2 -2/-35', 'Cond_3 -1/-30', 'Cond_4 0/-25', 'Cond_5 1/-20', 'Cond_6 2/-15', 'Cond_7 4/-10', 'Cond_8 7/-5', 'Cond_9 -7/0', 'Cond_10 -4/5', 'Cond_11 -2/10', 'Cond_12 -1/15', 'Cond_13 0/20', 'Cond_14 1/25', 'Cond_15 2/30', 'Cond_16 4/35', 'Cond_17 7/40'])
    for nbessai in range (13):
        k=k+1
        c='Essai'+str(k)
        print([nbessai, nbcondition])
        writer.writerow([ c,data2[0][list(data2[0].keys())[nbessai]],  data2[1][list(data2[1].keys())[nbessai]],  data2[2][list(data2[2].keys())[nbessai]],  data2[3][list(data2[3].keys())[nbessai]],  data2[4][list(data2[4].keys())[nbessai]],  data2[5][list(data2[5].keys())[nbessai]],  data2[6][list(data2[6].keys())[nbessai]],  data2[7][list(data2[7].keys())[nbessai]],  data2[8][list(data2[8].keys())[nbessai]],  data2[9][list(data2[9].keys())[nbessai]],  data2[10][list(data2[10].keys())[nbessai]],  data2[11][list(data2[11].keys())[nbessai]],  data2[12][list(data2[12].keys())[nbessai]],  data2[13][list(data2[13].keys())[nbessai]],  data2[14][list(data2[14].keys())[nbessai]],  data2[15][list(data2[15].keys())[nbessai]],  data2[16][list(data2[16].keys())[nbessai]],  data2[17][list(data2[17].keys())[nbessai]]  ])

#%%
#%% Faire un excel de RT
import csv

name = 'psych_RFT_RT'+ sub + '.csv'
nbcondition=0
nbessai=0

with open(name, 'w', newline ='') as file2:
    k=0
    writer=csv.writer(file2)
    writer.writerow(['Essai','Cond_0 -7/-45', 'Cond_1 -4/-40', 'Cond_2 -2/-35', 'Cond_3 -1/-30', 'Cond_4 0/-25', 'Cond_5 1/-20', 'Cond_6 2/-15', 'Cond_7 4/-10', 'Cond_8 7/-5', 'Cond_9 -7/0', 'Cond_10 -4/5', 'Cond_11 -2/10', 'Cond_12 -1/15', 'Cond_13 0/20', 'Cond_14 1/25', 'Cond_15 2/30', 'Cond_16 4/35', 'Cond_17 7/40'])
    for nbessai in range (13):
        k=k+1
        c='Essai'+str(k)
        print([nbessai, nbcondition])
       #writer.writerow([ c,data[0][list(data[0].keys())[nbessai]],  data[1][list(data[1].keys())[nbessai]],  data[2][list(data[2].keys())[nbessai]],  data[3][list(data[3].keys())[nbessai]],  data[4][list(data[4].keys())[nbessai]],  data[5][list(data[5].keys())[nbessai]],  data[6][list(data[6].keys())[nbessai]],  data[7][list(data[7].keys())[nbessai]],  data[8][list(data[8].keys())[nbessai]],  data[9][list(data[9].keys())[nbessai]],  data[10][list(data[10].keys())[nbessai]],  data[11][list(data[11].keys())[nbessai]],  data[12][list(data[12].keys())[nbessai]],  data[13][list(data[13].keys())[nbessai]],  data[14][list(data[14].keys())[nbessai]],  data[15][list(data[15].keys())[nbessai]],  data[16][list(data[16].keys())[nbessai]],  data[17][list(data[17].keys())[nbessai]]  ])
        writer.writerow([ c,data2[0][list(data2[0].keys())[nbessai]],  data2[1][list(data2[1].keys())[nbessai]],  data2[2][list(data2[2].keys())[nbessai]],  data2[3][list(data2[3].keys())[nbessai]],  data2[4][list(data2[4].keys())[nbessai]],  data2[5][list(data2[5].keys())[nbessai]],  data2[6][list(data2[6].keys())[nbessai]],  data2[7][list(data2[7].keys())[nbessai]],  data2[8][list(data2[8].keys())[nbessai]],  data2[9][list(data2[9].keys())[nbessai]],  data2[10][list(data2[10].keys())[nbessai]],  data2[11][list(data2[11].keys())[nbessai]],  data2[12][list(data2[12].keys())[nbessai]],  data2[13][list(data2[13].keys())[nbessai]],  data2[14][list(data2[14].keys())[nbessai]],  data2[15][list(data2[15].keys())[nbessai]],  data2[16][list(data2[16].keys())[nbessai]],  data2[17][list(data2[17].keys())[nbessai]]  ])



 

#%% Avoir la liste des conditions à mettre titre excel
listeligne=[-7, -4, -2, -1, 0, 1, 2, 4, 7,-7, -4, -2, -1, 0, 1, 2, 4, 7]
listecarre=[-45, -40,-35,-30,-25,-20,-15,-10,-5,0,5,10,15,20,25,30,35,40]
listecond=[]
for v in range (18):
    chaine='Cond_'+str(v) + ' ' +str(listeligne[v])+ '/' + str(listecarre[v])
    listecond.append(chaine)
 
print(listecond)

# %%
