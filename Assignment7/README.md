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
    imgStartTime = wait_timer.getTime()
    core.wait(2) #wait .5 seconds, then:
    imgEndTime = wait_timer.getTime()
    
    fix_text.draw()
    win.flip()
    core.wait(2)
    
    print("Image duration was {} seconds". format(imgEndTime - imgStartTime))
    
    
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
