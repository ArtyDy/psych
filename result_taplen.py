#%%

import scipy.io


sub='sub-22ML'
datapath= sub + '/' + 'results_timerep_' + sub+'_taplen'+'.mat'
mat=scipy.io.loadmat(datapath)

conds=['600', '1200', '1000', '800', '800', '1200', '1200', '600', '800',
       '400', '1200', '1600', '1200', '400', '400', '600', '800', '600',
       '400', '400', '1400', '600', '1000', '400', '1000', '1600', '800',
       '1000', '1400', '1400', '1600', '1400', '1400', '600', '400',
       '1200', '1600', '1200', '1000', '800', '600', '1600', '400',
       '1000', '1600', '600', '400', '800', '1600', '1400', '800', '1200',
       '1000', '1000', '1600', '1200', '400', '1400', '1400', '800',
       '1200', '1000', '600', '1000', '1600', '800', '1400', '1400',
       '600', '1600']

listecond=['400','600','800','1000','1200','1400','1600']
listeresult=[]

data=dict()
for i in listecond:
    data[i]=dict()

for cond, j in zip (conds, range (len(conds))) :
    for c in listecond :
        if c==cond :
            data[c]['essai'+ str(j)]=mat[sub][:,1][j]
            


# %% Excel
import csv

name = 'results_onetap_'+ sub + '.csv'
nbparcond=10

with open(name, 'w', newline ='') as file2:
    writer=csv.writer(file2)
    writer.writerow(['Essai','400','600','800','1000','1200','1400'])

    for n in range(10) :
        #writer.writerow(['Essai'+str(n),str(listeresult[n]),str(listeresult[n+nbparcond]),str(listeresult[n+nbparcond*2]),str(listeresult[n+nbparcond*3]),str(listeresult[n+nbparcond* 4]),str(listeresult[n+nbparcond*5])])
        writer.writerow(['Essai'+str(n),data['400'][[key for key in data['400'].keys()][n]],data['800'][[key for key in data['800'].keys()][n]],data['1000'][[key for key in data['1000'].keys()][n]],data['1200'][[key for key in data['1200'].keys()][n]],data['1400'][[key for key in data['1400'].keys()][n]],data['1600'][[key for key in data['1600'].keys()][n]] ])


# %%
