#%%
from turtle import pos
import psychopy
from psychopy import visual, core, event
from scipy.io import savemat
import random
from pathlib import Path

sub='sub-test'
dir ="/" + sub
Path(dir).mkdir(parents=True, exist_ok=True)

# défini windows
win = psychopy.visual.Window(
    size=[400, 400],
    units="pix",
    fullscr=True,
    color="black",
    screen=1
)
clock=core.Clock()
#AFFICHAGE ECRAN NOIR
win.flip()
core.wait(0.5)

#définition cercle bleu 
cbleu=visual.Circle(win, radius=50, edges=32, units='', lineWidth=2.5, lineColor='aqua', lineColorSpace='aqua',fillColor='aqua', fillColorSpace=None)
cbleuhaut=visual.Circle(win, radius=50, edges=32, units='', lineWidth=2.5, lineColor='aqua', lineColorSpace='aqua',fillColor='aqua', fillColorSpace=None, pos=[0,300])
cbleubas=visual.Circle(win, radius=50, edges=32, units='', lineWidth=2.5, lineColor='aqua', lineColorSpace='aqua',fillColor='aqua', fillColorSpace=None, pos=[0,-300])
cbleugauche=visual.Circle(win, radius=50, edges=32, units='', lineWidth=2.5, lineColor='aqua', lineColorSpace='aqua',fillColor='aqua', fillColorSpace=None, pos=[-300,0])
cbleudroite=visual.Circle(win, radius=50, edges=32, units='', lineWidth=2.5, lineColor='aqua', lineColorSpace='aqua',fillColor='aqua', fillColorSpace=None, pos=[300,0])


#définition cercle rouge
crouge=visual.Circle(win, radius=50, edges=32, units='', lineWidth=2.5, lineColor='red', lineColorSpace='red',fillColor='red', fillColorSpace=None)
crougehaut=visual.Circle(win, radius=50, edges=32, units='', lineWidth=2.5, lineColor='red', lineColorSpace='red',fillColor='red', fillColorSpace=None, pos=[0,300])
crougebas=visual.Circle(win, radius=50, edges=32, units='', lineWidth=2.5, lineColor='red', lineColorSpace='red',fillColor='red', fillColorSpace=None, pos=[0,-300])
crougegauche=visual.Circle(win, radius=50, edges=32, units='', lineWidth=2.5, lineColor='red', lineColorSpace='red',fillColor='red', fillColorSpace=None, pos=[-300,0])
crougedroite=visual.Circle(win, radius=50, edges=32, units='', lineWidth=2.5, lineColor='red', lineColorSpace='red',fillColor='red', fillColorSpace=None, pos=[300,0])

#définition des carrés
rect=visual.Rect(win, width=100, height=100, lineWidth=5, lineColor=[1, 1, 1],pos=[-300,0] )
rect1=visual.Rect(win, width=100, height=100, lineWidth=5, lineColor=[1, 1, 1],pos=[300,0] )
rect2=visual.Rect(win, width=100, height=100, lineWidth=5, lineColor=[1, 1, 1],pos=[0,300] )
rect3=visual.Rect(win, width=100, height=100, lineWidth=5, lineColor=[1, 1, 1],pos=[0,-300] )
listecondition=['GG']
# listecondition=['GG','GD','GH','GB','NGG','NGD','NGH','NGB','CG','CD','CH','CB']

# listecondition=['NG', 'NG', 'G', 'NG', 'G', 'G', 'NG', 'NG', 'C', 'G', 'G', 'C', 'C', 'C', 'G', 'C', 'NG', 'C', 'G', 'NG', 'C', 'NG', 'G', 'C', 'G', 'C', 'C', 'G', 'G', 'NG', 'NG', 'NG', 'G', 'C', 'C', 'NG', 'NG', 'G', 'NG', 'NG', 'G', 'NG', 'C', 'C', 'G', 'C', 'C', 'C', 'G', 'C', 'G', 'NG', 'C', 'G', 'G', 'NG', 'C', 'C', 'G', 'G', 'G', 'C', 'C', 'NG', 'C', 'NG', 'C', 'NG', 'G', 'C', 'NG', 'NG', 'NG', 'NG', 'G', 'C', 'NG', 'G', 'NG', 'NG', 'G', 'G', 'NG', 'G', 'C', 'C', 'NG', 'C', 'NG', 'G', 'G', 'NG', 'G', 'C', 'G', 'NG', 'C', 'NG', 'C', 'G', 'C', 'C', 'C', 'G', 'NG', 'G', 'G', 'G', 'NG', 'C', 'NG', 'NG', 'C', 'C', 'G', 'NG', 'C', 'G', 'C', 'NG', 'G', 'C', 'NG', 'G', 'NG', 'C', 'C', 'G', 'NG', 'NG', 'G', 'C', 'G', 'NG', 'G']

