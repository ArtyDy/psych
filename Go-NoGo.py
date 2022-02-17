#%%
from turtle import pos
import psychopy
from psychopy import visual, core, event
from scipy.io import savemat

# défini windows
win = psychopy.visual.Window(
    size=[400, 400],
    units="pix",
    fullscr=True,
    color="black"
)

#AFFICHAGE ECRAN NOIR
win.flip()
core.wait(0.5)

#affichage croix blanche
ligne=visual.Line(win, start=[-40,0], end=[40,0], lineColor="white", lineWidth=5)
ligne.draw()
ligne1=visual.Line(win, start=[0,-40], end=[0,40], lineColor="white", lineWidth=5)
ligne1.draw()

#AFFICHAGE ECRAN NOIR
win.flip()
core.wait(0.5)

#AFFICHAGE ECRAN NOIR
win.flip()
core.wait(0.3)

#affichage cercle bleu 

#affichage cercle rouge 

#AFFICHAGE V 100ms
win.flip()
core.wait(0.1)
win.close()

# %%
