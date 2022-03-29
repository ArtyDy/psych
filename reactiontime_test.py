#%%
sub='sub-07DB'
from turtle import Screen, pos
import psychopy
from psychopy import visual, core, event
from scipy.io import savemat
import os

# défini windows
win = psychopy.visual.Window(
    
    units="pix",
    fullscr=True,
    color="black", screen=1
)

listecondition=['H', 'B', 'D', 'G', 'D', 'H', 'D', 'B', 'H', 'B', 'G', 'B', 'G', 'B', 'G', 'H', 'D', 'D', 'G', 'D', 'G', 'B', 'B', 'B', 'D', 'H', 'B', 'B', 'D', 'B', 'G', 'B', 'H', 'H', 'B', 'H', 'H', 'B', 'G', 'H', 'D', 'B', 'H', 'B', 'G', 'D', 'H', 'H', 'G', 'H', 'B', 'D', 'D', 'B', 'D', 'G', 'G', 'H', 'G', 'D', 'G', 'D', 'B', 'H', 'G', 'G', 'B', 'B', 'D', 'D', 'G', 'B', 'D', 'H', 'G', 'G', 'B', 'D', 'B', 'D', 'B', 'H', 'G', 'H', 'B', 'D', 'G', 'H', 'G', 'B', 'D', 'H', 'D', 'D', 'G', 'H', 'H', 'G', 'G', 'H', 'H', 'D', 'H', 'G', 'D', 'G', 'H', 'G', 'B', 'D', 'B', 'B', 'H', 'D', 'D', 'H', 'H', 'G', 'D', 'G']
listetemps=[0.2, 0.5, 0.2, 0.5, 0.8, 0.5, 0.8, 0.5, 0.8, 0.8, 0.8, 0.8, 0.2, 0.2, 0.8, 0.5, 0.2, 0.2, 0.5, 0.5, 0.8, 0.8, 0.8, 0.2, 0.5, 0.2, 0.8, 0.5, 0.8, 0.2, 0.2, 0.8, 0.8, 0.5, 0.8, 0.5, 0.2, 0.5, 0.8, 0.8, 0.8, 0.2, 0.8, 0.8, 0.2, 0.5, 0.2, 0.2, 0.5, 0.2, 0.2, 0.8, 0.2, 0.2, 0.8, 0.8, 0.5, 0.2, 0.8, 0.2, 0.8, 0.5, 0.5, 0.8, 0.8, 0.2, 0.2, 0.2, 0.2, 0.8, 0.8, 0.5, 0.8, 0.8, 0.2, 0.5, 0.5, 0.8, 0.8, 0.2, 0.5, 0.5, 0.2, 0.8, 0.5, 0.5, 0.5, 0.5, 0.2, 0.5, 0.8, 0.5, 0.5, 0.2, 0.5, 0.8, 0.8, 0.5, 0.5, 0.5, 0.5, 0.5, 0.2, 0.8, 0.2, 0.5, 0.2, 0.2, 0.8, 0.5, 0.2, 0.2, 0.5, 0.5, 0.5, 0.2, 0.8, 0.2, 0.2, 0.2]
#listecondition = ["G","D","H","B"]
#listecondition = ['DV', 'GV', 'GV', 'GV', 'GF', 'DV', 'GF', 'GF', 'GV', 'DV', 'DV', 'GV', 'GV', 'GV', 'GV', 'DV', 'DV', 'DF', 'GV', 'DF', 'GF', 'GV', 'DV', 'GV', 'DV', 'DF', 'DV', 'DV', 'GF', 'DV', 'DV', 'DF', 'DF', 'GV', 'GV', 'DV', 'DV', 'DV', 'GV', 'GV']
###listecondition=['DF', 'DV', 'DV', 'GV', 'GV', 'DF', 'GF', 'DV', 'DF', 'DV', 'GV', 'DV', 'DV', 'DV', 'DF', 'DF', 'GV', 'GV', 'DV', 'GV', 'DV', 'DV', 'DV', 'DF', 'DV', 'DV', 'DF', 'GV', 'DV', 'DF', 'GV', 'DF', 'GV', 'GV', 'GV', 'GF', 'GV', 'GV', 'DV', 'DV', 'GF', 'GV', 'GV', 'DF', 'GV', 'GV', 'DF', 'GV', 'GF', 'GF', 'GV', 'GV', 'DV', 'DV', 'GF', 'DV', 'GV', 'DV', 'GV', 'GV', 'GV', 'DV', 'GV', 'DV', 'DV', 'GV', 'GV', 'GV', 'DV', 'GF', 'GV', 'DV', 'DF', 'DF', 'GV', 'DV', 'DV', 'GV', 'DV', 'GV', 'GV', 'DV', 'GV', 'DV', 'GV', 'DV', 'DF', 'DV', 'GV', 'DV', 'GV', 'DV', 'GF', 'GF', 'DV', 'DV', 'GV', 'DV', 'DV', 'GV', 'DV', 'GF', 'GV', 'GF', 'GV', 'DV', 'GV', 'DV', 'DV', 'DF', 'DF', 'GF', 'DV', 'GF', 'GV', 'GV', 'GF', 'GV', 'GF', 'DV', 'DV', 'DV', 'GV', 'GF', 'DF', 'GV', 'GF', 'GV', 'DV', 'GV', 'GV', 'DV', 'DF', 'DV', 'GV', 'DV', 'DV', 'GF', 'GV', 'DV', 'GV', 'GV', 'GV', 'DV', 'DV', 'GF', 'GV', 'DF', 'GV', 'GF', 'DF', 'DV', 'DV', 'GV', 'DV', 'GV', 'DV', 'DV', 'DV', 'GV']
# listecondition=['DV', 'DV', 'DV', 'DV']

