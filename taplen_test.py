#%%

from turtle import pos
import psychopy
from psychopy import visual, core, event
from scipy.io import savemat
import random
from pathlib import Path
from psychopy.hardware import keyboard


#%% tap length
#                                                                                                                                                          # %%
sub='sub-88VP'

kb=keyboard.Keyboard()
conds=['600', '1200', '1000', '800', '800', '1200', '1200', '600', '800',
       '400', '1200', '1600', '1200', '400', '400', '600', '800', '600',
       '400', '400', '1400', '600', '1000', '400', '1000', '1600', '800',
       '1000', '1400', '1400', '1600', '1400', '1400', '600', '400',
       '1200', '1600', '1200', '1000', '800', '600', '1600', '400',
       '1000', '1600', '600', '400', '800', '1600', '1400', '800', '1200',
       '1000', '1000', '1600', '1200', '400', '1400', '1400', '800',
       '1200', '1000', '600', '1000', '1600', '800', '1400', '1400',
       '600', '1600']
# conds=['400', '600', '800', '1000', '1200', '1400', '1600']
# conds=['400', '600', '800', '1000']
win = psychopy.visual.Window(
    size=[400, 400],
    units="pix",
    fullscr=True,
    color="black",
    screen=1
)
rect=visual.Circle(win, radius=100,fillColor="grey", lineWidth=5, lineColor="grey",pos=[0,0] )

keys=[]
clock=core.Clock()

for cond in conds:
    # clock=core.Clock()
    event.clearEvents()
    ligne=visual.Line(win, start=[-40,0], end=[40,0], lineColor="white", lineWidth=5)
    ligne1=visual.Line(win, start=[0,-40], end=[0,40], lineColor="white", lineWidth=5)
    ligne.draw()
    ligne1.draw()
    win.flip()
    core.wait(1.5)
    win.flip()
    core.wait(1.5)
    if cond=="400":

        rect.draw()
        win.flip()
        core.wait(0.4)
        text=visual.TextStim(win,height=50, text="Reproduction", color="white")
        text.draw()
        win.flip()
        core.wait(0.5)
        # rect.draw()
        win.flip()
        clock.reset()
        key=kb.waitKeys(keyList=['space', 'esc'])
        # key=event.getKeys(keyList=['space', 'esc'])
        core.wait(3)
        if 'space'in key:
            
            keys.append(key[0].duration)
        if 'escape' in key:
            win.close()
            core.quit()
    if cond=="600":

        rect.draw()
        win.flip()
        core.wait(0.6)
        text=visual.TextStim(win,height=50, text="Reproduction", color="white")
        text.draw()
        win.flip()
        core.wait(0.5)
        # rect.draw()
        win.flip()
        clock.reset()
        key=kb.waitKeys(keyList=['space', 'esc'])
        core.wait(3)

        if 'space'in key:
            
            keys.append(key[0].duration)
        if 'escape' in key:
            win.close()
            core.quit()

    if cond=="800":

        rect.draw()
        win.flip()
        core.wait(0.8)
        text=visual.TextStim(win,height=50, text="Reproduction", color="white")
        text.draw()
        win.flip()
        core.wait(0.5)
        # rect.draw()
        win.flip()
        clock.reset()
        key=kb.waitKeys(keyList=['space', 'esc'])
        core.wait(3)
 
        if 'space'in key:
            
            keys.append(key[0].duration)
        if 'escape' in key:
            win.close()
            core.quit()

    if cond=="1000":

        rect.draw()
        win.flip()
        core.wait(1)
        text=visual.TextStim(win,height=50, text="Reproduction", color="white")
        text.draw()
        win.flip()
        core.wait(0.5)
        # rect.draw()
        win.flip()
        clock.reset()
        key=kb.waitKeys(keyList=['space', 'esc'])
        core.wait(3)
        
        if 'space'in key:
            
            keys.append(key[0].duration)
        if 'escape' in key:
            win.close()
            core.quit()

    if cond=="1200":

        rect.draw()
        win.flip()
        core.wait(1.2)
        text=visual.TextStim(win,height=50, text="Reproduction", color="white")
        text.draw()
        win.flip()
        core.wait(0.5)
        # rect.draw()
        win.flip()
        clock.reset()
        key=kb.waitKeys(keyList=['space', 'esc'])
        core.wait(3)

        if 'space'in key:
           
            keys.append(key[0].duration)
        if 'escape' in key:
            win.close()
            core.quit()
    if cond=="1400":

        rect.draw()
        win.flip()
        core.wait(1.4)
        text=visual.TextStim(win,height=50, text="Reproduction", color="white")
        text.draw()
        win.flip()
        core.wait(0.5)
        # rect.draw()
        win.flip()
        clock.reset()
        key=kb.waitKeys(keyList=['space', 'esc'])
        core.wait(3)

        if 'space'in key:
            
            keys.append(key[0].duration)
        if 'escape' in key:
            win.close()
            core.quit()

    if cond=="1600":

        rect.draw()
        win.flip()
        core.wait(1.6)
        text=visual.TextStim(win,height=50, text="Reproduction", color="white")
        text.draw()
        win.flip()
        core.wait(0.5)
        # rect.draw()
        win.flip()
        clock.reset()
        key=kb.waitKeys(keyList=['space', 'esc'])
        core.wait(3)

        if 'space'in key:
            
            keys.append(key[0].duration)
        if 'escape' in key:
            win.close()
            core.quit()
filename='E:/Manip/Psych/psych/results_timerep_' + sub + '_taplen.mat'
results=dict({sub:keys})

savemat(filename, results)
win.close()
                                                                                                                                                                # %%