# listecondition = ['C', 'NG', 'G', 'G', 'C', 'NG', 'NG', 'NG', 'NG', 'G', 'G', 'C', 'G', 'NG', 'G', 'C', 'C', 'NG', 'G', 'G', 'G', 'NG', 'G', 'C', 'C', 'NG', 'C', 'C', 'C', 'NG', 'C', 'NG', 'C', 'NG', 'G', 'NG', 'C', 'NG', 'C', 'C', 'NG', 'G', 'G', 'C', 'C', 'C', 'G', 'G', 'NG', 'NG', 'C', 'NG', 'C', 'C', 'G', 'C', 'C', 'NG', 'C', 'G', 'NG', 'C', 'G', 'G', 'NG', 'NG', 'G', 'G', 'G', 'C', 'C', 'C', 'NG', 'NG', 'NG', 'G', 'G', 'NG', 'NG', 'G', 'NG', 'C', 'NG', 'G', 'G', 'G', 'C', 'NG', 'G', 'G']
# listecondition = ['NG', 'C', 'G', 'C', 'C', 'NG', 'NG', 'G', 'NG', 'G', 'NG', 'G', 'G', 'C', 'NG', 'G', 'NG', 'C', 'C', 'G', 'G', 'C', 'NG', 'C', 'C', 'G', 'C', 'NG', 'C', 'C', 'G', 'G', 'C', 'G', 'NG', 'C', 'NG', 'C', 'G', 'G', 'NG', 'G', 'NG', 'C', 'NG', 'C', 'NG', 'NG', 'G', 'NG', 'G', 'G', 'G', 'G', 'NG', 'NG', 'C', 'NG', 'C', 'G', 'NG', 'G', 'C', 'G', 'G', 'C', 'C', 'NG', 'C', 'NG', 'C', 'C', 'G', 'C', 'G', 'NG', 'C', 'NG', 'NG', 'NG', 'NG', 'C', 'G', 'G', 'C', 'NG', 'C', 'G', 'NG', 'G']
#listecondition=['G', 'NG', 'G', 'NG', 'NG', 'C', 'G', 'G', 'NG', 'G', 'C', 'NG','NG', 'G', 'NG', 'C', 'C', 'G', 'G', 'NG', 'C', 'G', 'G', 'NG','NG', 'G', 'G', 'C', 'C', 'C', 'C', 'G', 'G', 'G', 'NG', 'G', 'C','G', 'G', 'C', 'G', 'NG', 'NG', 'NG', 'C', 'NG', 'C', 'G', 'G','C', 'C', 'C', 'NG', 'G', 'NG', 'C', 'C', 'C', 'G', 'C', 'NG', 'C','G', 'C', 'NG', 'G', 'NG', 'C', 'C', 'NG', 'C', 'C', 'G', 'NG',

listespace=[]
keyss=[]

