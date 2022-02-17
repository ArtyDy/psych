#%%
from turtle import pos
import psychopy
from psychopy import visual, core, event
from scipy.io import savemat

sub='sub-00AD'
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

#définition cercle bleu 
cbleu=visual.Circle(win, radius=150, edges=32, units='', lineWidth=2.5, lineColor='aqua', lineColorSpace='aqua',fillColor='aqua', fillColorSpace=None)

#définition cercle rouge
crouge=visual.Circle(win, radius=150, edges=32, units='', lineWidth=2.5, lineColor='red', lineColorSpace='red',fillColor='red', fillColorSpace=None)

listecondition = ["C","G","NG"]
pos=[]
poss=[]
buttonss=[]
timess=[]

for i in range (3):
    k=listecondition[i]

    #initialisation sourie bas écran
    mouse=event.Mouse(win=win, visible=True, newPos=[0,-350])

    #affichage croix blanche
    ligne=visual.Line(win, start=[-40,0], end=[40,0], lineColor="white", lineWidth=5)
    ligne.draw()
    ligne1=visual.Line(win, start=[0,-40], end=[0,40], lineColor="white", lineWidth=5)
    ligne1.draw()
    win.flip()
    core.wait(1)
    
    if k == 'G':
        #AFFICHAGE CONDITION GO B-B-B-B
        cbleu.draw()
        win.flip()
        core.wait(0.8)
        win.flip()
        core.wait(0.2)

        cbleu.draw()
        win.flip()
        core.wait(0.8)
        win.flip()
        core.wait(0.2)

        cbleu.draw()
        win.flip()
        core.wait(0.8)
        win.flip()
        core.wait(0.2)

        # cbleu.draw()
        mouse.clickReset()

        # win.flip()
        # core.wait(0.8)
        # win.flip()
        # core.wait(0.2)

        # win.flip()
        
        #tant que 3scd ne se sont pas écoulé (60frame/scd)
        j=0
        poss=[]
        time=[]
        button=[]
        while j != 120:
            if j<=48:
                cbleu.draw()
                
            win.flip()
            j+=1
            buttons, times = mouse.getPressed(getTime=True)
            # if buttons[0]:
            #     print(buttons)
            #     print(times)
            # print ('le button Go est a')
            # print (buttons)
            time.append(times)
            button.append(buttons)
            poss.append([mouse.getPos()[0], mouse.getPos()[1]]) #je prend la position de la sourie : dans vecteur poss
        pos.append(poss) #j'incrémente dans dictionnaire pos
        buttonss.append(button)
        timess.append(time)
        core.wait(2)
        results=dict()
        for k in range(len(pos)):
            
            results['Pos']=pos[k]
            results['Buttons']=buttonss[k]
            results['Times']=timess[k]
        filename="results_"+ sub + "_" + str('%02d' % i) + ".mat"
        savemat(filename, results)
    if k == 'C':
        #AFFICHAGE CONDITION CONTROLE R-R-R-R
        crouge.draw()
        win.flip()
        core.wait(0.8)
        win.flip()
        core.wait(0.2)

        crouge.draw()
        win.flip()
        core.wait(0.8)
        win.flip()
        core.wait(0.2)

        crouge.draw()
        win.flip()
        core.wait(0.8)
        win.flip()
        core.wait(0.2)

        # crouge.draw()
        mouse.clickReset()
        # win.flip()
        # core.wait(0.8)
        # win.flip()
        # core.wait(0.2)

        # win.flip()
        # core.wait(2)

        #tant que 3scd ne se sont pas écoulé (60frame/scd)
        j=0
        time=[]
        button=[]
        while j != 120:
            if j<=48:
                crouge.draw()
                
            win.flip()
            j+=1
            buttons, times = mouse.getPressed(getTime=True)
            # if buttons[0]:
            #     print(buttons)
            #     print(times)
            # print ('le button Controle est a')
            # print (buttons)
            time.append(times)
            button.append(buttons)
            poss.append([mouse.getPos()[0], mouse.getPos()[1]]) #je prend la position de la sourie : dans vecteur poss
        pos.append(poss) #j'incrémente dans dictionnaire pos
        buttonss.append(button)
        timess.append(time)
        results=dict()
        for k in range(len(pos)):
            
            results['Pos']=pos[k]
            results['Buttons']=buttonss[k]
            results['Times']=timess[k]
        filename="results_"+ sub + "_" + str('%02d' % i) + ".mat"
        savemat(filename, results)

    if k == 'NG':
        #AFFICHAGE CONDITION NO GO B-B-B-R
        cbleu.draw()
        win.flip()
        core.wait(0.8)
        win.flip()
        core.wait(0.2)

        cbleu.draw()
        win.flip()
        core.wait(0.8)
        win.flip()
        core.wait(0.2)

        cbleu.draw()
        win.flip()
        core.wait(0.8)
        win.flip()
        core.wait(0.2)

        
        mouse.clickReset()

        # win.flip()
        # core.wait(0.8)
        # win.flip()
        # core.wait(0.2)

        # win.flip()
        # core.wait(2)

        j=0
        #tant que 3scd ne se sont pas écoulé (60frame/scd)
        time=[]
        button=[]
        while j != 120:
            if j<=48:
                crouge.draw()
                
            win.flip()
            j+=1
            buttons, times = mouse.getPressed(getTime=True)
            # if buttons[0]:
                # print(buttons)
                # print(times)
            # print ('le button No Go est a')
            # print (buttons)
            time.append(times)
            button.append(buttons)
            poss.append([mouse.getPos()[0], mouse.getPos()[1]]) #je prend la position de la sourie : dans vecteur poss
        pos.append(poss) #j'incrémente dans dictionnaire pos
        timess.append(time)
        buttonss.append(button)
        results=dict()
        for k in range(len(pos)):
            
            results['Pos']=pos[k]
            results['Buttons']=buttonss[k]
            results['Times']=timess[k]
        filename="results_"+ sub + "_" + str('%02d' % i) + ".mat"
        savemat(filename, results)


#AFFICHAGE FIN
win.close()





# %%
