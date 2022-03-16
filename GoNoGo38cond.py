#%%

from turtle import pos
import psychopy
from psychopy import visual, core, event
from psychopy.hardware import keyboard
from scipy.io import savemat
import random
from pathlib import Path
import os

kb=keyboard.Keyboard()
sub='sub-test'
# dir ="/" + sub
# Path(dir).mkdir(parents=True, exist_ok=True)

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
cbleu=visual.Circle(win, radius=50, edges=32, units='', lineWidth=2.5, lineColor='green', lineColorSpace='green',fillColor='green', fillColorSpace=None)
cbleuhaut=visual.Circle(win, radius=50, edges=32, units='', lineWidth=2.5, lineColor='green', lineColorSpace='green',fillColor='green', fillColorSpace=None, pos=[0,300])
cbleubas=visual.Circle(win, radius=50, edges=32, units='', lineWidth=2.5, lineColor='green', lineColorSpace='green',fillColor='green', fillColorSpace=None, pos=[0,-300])
cbleugauche=visual.Circle(win, radius=50, edges=32, units='', lineWidth=2.5, lineColor='green', lineColorSpace='green',fillColor='green', fillColorSpace=None, pos=[-300,0])
cbleudroite=visual.Circle(win, radius=50, edges=32, units='', lineWidth=2.5, lineColor='green', lineColorSpace='green',fillColor='green', fillColorSpace=None, pos=[300,0])


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

# listecondition=['GG', 'GD', 'NGB', 'GG', 'NGG', 'GG', 'NGD', 'GH', 'NGB', 'GH', 'NGG', 'GH', 'NGH', 'GB', 'GH', 'GG', 'NGB', 'GB', 'NGH', 'GD', 'NGH', 'GH', 'NGH', 'NGG', 'GD', 'GD', 'GG', 'GG', 'NGG', 'GH', 'GD', 'GD', 'NGD', 'NGD', 'GH', 'NGB', 'NGB', 'NGG', 'NGB', 'NGB', 'GB', 'NGH', 'NGH', 'GG', 'GD', 'NGG', 'NGG', 'GB', 'NGB', 'NGH', 'NGG', 'NGB', 'NGD', 'NGG', 'GB', 'GH', 'NGD', 'GG', 'NGH', 'GG', 'NGB', 'NGB', 'GB', 'GG', 'NGB', 'GB', 'GH', 'GG', 'GH', 'NGD', 'GG', 'NGD', 'GD', 'GH', 'NGH', 'GG', 'NGH', 'NGD', 'NGD', 'NGG', 'NGD', 'GG', 'GH', 'GH', 'NGD', 'GD', 'NGG', 'NGH', 'GB', 'NGB', 'NGD', 'NGG', 'GB', 'NGG', 'NGD', 'NGD', 'NGH', 'GD', 'NGH', 'NGH', 'GG', 'GB', 'GG', 'GG', 'GH', 'GG', 'GB', 'GG', 'GB', 'NGB', 'NGD', 'GB', 'NGH', 'NGD', 'NGG', 'NGB', 'NGB', 'GB', 'NGH', 'NGB', 'NGG', 'NGG', 'GD', 'NGD', 'GB', 'GD', 'NGH', 'GD', 'NGG', 'GH', 'NGB', 'NGG', 'NGG', 'NGG', 'GH', 'GG', 'NGD', 'GG', 'GD', 'NGB', 'NGH', 'NGH', 'NGD', 'GB', 'NGG', 'GD', 'GB', 'GG', 'GH', 'GB', 'NGB', 'NGG', 'NGB', 'GH', 'GB', 'GD', 'GG', 'NGD', 'NGD', 'GD', 'GH', 'GD', 'GD', 'NGG', 'NGB', 'GD', 'NGB', 'GG', 'NGD', 'GG', 'NGH', 'GH', 'GG', 'GD', 'GD', 'GH', 'GH', 'GB', 'GB', 'GB', 'NGG', 'NGH', 'NGD', 'NGD', 'NGD', 'NGB', 'GB', 'GH', 'GD', 'GB', 'GB', 'GH', 'GD', 'GG', 'NGH', 'GH', 'GH', 'NGB', 'NGG', 'NGH', 'NGH', 'GD', 'NGG', 'GB', 'GB', 'NGG', 'GD', 'GG', 'NGG', 'NGG', 'NGD', 'GD', 'NGD', 'GG', 'NGH', 'GG', 'NGD', 'NGG', 'GB', 'GH', 'NGH', 'GB', 'GH', 'NGH', 'NGB', 'GD', 'GD', 'NGH', 'NGB', 'NGH', 'NGB', 'GD', 'NGH', 'GH', 'NGD', 'NGD', 'GB', 'NGB', 'GH', 'NGB']

