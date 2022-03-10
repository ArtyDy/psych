#%%
sub='sub-test'

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


# cnds_order=shuffle(np.tile(range(162), 2))
# cnds_order=[15,  4,  1, 13, 14, 12, 10,  4, 12,  7, 16,  5, 11,  6,  3, 12, 17,6,  9, 14,  5, 11, 16,  4, 11,  2,  6, 10,  3,  3, 14, 14, 15,  0,9,  5,  7,  7, 14,  2,  9,  2,  2,  9,  5,  9, 10, 11,  8,  6,  8,7, 17,  7, 12, 17, 12,  8, 10, 14,  8, 16, 14, 13, 15,  1,  2,  0,13, 10, 17,  7, 17,  5, 11, 13, 11, 14,  9,  7,  9, 10,  5,  7,  7,4, 17,  7,  7,  3, 13, 16, 16, 17,  8,  0,  3, 17,  1, 17,  8, 14,8,  3,  1,  4, 16,  5,  4,  3, 11,  1, 13,  9,  3, 10,  5, 16, 17,15, 10,  2,  1, 10, 10, 11, 15,  4,  4,  4, 13,  4,  0,  1,  0,  7,6,  6, 17,  0,  4,  3,  2, 16, 15, 15, 10, 15,  6,  8, 11,  8,  6, 11,  1, 10, 15, 13,  9,  6, 14, 16, 12,  5, 15, 16,  9,  9,  1, 13, 11,  9,  6, 12,  0,  6, 17, 11,  8, 15, 12, 14,  5, 12, 12, 13, 13, 2,  1, 12,  5,  5,  0,  0,  0,  4,  2, 16,  6, 12,  2,  9,  1,  8, 5, 16, 15, 17,  8, 15,  2,  4,  1,  2, 14,  7,  8,  3,  3,  2,  3,11, 16,  3, 13,  0,  6, 14, 10,  1, 13, 12,  0,  0]
cnds_order=[ 96,  11, 115,  22, 126,  24,  49,  47,  76, 110, 105,   2, 159,   17, 143,  82, 114, 150, 139, 141, 131,  63, 107,  91, 105,  16,   78, 159,  48, 148,  24, 147,  70,  57,  22,  80,  85,   1,  29,   54,  54,  53,   7, 134, 155,  71,  79,  23,  97, 138,  31,  23,  139,  59, 147,  73, 121,  21,  27, 145,   0, 118, 142, 137, 160,  72,  56,   5,  15,  88,  34,  46, 123,  47,  33, 136,  84,  82,  125,  99,  37,   4,  93,  57,  35, 121,  51,  93,  65, 155,  27, 111,  34,  61, 143,  41,  67, 131, 153,   9, 104, 106,  64, 100, 125, 124,  98,  95, 133,  37, 157, 113,  87, 108,  38, 134, 151,  152,  45, 128,  40, 119,  86,  35, 135,  77,  49, 117,  60,  38, 126,   8,  97,  51,  42, 127,  25,  21,  83,  84, 128,  75,  56,  13, 156,  55,  43, 138,  52, 142,  62, 108,  26, 127,  12, 149,   31, 112, 109, 152, 124,  64,  96,  74, 101,  88,  26,  52, 156,  116, 145,   4, 144,  99,   0,   1,  67,  62,  61,  86,  77, 118,  91,  73,  90, 122,  89,  50,  10, 137, 106,   7, 141,  87,  68,  92,  92,   3,  36, 103, 151,  14,   2,  28, 150,  89,  39, 109, 153,  25, 104,  15, 113,  13,  18,  63, 161,  80, 123, 122,  81, 154, 148,  69,  55, 129,  20,  59, 115,  60,  36,  75, 130, 100,    30,  18,  98,  44,  72,  39,  58,  41,  42, 161, 101, 117, 158, 90,  83, 111, 146, 132,  85, 102, 158, 146,  81,  71,  12,  40,  133, 119,  20,  43, 112,  53,  28,  32,   5,  46,  94, 135,  58, 9,  65, 136, 132,  66, 130,  33,  95, 107,   8,  76,  10, 114, 140,  29, 160,  19, 110, 140, 129, 120,  70, 103,  19, 157,   6, 11,  16,   3, 144,  30,  69,  68,  17,   6,  14,  45,  78,  44,66,  79, 116,  48,  32, 120,  94, 149,  74,  50, 102, 154]

cnds_len=range(len(cnds_order))

# cnds_len=[0, 1]
# cnds_order=shuffle(np.tile(range(18), 13))
for k in cnds_len[:5]:
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
