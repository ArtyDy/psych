#%%
import scipy.io
import numpy as np


sub='sub-04AM'

datapath= sub + '/' + 'results_RFT_' + sub+'_.mat'
mat=scipy.io.loadmat(datapath)

data=dict()
data2=dict()

for k in range(162):
    data[k]=dict()
    data2[k]=dict()
    
# %%
