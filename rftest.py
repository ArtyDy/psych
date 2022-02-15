#%%

import psychopy
from psychopy import visual, core



win = psychopy.visual.Window(
    size=[400, 400],
    units="pix",
    fullscr=True,
    color=[0, 0, 0]
)

rect=visual.Rect(win, width=50, height=50,fillColor=[0, 0, 0], lineWidth=5, lineColor=[1, 1, 1] )
rect.draw()
win.flip()
core.wait(5)
win.close()
# %%
