#%%
#%%
import scipy.io
import numpy as np


sub='sub-02PC'

datapath='E:/Manip/Psych/psych/'+sub+'/' + 'results_RFT_' + sub+'_.mat'
mat=scipy.io.loadmat(datapath)

# listeligne=[-7, -4, -2, -1, 0, 1, 2, 4, 7,-7, -4, -2, -1, 0, 1, 2, 4, 7]
# listecarre=[-45, -40,-35,-30,-25,-20,-15,-10,-5,0,5,10,15,20,25,30,35,40]
# listeligne=[-7, -4, -2, -1, 0, 1, 2, 4, 7,-7, -4, -2, -1, 0, 1, 2, 4, 7]
# listecarre=[-45, -40,-35,-30,-25,-20,-15,-10,-5,0,5,10,15,20,25,30,35,40]
# listecondition=[15,4,  1, 13, 14, 12, 10,  4, 12,  7, 16,  5, 11,  6,  3, 12, 17,6,  9, 14,  5, 11, 16,  4, 11,  2,  6, 10,  3,  3, 14, 14, 15,  0,9,  5,  7,  7, 14,  2,  9,  2,  2,  9,  5,  9, 10, 11,  8,  6,  8,7, 17,  7, 12, 17, 12,  8, 10, 14,  8, 16, 14, 13, 15,  1,  2,  0,13, 10, 17,  7, 17,  5, 11, 13, 11, 14,  9,  7,  9, 10,  5,  7,  7,4, 17,  7,  7,  3, 13, 16, 16, 17,  8,  0,  3, 17,  1, 17,  8, 14,8,  3,  1,  4, 16,  5,  4,  3, 11,  1, 13,  9,  3, 10,  5, 16, 17,15, 10,  2,  1, 10, 10, 11, 15,  4,  4,  4, 13,  4,  0,  1,  0,  7,6,  6, 17,  0,  4,  3,  2, 16, 15, 15, 10, 15,  6,  8, 11,  8,  6, 11,  1, 10, 15, 13,  9,  6, 14, 16, 12,  5, 15, 16,  9,  9,  1, 13, 11,  9,  6, 12,  0,  6, 17, 11,  8, 15, 12, 14,  5, 12, 12, 13, 13, 2,  1, 12,  5,  5,  0,  0,  0,  4,  2, 16,  6, 12,  2,  9,  1,  8, 5, 16, 15, 17,  8, 15,  2,  4,  1,  2, 14,  7,  8,  3,  3,  2,  3,11, 16,  3, 13,  0,  6, 14, 10,  1, 13, 12,  0,  0]
rect_oris=[ -35, -25, -15, -5, 5, 15, 25, 35]
rod_oris=[-7, -4, -2, -1, 1, 2, 4, 7]
cnds_order=[40, 62, 20, 19, 39, 53, 20, 61,  4, 48,  9, 51, 49, 40, 29, 15, 12,10, 39, 17, 10, 39, 32, 37, 59,  3, 63, 45, 28, 22,  5, 42, 58, 33,23, 52, 60,  8, 53,  9, 21, 56, 52, 63, 63, 16, 48,  2, 34, 60, 30,1, 55,  8, 30, 25, 38, 54,  6, 34, 37, 41, 46, 14,  6, 50, 12, 58,26, 16, 37,  1,  4, 34, 10,  0, 56, 35, 42, 47, 45, 27, 41, 55, 48,18, 29, 59, 32,  5, 10, 13, 30, 42, 39, 51,  4, 17, 47, 47, 12, 43,47, 23, 44, 43, 26, 14, 35, 25, 49, 31, 50, 14, 40,  5, 32, 17, 34,44, 37, 57, 45, 43, 31,  5, 15, 11, 61, 46, 38, 50, 21, 23, 34, 36,8,  6, 11, 19, 20, 20,  9, 11, 38, 57, 62, 55, 37, 60, 59, 53, 35,55, 31, 40, 56, 29, 62, 49, 48, 30,  3,  3, 39,  6,  5, 23,  7, 51,40, 48, 47, 26, 19, 54, 53, 36, 51, 21, 18, 46, 22, 41, 57, 61, 54,29, 59, 32, 32, 13, 22,  8, 44, 39, 24, 34, 52, 31, 51, 35, 19, 49,26, 28, 53, 49, 14,  9, 56, 36, 49, 44, 12, 37, 40, 45,  0, 54, 57,14, 48, 45,  1, 52, 63, 23, 55, 42,  0, 63, 26, 61,  4, 43, 13, 37,31, 13,  0, 62, 11, 42, 53, 24, 13, 35, 18, 33, 12, 13, 29, 16, 62,14, 41, 53, 52,  0,  6, 58, 59, 10, 38,  9, 42, 57,  3, 20, 33, 63,1, 56, 56, 39, 18, 26,  3,  7, 53, 18, 39, 61, 21, 30, 10,  1, 29,38,  5, 28,  5, 47, 41, 43, 63, 57, 39, 43, 48,  8, 44, 47, 43,  7,7, 19, 37,  8, 11, 45,  9, 20, 21,  2, 33,  6, 13, 17,  3, 18, 46,2, 58, 42, 24, 30,  7,  8,  8, 42, 34, 14,  6, 29, 60, 41, 52, 62,38, 14,  4, 42, 21, 11, 19, 20, 15, 27, 27, 25, 30, 10, 59, 57, 16,27, 56, 12, 50, 15, 15, 46, 35, 11, 35, 60, 17, 55, 49, 58, 32, 47,6, 11, 23, 35, 13, 31, 50, 24, 22, 26, 55, 41, 50, 33, 31, 34, 44,60, 15,  2, 58, 63, 28, 44, 55,  7, 50, 12, 40,  0, 61,  0, 46, 49,4, 59, 27, 18, 25, 12, 22, 10, 57, 55, 61, 51, 35, 44, 32, 35, 52,19, 17, 60, 28,  5, 17, 11, 49,  2,  3, 32, 42, 34, 32, 41, 54, 44,56,  0, 25, 22,  9, 40, 47, 23,  9, 29, 58, 23,  0, 45, 43, 45, 51,21, 48, 63, 36,  2, 19, 28, 30, 16, 14, 17, 57,  7, 54, 24,  5, 44,24, 21, 10, 26, 18, 26, 36, 28, 33, 18, 38, 27, 52, 59, 15, 31, 16,2, 38, 22, 49, 56, 26,  1, 54, 20, 52,  7,  3, 13, 18, 36,  2, 38,62,  4,  8,  9,  4, 54, 30, 54, 45, 33, 33, 17, 21,  1, 29, 25, 19,43, 16, 59, 54, 36, 52,  3, 41, 61, 12, 50,  6, 46, 25, 38, 48,  0,9, 27,  8, 46, 19, 25, 36, 15, 31, 16,  2, 36, 50,  5,  7, 10, 48,14, 21, 22, 28,  4, 28, 60, 47, 32, 28, 60, 46,  2, 37, 23,  6, 46,16, 29, 17, 24, 11, 15, 24, 60, 27, 61, 16, 58, 51, 20, 24, 51, 22,41, 58, 27, 61, 45, 53,  1, 62, 62,  3, 23,  4, 27, 63, 12,  7, 33,1, 13, 62, 22, 53, 36, 55, 50, 15, 43, 51, 39, 59, 30, 40,  1, 25,31, 33, 58, 37, 24, 40, 56, 57, 20, 34, 25]