# listecondition=['D','G','H','B']
# listetemps=[0.2,0.5,0.8,0.2]
#pos=[]
listecond=['D','G','H','B']
listespace=[]

#définition des carrés
rect=visual.Rect(win, width=100, height=100,fillColor="black", lineWidth=5, lineColor=[1, 1, 1],pos=[-300,0] )
rect1=visual.Rect(win, width=100, height=100,fillColor="black", lineWidth=5, lineColor=[1, 1, 1],pos=[300,0] )
rect2=visual.Rect(win, width=100, height=100,fillColor="black", lineWidth=5, lineColor=[1, 1, 1],pos=[0,300] )
rect3=visual.Rect(win, width=100, height=100,fillColor="black", lineWidth=5, lineColor=[1, 1, 1],pos=[0,-300] )

#croix rouge
lignerouge=visual.Line(win, start=[-40,0], end=[40,0], lineColor="red", lineWidth=5)
lignerouge1=visual.Line(win, start=[0,-40], end=[0,40], lineColor="red", lineWidth=5)

#croix verte
ligneverte=visual.Line(win, start=[-40,0], end=[40,0], lineColor="green", lineWidth=5)
ligneverte1=visual.Line(win, start=[0,-40], end=[0,40], lineColor="green", lineWidth=5)