#%%

from scipy.io import loadmat

mat=loadmat('results_timerep_sub-00test_onetap.mat')
# %%
# #%% one tap
# sub='sub-test'

# kb=keyboard.Keyboard()
# # conds=['400', '600', '800', '1000', '1200', '1400', '1600']

# conds=['600', '1200', '1000', '800', '800', '1200', '1200', '600', '800',
#        '400', '1200', '1600', '1200', '400', '400', '600', '800', '600',
#        '400', '400', '1400', '600', '1000', '400', '1000', '1600', '800',
#        '1000', '1400', '1400', '1600', '1400', '1400', '600', '400',
#        '1200', '1600', '1200', '1000', '800', '600', '1600', '400',
#        '1000', '1600', '600', '400', '800', '1600', '1400', '800', '1200',
#        '1000', '1000', '1600', '1200', '400', '1400', '1400', '800',
#        '1200', '1000', '600', '1000', '1600', '800', '1400', '1400',
#        '600', '1600']
# win = psychopy.visual.Window(
#     size=[400, 400],
#     units="pix",
#     fullscr=True,
#     color="black",
#     screen=1
# )
# rect=visual.Circle(win, radius=100,fillColor="white", lineWidth=5, lineColor=[1, 1, 1],pos=[0,0] )

# keys=[]
# clock=core.Clock()

# for cond in conds:
#     # clock=core.Clock()
#     event.clearEvents()
#     ligne=visual.Line(win, start=[-40,0], end=[40,0], lineColor="white", lineWidth=5)
#     ligne1=visual.Line(win, start=[0,-40], end=[0,40], lineColor="white", lineWidth=5)
#     ligne.draw()
#     ligne1.draw()
#     win.flip()
#     core.wait(1.5)
#     win.flip()
#     core.wait(1.5)
#     if cond=="400":

#         rect.draw()
#         win.flip()
#         core.wait(0.4)
#         text=visual.TextStim(win,height=50, text="Reproduction", color="white")
#         text.draw()
#         win.flip()
#         core.wait(0.5)
#         rect.draw()
#         win.flip()
#         clock.reset()
#         key=event.waitKeys(keyList=['space', 'esc'], timeStamped=clock)
#         if 'space'in key[0]:
            
#             keys.append(key[0])
#         if 'esc' in key[0]:
#             win.close()
#     if cond=="600":

#         rect.draw()
#         win.flip()
#         core.wait(0.6)
#         text=visual.TextStim(win,height=50, text="Reproduction", color="white")
#         text.draw()
#         win.flip()
#         core.wait(0.5)
#         rect.draw()
#         win.flip()
#         clock.reset()
#         key=event.waitKeys(keyList=['space', 'esc'], timeStamped=clock)
#         if 'space'in key[0]:
            
#             keys.append(key[0])
#         if 'esc' in key[0]:
#             win.close()

#     if cond=="800":

#         rect.draw()
#         win.flip()
#         core.wait(0.8)
#         text=visual.TextStim(win,height=50, text="Reproduction", color="white")
#         text.draw()
#         win.flip()
#         core.wait(0.5)
#         rect.draw()
#         win.flip()
#         clock.reset()
#         key=event.waitKeys(keyList=['space', 'esc'], timeStamped=clock)
#         if 'space'in key[0]:
            
#             keys.append(key[0])
#         if 'esc' in key[0]:
#             win.close()

#     if cond=="1000":

#         rect.draw()
#         win.flip()
#         core.wait(1)
#         text=visual.TextStim(win,height=50, text="Reproduction", color="white")
#         text.draw()
#         win.flip()
#         core.wait(0.5)
#         rect.draw()
#         win.flip()
#         clock.reset()
#         key=event.waitKeys(keyList=['space', 'esc'], timeStamped=clock)
#         if 'space'in key[0]:
            
#             keys.append(key[0])
#         if 'esc' in key[0]:
#             win.close()

#     if cond=="1200":

#         rect.draw()
#         win.flip()
#         core.wait(1.2)
#         text=visual.TextStim(win,height=50, text="Reproduction", color="white")
#         text.draw()
#         win.flip()
#         core.wait(0.5)
#         rect.draw()
#         win.flip()
#         clock.reset()
#         key=event.waitKeys(keyList=['space', 'esc'], timeStamped=clock)
#         if 'space'in key[0]:
           
#             keys.append(key[0])
#         if 'esc' in key[0]:
#             win.close()
#     if cond=="1400":

#         rect.draw()
#         win.flip()
#         core.wait(1.4)
#         text=visual.TextStim(win,height=50, text="Reproduction", color="white")
#         text.draw()
#         win.flip()
#         core.wait(0.5)
#         rect.draw()
#         win.flip()
#         clock.reset()
#         key=event.waitKeys(keyList=['space', 'esc'], timeStamped=clock)
#         if 'space'in key[0]:
            
#             keys.append(key[0])
#         if 'esc' in key[0]:
#             win.close()

#     if cond=="1600":

#         rect.draw()
#         win.flip()
#         core.wait(1.6)
#         text=visual.TextStim(win,height=50, text="Reproduction", color="white")
#         text.draw()
#         win.flip()
#         core.wait(0.5)
#         rect.draw()
#         win.flip()
#         clock.reset()
#         key=event.waitKeys(keyList=['space', 'esc'], timeStamped=clock)
#         if 'space'in key[0]:
            
#             keys.append(key[0])
#         if 'esc' in key[0]:
#             win.close()
# filename='results_timerep_' + sub + '_onetap.mat'

# results=dict({sub:keys})

# savemat(filename, results)


# win.close()
