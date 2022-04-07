#%%
sub='sub-26CR'

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
# rect_oris=range(-45, 41, 5)
# rod_oris=[-7, -4, -2, -1, 0, 1, 2, 4, 7]
rect_oris=[  -20, -15, -10, -5, 5,10, 15, 20]
rod_oris=[-7, -4, -2, -1, 1, 2, 4, 7]
rect_oriss=sorted(np.tile(rect_oris, len(rod_oris)))
rod_oriss=np.tile(rod_oris, len(rect_oris))


# cnds_order=shuffle(np.tile(range(162), 2))
# cnds_order=[15,  4,  1, 13, 14, 12, 10,  4, 12,  7, 16,  5, 11,  6,  3, 12, 17,6,  9, 14,  5, 11, 16,  4, 11,  2,  6, 10,  3,  3, 14, 14, 15,  0,9,  5,  7,  7, 14,  2,  9,  2,  2,  9,  5,  9, 10, 11,  8,  6,  8,7, 17,  7, 12, 17, 12,  8, 10, 14,  8, 16, 14, 13, 15,  1,  2,  0,13, 10, 17,  7, 17,  5, 11, 13, 11, 14,  9,  7,  9, 10,  5,  7,  7,4, 17,  7,  7,  3, 13, 16, 16, 17,  8,  0,  3, 17,  1, 17,  8, 14,8,  3,  1,  4, 16,  5,  4,  3, 11,  1, 13,  9,  3, 10,  5, 16, 17,15, 10,  2,  1, 10, 10, 11, 15,  4,  4,  4, 13,  4,  0,  1,  0,  7,6,  6, 17,  0,  4,  3,  2, 16, 15, 15, 10, 15,  6,  8, 11,  8,  6, 11,  1, 10, 15, 13,  9,  6, 14, 16, 12,  5, 15, 16,  9,  9,  1, 13, 11,  9,  6, 12,  0,  6, 17, 11,  8, 15, 12, 14,  5, 12, 12, 13, 13, 2,  1, 12,  5,  5,  0,  0,  0,  4,  2, 16,  6, 12,  2,  9,  1,  8, 5, 16, 15, 17,  8, 15,  2,  4,  1,  2, 14,  7,  8,  3,  3,  2,  3,11, 16,  3, 13,  0,  6, 14, 10,  1, 13, 12,  0,  0]
# cnds_order=[ 96,  11, 115,  22, 126,  24,  49,  47,  76, 110, 105,   2, 159,   17, 143,  82, 114, 150, 139, 141, 131,  63, 107,  91, 105,  16,   78, 159,  48, 148,  24, 147,  70,  57,  22,  80,  85,   1,  29,   54,  54,  53,   7, 134, 155,  71,  79,  23,  97, 138,  31,  23,  139,  59, 147,  73, 121,  21,  27, 145,   0, 118, 142, 137, 160,  72,  56,   5,  15,  88,  34,  46, 123,  47,  33, 136,  84,  82,  125,  99,  37,   4,  93,  57,  35, 121,  51,  93,  65, 155,  27, 111,  34,  61, 143,  41,  67, 131, 153,   9, 104, 106,  64, 100, 125, 124,  98,  95, 133,  37, 157, 113,  87, 108,  38, 134, 151,  152,  45, 128,  40, 119,  86,  35, 135,  77,  49, 117,  60,  38, 126,   8,  97,  51,  42, 127,  25,  21,  83,  84, 128,  75,  56,  13, 156,  55,  43, 138,  52, 142,  62, 108,  26, 127,  12, 149,   31, 112, 109, 152, 124,  64,  96,  74, 101,  88,  26,  52, 156,  116, 145,   4, 144,  99,   0,   1,  67,  62,  61,  86,  77, 118,  91,  73,  90, 122,  89,  50,  10, 137, 106,   7, 141,  87,  68,  92,  92,   3,  36, 103, 151,  14,   2,  28, 150,  89,  39, 109, 153,  25, 104,  15, 113,  13,  18,  63, 161,  80, 123, 122,  81, 154, 148,  69,  55, 129,  20,  59, 115,  60,  36,  75, 130, 100,    30,  18,  98,  44,  72,  39,  58,  41,  42, 161, 101, 117, 158, 90,  83, 111, 146, 132,  85, 102, 158, 146,  81,  71,  12,  40,  133, 119,  20,  43, 112,  53,  28,  32,   5,  46,  94, 135,  58, 9,  65, 136, 132,  66, 130,  33,  95, 107,   8,  76,  10, 114, 140,  29, 160,  19, 110, 140, 129, 120,  70, 103,  19, 157,   6, 11,  16,   3, 144,  30,  69,  68,  17,   6,  14,  45,  78,  44,66,  79, 116,  48,  32, 120,  94, 149,  74,  50, 102, 154]
# cnds_order=[0, 1, 2, 3]

