#%%

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

ans=dict()
rect_oris=np.tile(range(-45, 41, 5),5)
rod_oris=np.tile(np.tile([-7, -4, -2, -1, 0, 1, 2, 4, 7],2), 5)
cnds_order=shuffle(np.tile(range(18), 5))
for k in cnds_order:
    rect=visual.Rect(win, width=200, height=200,fillColor="black", lineWidth=5, lineColor=[1, 1, 1], ori=rect_oris[cnds_order[k]] )
    rect.draw()
    line=visual.Line(win, lineWidth=5, start =[0, -80], end=[0, 80], lineColor="white", ori=rod_oris[cnds_order[k]])
    line.draw()
    win.flip()
    key=event.waitKeys(keyList=['left', 'right', 'esc'])
    if key=='esc':
        win.close()
    elif key=='left':
        ans[k]=key
    elif key=='right':
        ans[k]=key

savemat("results.mat", ans)
win.close()
   
   
    # %%
