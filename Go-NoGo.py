#%%
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

#AFFICHAGE ECRAN NOIR
win.flip()
core.wait(0.5)

#définition cercle bleu 
cbleu=visual.Circle(win, radius=150, edges=32, units='', lineWidth=2.5, lineColor='aqua', lineColorSpace='aqua',fillColor='aqua', fillColorSpace=None)

#définition cercle rouge
crouge=visual.Circle(win, radius=150, edges=32, units='', lineWidth=2.5, lineColor='red', lineColorSpace='red',fillColor='red', fillColorSpace=None)

listecondition=['C','G','NG']
# listecondition = ['C', 'NG', 'G', 'G', 'C', 'NG', 'NG', 'NG', 'NG', 'G', 'G', 'C', 'G', 'NG', 'G', 'C', 'C', 'NG', 'G', 'G', 'G', 'NG', 'G', 'C', 'C', 'NG', 'C', 'C', 'C', 'NG', 'C', 'NG', 'C', 'NG', 'G', 'NG', 'C', 'NG', 'C', 'C', 'NG', 'G', 'G', 'C', 'C', 'C', 'G', 'G', 'NG', 'NG', 'C', 'NG', 'C', 'C', 'G', 'C', 'C', 'NG', 'C', 'G', 'NG', 'C', 'G', 'G', 'NG', 'NG', 'G', 'G', 'G', 'C', 'C', 'C', 'NG', 'NG', 'NG', 'G', 'G', 'NG', 'NG', 'G', 'NG', 'C', 'NG', 'G', 'G', 'G', 'C', 'NG', 'G', 'G']
# listecondition = ['NG', 'C', 'G', 'C', 'C', 'NG', 'NG', 'G', 'NG', 'G', 'NG', 'G', 'G', 'C', 'NG', 'G', 'NG', 'C', 'C', 'G', 'G', 'C', 'NG', 'C', 'C', 'G', 'C', 'NG', 'C', 'C', 'G', 'G', 'C', 'G', 'NG', 'C', 'NG', 'C', 'G', 'G', 'NG', 'G', 'NG', 'C', 'NG', 'C', 'NG', 'NG', 'G', 'NG', 'G', 'G', 'G', 'G', 'NG', 'NG', 'C', 'NG', 'C', 'G', 'NG', 'G', 'C', 'G', 'G', 'C', 'C', 'NG', 'C', 'NG', 'C', 'C', 'G', 'C', 'G', 'NG', 'C', 'NG', 'NG', 'NG', 'NG', 'C', 'G', 'G', 'C', 'NG', 'C', 'G', 'NG', 'G']
#listecondition=['G', 'NG', 'G', 'NG', 'NG', 'C', 'G', 'G', 'NG', 'G', 'C', 'NG','NG', 'G', 'NG', 'C', 'C', 'G', 'G', 'NG', 'C', 'G', 'G', 'NG','NG', 'G', 'G', 'C', 'C', 'C', 'C', 'G', 'G', 'G', 'NG', 'G', 'C','G', 'G', 'C', 'G', 'NG', 'NG', 'NG', 'C', 'NG', 'C', 'G', 'G','C', 'C', 'C', 'NG', 'G', 'NG', 'C', 'C', 'C', 'G', 'C', 'NG', 'C','G', 'C', 'NG', 'G', 'NG', 'C', 'C', 'NG', 'C', 'C', 'G', 'NG',
'NG', 'G', 'NG', 'G', 'C', 'C', 'NG', 'C', 'G', 'C', 'G', 'C',
'NG', 'G', 'NG', 'C', 'G', 'G', 'G', 'G', 'C', 'G', 'NG', 'NG',
'NG', 'G', 'C', 'C', 'G', 'NG', 'NG', 'C', 'C', 'C', 'NG', 'C',
'C', 'C', 'NG', 'C', 'NG', 'C', 'G', 'C', 'G', 'C', 'G', 'NG', 'G',
'NG', 'NG', 'C', 'G', 'C', 'G', 'NG', 'C', 'NG', 'NG', 'NG', 'NG',
'G', 'C', 'G', 'G', 'NG', 'C', 'G', 'G', 'NG', 'NG', 'G', 'C', 'G',
'NG', 'G', 'C', 'NG', 'C', 'NG', 'NG', 'C', 'G', 'C', 'G', 'NG',
'NG', 'NG', 'C', 'G', 'C', 'G', 'NG', 'G', 'NG', 'NG', 'C', 'G',
'NG', 'NG', 'NG', 'G', 'NG', 'C', 'C', 'G']

pos=[]
poss=[]
buttonss=[]
timess=[]