# cnds_order=[40, 62, 20, 19, 39, 53, 20, 61,  4, 48,  9, 51, 49, 40, 29, 15, 12,
#        10, 39, 17, 10, 39, 32, 37, 59,  3, 63, 45, 28, 22,  5, 42, 58, 33,
#        23, 52, 60,  8, 53,  9, 21, 56, 52, 63, 63, 16, 48,  2, 34, 60, 30,
#         1, 55,  8, 30, 25, 38, 54,  6, 34, 37, 41, 46, 14,  6, 50, 12, 58,
#        26, 16, 37,  1,  4, 34, 10,  0, 56, 35, 42, 47, 45, 27, 41, 55, 48,
#        18, 29, 59, 32,  5, 10, 13, 30, 42, 39, 51,  4, 17, 47, 47, 12, 43,
#        47, 23, 44, 43, 26, 14, 35, 25, 49, 31, 50, 14, 40,  5, 32, 17, 34,
#        44, 37, 57, 45, 43, 31,  5, 15, 11, 61, 46, 38, 50, 21, 23, 34, 36,
#         8,  6, 11, 19, 20, 20,  9, 11, 38, 57, 62, 55, 37, 60, 59, 53, 35,
#        55, 31, 40, 56, 29, 62, 49, 48, 30,  3,  3, 39,  6,  5, 23,  7, 51,
#        40, 48, 47, 26, 19, 54, 53, 36, 51, 21, 18, 46, 22, 41, 57, 61, 54,
#        29, 59, 32, 32, 13, 22,  8, 44, 39, 24, 34, 52, 31, 51, 35, 19, 49,
#        26, 28, 53, 49, 14,  9, 56, 36, 49, 44, 12, 37, 40, 45,  0, 54, 57,
#        14, 48, 45,  1, 52, 63, 23, 55, 42,  0, 63, 26, 61,  4, 43, 13, 37,
#        31, 13,  0, 62, 11, 42, 53, 24, 13, 35, 18, 33, 12, 13, 29, 16, 62,
#        14, 41, 53, 52,  0,  6, 58, 59, 10, 38,  9, 42, 57,  3, 20, 33, 63,
#         1, 56, 56, 39, 18, 26,  3,  7, 53, 18, 39, 61, 21, 30, 10,  1, 29,
#        38,  5, 28,  5, 47, 41, 43, 63, 57, 39, 43, 48,  8, 44, 47, 43,  7,
#         7, 19, 37,  8, 11, 45,  9, 20, 21,  2, 33,  6, 13, 17,  3, 18, 46,
#         2, 58, 42, 24, 30,  7,  8,  8, 42, 34, 14,  6, 29, 60, 41, 52, 62,
#        38, 14,  4, 42, 21, 11, 19, 20, 15, 27, 27, 25, 30, 10, 59, 57, 16,
#        27, 56, 12, 50, 15, 15, 46, 35, 11, 35, 60, 17, 55, 49, 58, 32, 47,
#         6, 11, 23, 35, 13, 31, 50, 24, 22, 26, 55, 41, 50, 33, 31, 34, 44,
#        60, 15,  2, 58, 63, 28, 44, 55,  7, 50, 12, 40,  0, 61,  0, 46, 49,
#         4, 59, 27, 18, 25, 12, 22, 10, 57, 55, 61, 51, 35, 44, 32, 35, 52,
#        19, 17, 60, 28,  5, 17, 11, 49,  2,  3, 32, 42, 34, 32, 41, 54, 44,
#        56,  0, 25, 22,  9, 40, 47, 23,  9, 29, 58, 23,  0, 45, 43, 45, 51,
#        21, 48, 63, 36,  2, 19, 28, 30, 16, 14, 17, 57,  7, 54, 24,  5, 44,
#        24, 21, 10, 26, 18, 26, 36, 28, 33, 18, 38, 27, 52, 59, 15, 31, 16,
#         2, 38, 22, 49, 56, 26,  1, 54, 20, 52,  7,  3, 13, 18, 36,  2, 38,
#        62,  4,  8,  9,  4, 54, 30, 54, 45, 33, 33, 17, 21,  1, 29, 25, 19,
#        43, 16, 59, 54, 36, 52,  3, 41, 61, 12, 50,  6, 46, 25, 38, 48,  0,
#         9, 27,  8, 46, 19, 25, 36, 15, 31, 16,  2, 36, 50,  5,  7, 10, 48,
#        14, 21, 22, 28,  4, 28, 60, 47, 32, 28, 60, 46,  2, 37, 23,  6, 46,
#        16, 29, 17, 24, 11, 15, 24, 60, 27, 61, 16, 58, 51, 20, 24, 51, 22,
#        41, 58, 27, 61, 45, 53,  1, 62, 62,  3, 23,  4, 27, 63, 12,  7, 33,
#         1, 13, 62, 22, 53, 36, 55, 50, 15, 43, 51, 39, 59, 30, 40,  1, 25,
#        31, 33, 58, 37, 24, 40, 56, 57, 20, 34, 25]
# cnds_len=[0, 1]
# cnds_order=shuffle(np.tile(range(18), 13))
# cnds_order=[40, 62, 20, 19]
cnds_order=[59, 57, 49, 63,  4, 50, 15, 16, 54, 18, 43, 38,  6,  4, 20, 29, 42,27,  5,  4, 44, 35, 40, 28, 10,  6, 41, 48, 37, 12,  4, 33, 12, 48,4, 57, 56, 44, 14,  0, 18, 50, 21,  0, 35, 12, 23, 42, 36, 38,  9,3, 61, 15, 57,  2, 62, 40, 38, 26, 42, 34, 26, 63, 31, 62,  1, 44,30, 11, 41, 46, 39,  8, 39, 49, 19, 17, 23, 61, 12, 32, 34,  1, 36,58,  2, 27, 31, 56, 14, 11, 22, 49, 28, 11,  6, 30, 47, 15, 27, 63,0, 46, 20,  6, 37, 39,  1,  9,  9, 30,  2,  9, 43, 22, 31,  8, 60,5, 32,  2,  1, 63, 56, 34, 24, 58, 23, 48, 48, 13, 27, 53, 35, 23,19, 59, 46, 55, 24, 31, 32, 30, 47, 53, 62, 44, 15, 48, 31, 51, 10,30, 49, 51,  0, 58, 58, 34, 24, 22, 50, 23,  6,  4, 48, 17, 40, 62,58, 25, 31, 25, 12,  5,  9, 20, 55, 23, 28, 45, 29, 13, 24, 46, 33,2, 57,  5, 26,  3,  8,  9, 21, 27, 25, 43, 40,  7, 61, 24, 36,  2,50, 60, 48, 42, 35, 56, 54,  8, 28, 10,  1, 53, 43, 57, 38,  1, 47,35, 54, 59, 42, 22,  7, 35, 51, 25, 12, 45,  8, 58, 60, 27, 13, 18,34, 15, 55,  3, 43, 45, 55,  2, 38, 19, 41, 52, 26, 33,  7, 55, 29,22, 14, 26, 16, 10, 54, 10, 20,  6, 13, 17, 60, 31, 60, 43, 30,  7,52, 11, 54,  3, 29, 53, 51, 23, 37, 33, 26, 47, 21, 40, 14,  8, 61,11, 32, 36, 34, 16, 46, 25, 16,  5,  3, 30, 62, 32, 13,  8, 50, 38,25, 51, 10, 14, 29, 18, 19, 24, 19, 10, 17, 20, 61, 55, 13, 14,  4,16, 45, 62, 49, 54, 42, 44, 63, 34, 33, 35, 47, 52, 24, 39, 16, 51,0, 26, 15, 19, 37, 39, 52, 63, 27, 53, 58, 60, 11, 46, 14,  5, 28,19, 43, 20, 49, 52, 32, 40, 42, 57, 56,  5, 45, 59, 62, 36, 17,  6,0,  0, 47, 36, 61,  7, 50, 17, 18, 59, 61, 59, 51, 28, 49, 63,  7,33, 18, 56, 15, 39, 12, 21, 41, 16, 25, 56, 52, 32, 21, 52, 11, 53,22, 28, 37, 17, 60, 57, 40, 22, 59, 55, 38,  3, 44, 13, 45, 54, 45,47, 39, 36, 41, 21,  3, 41, 53, 18, 46, 29, 33,  7, 41, 37, 21, 44,20, 37, 50,  9,  1, 29]
# cnds_order=[40, 62, 20, 19]