for i in range(len(listecondition)):
    print(i)
    print(listecondition[i])
    k=listecondition[i]
    mouse=event.Mouse(win=win, visible=False, newPos=[0,0])
    #poss=[]
    if k == "D":
        #affichage croix rouge
        lignerouge.draw()
        lignerouge1.draw()

        #affichage carrés gauche, droit, haut, bas
        rect.draw()
        rect1.draw()
        rect2.draw()
        rect3.draw()

        # AFFICHAGE BASE ROUGE
        win.flip()
        core.wait(2)

        #affichage croix verte
        ligneverte.draw()
        ligneverte1.draw()
        rect.draw()
        rect1.draw()
        rect2.draw()
        rect3.draw()

        # AFFICHAGE BASE VERTE
        win.flip()
        core.wait(listetemps[i])

        # #affichage stimulus droit
        # ligneverte.draw()
        # ligneverte1.draw()
        # rect.draw()
        # rect1.draw()

        clock=core.Clock()
        
        bool=0

        while(bool==0):
            ligneverte.draw()
            ligneverte1.draw()
            rect.draw()
            rect1.draw()
            rect2.draw()
            rect3.draw()
            etoile1=visual.Line(win, start=[285,0], end=[315,0], lineColor=[1,1,1], lineWidth=5)
            etoile1.draw()
            etoile2=visual.Line(win, start=[300,15], end=[300,-15], lineColor=[1,1,1], lineWidth=5)
            etoile2.draw()
            etoile3=visual.Line(win, start=[310,10], end=[290,-10], lineColor=[1,1,1], lineWidth=5)
            etoile3.draw()
            etoile4=visual.Line(win, start=[290,10], end=[310,-10], lineColor=[1,1,1], lineWidth=5)
            etoile4.draw()
            win.flip()

            clock=core.Clock()
            keys=event.waitKeys(keyList=['space'], timeStamped=clock)
            listespace.append(keys[0][1])
            bool=1

            #poss.append([mouse.getPos()[0], mouse.getPos()[1]])
        #pos.append(poss)

    if k == "H":
        
        #affichage croix rouge
        lignerouge.draw()
        lignerouge1.draw()

        #affichage carrés
        rect.draw()
        rect1.draw()
        rect2.draw()
        rect3.draw()

        # AFFICHAGE BASE ROUGE
        win.flip()
        core.wait(2)

        #affichage croix verte
        ligneverte.draw()
        ligneverte1.draw()
        rect.draw()
        rect1.draw()
        rect2.draw()
        rect3.draw()

        # AFFICHAGE BASE VERTE
        win.flip()
        core.wait(listetemps[i])

        #affichage stimulus droit
        ligneverte.draw()
        ligneverte1.draw()
        rect.draw()
        rect1.draw()
        rect2.draw()
        rect3.draw()

        bool=0

        while(bool==0):
            ligneverte.draw()
            ligneverte1.draw()
            rect.draw()
            rect1.draw()
            rect2.draw()
            rect3.draw()

            etoile1=visual.Line(win, start=[0,285], end=[0,315], lineColor=[1,1,1], lineWidth=5)
            etoile1.draw()
            etoile2=visual.Line(win, start=[15,300], end=[-15,300], lineColor=[1,1,1], lineWidth=5)
            etoile2.draw()
            etoile3=visual.Line(win, start=[10,310], end=[-10,290], lineColor=[1,1,1], lineWidth=5)
            etoile3.draw()
            etoile4=visual.Line(win, start=[10,290], end=[-10,310], lineColor=[1,1,1], lineWidth=5)
            etoile4.draw()
            win.flip()
            #poss.append([mouse.getPos()[0],mouse.getPos()[1]])

            clock=core.Clock()
            keys=event.waitKeys(keyList=['space'], timeStamped=clock)
            listespace.append(keys[0][1])
            bool=1
        #pos.append(poss)

    if k == "G":
        #affichage croix rouge
        lignerouge.draw()
        lignerouge1.draw()

        #affichage carrés
        rect.draw()
        rect1.draw()
        rect2.draw()
        rect3.draw()

        # AFFICHAGE BASE ROUGE
        win.flip()
        core.wait(2)

        #affichage croix verte
        ligneverte.draw()
        ligneverte1.draw()
        rect.draw()
        rect1.draw()
        rect2.draw()
        rect3.draw()

        # AFFICHAGE BASE VERTE
        win.flip()
        core.wait(listetemps[i])

        #affichage stimulus gauche
        ligneverte.draw()
        ligneverte1.draw()
        rect.draw()
        rect1.draw()
        rect2.draw()
        rect3.draw()

        bool=0
        while(bool==0):
            ligneverte.draw()
            ligneverte1.draw()
            rect.draw()
            rect1.draw()
            rect2.draw()
            rect3.draw()
            etoile1=visual.Line(win, start=[-285,0], end=[-315,0], lineColor=[1,1,1], lineWidth=5)
            etoile1.draw()
            etoile2=visual.Line(win, start=[-300,15], end=[-300,-15], lineColor=[1,1,1], lineWidth=5)
            etoile2.draw()
            etoile3=visual.Line(win, start=[-310,10], end=[-290,-10], lineColor=[1,1,1], lineWidth=5)
            etoile3.draw()
            etoile4=visual.Line(win, start=[-290,10], end=[-310,-10], lineColor=[1,1,1], lineWidth=5)
            etoile4.draw()
            win.flip()

            clock=core.Clock()
            keys=event.waitKeys(keyList=['space'], timeStamped=clock)
            listespace.append(keys[0][1])
            bool=1
        


    if k == "B":
        #affichage croix rouge
        lignerouge.draw()
        lignerouge1.draw()

        #affichage carrés
        rect.draw()
        rect1.draw()
        rect2.draw()
        rect3.draw()

        # AFFICHAGE BASE ROUGE
        win.flip()
        core.wait(2)

        #affichage croix verte
        ligneverte.draw()
        ligneverte1.draw()
        rect.draw()
        rect1.draw()
        rect2.draw()
        rect3.draw()

        # AFFICHAGE BASE VERTE
        win.flip()
        core.wait(listetemps[i])

        #affichage stimulus gauche
        ligneverte.draw()
        ligneverte1.draw()
        rect.draw()
        rect1.draw()
        rect2.draw()
        rect3.draw()
        
        bool=0
        while(bool==0):
            ligneverte.draw()
            ligneverte1.draw()
            rect.draw()
            rect1.draw()
            rect2.draw()
            rect3.draw()
            etoile1=visual.Line(win, start=[0,-285], end=[0,-315], lineColor=[1,1,1], lineWidth=5)
            etoile1.draw()
            etoile2=visual.Line(win, start=[15,-300], end=[-15,-300], lineColor=[1,1,1], lineWidth=5)
            etoile2.draw()
            etoile3=visual.Line(win, start=[10,-310], end=[-10,-290], lineColor=[1,1,1], lineWidth=5)
            etoile3.draw()
            etoile4=visual.Line(win, start=[10,-290], end=[-10,-310], lineColor=[1,1,1], lineWidth=5)
            etoile4.draw()
            win.flip()

            clock=core.Clock()
            keys=event.waitKeys(keyList=['space'], timeStamped=clock)
            listespace.append(keys[0][1])
            bool=1

        #pos.append(poss)
    # AFFICHAGE STIMULUS
            
results=dict()
for k in range(len(listecondition)): #a voir ?
    essai='Essai'+str(k)
    results[essai]=listespace[k]

# os.mkdir(sub)
filename = 'E:/Manip/Psych/psych/results_RT_'+ sub +'.mat'
savemat(filename, results)
win.close()









 #%%
# import random

# listecondition=[]
# listetemps=[]
# liste=['D2','D5','D8','G2','G5','G8','H2','H5','H8','B2','B5','B8','D2','D5','D8','G2','G5','G8','H2','H5','H8','B2','B5','B8','D2','D5','D8','G2','G5','G8','H2','H5','H8','B2','B5','B8','D2','D5','D8','G2','G5','G8','H2','H5','H8','B2','B5','B8','D2','D5','D8','G2','G5','G8','H2','H5','H8','B2','B5','B8','D2','D5','D8','G2','G5','G8','H2','H5','H8','B2','B5','B8','D2','D5','D8','G2','G5','G8','H2','H5','H8','B2','B5','B8','D2','D5','D8','G2','G5','G8','H2','H5','H8','B2','B5','B8','D2','D5','D8','G2','G5','G8','H2','H5','H8','B2','B5','B8','D2','D5','D8','G2','G5','G8','H2','H5','H8','B2','B5','B8']
# random.shuffle(liste)

