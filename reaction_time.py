#%%
from turtle import pos
import psychopy
from psychopy import visual, core, event


# défini windows
win = psychopy.visual.Window(
    size=[400, 400],
    units="pix",
    fullscr=True,
    color="black"
)

#affichage croix rouge
ligne=visual.Line(win, start=[-40,0], end=[40,0], lineColor="red", lineWidth=5)
ligne.draw()
ligne1=visual.Line(win, start=[0,-40], end=[0,40], lineColor="red", lineWidth=5)
ligne1.draw()

#affichage carré gauche
rect=visual.Rect(win, width=100, height=100,fillColor="black", lineWidth=5, lineColor=[1, 1, 1],pos=[-340,0] )
rect.draw()

#affichage carré droit
rect1=visual.Rect(win, width=100, height=100,fillColor="black", lineWidth=5, lineColor=[1, 1, 1],pos=[340,0] )
rect1.draw()

# AFFICHAGE BASE ROUGE
win.flip()
core.wait(0.8)

#affichage croix verte
ligne=visual.Line(win, start=[-40,0], end=[40,0], lineColor="green", lineWidth=5)
ligne.draw()
ligne1=visual.Line(win, start=[0,-40], end=[0,40], lineColor="green", lineWidth=5)
ligne1.draw()
rect.draw()
rect1.draw()

# AFFICHAGE BASE VERTE
win.flip()
core.wait(0.8)

#affichage cue gauche
ligne.draw()
ligne1.draw()
rect.draw()
rect1.draw()
fleche=visual.Line(win, start=[-120,0], end=[-180,0], lineColor=[1,1,1], lineWidth=5)
fleche.draw()
fleche1=visual.Line(win, start=[-180,0], end=[-165,-10], lineColor=[1,1,1], lineWidth=5)
fleche1.draw()
fleche2=visual.Line(win, start=[-180,0], end=[-165,10], lineColor=[1,1,1], lineWidth=5)
fleche2.draw()

#AFFICHAGE CUE
win.flip()
core.wait(2.36)

#AFFICHAGE BASE VERTE DELAI
ligne.draw()
ligne1.draw()
rect.draw()
rect1.draw()
win.flip()
core.wait(1.5)

#affichage stimulus gauche
ligne.draw()
ligne1.draw()
rect.draw()
rect1.draw()

while(event.Mouse.getPressed('self')[0]!=1):
    ligne.draw()
    ligne1.draw()
    rect.draw()
    rect1.draw()
    etoile1=visual.Line(win, start=[-325,0], end=[-355,0], lineColor=[1,1,1], lineWidth=5)
    etoile1.draw()
    etoile2=visual.Line(win, start=[-340,15], end=[-340,-15], lineColor=[1,1,1], lineWidth=5)
    etoile2.draw()
    etoile3=visual.Line(win, start=[-350,10], end=[-330,-10], lineColor=[1,1,1], lineWidth=5)
    etoile3.draw()
    etoile4=visual.Line(win, start=[-330,10], end=[-350,-10], lineColor=[1,1,1], lineWidth=5)
    etoile4.draw()

# AFFICHAGE STIMULUS
    win.flip()
# core.wait(0.3)

# buttons = event.mouse.getPressed()
# while buttons== [0, 0, 0]:
#     buttons = event.mouse.getPressed()
#     if buttons == [1, 0, 0]:
#         break
#AFFICHAGE DELAI
ligne.draw()
ligne1.draw()
rect.draw()
rect1.draw()
win.flip()
core.wait(0.3)
win.close()


# %%
#affichage cue gauche
fleche=visual.Line(win, start=[50,0], end=[90,0], lineColor=[1,1,1], lineWidth=5)
fleche.draw()
fleche1=visual.Line(win, start=[90,0], end=[80,-10], lineColor=[1,1,1], lineWidth=5)
fleche1.draw()
fleche2=visual.Line(win, start=[90,0], end=[80,10], lineColor=[1,1,1], lineWidth=5)
fleche2.draw()