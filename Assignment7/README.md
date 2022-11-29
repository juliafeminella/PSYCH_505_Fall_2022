 # Wait exercises
 ```
 #=====================
        #START TRIAL
        #===================== 
        #-draw fixation
        fix_target.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        core.wait(0.5)

        #-draw image
        my_image.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        core.wait(0.5)
        trial_timer.getTime()

        
        #-draw end trial text
        my_text.text = end_trial_msg
        my_text.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        core.wait(3)
```

# Clock exercises
## 1
```
from psychopy import visual
from psychopy import gui
from psychopy import core
from psychopy import visual, monitors
from datetime import datetime
import os

#=====================
#PATH SETTINGS
#=====================
#-define the main directory where you will keep all of your experiment files
main_dir = os.getcwd()

#-define the directory where you will save your data
data_dir = os.path.join(main_dir,'data')

#-if you will be presenting images, define the image directory
image_dir = os.path.join(main_dir,'images')

#define the monitor parameters
mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1600,900])
win = visual.Window(monitor=mon) #define a window

my_image = visual.ImageStim(win)

stims = ['face01.jpg','face02.jpg','face03.jpg'] #create a list if images to show
nTrials=3 #create a number of trials for your images

end_trial_msg = "End of trial"
end_trial_text = visual.TextStim(win, text = end_trial_msg)
fix_text = visual.TextStim(win, text = "+")

wait_timer = core.Clock()

for trial in range(nTrials): #loop through trials
    
    my_image.image = os.path.join(image_dir,stims[trial])
    
    fix_text.draw()
    win.flip()
    core.wait(2)
    
    my_image.draw() #draw
    win.flip() #show
    Start_time = wait_timer.getTime()
    core.wait(2) #wait .5 seconds, then:
    End_time = wait_timer.getTime()
    
    fix_text.draw()
    win.flip()
    core.wait(2)
    
    print("Image duration was {} seconds". format(End_time - Start_time))
    
    
win.close() #close the window after trials have looped 
```
> Image duration was 1.9998066000007384 seconds. It seems to be reasonably precise 

## 2. 
```
from psychopy import visual
from psychopy import gui
from psychopy import core
from psychopy import visual, monitors
from datetime import datetime
import os

#=====================
#PATH SETTINGS
#=====================
#-define the main directory where you will keep all of your experiment files
main_dir = os.getcwd()

#-define the directory where you will save your data
data_dir = os.path.join(main_dir,'data')

#-if you will be presenting images, define the image directory
image_dir = os.path.join(main_dir,'images')

#define the monitor parameters
mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1600,900])
win = visual.Window(monitor=mon) #define a window

my_image = visual.ImageStim(win)

stims = ['face01.jpg','face02.jpg','face03.jpg', 'face04.jpg', 'face05.jpg'] #create a list if images to show
nTrials=5 #create a number of trials for your images
nBlocks= 2

end_trial_msg = "End of trial"
end_trial_text = visual.TextStim(win, text = end_trial_msg)
fix_text = visual.TextStim(win, text = "+")

clock_wait_timer = core.Clock()
pres_timer = core.Clock()

for block in range(nBlocks):
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    for trial in range(nTrials):
        #-set stimuli and stimulus properties for the current trial
        my_image.image = os.path.join(image_dir,stims[trial])
        
        #reset stimulus presentation timer right before the first stimulus should appear
        clock_wait_timer.reset()
        #-draw stimulus
        Start_time = clock_wait_timer.getTime()
        while pres_timer.getTime() <=2: #2 seconds
            my_image.draw() #draw
            win.flip() #show
        End_time= clock_wait_timer.getTime()

        print("Image presentation lasted {} seconds".format(End_time - Start_time))

win.close() #close the window after trials have looped  
```
> Image presentation 1.9805755999987014 seconds, It was slightly less precise. 

## 3.
```
#=====================
#PATH SETTINGS
#=====================
#-define the main directory where you will keep all of your experiment files
main_dir = os.getcwd()

#-define the directory where you will save your data
data_dir = os.path.join(main_dir,'data')

#-if you will be presenting images, define the image directory
image_dir = os.path.join(main_dir,'images')

#define the monitor parameters
mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1600,900])
win = visual.Window(monitor=mon) #define a window

my_image = visual.ImageStim(win)

stims = ['face01.jpg','face02.jpg','face03.jpg', 'face04.jpg', 'face05.jpg'] #create a list if images to show
nTrials=5 #create a number of trials for your images

end_trial_msg = "End of trial"
end_trial_text = visual.TextStim(win, text = end_trial_msg)
fix_text = visual.TextStim(win, text = "+")

countdown_timer = core.Clock()
pres_timer = core.CountdownTimer()

#=====================
#TRIAL SEQUENCE
#=====================    
for trial in range(nTrials):
    #-set stimuli and stimulus properties for the current trial
    my_image.image = os.path.join(image_dir,stims[trial])
        
    #reset stimulus presentation timer right before the first stimulus should appear
    pres_timer.reset()
    pres_timer.add(2)
    #-draw stimulus
    Start_time = countdown_timer.getTime()
    while pres_timer.getTime() > 0:
        my_image.draw() #draw
        win.flip() #show
    End_time= countdown_timer.getTime()

    fix_text.draw()
    win.flip()
    core.wait(2)

    print("Image presentation lasted {} seconds".format(End_time - Start_time))

win.close() #close the window after trials have looped
```
> Image presentation lasted 2.007031899998765 seconds. It seems to be slightly more precise, though there isn't too much of a difference. 