# for i in liste :
#     if i == 'D2' :
#         listecondition.append('D')
#         listetemps.append(0.2)
#     if i == 'D5' :
#         listecondition.append('D')
#         listetemps.append(0.5)
#     if i == 'D8' :
#         listecondition.append('D')
#         listetemps.append(0.8)
#     if i == 'G2' :
#         listecondition.append('G')
#         listetemps.append(0.2)
#     if i == 'G5' :
#         listecondition.append('G')
#         listetemps.append(0.5)
#     if i == 'G8' :
#         listecondition.append('G')
#         listetemps.append(0.8)
#     if i == 'H2' :
#         listecondition.append('H')
#         listetemps.append(0.2)
#     if i == 'H5' :
#         listecondition.append('H')
#         listetemps.append(0.5)
#     if i == 'H8' :
#         listecondition.append('H')
#         listetemps.append(0.8)
#     if i == 'B2' :
#         listecondition.append('B')
#         listetemps.append(0.2)
#     if i == 'B5' :
#         listecondition.append('B')
#         listetemps.append(0.5)
#     if i == 'B8' :
#         listecondition.append('B')
#         listetemps.append(0.8)


# print(listecondition)
# print(listetemps)


# # #%%

# # from turtle import Screen, pos
# # import psychopy
# # from psychopy import visual, core, event
# # from scipy.io import savemat

# # # défini windows
# # win = psychopy.visual.Window(
    
# #     units="pix",
# #     fullscr=True,
# #     color="black", screen=1
# # )
# # clock=core.Clock()
# # psychopy.event.waitKeys()
# # keys=event.waitKeys(keyList=['space'], timeStamped=clock)
# # print(keys)
# # win.close()
















#          #%%
# # #affichage cue gauche
# #         ligne.draw()
# #         ligne1.draw()
# #         rect.draw()
# #         rect1.draw()
# #         fleche=visual.Line(win, start=[-120,0], end=[-180,0], lineColor=[1,1,1], lineWidth=5)
# #         fleche.draw()
# #         fleche1=visual.Line(win, start=[-180,0], end=[-165,-10], lineColor=[1,1,1], lineWidth=5)
# #         fleche1.draw()
# #         fleche2=visual.Line(win, start=[-180,0], end=[-165,10], lineColor=[1,1,1], lineWidth=5)
# #         fleche2.draw()




# #         #affichage cue droite
# #         ligne.draw()
# #         ligne1.draw()
# #         rect.draw()
# #         rect1.draw()
# #         fleche=visual.Line(win, start=[120,0], end=[180,0], lineColor=[1,1,1], lineWidth=5)
# #         fleche.draw()
# #         fleche1=visual.Line(win, start=[180,0], end=[165,-10], lineColor=[1,1,1], lineWidth=5)
# #         fleche1.draw()
# #         fleche2=visual.Line(win, start=[180,0], end=[165,10], lineColor=[1,1,1], lineWidth=5)
# #         fleche2.draw()













# # #%%
# # from turtle import pos
# # import psychopy
# # from psychopy import visual, core, event
# # import random

# # listecondition = ["GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GF","GF","GF","GF","GF","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DF","DF","DF","DF","DF","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GF","GF","GF","GF","GF","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DF","DF","DF","DF","DF","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GF","GF","GF","GF","GF","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DF","DF","DF","DF","DF","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GF","GF","GF","GF","GF","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DF","DF","DF","DF","DF"]
# # #listerandom = ["GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GF","GF","GF","GF","GF","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DF","DF","DF","DF","DF"]
# # #listecondition=['DF', 'DV', 'DV', 'GV', 'GV', 'DF', 'GF', 'DV', 'DF', 'DV', 'GV', 'DV', 'DV', 'DV', 'DF', 'DF', 'GV', 'GV', 'DV', 'GV', 'DV', 'DV', 'DV', 'DF', 'DV', 'DV', 'DF', 'GV', 'DV', 'DF', 'GV', 'DF', 'GV', 'GV', 'GV', 'GF', 'GV', 'GV', 'DV', 'DV', 'GF', 'GV', 'GV', 'DF', 'GV', 'GV', 'DF', 'GV', 'GF', 'GF', 'GV', 'GV', 'DV', 'DV', 'GF', 'DV', 'GV', 'DV', 'GV', 'GV', 'GV', 'DV', 'GV', 'DV', 'DV', 'GV', 'GV', 'GV', 'DV', 'GF', 'GV', 'DV', 'DF', 'DF', 'GV', 'DV', 'DV', 'GV', 'DV', 'GV', 'GV', 'DV', 'GV', 'DV', 'GV', 'DV', 'DF', 'DV', 'GV', 'DV', 'GV', 'DV', 'GF', 'GF', 'DV', 'DV', 'GV', 'DV', 'DV', 'GV', 'DV', 'GF', 'GV', 'GF', 'GV', 'DV', 'GV', 'DV', 'DV', 'DF', 'DF', 'GF', 'DV', 'GF', 'GV', 'GV', 'GF', 'GV', 'GF', 'DV', 'DV', 'DV', 'GV', 'GF', 'DF', 'GV', 'GF', 'GV', 'DV', 'GV', 'GV', 'DV', 'DF', 'DV', 'GV', 'DV', 'DV', 'GF', 'GV', 'DV', 'GV', 'GV', 'GV', 'DV', 'DV', 'GF', 'GV', 'DF', 'GV', 'GF', 'DF', 'DV', 'DV', 'GV', 'DV', 'GV', 'DV', 'DV', 'DV', 'GV']

