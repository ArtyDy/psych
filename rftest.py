#%%
sub='sub-00AD'

from logging import shutdown
import psychopy

import random
import numpy as np
from psychopy import visual, core, event
from sklearn.utils import shuffle
from scipy.io import savemat



win = psychopy.visual.Window(
    size=[400, 400],
    units="pix",
    fullscr=True,
    color="black"
)

res_keys=[]
res_rt=[]
data_dict=dict()

n_trials=20
rect_oris=np.tile(range(-45, 41, 5),n_trials)
rod_oris=np.tile(np.tile([-7, -4, -2, -1, 0, 1, 2, 4, 7],2), n_trials)
cnds_order=[ 4,  0,  3,  2,  3, 15,  8, 17, 11, 14, 13,  0, 11, 13,  2, 17,  5,10, 17,  8, 15, 15, 11,  4,  7, 12, 13, 10,  3, 16,  6,  0,  9,  5,11,  3,  3,  6,  7, 10,  7, 15,  9, 17, 13,  8,  6,  7, 14,  9,  0,13, 13, 12, 11, 17,  8,  5, 16,  1,  6,  0, 14, 12,  7,  8,  6, 12,5, 15,  4, 10,  1,  4, 15,  6, 17, 12,  5,  5, 12,  7,  9, 10,  9,3,  1, 11,  0,  4, 15, 15,  7, 14, 16, 14,  1,  6, 15, 15,  8,  6,16,  7, 15,  8,  1,  7, 16, 15,  3,  8,  0,  2, 17,  1, 17,  8,  5,13,  5,  9, 13, 14, 14,  8,  0,  1,  6,  5,  4, 16,  1,  0, 15, 16,6, 12, 12, 13, 14,  0, 15,  3,  7,  8, 13,  3,  4,  4,  0,  6, 16,9,  8,  7,  8, 15, 11,  0, 17, 16, 14,  3,  2, 13, 13,  3, 10,  0,11, 11,  6, 10,  8,  4, 17,  2, 10, 14,  4, 11, 10, 15,  9, 17,  4,5, 16, 14, 16, 10,  2,  5, 13, 17,  1,  4,  1,  4,  0, 16, 12, 15,6, 12, 11, 14,  9,  5,  7,  7,  3,  2, 16,  0,  8, 14, 13,  5, 17,17, 11,  4, 10, 17, 16,  0,  9,  7, 10, 12, 10,  1,  3, 17,  8, 16,7, 13,  1,  0, 10,  5,  4,  9,  2, 13,  1, 14, 15, 14,  9,  1,  7,9,  6, 14, 12, 13, 16,  1, 12,  1, 13, 10, 16,  2,  7,  9, 14,  4,14,  8, 11,  0, 12, 15, 12, 12,  8, 14,  3, 16, 13,  4, 10,  2,  1,3, 16, 16,  2,  6,  3,  9,  5,  3,  5,  4,  7,  2,  2,  5,  1,  0,4, 11, 10, 13,  9,  7,  7,  5, 14,  3,  6, 15, 11,  3, 12, 17, 17,10,  2, 17, 12,  1,  2, 12,  1,  6,  6, 11,  2,  9, 11,  5, 11, 11,6,  5,  8,  6, 10, 12, 17,  9,  4,  9,  3, 11,  2,  2,  2,  8,  9, 2,  0, 10]
# cnds_len=range(len(cnds_order))
cnds_len=[0, 1]
for k in cnds_len:
    line1=visual.Line(win,start=[0, 50], end=[0, -50], lineWidth=5, lineColor="White")
    line2=visual.Line(win,start=[-50, 0], end=[50, 0], lineWidth=5, lineColor="White")
    line1.draw()
    line2.draw()
    win.flip()
    core.wait(1)
    win.flip()
    core.wait(1)
    data_dict[str(k)]=dict()
    clock=core.Clock()
    rect=visual.Rect(win, width=200, height=200,fillColor="black", lineWidth=5, lineColor=[1, 1, 1], ori=rect_oris[cnds_order[k]] )
    rect.draw()
    
    win.flip()
    core.wait(2.5)
    rect=visual.Rect(win, width=200, height=200,fillColor="black", lineWidth=5, lineColor=[1, 1, 1], ori=rect_oris[cnds_order[k]] )
    rect.draw()
    line=visual.Line(win, lineWidth=5, start =[0, -80], end=[0, 80], lineColor="white", ori=rod_oris[cnds_order[k]])
    line.draw()
    clock=core.Clock()
    win.flip()
    core.wait(0.33)
    rect=visual.Rect(win, width=200, height=200,fillColor="black", lineWidth=5, lineColor=[1, 1, 1], ori=rect_oris[cnds_order[k]] )
    rect.draw()
    clock=core.Clock()
    win.flip()
    keys=event.waitKeys(keyList=['left', 'right', 'Esc'], timeStamped=clock)
    print(keys)
    if keys[0][0]=='Esc':

        shutdown()
    else:   
        res_keys.append(keys[0][0])
        res_rt.append(keys[0][1])
       
 
data_dict['keys_pressed']=res_keys
data_dict['RT']=res_rt
filename="results_RFT_"+sub+"_.mat"
savemat(filename, data_dict)
win.close()
   
   
    # %%

# %%