for i in range (1): #180
    print(i)
    print(listecondition[i])
    k=listecondition[i]

    #initialisation sourie pas visible
    #mouse=event.Mouse(win=win, visible=False, newPos=[0,-350])
    mouse=event.Mouse(win=win, visible=False, newPos=[0,-350])
    
    rect.draw()
    rect1.draw()
    rect2.draw()
    rect3.draw()
    win.flip()
    core.wait(2)

    #affichage croix blanche
    ligne=visual.Line(win, start=[-40,0], end=[40,0], lineColor="white", lineWidth=5)
    ligne1=visual.Line(win, start=[0,-40], end=[0,40], lineColor="white", lineWidth=5)
    ligne.draw()
    ligne1.draw()
    rect.draw()
    rect1.draw()
    rect2.draw()
    rect3.draw()
    win.flip()
    core.wait(2)
    rect.draw()
    rect1.draw()
    rect2.draw()
    rect3.draw()
    win.flip()
    core.wait(0.2)

    #GO-NO-GO

    if k == 'GG' or 'GD' or 'GH' or 'GB' or 'NGG' or 'NGD' or 'NGH' or 'NGB' or 'CG' or 'CD' or 'CH' or 'CB':
        
        #AFFICHAGE CONDITION GO B-B-B-B
        if k== 'CG' or 'CD' or 'CH' or 'CB':
            c=crouge
        else :
            c=cbleu
        
        c.draw()
        rect.draw()
        rect1.draw()
        rect2.draw()
        rect3.draw()
        win.flip()
        core.wait(0.8)
        rect.draw()
        rect1.draw()
        rect2.draw()
        rect3.draw()
        win.flip()
        core.wait(0.2)

        c.draw()
        rect.draw()
        rect1.draw()
        rect2.draw()
        rect3.draw()
        win.flip()
        core.wait(0.8)
        rect.draw()
        rect1.draw()
        rect2.draw()
        rect3.draw()
        win.flip()
        core.wait(0.2)

        c.draw()
        rect.draw()
        rect1.draw()
        rect2.draw()
        rect3.draw()
        win.flip()
        core.wait(0.8)
        rect.draw()
        rect1.draw()
        rect2.draw()
        rect3.draw()
        win.flip()
        core.wait(0.2)
    
        clock=core.Clock()
        g=0
        keys=[]

        while g!=60:
            if g<=48:
                if k == 'GH':
                    cbleuhaut.draw()
                if k == 'GB' :
                    cbleubas.draw()
                if k == 'GG':
                    cbleugauche.draw()
                if k == 'GD':
                    cbleudroite.draw()
                if k == 'NGD':
                    crougedroite.draw()
                if k == 'NGG':
                    crougegauche.draw()
                if k == 'NGH':
                    crougehaut.draw()
                if k == 'NGB':
                    crougebas.draw()
                if k == 'CD':
                    crougedroite.draw()
                if k == 'CG':
                    crougegauche.draw()
                if k == 'CH':
                    crougehaut.draw()
                if k == 'CB':
                    crougebas.draw()
            rect.draw()
            rect1.draw()
            rect2.draw()
            rect3.draw() 
            win.flip()
            g=g+1
            ke=event.getKeys(keyList=['space'], timeStamped=clock)
            if ke != []:
                keys.append(ke)
            # else:
            #     keys.append([])
        
        keyss.append(keys) 
        # listespace.append(ke)

        rect.draw()
        rect1.draw()
        rect2.draw()
        rect3.draw()
        win.flip()
        core.wait(0.2)

        # listespace.append(ke)
        # results=dict()
        # filename="results_gng_"+ sub + "_" + str('%02d' % i) + ".mat"
        # savemat(filename, results)

    # if k == 'C':
    #     #AFFICHAGE CONDITION CONTROLE R-R-R-R
    #     crouge.draw()
    #     rect.draw()
    #     rect1.draw()
    #     rect2.draw()
    #     rect3.draw()
    #     win.flip()
    #     core.wait(0.8)
    #     rect.draw()
    #     rect1.draw()
    #     rect2.draw()
    #     rect3.draw()
    #     win.flip()
    #     core.wait(0.2)

    #     crouge.draw()
    #     rect.draw()
    #     rect1.draw()
    #     rect2.draw()
    #     rect3.draw()
    #     win.flip()
    #     core.wait(0.8)
    #     rect.draw()
    #     rect1.draw()
    #     rect2.draw()
    #     rect3.draw()
    #     win.flip()
    #     core.wait(0.2)

    #     crouge.draw()
    #     rect.draw()
    #     rect1.draw()
    #     rect2.draw()
    #     rect3.draw()
    #     win.flip()
    #     core.wait(0.8)
    #     rect.draw()
    #     rect1.draw()
    #     rect2.draw()
    #     rect3.draw()
    #     win.flip()
    #     core.wait(0.2)
       
    #     clock=core.Clock()
    #     g=0
    #     keys=[]
    #     while g!=60:
    #         if g<=48:
    #             crouge.draw()
    #         rect.draw()
    #         rect1.draw()
    #         rect2.draw()
    #         rect3.draw() 
    #         win.flip()
    #         g=g+1
    #         ke=event.getKeys(keyList=['space'], timeStamped=clock)
    #         if ke != []:
    #             keys.append(ke)
    #         # else:
    #         #     keys.append([])
        
    #     keyss.append(keys) 


    #     rect.draw()
    #     rect1.draw()
    #     rect2.draw()
    #     rect3.draw()
    #     win.flip()
    #     core.wait(0.2)

    #     # results=dict()
        # filename="results_gng_"+ sub + "_" + str('%02d' % i) + ".mat"
        # savemat(filename, results)

    # if k == 'NG':
    #     #AFFICHAGE CONDITION NO GO B-B-B-R
    #     cbleu.draw()
    #     rect.draw()
    #     rect1.draw()
    #     rect2.draw()
    #     rect3.draw()
    #     win.flip()
    #     core.wait(0.8)
    #     rect.draw()
    #     rect1.draw()
    #     rect2.draw()
    #     rect3.draw()
    #     win.flip()
    #     core.wait(0.2)

    #     cbleu.draw()
    #     rect.draw()
    #     rect1.draw()
    #     rect2.draw()
    #     rect3.draw()
    #     win.flip()
    #     core.wait(0.8)
    #     rect.draw()
    #     rect1.draw()
    #     rect2.draw()
    #     rect3.draw()
    #     win.flip()
    #     core.wait(0.2)

    #     cbleu.draw()
    #     rect.draw()
    #     rect1.draw()
    #     rect2.draw()
    #     rect3.draw()
    #     win.flip()
    #     core.wait(0.8)
    #     rect.draw()
    #     rect1.draw()
    #     rect2.draw()
    #     rect3.draw()
    #     win.flip()
    #     core.wait(0.2)

    #     clock=core.Clock()
    #     g=0
    #     keys=[]
    #     while g!=60:
    #         if g<=48:
    #             crouge.draw()
    #         rect.draw()
    #         rect1.draw()
    #         rect2.draw()
    #         rect3.draw() 
    #         win.flip()
    #         g=g+1
    #         ke=event.getKeys(keyList=['space'], timeStamped=clock)
    #         if ke != []:
    #             keys.append(ke)
    #         # else:
    #         #  keys.append([])
        
    #     keyss.append(keys) 

    #     rect.draw()
    #     rect1.draw()
    #     rect2.draw()
    #     rect3.draw()
    #     win.flip()
    #     core.wait(0.2)

        
            
    #     #     results['Pos']=pos[k]
        #     results['Buttons']=buttonss[k]
        #     results['Times']=timess[k]
        