# # random.shuffle(listecondition)
# # print (listecondition)















# # #%%
# # from turtle import pos
# # import psychopy
# # from psychopy import visual, core, event
# # import random

# # listecondition = ["GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GF","GF","GF","GF","GF","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DF","DF","DF","DF","DF","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GF","GF","GF","GF","GF","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DF","DF","DF","DF","DF","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GF","GF","GF","GF","GF","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DF","DF","DF","DF","DF","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GF","GF","GF","GF","GF","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DF","DF","DF","DF","DF"]
# # #listerandom = ["GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GV","GF","GF","GF","GF","GF","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DV","DF","DF","DF","DF","DF"]

# # random.shuffle(listecondition)
# # print (listecondition)
# # liste=['DF', 'DV', 'DV', 'GV', 'GV', 'DF', 'GF', 'DV', 'DF', 'DV', 'GV', 'DV', 'DV', 'DV', 'DF', 'DF', 'GV', 'GV', 'DV', 'GV', 'DV', 'DV', 'DV', 'DF', 'DV', 'DV', 'DF', 'GV', 'DV', 'DF', 'GV', 'DF', 'GV', 'GV', 'GV', 'GF', 'GV', 'GV', 'DV', 'DV', 'GF', 'GV', 'GV', 'DF', 'GV', 'GV', 'DF', 'GV', 'GF', 'GF', 'GV', 'GV', 'DV', 'DV', 'GF', 'DV', 'GV', 'DV', 'GV', 'GV', 'GV', 'DV', 'GV', 'DV', 'DV', 'GV', 'GV', 'GV', 'DV', 'GF', 'GV', 'DV', 'DF', 'DF', 'GV', 'DV', 'DV', 'GV', 'DV', 'GV', 'GV', 'DV', 'GV', 'DV', 'GV', 'DV', 'DF', 'DV', 'GV', 'DV', 'GV', 'DV', 'GF', 'GF', 'DV', 'DV', 'GV', 'DV', 'DV', 'GV', 'DV', 'GF', 'GV', 'GF', 'GV', 'DV', 'GV', 'DV', 'DV', 'DF', 'DF', 'GF', 'DV', 'GF', 'GV', 'GV', 'GF', 'GV', 'GF', 'DV', 'DV', 'DV', 'GV', 'GF', 'DF', 'GV', 'GF', 'GV', 'DV', 'GV', 'GV', 'DV', 'DF', 'DV', 'GV', 'DV', 'DV', 'GF', 'GV', 'DV', 'GV', 'GV', 'GV', 'DV', 'DV', 'GF', 'GV', 'DF', 'GV', 'GF', 'DF', 'DV', 'DV', 'GV', 'DV', 'GV', 'DV', 'DV', 'DV', 'GV']


# # #listecondition=['DF', 'DV', 'DV', 'GV', 'GV', 'DF', 'GF', 'DV', 'DF', 'DV', 'GV', 'DV', 'DV', 'DV', 'DF', 'DF', 'GV', 'GV', 'DV', 'GV', 'DV', 'DV', 'DV', 'DF', 'DV', 'DV', 'DF', 'GV', 'DV', 'DF', 'GV', 'DF', 'GV', 'GV', 'GV', 'GF', 'GV', 'GV', 'DV', 'DV', 'GF', 'GV', 'GV', 'DF', 'GV', 'GV', 'DF', 'GV', 'GF', 'GF', 'GV', 'GV', 'DV', 'DV', 'GF', 'DV', 'GV', 'DV', 'GV', 'GV', 'GV', 'DV', 'GV', 'DV', 'DV', 'GV', 'GV', 'GV', 'DV', 'GF', 'GV', 'DV', 'DF', 'DF', 'GV', 'DV', 'DV', 'GV', 'DV', 'GV', 'GV', 'DV', 'GV', 'DV', 'GV', 'DV', 'DF', 'DV', 'GV', 'DV', 'GV', 'DV', 'GF', 'GF', 'DV', 'DV', 'GV', 'DV', 'DV', 'GV', 'DV', 'GF', 'GV', 'GF', 'GV', 'DV', 'GV', 'DV', 'DV', 'DF', 'DF', 'GF', 'DV', 'GF', 'GV', 'GV', 'GF', 'GV', 'GF', 'DV', 'DV', 'DV', 'GV', 'GF', 'DF', 'GV', 'GF', 'GV', 'DV', 'GV', 'GV', 'DV', 'DF', 'DV', 'GV', 'DV', 'DV', 'GF', 'GV', 'DV', 'GV', 'GV', 'GV', 'DV', 'DV', 'GF', 'GV', 'DF', 'GV', 'GF', 'DF', 'DV', 'DV', 'GV', 'DV', 'GV', 'DV', 'DV', 'DV', 'GV']


