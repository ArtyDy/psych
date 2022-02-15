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

listecondition = ["GV","GF","DV","DF"]

for i in range (4):
    print(listecondition[i])
    k=listecondition[i]
    mouse=event.Mouse(win=win, visible=True, newPos=[0,0])
    if k == "GF":
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

        #affichage stimulus droit
        ligne.draw()
        ligne1.draw()
        rect.draw()
        rect1.draw()

        while(event.Mouse.getPressed('self')[0]!=1):
            ligne.draw()
            ligne1.draw()
            rect.draw()
            rect1.draw()
            etoile1=visual.Line(win, start=[325,0], end=[355,0], lineColor=[1,1,1], lineWidth=5)
            etoile1.draw()
            etoile2=visual.Line(win, start=[340,15], end=[340,-15], lineColor=[1,1,1], lineWidth=5)
            etoile2.draw()
            etoile3=visual.Line(win, start=[350,10], end=[330,-10], lineColor=[1,1,1], lineWidth=5)
            etoile3.draw()
            etoile4=visual.Line(win, start=[330,10], end=[350,-10], lineColor=[1,1,1], lineWidth=5)
            etoile4.draw()
            win.flip()
            pos.append([event.Mouse.getPos()[0],event.Mouse.getPos()[1]])

    if k == "DV":
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

        #affichage cue droite
        ligne.draw()
        ligne1.draw()
        rect.draw()
        rect1.draw()
        fleche=visual.Line(win, start=[120,0], end=[180,0], lineColor=[1,1,1], lineWidth=5)
        fleche.draw()
        fleche1=visual.Line(win, start=[180,0], end=[165,-10], lineColor=[1,1,1], lineWidth=5)
        fleche1.draw()
        fleche2=visual.Line(win, start=[180,0], end=[165,10], lineColor=[1,1,1], lineWidth=5)
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

        #affichage stimulus droit
        ligne.draw()
        ligne1.draw()
        rect.draw()
        rect1.draw()

        while(event.Mouse.getPressed('self')[0]!=1):
            ligne.draw()
            ligne1.draw()
            rect.draw()
            rect1.draw()
            etoile1=visual.Line(win, start=[325,0], end=[355,0], lineColor=[1,1,1], lineWidth=5)
            etoile1.draw()
            etoile2=visual.Line(win, start=[340,15], end=[340,-15], lineColor=[1,1,1], lineWidth=5)
            etoile2.draw()
            etoile3=visual.Line(win, start=[350,10], end=[330,-10], lineColor=[1,1,1], lineWidth=5)
            etoile3.draw()
            etoile4=visual.Line(win, start=[330,10], end=[350,-10], lineColor=[1,1,1], lineWidth=5)
            etoile4.draw()
            win.flip()
        

    if k == "DF":
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

        #affichage cue droite
        ligne.draw()
        ligne1.draw()
        rect.draw()
        rect1.draw()
        fleche=visual.Line(win, start=[120,0], end=[180,0], lineColor=[1,1,1], lineWidth=5)
        fleche.draw()
        fleche1=visual.Line(win, start=[180,0], end=[165,-10], lineColor=[1,1,1], lineWidth=5)
        fleche1.draw()
        fleche2=visual.Line(win, start=[180,0], end=[165,10], lineColor=[1,1,1], lineWidth=5)
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
            win.flip()
            
        win.close()


    if k == "GV":
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
        pos=[]
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
            win.flip()
        pos.append([event.Mouse.getPos('self')[0], event.Mouse.getPos('self')[1]])
    # AFFICHAGE STIMULUS
            
    # core.wait(0.3)


    #AFFICHAGE DELAI
    # ligne.draw()
    # ligne1.draw()
    # rect.draw()
    # rect1.draw()
    # win.flip()
    # core.wait(0.3)
    
win.close()

#%%
from turtle import pos
import psychopy
from psychopy import visual, core, event
import random

listecondition = ["GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GF","GF","GF","GF","GF","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DF","DF","DF","DF","DF"]
listerandom = ["GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GF","GF","GF","GF","GF","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DF","DF","DF","DF","DF"]
random.shuffle(listerandom)
print (listerandom)

#listecondition = ['DV', 'GV', 'GV', 'GV', 'GF', 'DV', 'GF', 'GF', 'GV', 'DV', 'DV', 'GV', 'GV', 'GV', 'GV', 'DV', 'DV', 'DF', 'GV', 'DF', 'GF', 'GV', 'DV', 'GV', 'DV', 'DF', 'DV', 'DV', 'GF', 'DV', 'DV', 'DF', 'DF', 'GV', 'GV', 'DV', 'DV', 'DV', 'GV', 'GV']
#%% droite faux

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

#affichage cue droite
ligne.draw()
ligne1.draw()
rect.draw()
rect1.draw()
fleche=visual.Line(win, start=[120,0], end=[180,0], lineColor=[1,1,1], lineWidth=5)
fleche.draw()
fleche1=visual.Line(win, start=[180,0], end=[165,-10], lineColor=[1,1,1], lineWidth=5)
fleche1.draw()
fleche2=visual.Line(win, start=[180,0], end=[165,10], lineColor=[1,1,1], lineWidth=5)
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
    win.flip()
    
win.close()




#%% droite vrai

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

#affichage cue droite
ligne.draw()
ligne1.draw()
rect.draw()
rect1.draw()
fleche=visual.Line(win, start=[120,0], end=[180,0], lineColor=[1,1,1], lineWidth=5)
fleche.draw()
fleche1=visual.Line(win, start=[180,0], end=[165,-10], lineColor=[1,1,1], lineWidth=5)
fleche1.draw()
fleche2=visual.Line(win, start=[180,0], end=[165,10], lineColor=[1,1,1], lineWidth=5)
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

#affichage stimulus droit
ligne.draw()
ligne1.draw()
rect.draw()
rect1.draw()

while(event.Mouse.getPressed('self')[0]!=1):
    ligne.draw()
    ligne1.draw()
    rect.draw()
    rect1.draw()
    etoile1=visual.Line(win, start=[325,0], end=[355,0], lineColor=[1,1,1], lineWidth=5)
    etoile1.draw()
    etoile2=visual.Line(win, start=[340,15], end=[340,-15], lineColor=[1,1,1], lineWidth=5)
    etoile2.draw()
    etoile3=visual.Line(win, start=[350,10], end=[330,-10], lineColor=[1,1,1], lineWidth=5)
    etoile3.draw()
    etoile4=visual.Line(win, start=[330,10], end=[350,-10], lineColor=[1,1,1], lineWidth=5)
    etoile4.draw()
    win.flip()
    
win.close()




# %% gauche faux
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
    win.flip()
    
win.close()







#%%
listecondition = ["GV","GF","DV","DF"]
listecondition
for i in range (4):
    k=1
    print ('a')
    print(listecondition[k])







# %% Copie base

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


#AFFICHAGE DELAI
ligne.draw()
ligne1.draw()
rect.draw()
rect1.draw()
win.flip()
core.wait(0.3)
win.close()