for i in range (180):
    print(i)
    k=listecondition[i]

    #initialisation sourie bas écran
    mouse=event.Mouse(win=win, visible=True, newPos=[0,-350])
    mouse.setVisible(0)
    #affichage croix blanche
    ligne=visual.Line(win, start=[-40,0], end=[40,0], lineColor="white", lineWidth=5)
    ligne.draw()
    ligne1=visual.Line(win, start=[0,-40], end=[0,40], lineColor="white", lineWidth=5)
    ligne1.draw()
    win.flip()
    core.wait(2)
    pos=[]
    timess=[]
    buttonss=[]
    
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
        mouse.setPos([0, -350])
        mouse.visible='True'
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
            mouse.setVisible(1)
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
        # core.wait(2)
        results=dict()
        for k in range(len(pos)):
            
            results['Pos']=pos[k]
            results['Buttons']=buttonss[k]
            results['Times']=timess[k]
        filename="results_gng_"+ sub + "_" + str('%02d' % i) + ".mat"
        savemat(filename, results)
    if k == 'C':
        #AFFICHAGE CONDITION CONTROLE R-R-R-R
        mouse.setVisible(0)
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
        mouse.setPos([0, -350])
        mouse.visible='True'
        # win.flip()
        # core.wait(0.8)
        # win.flip()
        # core.wait(0.2)

        # win.flip()
        # core.wait(2)

        #tant que 3scd ne se sont pas écoulé (60frame/scd)
        j=0
        poss=[]
        time=[]
        button=[]
        while j != 120:
            mouse.setVisible(1)
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
        filename="results_gng_"+ sub + "_" + str('%02d' % i) + ".mat"
        savemat(filename, results)

    if k == 'NG':
        #AFFICHAGE CONDITION NO GO B-B-B-R
        mouse.setVisible(0)
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
        mouse.setPos([0, -350])

        # win.flip()
        # core.wait(0.8)
        # win.flip()
        # core.wait(0.2)

        # win.flip()
        # core.wait(2)

        j=0
        #tant que 3scd ne se sont pas écoulé (60frame/scd)
        poss=[]
        time=[]
        button=[]
        while j != 120:
            mouse.setVisible(1)
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
        filename="results_gng_"+ sub + "_" + str('%02d' % i) + ".mat"
        savemat(filename, results)


#AFFICHAGE FIN
win.close()





# %%
import random

#listecondition = ["C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG"]
#listerandom = ["C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG","NG"]
#listecondition = ['C', 'NG', 'G', 'G', 'C', 'NG', 'NG', 'NG', 'NG', 'G', 'G', 'C', 'G', 'NG', 'G', 'C', 'C', 'NG', 'G', 'G', 'G', 'NG', 'G', 'C', 'C', 'NG', 'C', 'C', 'C', 'NG', 'C', 'NG', 'C', 'NG', 'G', 'NG', 'C', 'NG', 'C', 'C', 'NG', 'G', 'G', 'C', 'C', 'C', 'G', 'G', 'NG', 'NG', 'C', 'NG', 'C', 'C', 'G', 'C', 'C', 'NG', 'C', 'G', 'NG', 'C', 'G', 'G', 'NG', 'NG', 'G', 'G', 'G', 'C', 'C', 'C', 'NG', 'NG', 'NG', 'G', 'G', 'NG', 'NG', 'G', 'NG', 'C', 'NG', 'G', 'G', 'G', 'C', 'NG', 'G', 'G']
#listecondition=['G', 'G', 'C', 'NG', 'C', 'C', 'NG', 'G', 'NG', 'G', 'G', 'NG', 'C', 'NG', 'C', 'C', 'NG', 'NG', 'C', 'C', 'G', 'C', 'C', 'C', 'G', 'NG', 'G', 'G', 'NG', 'NG', 'G', 'NG', 'G', 'C', 'NG', 'G', 'G', 'NG', 'C', 'NG', 'C', 'G', 'C', 'NG', 'C', 'C', 'G', 'C', 'C', 'G', 'NG', 'NG', 'C', 'G', 'NG', 'G', 'NG', 'C', 'C', 'G', 'NG', 'G', 'C', 'C', 'G', 'C', 'G', 'NG', 'NG', 'C', 'C', 'G', 'NG', 'NG', 'G', 'C', 'G', 'G', 'NG', 'NG', 'NG', 'G', 'C', 'G', 'C', 'G', 'NG', 'G', 'NG', 'NG']
listecondition=['C', 'NG', 'C', 'NG', 'NG', 'C', 'C', 'NG', 'C', 'C', 'NG', 'NG', 'C', 'G', 'NG', 'NG', 'NG', 'NG', 'C', 'G', 'NG', 'C', 'C', 'C', 'G', 'NG', 'C', 'G', 'G', 'C', 'NG', 'NG', 'C', 'NG', 'NG', 'C', 'G', 'NG', 'NG', 'G', 'G', 'G', 'NG', 'NG', 'G', 'C', 'NG', 'NG', 'NG', 'NG', 'G', 'C', 'C', 'G', 'C', 'C', 'C', 'C', 'G', 'C', 'NG', 'C', 'G', 'NG', 'C', 'G', 'C', 'G', 'G', 'NG', 'C', 'C', 'G', 'G', 'NG', 'G', 'G', 'NG', 'C', 'C', 'G', 'G', 'G', 'G', 'NG', 'G', 'G', 'G', 'G', 'G']
random.shuffle(listecondition)
print (listecondition)

#listecondition = ['C', 'NG', 'G', 'G', 'C', 'NG', 'NG', 'NG', 'NG', 'G', 'G', 'C', 'G', 'NG', 'G', 'C', 'C', 'NG', 'G', 'G', 'G', 'NG', 'G', 'C', 'C', 'NG', 'C', 'C', 'C', 'NG', 'C', 'NG', 'C', 'NG', 'G', 'NG', 'C', 'NG', 'C', 'C', 'NG', 'G', 'G', 'C', 'C', 'C', 'G', 'G', 'NG', 'NG', 'C', 'NG', 'C', 'C', 'G', 'C', 'C', 'NG', 'C', 'G', 'NG', 'C', 'G', 'G', 'NG', 'NG', 'G', 'G', 'G', 'C', 'C', 'C', 'NG', 'NG', 'NG', 'G', 'G', 'NG', 'NG', 'G', 'NG', 'C', 'NG', 'G', 'G', 'G', 'C', 'NG', 'G', 'G']

# %%

# %%
