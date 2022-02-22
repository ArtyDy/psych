#%%
sub='sub-04AM'

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
    color="black",
    screen=1
)

res_keys=[]
res_rt=[]
data_dict=dict()

n_trials=2
rect_oris=range(-45, 41, 5)
rod_oris=[-7, -4, -2, -1, 0, 1, 2, 4, 7]
rect_oriss=sorted(np.tile(rect_oris, len(rod_oris)))
rod_oriss=np.tile(rod_oris, len(rect_oris))


cnds_order=shuffle(np.tile(range(162), 2))
# cnds_order=[15,  4,  1, 13, 14, 12, 10,  4, 12,  7, 16,  5, 11,  6,  3, 12, 17,6,  9, 14,  5, 11, 16,  4, 11,  2,  6, 10,  3,  3, 14, 14, 15,  0,9,  5,  7,  7, 14,  2,  9,  2,  2,  9,  5,  9, 10, 11,  8,  6,  8,7, 17,  7, 12, 17, 12,  8, 10, 14,  8, 16, 14, 13, 15,  1,  2,  0,13, 10, 17,  7, 17,  5, 11, 13, 11, 14,  9,  7,  9, 10,  5,  7,  7,4, 17,  7,  7,  3, 13, 16, 16, 17,  8,  0,  3, 17,  1, 17,  8, 14,8,  3,  1,  4, 16,  5,  4,  3, 11,  1, 13,  9,  3, 10,  5, 16, 17,15, 10,  2,  1, 10, 10, 11, 15,  4,  4,  4, 13,  4,  0,  1,  0,  7,6,  6, 17,  0,  4,  3,  2, 16, 15, 15, 10, 15,  6,  8, 11,  8,  6, 11,  1, 10, 15, 13,  9,  6, 14, 16, 12,  5, 15, 16,  9,  9,  1, 13, 11,  9,  6, 12,  0,  6, 17, 11,  8, 15, 12, 14,  5, 12, 12, 13, 13, 2,  1, 12,  5,  5,  0,  0,  0,  4,  2, 16,  6, 12,  2,  9,  1,  8, 5, 16, 15, 17,  8, 15,  2,  4,  1,  2, 14,  7,  8,  3,  3,  2,  3,11, 16,  3, 13,  0,  6, 14, 10,  1, 13, 12,  0,  0]
cnds_len=range(len(cnds_order))

# cnds_len=[0, 1]
# cnds_order=shuffle(np.tile(range(18), 13))
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
    rect=visual.Rect(win, width=200, height=200,fillColor="black", lineWidth=5, lineColor=[1, 1, 1], ori=rect_oriss[cnds_order[k]] )
    rect.draw()
    
    win.flip()
    core.wait(2.5)
    rect=visual.Rect(win, width=200, height=200,fillColor="black", lineWidth=5, lineColor=[1, 1, 1], ori=rect_oriss[cnds_order[k]] )
    rect.draw()
    line=visual.Line(win, lineWidth=5, start =[0, -80], end=[0, 80], lineColor="white", ori=rod_oriss[cnds_order[k]])
    line.draw()
    clock=core.Clock()
    win.flip()
    core.wait(0.33)
    rect=visual.Rect(win, width=200, height=200,fillColor="black", lineWidth=5, lineColor=[1, 1, 1], ori=rect_oriss[cnds_order[k]] )
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
