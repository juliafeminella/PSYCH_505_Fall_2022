# Dialog box exercises

Before starting the exercise I'm importing what I'll need

```
from psychopy import gui
from psychopy import core
from psychopy import visual, monitors
from datetime import datetime
import os
```
1. Edit the dictionary "exp_info" so you have a variable called "session", with "1" preset as the session number.
2. Edit the "gender" variable in "exp_info" so the subject can write in whatever they want into an empty box, instead of the drop-down list
```
#create dictionary
exp_info = {'session':1,'subject_nr':0, 'age':0, 'handedness':('right','left','ambi'), 
            'gender':'' 
            }

print(exp_info)
```

Using DlgFromDict:

1. Customize my_dlg so that you have a title for your dialog box: "subject info".
2. Set the variable "session" as fixed. What happens?
3. Set the order of the variables as session, subject_nr, age, gender, handedness.
4. Once you have done all of the above, don't show "my_dlg" right away. Tell your experiment to print "All variables have been created! Now ready to show the dialog box!". Then, show the dialog box.
5. Fill in the following pseudocode with the real code you have learned so far:

```
print("All variables have been created! Now ready to show the dialog box!")

#=====================
#COLLECT PARTICIPANT INFO
#=====================
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
```

> When you set a variable as 'fixed' a field that can't be edited is added to the dialog box. 

# Monitorand window exercises

1. How does changing "units" affect how you define your window size?
> In Psychopy you can specify your stimulus in various unities of measure and the program will calculate the appropriate pixel size for you. Changing the unity might result in different sizes and angles

2. How does changing colorSpace affect how you define the color of your window? Can you define colors by name?
> The name of the color space currently being used. Changing color space will change the color from the default to a new selected color. There are three basic color spaces that PsychoPy® can use, RGB, DKL and LMS but colors can also be specified by a name (e.g. ‘DarkSalmon’) or by a hexadecimal string (e.g. ‘#00FF00’), given that this name is one of the 140 currently supported HTML colors. Psychopy will conver this to a RGB space.

3. Fill in the following pseudocode with the real code you have learned so far:
```
#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
#-define the monitor settings using psychopy functions
mon = monitors.Monitor('myMonitor', width=35.56, distance=60) 

#-define the window (size, color, units, fullscreen mode) using psychopy functions
mon.setSizePix([1600,900])

win = visual.Window(monitor=mon, size=(800,800), color=[-1,-1,-1])
```

# Stimulus exercises
For this, I included all the answers in one code. I hope that's okay. 

Check the psychopy help page on "ImageStim" to help you solve these exercises:

1. Write a short script that shows different face images from the image directory at 400x400 pixels in size. What does this do to the images? How can you keep the proper image dimensions and still change the size?
2. Write a short script that makes one image appear at a time, each in a different quadrant of your screen (put the window in fullscreen mode). Think about how you can calculate window locations without using a trial-and-error method.
3. Create a fixation cross stimulus (hint:text stimulus).
4. Fill in the following pseudocode with the real code you have learned so far:

```
import numpy as np

#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
#-define experiment start text unsing psychopy functions
start_msg = 'Welcome to my experiment!'
my_text = visual.TextStim(win, text=start_msg)

#-define block (start)/end text using psychopy functions
block_msg = "Press any key to continue to the next block."
end_trial_msg = "End of trial. Press any key to continue."

#-define stimuli using psychopy functions (images, fixation cross)
os.chdir('/home/shoarly/Documents/pytutorial/exp') 
main_dir = os.getcwd() 
image_dir = os.path.join(main_dir,'images') 

pic_loc = os.path.join(image_dir,'face01.jpg') #point to the specific image

my_image = visual.ImageStim(win, image=pic_loc, units = 'pix', size = [400,400]) #image= the specific image (the entire directory)

stims = ['face01.png', 'face02.png','face03.png','face04.png']

fix_target = TextStim(win, '+') # create fixation cross

nBlocks= 2
nTrials= 4

#=====================
#START EXPERIMENT
#=====================
#-present start message text
my_text = visual.TextStim(win) #create the text stimulus but don't define the text yet

my_text.text = start_msg #define the text
my_text.draw()
win.flip() #show

#-allow participant to begin experiment with button press
event.waitKeys() #wait for keypress

win.close() #close the window

#=====================
#BLOCK SEQUENCE
#=====================
#-for loop for nBlocks
for block in range(nBlocks):
    #-present block start message
    my_text.text = block_msg #define the text
    my_text.draw()
    win.flip()
    event.waitKeys() #wait for keypress
    
    #-randomize order of trials here
    np.random.shuffle(stims)
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials
    for trial in range(nTrials):
        #-set stimuli and stimulus properties for the current trial
        my_image.image = os.path.join(image_dir,stims[trial])
        

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
        
        #-draw end trial text
        my_text.text = end_trial_msg
        my_text.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        event.waitKeys()
        
#======================
# END OF EXPERIMENT
#======================        
#-close window
win.close()
```