# rect_cond=[-35, -35, -35, -35, -35, -35, -35, -35, -25, -25, -25, -25, -25, -25, -25, -25, -15, -15, -15, -15, -15, -15, -15, -15, -5, -5, -5, -5, -5, -5, -5, -5, 5, 5, 5, 5, 5, 5, 5, 5, 15, 15, 15, 15, 15, 15, 15, 15, 25, 25, 25, 25, 25, 25, 25, 25, 35, 35, 35, 35, 35, 35, 35, 35]
# rod_cond=[-7 -4 -2 -1  1  2  4  7 -7 -4 -2 -1  1  2  4  7 -7 -4 -2 -1  1  2  4  7
#  -7 -4 -2 -1  1  2  4  7 -7 -4 -2 -1  1  2  4  7 -7 -4 -2 -1  1  2  4  7
#  -7 -4 -2 -1  1  2  4  7 -7 -4 -2 -1  1  2  4  7]

rect_oriss=sorted(np.tile(rect_oris, len(rod_oris)))
rod_oriss=np.tile(rod_oris, len(rect_oris))

#définition taille du cictionnaire
data=dict()
data2=dict()
for i in range (64):
    data[i]=dict()
    data2[i]=dict()

#enregistrement de data[4][essai8][faux]
for l, cond in zip(range(640), cnds_order):
    data[cond]['Essai'+str(l)]=mat['keys_pressed'][l]
    data2[cond]['Essai'+str(l)]=mat['RT'][0][l]



print('ok')

#%% faire une liste pour 1er ligne excel
rect_oris=[ -35, -25, -15, -5, 5, 15, 25, 35]
rod_oris=[-7, -4, -2, -1, 1, 2, 4, 7]
liste=[]

for j in  rect_oris:
    for g in rod_oris:
        liste.append(str(j)+'/'+str(g))


# %% Faire un plot
import matplotlib.pyplot as plt

#prend le vecteur des éléments de data2[0]
plt.plot([data2[0][k] for k in data2[0].keys()])


#%% Faire un excel de Right Left
import csv

