#%%
import psychopy
from psychopy import visual, core


# défini windows
win = psychopy.visual.Window(
    size=[400, 400],
    units="pix",
    fullscr=True,
    color=[0, 0, 0]
)

#affichage croix
ligne=visual.Line(win, start=[-20,0], end=[20,0], lineColor=[1,1,1], lineWidth=5)
ligne.draw()
ligne2=visual.Line(win, start=[0,-20], end=[0,20], lineColor=[1,1,1], lineWidth=5)
ligne2.draw()

# affichage
win.flip()
core.wait(5)
win.close()

#affichage stimuli


# %%