# # #listecondition = ['DV', 'GV', 'GV', 'GV', 'GF', 'DV', 'GF', 'GF', 'GV', 'DV', 'DV', 'GV', 'GV', 'GV', 'GV', 'DV', 'DV', 'DF', 'GV', 'DF', 'GF', 'GV', 'DV', 'GV', 'DV', 'DF', 'DV', 'DV', 'GF', 'DV', 'DV', 'DF', 'DF', 'GV', 'GV', 'DV', 'DV', 'DV', 'GV', 'GV']
# # #listecondition = ['DV', 'GV', 'GV', 'GV', 'GF', 'DV', 'GF', 'GF', 'GV', 'DV', 'DV', 'GV', 'GV', 'GV', 'GV', 'DV', 'DV', 'DF', 'GV', 'DF', 'GF', 'GV', 'DV', 'GV', 'DV', 'DF', 'DV', 'DV', 'GF', 'DV', 'DV', 'DF', 'DF', 'GV', 'GV', 'DV', 'DV', 'DV', 'GV', 'GV']
# # #%% droite faux

# # from turtle import pos
# # import psychopy
# # from psychopy import visual, core, event


# # # défini windows
# # win = psychopy.visual.Window(
# #     size=[400, 400],
# #     units="pix",
# #     fullscr=True,
# #     color="black"
# # )

# # #affichage croix rouge
# # ligne=visual.Line(win, start=[-40,0], end=[40,0], lineColor="red", lineWidth=5)
# # ligne.draw()
# # ligne1=visual.Line(win, start=[0,-40], end=[0,40], lineColor="red", lineWidth=5)
# # ligne1.draw()

# # #affichage carré gauche
# # rect=visual.Rect(win, width=100, height=100,fillColor="black", lineWidth=5, lineColor=[1, 1, 1],pos=[-340,0] )
# # rect.draw()

# # #affichage carré droit
# # rect1=visual.Rect(win, width=100, height=100,fillColor="black", lineWidth=5, lineColor=[1, 1, 1],pos=[340,0] )
# # rect1.draw()

# # # AFFICHAGE BASE ROUGE
# # win.flip()
# # core.wait(0.8)

# # #affichage croix verte
# # ligne=visual.Line(win, start=[-40,0], end=[40,0], lineColor="green", lineWidth=5)
# # ligne.draw()
# # ligne1=visual.Line(win, start=[0,-40], end=[0,40], lineColor="green", lineWidth=5)
# # ligne1.draw()
# # rect.draw()
# # rect1.draw()

# # # AFFICHAGE BASE VERTE
# # win.flip()
# # core.wait(0.8)

# # #affichage cue droite
# # ligne.draw()
# # ligne1.draw()
# # rect.draw()
# # rect1.draw()
# # fleche=visual.Line(win, start=[120,0], end=[180,0], lineColor=[1,1,1], lineWidth=5)
# # fleche.draw()
# # fleche1=visual.Line(win, start=[180,0], end=[165,-10], lineColor=[1,1,1], lineWidth=5)
# # fleche1.draw()
# # fleche2=visual.Line(win, start=[180,0], end=[165,10], lineColor=[1,1,1], lineWidth=5)
# # fleche2.draw()

# # #AFFICHAGE CUE
# # win.flip()
# # core.wait(2.36)

# # #AFFICHAGE BASE VERTE DELAI
# # ligne.draw()
# # ligne1.draw()
# # rect.draw()
# # rect1.draw()
# # win.flip()
# # core.wait(1.5)

# # #affichage stimulus gauche
# # ligne.draw()
# # ligne1.draw()
# # rect.draw()
# # rect1.draw()

# # while(event.Mouse.getPressed('self')[0]!=1):
# #     ligne.draw()
# #     ligne1.draw()
# #     rect.draw()
# #     rect1.draw()
# #     etoile1=visual.Line(win, start=[-325,0], end=[-355,0], lineColor=[1,1,1], lineWidth=5)
# #     etoile1.draw()
# #     etoile2=visual.Line(win, start=[-340,15], end=[-340,-15], lineColor=[1,1,1], lineWidth=5)
# #     etoile2.draw()
# #     etoile3=visual.Line(win, start=[-350,10], end=[-330,-10], lineColor=[1,1,1], lineWidth=5)
# #     etoile3.draw()
# #     etoile4=visual.Line(win, start=[-330,10], end=[-350,-10], lineColor=[1,1,1], lineWidth=5)
# #     etoile4.draw()
# #     win.flip()
    
# # win.close()
















# # #%%
# # data=dict()
# # data['lettre']=dict()

# # liste=['A','B','C']
# # data['lettre']=liste

# # #%% droite vrai

# # from turtle import pos
# # import psychopy
# # from psychopy import visual, core, event


# # # défini windows
# # win = psychopy.visual.Window(
# #     size=[400, 400],
# #     units="pix",
# #     fullscr=True,
# #     color="black"
# # )

# # #affichage croix rouge
# # ligne=visual.Line(win, start=[-40,0], end=[40,0], lineColor="red", lineWidth=5)
# # ligne.draw()
# # ligne1=visual.Line(win, start=[0,-40], end=[0,40], lineColor="red", lineWidth=5)
# # ligne1.draw()