name = 'E:/Manip/Psych/psych/psych_RFT_COTE_'+ sub + '.csv'
nbcondition=0
nbessai=0

with open(name, 'w', newline ='') as file2:
    k=0
    writer=csv.writer(file2)
    writer.writerow(['Essai','-35/-7', '-35/-4', '-35/-2', '-35/-1', '-35/1', '-35/2', '-35/4', '-35/7', '-25/-7', '-25/-4', '-25/-2', '-25/-1', '-25/1', '-25/2', '-25/4', '-25/7', '-15/-7', '-15/-4', '-15/-2', '-15/-1', '-15/1', '-15/2', '-15/4', '-15/7', '-5/-7', '-5/-4', '-5/-2', '-5/-1', '-5/1', '-5/2', '-5/4', '-5/7', '5/-7', '5/-4', '5/-2', '5/-1', '5/1', '5/2', '5/4', '5/7', '15/-7', '15/-4', '15/-2', '15/-1', '15/1', '15/2', '15/4', '15/7', '25/-7', '25/-4', '25/-2', '25/-1', '25/1', '25/2', '25/4', '25/7', '35/-7', '35/-4', '35/-2', '35/-1', '35/1', '35/2', '35/4', '35/7'])
    for nbessai in range (10):
        k=k+1
        c='Essai'+str(k)
        print([nbessai, nbcondition])
        writer.writerow([ c,data[0][list(data[0].keys())[nbessai]],  data[1][list(data[1].keys())[nbessai]],  data[2][list(data[2].keys())[nbessai]],  data[3][list(data[3].keys())[nbessai]],  data[4][list(data[4].keys())[nbessai]],  data[5][list(data[5].keys())[nbessai]],  data[6][list(data[6].keys())[nbessai]],  data[7][list(data[7].keys())[nbessai]],  data[8][list(data[8].keys())[nbessai]],  data[9][list(data[9].keys())[nbessai]],  data[10][list(data[10].keys())[nbessai]],  data[11][list(data[11].keys())[nbessai]],  data[12][list(data[12].keys())[nbessai]],  data[13][list(data[13].keys())[nbessai]],  data[14][list(data[14].keys())[nbessai]],  data[15][list(data[15].keys())[nbessai]],  data[16][list(data[16].keys())[nbessai]],  data[17][list(data[17].keys())[nbessai]] ,  data[18][list(data[18].keys())[nbessai]],  data[19][list(data[19].keys())[nbessai]],  data[20][list(data[20].keys())[nbessai]],  data[21][list(data[21].keys())[nbessai]],  data[22][list(data[22].keys())[nbessai]],  data[23][list(data[23].keys())[nbessai]],  data[24][list(data[24].keys())[nbessai]],  data[25][list(data[25].keys())[nbessai]],  data[26][list(data[26].keys())[nbessai]],  data[27][list(data[27].keys())[nbessai]],  data[28][list(data[28].keys())[nbessai]],  data[29][list(data[29].keys())[nbessai]],  data[30][list(data[30].keys())[nbessai]],  data[31][list(data[31].keys())[nbessai]],  data[32][list(data[32].keys())[nbessai]],  data[33][list(data[33].keys())[nbessai]],  data[34][list(data[34].keys())[nbessai]],  data[35][list(data[35].keys())[nbessai]],  data[36][list(data[36].keys())[nbessai]],  data[37][list(data[37].keys())[nbessai]],  data[38][list(data[38].keys())[nbessai]],  data[39][list(data[39].keys())[nbessai]],  data[40][list(data[40].keys())[nbessai]],  data[41][list(data[41].keys())[nbessai]],  data[42][list(data[42].keys())[nbessai]],  data[43][list(data[43].keys())[nbessai]],  data[44][list(data[44].keys())[nbessai]],  data[45][list(data[45].keys())[nbessai]],  data[46][list(data[46].keys())[nbessai]],  data[47][list(data[47].keys())[nbessai]],  data[48][list(data[48].keys())[nbessai]],  data[49][list(data[49].keys())[nbessai]],  data[50][list(data[50].keys())[nbessai]],  data[51][list(data[51].keys())[nbessai]],  data[52][list(data[52].keys())[nbessai]],  data[53][list(data[53].keys())[nbessai]],  data[54][list(data[54].keys())[nbessai]],  data[55][list(data[55].keys())[nbessai]],  data[56][list(data[56].keys())[nbessai]],  data[57][list(data[57].keys())[nbessai]],  data[58][list(data[58].keys())[nbessai]],  data[59][list(data[59].keys())[nbessai]],  data[60][list(data[60].keys())[nbessai]],  data[61][list(data[61].keys())[nbessai]],  data[62][list(data[62].keys())[nbessai]],  data[63][list(data[63].keys())[nbessai]] ])

#%% Faire un excel de RT
import csv

name = 'psych_RFT_COTE_'+ sub + '.csv'
nbcondition=0
nbessai=0

