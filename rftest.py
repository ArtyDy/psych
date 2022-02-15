#%%

import psychopy
from psychopy import visual, core



win = psychopy.visual.Window(
    size=[400, 400],
    units="pix",
    fullscr=True,
    color="black"
)

rect=visual.Rect(win, width=200, height=200,fillColor="black", lineWidth=5, lineColor=[1, 1, 1] )
rect.draw()
line=visual.Line(win, lineWidth=5, start =[0, -80], end=[0, 80], lineColor="white")
line.draw()
win.flip()
core.wait(5)
win.close()
  # %%