dicto=dict({sub:keyss})
filename="results_gng_"+ sub + ".mat"
savemat(filename, dicto)


#AFFICHAGE FIN
win.close()



 #%%


#%%
# TEST

from turtle import pos
import psychopy
from psychopy import visual, core, event
from scipy.io import savemat
import random
from pathlib import Path

sub='sub-test'
dir ="/" + sub
Path(dir).mkdir(parents=True, exist_ok=True)
# défini windows
win = psychopy.visual.Window(
    size=[400, 400],
    units="pix",
    fullscr=True,
    color="black",

    screen=1
)
clock=core.Clock()
win.flip()
ke=event.getKeys(keyList=['space'], timeStamped=clock)
print(ke)
core.wait(5)
win.close()





# %%
import random

#listecondition = ["C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG"]
#listerandom = ["C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG"]
#listecondition = ['C', 'NG', 'G', 'G', 'C', 'NG', 'NG', 'NG', 'NG', 'G', 'G', 'C', 'G', 'NG', 'G', 'C', 'C', 'NG', 'G', 'G', 'G', 'NG', 'G', 'C', 'C', 'NG', 'C', 'C', 'C', 'NG', 'C', 'NG', 'C', 'NG', 'G', 'NG', 'C', 'NG', 'C', 'C', 'NG', 'G', 'G', 'C', 'C', 'C', 'G', 'G', 'NG', 'NG', 'C', 'NG', 'C', 'C', 'G', 'C', 'C', 'NG', 'C', 'G', 'NG', 'C', 'G', 'G', 'NG', 'NG', 'G', 'G', 'G', 'C', 'C', 'C', 'NG', 'NG', 'NG', 'G', 'G', 'NG', 'NG', 'G', 'NG', 'C', 'NG', 'G', 'G', 'G', 'C', 'NG', 'G', 'G']
#listecondition=['G', 'G', 'C', 'NG', 'C', 'C', 'NG', 'G', 'NG', 'G', 'G', 'NG', 'C', 'NG', 'C', 'C', 'NG', 'NG', 'C', 'C', 'G', 'C', 'C', 'C', 'G', 'NG', 'G', 'G', 'NG', 'NG', 'G', 'NG', 'G', 'C', 'NG', 'G', 'G', 'NG', 'C', 'NG', 'C', 'G', 'C', 'NG', 'C', 'C', 'G', 'C', 'C', 'G', 'NG', 'NG', 'C', 'G', 'NG', 'G', 'NG', 'C', 'C', 'G', 'NG', 'G', 'C', 'C', 'G', 'C', 'G', 'NG', 'NG', 'C', 'C', 'G', 'NG', 'NG', 'G', 'C', 'G', 'G', 'NG', 'NG', 'NG', 'G', 'C', 'G', 'C', 'G', 'NG', 'G', 'NG', 'NG']
# listecondition=['C', 'NG', 'C', 'NG', 'NG', 'C', 'C', 'NG', 'C', 'C', 'NG', 'NG', 'C', 'G', 'NG', 'NG', 'NG', 'NG', 'C', 'G', 'NG', 'C', 'C', 'C', 'G', 'NG', 'C', 'G', 'G', 'C', 'NG', 'NG', 'C', 'NG', 'NG', 'C', 'G', 'NG', 'NG', 'G', 'G', 'G', 'NG', 'NG', 'G', 'C', 'NG', 'NG', 'NG', 'NG', 'G', 'C', 'C', 'G', 'C', 'C', 'C', 'C', 'G', 'C', 'NG', 'C', 'G', 'NG', 'C', 'G', 'C', 'G', 'G', 'NG', 'C', 'C', 'G', 'G', 'NG', 'G', 'G', 'NG', 'C', 'C', 'G', 'G', 'G', 'G', 'NG', 'G', 'G', 'G', 'G', 'G']