with open(name, 'w', newline ='') as file2:
    k=0
    writer=csv.writer(file2)
    writer.writerow(['Essai','-35/-7', '-35/-4', '-35/-2', '-35/-1', '-35/1', '-35/2', '-35/4', '-35/7', '-25/-7', '-25/-4', '-25/-2', '-25/-1', '-25/1', '-25/2', '-25/4', '-25/7', '-15/-7', '-15/-4', '-15/-2', '-15/-1', '-15/1', '-15/2', '-15/4', '-15/7', '-5/-7', '-5/-4', '-5/-2', '-5/-1', '-5/1', '-5/2', '-5/4', '-5/7', '5/-7', '5/-4', '5/-2', '5/-1', '5/1', '5/2', '5/4', '5/7', '15/-7', '15/-4', '15/-2', '15/-1', '15/1', '15/2', '15/4', '15/7', '25/-7', '25/-4', '25/-2', '25/-1', '25/1', '25/2', '25/4', '25/7', '35/-7', '35/-4', '35/-2', '35/-1', '35/1', '35/2', '35/4', '35/7'])
    for nbessai in range (10):
        k=k+1
        c='Essai'+str(k)
        print([nbessai, nbcondition])
        writer.writerow([ c,data[0][list(data[0].keys())[nbessai]],  data[1][list(data[1].keys())[nbessai]],  data[2][list(data[2].keys())[nbessai]],  data[3][list(data[3].keys())[nbessai]],  data[4][list(data[4].keys())[nbessai]],  data[5][list(data[5].keys())[nbessai]],  data[6][list(data[6].keys())[nbessai]],  data[7][list(data[7].keys())[nbessai]],  data[8][list(data[8].keys())[nbessai]],  data[9][list(data[9].keys())[nbessai]],  data[10][list(data[10].keys())[nbessai]],  data[11][list(data[11].keys())[nbessai]],  data[12][list(data[12].keys())[nbessai]],  data[13][list(data[13].keys())[nbessai]],  data[14][list(data[14].keys())[nbessai]],  data[15][list(data[15].keys())[nbessai]],  data[16][list(data[16].keys())[nbessai]],  data[17][list(data[17].keys())[nbessai]] ,  data[18][list(data[18].keys())[nbessai]],  data[19][list(data[19].keys())[nbessai]],  data[20][list(data[20].keys())[nbessai]],  data[21][list(data[21].keys())[nbessai]],  data[22][list(data[22].keys())[nbessai]],  data[23][list(data[23].keys())[nbessai]],  data[24][list(data[24].keys())[nbessai]],  data[25][list(data[25].keys())[nbessai]],  data[26][list(data[26].keys())[nbessai]],  data[27][list(data[27].keys())[nbessai]],  data[28][list(data[28].keys())[nbessai]],  data[29][list(data[29].keys())[nbessai]],  data[30][list(data[30].keys())[nbessai]],  data[31][list(data[31].keys())[nbessai]],  data[32][list(data[32].keys())[nbessai]],  data[33][list(data[33].keys())[nbessai]],  data[34][list(data[34].keys())[nbessai]],  data[35][list(data[35].keys())[nbessai]],  data[36][list(data[36].keys())[nbessai]],  data[37][list(data[37].keys())[nbessai]],  data[38][list(data[38].keys())[nbessai]],  data[39][list(data[39].keys())[nbessai]],  data[40][list(data[40].keys())[nbessai]],  data[41][list(data[41].keys())[nbessai]],  data[42][list(data[42].keys())[nbessai]],  data[43][list(data[43].keys())[nbessai]],  data[44][list(data[44].keys())[nbessai]],  data[45][list(data[45].keys())[nbessai]],  data[46][list(data[46].keys())[nbessai]],  data[47][list(data[47].keys())[nbessai]],  data[48][list(data[48].keys())[nbessai]],  data[49][list(data[49].keys())[nbessai]],  data[50][list(data[50].keys())[nbessai]],  data[51][list(data[51].keys())[nbessai]],  data[52][list(data[52].keys())[nbessai]],  data[53][list(data[53].keys())[nbessai]],  data[54][list(data[54].keys())[nbessai]],  data[55][list(data[55].keys())[nbessai]],  data[56][list(data[56].keys())[nbessai]],  data[57][list(data[57].keys())[nbessai]],  data[58][list(data[58].keys())[nbessai]],  data[59][list(data[59].keys())[nbessai]],  data[60][list(data[60].keys())[nbessai]],  data[61][list(data[61].keys())[nbessai]],  data[62][list(data[62].keys())[nbessai]],  data[63][list(data[63].keys())[nbessai]] ])

5
#%%
#%% Faire un excel de RT
import csv

name = 'psych_RFT_RT_'+ sub + '.csv'
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