# # #affichage carré gauche
# # rect=visual.Rect(win, width=100, height=100,fillColor="black", lineWidth=5, lineColor=[1, 1, 1],pos=[-340,0] )
# # rect.draw()

# # #affichage carré droit
# # rect1=visual.Rect(win, width=100, height=100,fillColor="black", lineWidth=5, lineColor=[1, 1, 1],pos=[340,0] )
# # rect1.draw()

# # # AFFICHAGE BASE ROUGE
# # win.flip()
# # core.wait(0.8)

# # #affichage croix verte
# # ligne=visual.Line(win, start=[-40,0], end=[40,0], lineColor="green", lineWidth=5)
# # ligne.draw()
# # ligne1=visual.Line(win, start=[0,-40], end=[0,40], lineColor="green", lineWidth=5)
# # ligne1.draw()
# # rect.draw()
# # rect1.draw()

# # # AFFICHAGE BASE VERTE
# # win.flip()
# # core.wait(0.8)

# # #affichage cue droite
# # ligne.draw()
# # ligne1.draw()
# # rect.draw()
# # rect1.draw()
# # fleche=visual.Line(win, start=[120,0], end=[180,0], lineColor=[1,1,1], lineWidth=5)
# # fleche.draw()
# # fleche1=visual.Line(win, start=[180,0], end=[165,-10], lineColor=[1,1,1], lineWidth=5)
# # fleche1.draw()
# # fleche2=visual.Line(win, start=[180,0], end=[165,10], lineColor=[1,1,1], lineWidth=5)
# # fleche2.draw()

# # #AFFICHAGE CUE
# # win.flip()
# # core.wait(2.36)

# # #AFFICHAGE BASE VERTE DELAI
# # ligne.draw()
# # ligne1.draw()
# # rect.draw()
# # rect1.draw()
# # win.flip()
# # core.wait(1.5)

# # #affichage stimulus droit
# # ligne.draw()
# # ligne1.draw()
# # rect.draw()
# # rect1.draw()

# # while(event.Mouse.getPressed('self')[0]!=1):
# #     ligne.draw()
# #     ligne1.draw()
# #     rect.draw()
# #     rect1.draw()
# #     etoile1=visual.Line(win, start=[325,0], end=[355,0], lineColor=[1,1,1], lineWidth=5)
# #     etoile1.draw()
# #     etoile2=visual.Line(win, start=[340,15], end=[340,-15], lineColor=[1,1,1], lineWidth=5)
# #     etoile2.draw()
# #     etoile3=visual.Line(win, start=[350,10], end=[330,-10], lineColor=[1,1,1], lineWidth=5)
# #     etoile3.draw()
# #     etoile4=visual.Line(win, start=[330,10], end=[350,-10], lineColor=[1,1,1], lineWidth=5)
# #     etoile4.draw()
# #     win.flip()
    
# # win.close()




# # # %% gauche faux
# # from turtle import pos
# # import psychopy
# # from psychopy import visual, core, event


# # # défini windows
# # win = psychopy.visual.Window(
# #     size=[400, 400],
# #     units="pix",
# #     fullscr=True,
# #     color="black"
# # )

# # #affichage croix rouge
# # ligne=visual.Line(win, start=[-40,0], end=[40,0], lineColor="red", lineWidth=5)
# # ligne.draw()
# # ligne1=visual.Line(win, start=[0,-40], end=[0,40], lineColor="red", lineWidth=5)
# # ligne1.draw()

# # #affichage carré gauche
# # rect=visual.Rect(win, width=100, height=100,fillColor="black", lineWidth=5, lineColor=[1, 1, 1],pos=[-340,0] )
# # rect.draw()

# # #affichage carré droit
# # rect1=visual.Rect(win, width=100, height=100,fillColor="black", lineWidth=5, lineColor=[1, 1, 1],pos=[340,0] )
# # rect1.draw()

# # # AFFICHAGE BASE ROUGE
# # win.flip()
# # core.wait(0.8)

# # #affichage croix verte
# # ligne=visual.Line(win, start=[-40,0], end=[40,0], lineColor="green", lineWidth=5)
# # ligne.draw()
# # ligne1=visual.Line(win, start=[0,-40], end=[0,40], lineColor="green", lineWidth=5)
# # ligne1.draw()
# # rect.draw()
# # rect1.draw()

# # # AFFICHAGE BASE VERTE
# # win.flip()
# # core.wait(0.8)

# # #affichage cue gauche
# # ligne.draw()
# # ligne1.draw()
# # rect.draw()
# # rect1.draw()
# # fleche=visual.Line(win, start=[-120,0], end=[-180,0], lineColor=[1,1,1], lineWidth=5)
# # fleche.draw()
# # fleche1=visual.Line(win, start=[-180,0], end=[-165,-10], lineColor=[1,1,1], lineWidth=5)
# # fleche1.draw()
# # fleche2=visual.Line(win, start=[-180,0], end=[-165,10], lineColor=[1,1,1], lineWidth=5)
# # fleche2.draw()


# # #AFFICHAGE CUE
# # win.flip()
# # core.wait(2.36)

# # #AFFICHAGE BASE VERTE DELAI
# # ligne.draw()
# # ligne1.draw()
# # rect.draw()
# # rect1.draw()
# # win.flip()
# # core.wait(1.5)