#bonne liste 168 essais 7/condition
listecondition=['GB', 'NGB', 'NGD', 'GD', 'NGB', 'NGH', 'NGH', 'GG', 'NGH', 'NGB', 'NGH', 'GB', 'NGG', 'GH', 'GG', 'NGD', 'GD', 'GG', 'GH', 'NGD', 'GG', 'GB', 'NGD', 'GD', 'GB', 'NGH', 'NGG', 'GH', 'GH', 'GB', 'NGD', 'NGG', 'NGH', 'GB', 'NGG', 'NGH', 'GD', 'GH', 'NGG', 'NGG', 'GD', 'GG', 'NGH', 'GG', 'NGG', 'NGD', 'NGB', 'NGD', 'NGD', 'NGH', 'GH', 'GD', 'GD', 'NGG', 'GB', 'GH', 'NGB', 'GG', 'NGB', 'GH', 'GG', 'GD', 'GB', 'NGH', 'GB', 'NGG', 'NGB', 'NGB', 'NGH', 'NGB', 'GG', 'GD', 'NGH', 'GB', 'NGD', 'NGD', 'GG', 'GG', 'GB', 'GD', 'NGH', 'GG', 'GG', 'GD', 'NGG', 'GH', 'NGH', 'GH', 'GH', 'GH', 'GB', 'NGD', 'NGB', 'NGH', 'NGG', 'NGG', 'GD', 'GH', 'GD', 'GG', 'GB', 'NGB', 'NGD', 'GH', 'GG', 'GH', 'NGB', 'NGG', 'GH', 'NGD', 'NGG', 'NGD', 'NGD', 'GD', 'NGH', 'GB', 'GD', 'NGG', 'NGD', 'GD', 'NGB', 'NGH', 'NGD', 'NGB', 'NGG', 'GG', 'GB', 'GG', 'GH', 'NGB', 'NGB', 'NGH', 'NGB', 'NGG', 'NGD', 'GH', 'GD', 'GB', 'NGH', 'NGB', 'GB', 'NGB', 'GB', 'NGG', 'GH', 'NGD', 'NGB', 'GD', 'GG', 'NGH', 'NGG', 'GD', 'NGH', 'GB', 'NGD', 'NGD', 'GD', 'GB', 'NGB', 'GH', 'NGG', 'GB', 'GG', 'GG', 'GH', 'GD', 'GG', 'NGG']
listetemps=[0.2, 0.8, 0.5, 0.8, 0.2, 0.2, 0.2, 0.5, 0.8, 0.5, 0.5, 0.5, 0.5, 0.2, 0.8, 0.2, 0.5, 0.8, 0.8, 0.8, 0.8, 0.2, 0.2, 0.8, 0.5, 0.8, 0.2, 0.2, 0.2, 0.2, 0.8, 0.2, 0.8, 0.2, 0.2, 0.5, 0.8, 0.5, 0.8, 0.5, 0.2, 0.2, 0.5, 0.2, 0.2, 0.5, 0.5, 0.8, 0.5, 0.8, 0.5, 0.8, 0.5, 0.5, 0.5, 0.8, 0.2, 0.8, 0.8, 0.2, 0.2, 0.2, 0.2, 0.5, 0.8, 0.2, 0.2, 0.5, 0.5, 0.8, 0.2, 0.5, 0.8, 0.5, 0.2, 0.2, 0.5, 0.2, 0.8, 0.2, 0.2, 0.5, 0.8, 0.2, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.2, 0.2, 0.8, 0.8, 0.8, 0.5, 0.8, 0.5, 0.5, 0.5, 0.8, 0.5, 0.5, 0.2, 0.5, 0.8, 0.8, 0.5, 0.2, 0.2, 0.8, 0.8, 0.5, 0.8, 0.2, 0.8, 0.5, 0.8, 0.8, 0.2, 0.8, 0.2, 0.8, 0.2, 0.5, 0.8, 0.5, 0.5, 0.5, 0.5, 0.8, 0.5, 0.2, 0.2, 0.5, 0.2, 0.2, 0.5, 0.5, 0.5, 0.8, 0.2, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.2, 0.2, 0.8, 0.2, 0.2, 0.2, 0.2, 0.8, 0.8, 0.8, 0.2, 0.5, 0.2, 0.8, 0.2, 0.5, 0.5, 0.5, 0.8, 0.8]
#=>liste=['GB2', 'NGB8', 'NGD5', 'GD8', 'NGB2', 'NGH2', 'NGH2', 'GG5', 'NGH8', 'NGB5', 'NGH5', 'GB5', 'NGG5', 'GH2', 'GG8', 'NGD2', 'GD5', 'GG8', 'GH8', 'NGD8', 'GG8', 'GB2', 'NGD2', 'GD8', 'GB5', 'NGH8', 'NGG2', 'GH2', 'GH2', 'GB2', 'NGD8', 'NGG2', 'NGH8', 'GB2', 'NGG2', 'NGH5', 'GD8', 'GH5', 'NGG8', 'NGG5', 'GD2', 'GG2', 'NGH5', 'GG2', 'NGG2', 'NGD5', 'NGB5', 'NGD8', 'NGD5', 'NGH8', 'GH5', 'GD8', 'GD5', 'NGG5', 'GB5', 'GH8', 'NGB2', 'GG8', 'NGB8', 'GH2', 'GG2', 'GD2', 'GB2', 'NGH5', 'GB8', 'NGG2', 'NGB2', 'NGB5', 'NGH5', 'NGB8', 'GG2', 'GD5', 'NGH8', 'GB5', 'NGD2', 'NGD2', 'GG5', 'GG2', 'GB8', 'GD2', 'NGH2', 'GG5', 'GG8', 'GD2', 'NGG8', 'GH8', 'NGH8', 'GH8', 'GH8', 'GH8', 'GB2', 'NGD2', 'NGB8', 'NGH8', 'NGG8', 'NGG5', 'GD8', 'GH5', 'GD5', 'GG5', 'GB8', 'NGB5', 'NGD5', 'GH2', 'GG5', 'GH8', 'NGB8', 'NGG5', 'GH2', 'NGD2', 'NGG8', 'NGD8', 'NGD5', 'GD8', 'NGH2', 'GB8', 'GD5', 'NGG8', 'NGD8', 'GD2', 'NGB8', 'NGH2', 'NGD8', 'NGB2', 'NGG5', 'GG8', 'GB5', 'GG5', 'GH5', 'NGB5', 'NGB8', 'NGH5', 'NGB2', 'NGG2', 'NGD5', 'GH2', 'GD2', 'GB5', 'NGH5', 'NGB5', 'GB8', 'NGB2', 'GB5', 'NGG5', 'GH5', 'NGD5', 'NGB5', 'GD5', 'GG2', 'NGH2', 'NGG8', 'GD2', 'NGH2', 'GB2', 'NGD2', 'NGD8', 'GD8', 'GB8', 'NGB2', 'GH5', 'NGG2', 'GB8', 'GG2', 'GG5', 'GH5', 'GD5', 'GG8', 'NGG8']