# listecondition=['NG','G','C','NG','G','C','NG','G','C','NG','G','C','NG','G','C','NG','G','C','NG','G','C','NG','G','C','NG','G','C','NG','G','C','NG','G','C','NG','G','C','NG','G','C','NG','G','C','NG','G','C','NG','G','C','NG','G','C','NG','G','C','NG','G','C','NG','G','C','NG','G','C','NG','G','C','NG','G','C','NG','G','C','NG','G','C','NG','G','C','NG','G','C','NG','G','C','NG','G','C','NG','G','C','NG','G','C','NG','G','C','NG','G','C','NG','G','C','NG','G','C','NG','G','C','NG','G','C','NG','G','C','NG','G','C','NG','G','C','NG','G','C','NG','G','C','NG','G','C','NG','G','C','NG','G','C',]
# random.shuffle(listecondition)
# print (listecondition)

#listecondition = ['C', 'NG', 'G', 'G', 'C', 'NG', 'NG', 'NG', 'NG', 'G', 'G', 'C', 'G', 'NG', 'G', 'C', 'C', 'NG', 'G', 'G', 'G', 'NG', 'G', 'C', 'C', 'NG', 'C', 'C', 'C', 'NG', 'C', 'NG', 'C', 'NG', 'G', 'NG', 'C', 'NG', 'C', 'C', 'NG', 'G', 'G', 'C', 'C', 'C', 'G', 'G', 'NG', 'NG', 'C', 'NG', 'C', 'C', 'G', 'C', 'C', 'NG', 'C', 'G', 'NG', 'C', 'G', 'G', 'NG', 'NG', 'G', 'G', 'G', 'C', 'C', 'C', 'NG', 'NG', 'NG', 'G', 'G', 'NG', 'NG', 'G', 'NG', 'C', 'NG', 'G', 'G', 'G', 'C', 'NG', 'G', 'G']
listeshuffle=['NG', 'NG', 'G', 'NG', 'G', 'G', 'NG', 'NG', 'C', 'G', 'G', 'C', 'C', 'C', 'G', 'C', 'NG', 'C', 'G', 'NG', 'C', 'NG', 'G', 'C', 'G', 'C', 'C', 'G', 'G', 'NG', 'NG', 'NG', 'G', 'C', 'C', 'NG', 'NG', 'G', 'NG', 'NG', 'G', 'NG', 'C', 'C', 'G', 'C', 'C', 'C', 'G', 'C', 'G', 'NG', 'C', 'G', 'G', 'NG', 'C', 'C', 'G', 'G', 'G', 'C', 'C', 'NG', 'C', 'NG', 'C', 'NG', 'G', 'C', 'NG', 'NG', 'NG', 'NG', 'G', 'C', 'NG', 'G', 'NG', 'NG', 'G', 'G', 'NG', 'G', 'C', 'C', 'NG', 'C', 'NG', 'G', 'G', 'NG', 'G', 'C', 'G', 'NG', 'C', 'NG', 'C', 'G', 'C', 'C', 'C', 'G', 'NG', 'G', 'G', 'G', 'NG', 'C', 'NG', 'NG', 'C', 'C', 'G', 'NG', 'C', 'G', 'C', 'NG', 'G', 'C', 'NG', 'G', 'NG', 'C', 'C', 'G', 'NG', 'NG', 'G', 'C', 'G', 'NG', 'G']
print(len(listeshuffle))



# %%

# %%