# # #affichage stimulus gauche
# # ligne.draw()
# # ligne1.draw()
# # rect.draw()
# # rect1.draw()

# # while(event.Mouse.getPressed('self')[0]!=1):
# #     ligne.draw()
# #     ligne1.draw()
# #     rect.draw()
# #     rect1.draw()
# #     etoile1=visual.Line(win, start=[-325,0], end=[-355,0], lineColor=[1,1,1], lineWidth=5)
# #     etoile1.draw()
# #     etoile2=visual.Line(win, start=[-340,15], end=[-340,-15], lineColor=[1,1,1], lineWidth=5)
# #     etoile2.draw()
# #     etoile3=visual.Line(win, start=[-350,10], end=[-330,-10], lineColor=[1,1,1], lineWidth=5)
# #     etoile3.draw()
# #     etoile4=visual.Line(win, start=[-330,10], end=[-350,-10], lineColor=[1,1,1], lineWidth=5)
# #     etoile4.draw()
# #     win.flip()
    
# # win.close()







# # #%%
# # listecondition = ["GV","GF","DV","DF"]
# # listecondition
# # for i in range (4):
# #     k=1
# #     print ('a')
# #     print(listecondition[k])







# # # %% Copie base

# # from turtle import pos
# # import psychopy
# # from psychopy import visual, core, event


# # # défini windows
# # win = psychopy.visual.Window(
# #     size=[400, 400],
# #     units="pix",
# #     fullscr=True,
# #     color="black"
# # )

# # #affichage croix rouge
# # ligne=visual.Line(win, start=[-40,0], end=[40,0], lineColor="red", lineWidth=5)
# # ligne.draw()
# # ligne1=visual.Line(win, start=[0,-40], end=[0,40], lineColor="red", lineWidth=5)
# # ligne1.draw()

# # #affichage carré gauche
# # rect=visual.Rect(win, width=100, height=100,fillColor="black", lineWidth=5, lineColor=[1, 1, 1],pos=[-340,0] )
# # rect.draw()

# # #affichage carré droit
# # rect1=visual.Rect(win, width=100, height=100,fillColor="black", lineWidth=5, lineColor=[1, 1, 1],pos=[340,0] )
# # rect1.draw()

# # # AFFICHAGE BASE ROUGE
# # win.flip()
# # core.wait(0.8)

# # #affichage croix verte
# # ligne=visual.Line(win, start=[-40,0], end=[40,0], lineColor="green", lineWidth=5)
# # ligne.draw()
# # ligne1=visual.Line(win, start=[0,-40], end=[0,40], lineColor="green", lineWidth=5)
# # ligne1.draw()
# # rect.draw()
# # rect1.draw()

# # # AFFICHAGE BASE VERTE
# # win.flip()
# # core.wait(0.8)

# # #affichage cue gauche
# # ligne.draw()
# # ligne1.draw()
# # rect.draw()
# # rect1.draw()
# # fleche=visual.Line(win, start=[-120,0], end=[-180,0], lineColor=[1,1,1], lineWidth=5)
# # fleche.draw()
# # fleche1=visual.Line(win, start=[-180,0], end=[-165,-10], lineColor=[1,1,1], lineWidth=5)
# # fleche1.draw()
# # fleche2=visual.Line(win, start=[-180,0], end=[-165,10], lineColor=[1,1,1], lineWidth=5)
# # fleche2.draw()

# # #AFFICHAGE CUE
# # win.flip()
# # core.wait(2.36)

# # #AFFICHAGE BASE VERTE DELAI
# # ligne.draw()
# # ligne1.draw()
# # rect.draw()
# # rect1.draw()
# # win.flip()
# # core.wait(1.5)

# # #affichage stimulus gauche
# # ligne.draw()
# # ligne1.draw()
# # rect.draw()
# # rect1.draw()

# # while(event.Mouse.getPressed('self')[0]!=1):
# #     ligne.draw()
# #     ligne1.draw()
# #     rect.draw()
# #     rect1.draw()
# #     etoile1=visual.Line(win, start=[-325,0], end=[-355,0], lineColor=[1,1,1], lineWidth=5)
# #     etoile1.draw()
# #     etoile2=visual.Line(win, start=[-340,15], end=[-340,-15], lineColor=[1,1,1], lineWidth=5)
# #     etoile2.draw()
# #     etoile3=visual.Line(win, start=[-350,10], end=[-330,-10], lineColor=[1,1,1], lineWidth=5)
# #     etoile3.draw()
# #     etoile4=visual.Line(win, start=[-330,10], end=[-350,-10], lineColor=[1,1,1], lineWidth=5)
# #     etoile4.draw()

# # # AFFICHAGE STIMULUS
# #     win.flip()
# # # core.wait(0.3)


# # #AFFICHAGE DELAI
# # ligne.draw()
# # ligne1.draw()
# # rect.draw()
# # rect1.draw()
# # win.flip()
# # core.wait(0.3)
# # win.close()


# # #%%
# # import scipy.io

# # mat=scipy.io.loadmat("E:\Manip\Psych\psych\\results_gng_sub-test.mat")
# # # %%

# # %%

# %%