# listecondition=['GG','NGG', 'GD', 'NGD']
# listetemps=[0.2, 1, 0.2, 1]

listespace=[]
keyss=[]

for i in range (len(listecondition)):#168
    print(i)
    print(listecondition[i])
    k=listecondition[i]

    #initialisation sourie pas visible
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
    core.wait(listetemps[i])

    #GO-NO-GO

    if k == 'GG' or k =='GD' or k =='GH' or k =='GB' or k =='NGG' or k =='NGD' or k =='NGH' or k =='NGB' or k =='CG' or k =='CD' or k =='CH' or k =='CB':
        if k== 'CG' or k =='CD' or k =='CH' or k =='CB' or k =='NGG' or k =='NGD' or k =='NGH' or k =='NGB':
            c=crouge
        else :
            c=cbleu
        
        clock.reset()
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
                
            rect.draw()
            rect1.draw()
            rect2.draw()
            rect3.draw() 
            win.flip()
            g=g+1
            ke=kb.getKeys(keyList=['space'])
            if ke:
                keys.append(['space', g/60])
                
        # dicto=dict({'Essai'+ str(i):keys})
        # savemat('caca_'+ str(i), dicto)
        keyss.append(keys) 

        rect.draw()
        rect1.draw()
        rect2.draw()
        rect3.draw()
        win.flip()
        core.wait(0.2)

dicto=dict({sub:keyss})
filename='E:/Manip/Psych/psych/results_gng_'+ sub + '.mat'
savemat(filename, dicto)
 

#AFFICHAGE FIN
win.close()
  #%%
# #%%
# import random