## 4. 
```
#=====================
#IMPORT MODULES
#=====================
#-import numpy and/or numpy functions *
import numpy as np

#-import psychopy functions
from psychopy import core, gui, visual, event, 

#-import file save functions
import json

#-(import other functions as necessary: os...)
import os
import datetime
from datetime import datetime


#=====================
#PATH SETTINGS
#=====================
#-define the main directory where you will keep all of your experiment files
main_dir = os.getcwd()

#-define the directory where you will save your data
data_dir = os.path.join(main_dir,'data')

#-if you will be presenting images, define the image directory
image_dir = os.path.join(main_dir,'images')

#-check that these directories exist
os.path.isdir(main_dir)
if not os.path.isdir(main_dir):
    raise Exception("Could not find the path!")

os.path.isdir(data_dir)
if not os.path.isdir(data_dir):
    raise Exception("Could not find the path!")

os.path.isdir(image_dir)
if not os.path.isdir(image_dir):
    raise Exception("Could not find the path!")

#=====================
#COLLECT PARTICIPANT INFO
#=====================
#create dictionary
exp_info = {'session':1,'subject_nr':0, 'age':0, 'handedness':('right','left','ambi'), 
            'gender':'' 
            }
#-create a dialogue box that will collect current participant number, age, gender, handedness
my_dlg = gui.DlgFromDict(dictionary=exp_info, 
                         title='subject info',  
                         fixed=['session'], 
                         order=['session','subject_nr','age','gender','handedness'])

#get date and time
date = datetime.now()
exp_info['date'] = str(date.day) + str(date.month) + str(date.year)
print(exp_info['date'])

#-create a unique filename for the data
filename = str(exp_info['subject_nr']) + '_' + exp_info['date'] + '.csv'

main_dir = os.getcwd() #define the main directory where experiment info is stored
sub_dir = os.path.join(main_dir,'sub_info',filename) #create a subject info directory to save subject info


#=====================
#STIMULUS AND TRIAL SETTINGS
#=====================
#-number of trials and blocks *
nTrials = 10
nBlocks = 2

#-stimulus names (and stimulus extensions, if images) *
stims = ['face01.jpg', 'face02.jpg', 'face03.jpg', 'face04.jpg', 'face05.jpg',
         'face06.jpg', 'face07.jpg', 'face08.jpg', 'face09.jpg', 'face10.jpg']

#-stimulus properties like size, orientation, location, duration *
s_size = [200,200]
s_location= [0,0]
s_duration = 1

#-start message text *
startMessage = "Hello! Press Enter to begin."

#=====================
#PREPARE DATA COLLECTION LISTS
#=====================
#-create an empty list for correct responses (e.g., "on this trial, a response of X is correct") *
correct_responses = []

#-create an empty list for participant responses (e.g., "on this trial, response was a X") *
participant = []

#-create an empty list for response accuracy collection (e.g., "was participant correct?") *
accuracy = []

#-create an empty list for response time collection *
response_time = []

#-create an empty list for recording the order of stimulus identities *
order_identities = []

#-create an empty list for recording the order of stimulus properties *
order_properties = []

#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
#define the monitor parameters
mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1600,900])

#-define the window (size, color, units, fullscreen mode) using psychopy functions
win = visual.Window(monitor=mon) #define a window

#-define stimuli using psychopy functions
my_image = visual.ImageStim(win)

end_trial_msg = "End of trial"
end_trial_text = visual.TextStim(win, text = end_trial_msg)
fix_text = visual.TextStim(win, text = "+")

#define the countdown clock at the beginning of the experiment
pres_timer = core.CountdownTimer()
block_timer = core.Clock()
trial_timer = core.Clock()

#=====================
#START EXPERIMENT
#=====================
#-present start message text
start_text.draw()
win.flip()
#-allow participant to begin experiment with button press
event.waitKeys()

#=====================
#BLOCK SEQUENCE
#=====================
#-for loop for nBlocks *
for block in range(nBlocks):
    block_timer.reset()
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    for trial in range(nTrials):
        trial_timer.reset()
        #-set stimuli and stimulus properties for the current trial
        #point to a different filename for each image
        my_image.image = os.path.join(image_dir,stims[trial])
    
        #reset stimulus presentation timer right before the first stimulus should appear
        pres_timer.reset()
        pres_timer.add(3) #add 3 seconds because your trial is 3 seconds
        #-draw stimulus
        while pres_timer.getTime() >= 2: #1 second
            fix_text.draw() #draw
            win.flip() #show  
        while 0 <= pres_timer.getTime() < 2: #2 seconds
            my_image.draw() #draw
            fix_text.draw() #draw fixation on top of the image
            win.flip() #show  
            
win.close()  
```