cnds_len=range(len(cnds_order))
for k in cnds_len:
    if k==150 or k==300:
        text=visual.TextStim(win,height=50, text="Pause", color="white")
        text.draw()
        win.flip()
        event.waitKeys()
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
    rect=visual.Rect(win, width=200, height=200,fillColor="black", lineWidth=5, lineColor="Grey", ori=rect_oriss[cnds_order[k]] )
    rect.draw()
    
    win.flip()
    core.wait(2.5)
    rect=visual.Rect(win, width=200, height=200,fillColor="black", lineWidth=5, lineColor="Grey", ori=rect_oriss[cnds_order[k]] )
    rect.draw()
    line=visual.Line(win, lineWidth=5, start =[0, -80], end=[0, 80], lineColor="Grey", ori=rod_oriss[cnds_order[k]])
    line.draw()
    clock=core.Clock()
    win.flip()
    core.wait(0.33)
    rect=visual.Rect(win, width=200, height=200,fillColor="black", lineWidth=5, lineColor='Grey', ori=rect_oriss[cnds_order[k]] )
    rect.draw()
    clock=core.Clock()
    win.flip()
    keys=event.waitKeys(keyList=['left', 'right', 'escape'], timeStamped=clock)
    print(keys)
    if keys[0][0]=='escape':
        data_dict['keys_pressed']=res_keys
        data_dict['RT']=res_rt
        filename="results_RFT_"+sub+"_.mat"
        savemat(filename, data_dict)    
        win.close()
        core.quit()
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