# listecondition=[]
# listetemps=[]
# # liste=[,'GD2','GD5','GD8','GG2','GG5','GG8','GH2','GH5','GH8','GB2','GB5','GB8','NGD2','NGD5','NGD8','NGG2','NGG5','NGG8','NGH2','NGH5','NGH8','NGB2','NGB5','NGB8']
# liste=['GD2','GD5','GD8','GG2','GG5','GG8','GH2','GH5','GH8','GB2','GB5','GB8','NGD2','NGD5','NGD8','NGG2','NGG5','NGG8','NGH2','NGH5','NGH8','NGB2','NGB5','NGB8','GD2','GD5','GD8','GG2','GG5','GG8','GH2','GH5','GH8','GB2','GB5','GB8','NGD2','NGD5','NGD8','NGG2','NGG5','NGG8','NGH2','NGH5','NGH8','NGB2','NGB5','NGB8','GD2','GD5','GD8','GG2','GG5','GG8','GH2','GH5','GH8','GB2','GB5','GB8','NGD2','NGD5','NGD8','NGG2','NGG5','NGG8','NGH2','NGH5','NGH8','NGB2','NGB5','NGB8','GD2','GD5','GD8','GG2','GG5','GG8','GH2','GH5','GH8','GB2','GB5','GB8','NGD2','NGD5','NGD8','NGG2','NGG5','NGG8','NGH2','NGH5','NGH8','NGB2','NGB5','NGB8','GD2','GD5','GD8','GG2','GG5','GG8','GH2','GH5','GH8','GB2','GB5','GB8','NGD2','NGD5','NGD8','NGG2','NGG5','NGG8','NGH2','NGH5','NGH8','NGB2','NGB5','NGB8','GD2','GD5','GD8','GG2','GG5','GG8','GH2','GH5','GH8','GB2','GB5','GB8','NGD2','NGD5','NGD8','NGG2','NGG5','NGG8','NGH2','NGH5','NGH8','NGB2','NGB5','NGB8','GD2','GD5','GD8','GG2','GG5','GG8','GH2','GH5','GH8','GB2','GB5','GB8','NGD2','NGD5','NGD8','NGG2','NGG5','NGG8','NGH2','NGH5','NGH8','NGB2','NGB5','NGB8']
# random.shuffle(liste)

# for i in liste :
#     if i == 'GD2' :
#         listecondition.append('GD')
#         listetemps.append(0.2)
#     if i == 'GD5' :
#         listecondition.append('GD')
#         listetemps.append(0.5)
#     if i == 'GD8' :
#         listecondition.append('GD')
#         listetemps.append(0.8)
#     if i == 'GG2' :
#         listecondition.append('GG')
#         listetemps.append(0.2)
#     if i == 'GG5' :
#         listecondition.append('GG')
#         listetemps.append(0.5)
#     if i == 'GG8' :
#         listecondition.append('GG')
#         listetemps.append(0.8)
#     if i == 'GH2' :
#         listecondition.append('GH')
#         listetemps.append(0.2)
#     if i == 'GH5' :
#         listecondition.append('GH')
#         listetemps.append(0.5)
#     if i == 'GH8' :
#         listecondition.append('GH')
#         listetemps.append(0.8)
#     if i == 'GB2' :
#         listecondition.append('GB')
#         listetemps.append(0.2)
#     if i == 'GB5' :
#         listecondition.append('GB')
#         listetemps.append(0.5)
#     if i == 'GB8' :
#         listecondition.append('GB')
#         listetemps.append(0.8)
#     #NG----
#     if i == 'NGD2' :
#         listecondition.append('NGD')
#         listetemps.append(0.2)
#     if i == 'NGD5' :
#         listecondition.append('NGD')
#         listetemps.append(0.5)
#     if i == 'NGD8' :
#         listecondition.append('NGD')
#         listetemps.append(0.8)
#     if i == 'NGG2' :
#         listecondition.append('NGG')
#         listetemps.append(0.2)
#     if i == 'NGG5' :
#         listecondition.append('NGG')
#         listetemps.append(0.5)
#     if i == 'NGG8' :
#         listecondition.append('NGG')
#         listetemps.append(0.8)
#     if i == 'NGH2' :
#         listecondition.append('NGH')
#         listetemps.append(0.2)
#     if i == 'NGH5' :
#         listecondition.append('NGH')
#         listetemps.append(0.5)
#     if i == 'NGH8' :
#         listecondition.append('NGH')
#         listetemps.append(0.8)
#     if i == 'NGB2' :
#         listecondition.append('NGB')
#         listetemps.append(0.2)
#     if i == 'NGB5' :
#         listecondition.append('NGB')
#         listetemps.append(0.5)
#     if i == 'NGB8' :
#         listecondition.append('NGB')
#         listetemps.append(0.8)


# print(listecondition)
# print(listetemps)

#                                                                                                                                                                                                                                                              # %%

      # %%
  