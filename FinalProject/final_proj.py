#=====================
#IMPORT MODULES
#=====================
import numpy as np
from psychopy import visual, gui, core, event, visual, monitors
import pandas as pd
import json #-import file save functions
import os #-(import other functions as necessary: os...)
from datetime import datetime

#=====================
#PATH SETTINGS
#=====================
#-define the main directory where you will keep all of your experiment files
main_dir = os.getcwd()

#-define the directory where you will save your data
path = os.path.join(main_dir, 'data')

#-if you will be presenting images, define the image directory
image_dir = os.path.join(main_dir,'images')

#=====================
#COLLECT PARTICIPANT INFO
#=====================
#create dictionary
exp_info = {'session':1,'subject_nr':'', 'age':'', 'handedness':('right','left','ambi'), 
            'gender':'' 
            }
#-create a dialogue box that will collect current participant number, age, gender, handedness
my_dlg = gui.DlgFromDict(dictionary=exp_info, 
                         title='subject info',  
                         fixed=['session'], 
                         order=['session','subject_nr','age','gender','handedness'])

exp_info['date'] = datetime.now() 
filename = (str(exp_info['subject_nr']) + '_outputFile.csv')

#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
# Define number of trials and blocks
nTrials = 16
nBlocks = 2
totalTrials = nTrials*nBlocks
nEach = int(totalTrials/4)

#define the monitor parameters
mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1600,900])
win = visual.Window(monitor=mon) #define a window

#Prepare data collection lists
# Create empty lists to compute colours, accuracy, rt, trial and block number
condition = [0]*totalTrials
response = [0]*totalTrials
responseTimes = [0]*totalTrials
trialNumbers = [0]*totalTrials
blockNumbers = [0]*totalTrials

# Define stimulus properties 
## Texts
instructText = visual.TextStim(win, text='Welcome to the experiment. You will be presented with a series of images and asked to judge their likeability. You will indicate your response with the keyboard. Press: [1] = very deslikable, [2] = somewhat deslikable, [3] = not likeable nor deslikable, [4] = somewaht likeable, [5] = very likeable. Press any key to begin the experiment.')
endingText = visual.TextStim(win, text = 'Thank you for completing this experiment! Press any key to exit')

#Fixation cross
fix_text = visual.TextStim(win, text = "+")

# Define lists with stimulus names
stims = ['pic1.jpeg','pic2.jpeg','pic3.jpeg','pic4.jpeg','pic5.jpeg','pic6.jpeg','pic7.jpeg','pic8.jpeg','pic9.jpeg','pic10.jpeg','pic11.jpeg','pic12.jpeg','pic13.jpeg','pic14.jpeg','pic15.jpeg','pic16.jpeg']*2 #create a list if images to show
classification = ['shapeless robot']*nEach + ['human features']*nEach + ['human like']*nEach + ['very human like']*nEach #List of possible conditions
trials = list(zip(stims,classification*nBlocks)) 
np.random.shuffle(trials)
my_image = visual.ImageStim(win)

#=====================
#START EXPERIMENT
#=====================
# Present instruction text 
instructText.draw()
win.flip()
event.waitKeys()  #wait for keypress

# Define timer for trials 
rt_timer = core.Clock()

#=====================
#BLOCK SEQUENCE
#=====================
for iblock in range(nBlocks):
    # Define and draw start of the block text
    instructText.text = 'Press any key to begin Block ' + str(iblock+1)
    instructText.draw() # Draw start of block text
    win.flip() # Flip (present) start of the block text
    event.waitKeys()

    for trial in range(nTrials): #loop through trials
        # Set counters for blocks and trials
        overallTrial = iblock*nTrials+trial
        blockNumbers[overallTrial] = iblock+1
        trialNumbers[overallTrial] = trial+1
        condition[overallTrial] = trials[overallTrial][1]

        #Set stimuli
        my_image.image = os.path.join(image_dir,trials[overallTrial][0])
        
        #=====================
        #START TRIAL
        #===================== 

        # Draw fixation cross
        fix_text.draw() #-draw fixation
        win.flip() #-flip window
        core.wait(.5) #-wait time (stimulus duration)
        
        rt_timer.reset()
        event.clearEvents(eventType='keyboard')
        
        #Present images
        my_image.draw() #draw
        win.flip() #show
        keys = event.waitKeys(keyList=['1', '2', '3','4','5']) #waits for 2 seconds then continues
        if keys:
            response[overallTrial]= keys
            print('Block:', iblock+1, 'Trial:', trial +1, 'Condition:', trials[trial][1], 'RT:', rt_timer.getTime(), 'Response:', keys) #get time at which the subject made a keypress
        
# Export data to csv file
df = pd.DataFrame(data={
 "Block Number": blockNumbers, 
 "Trial Number": trialNumbers, 
 "Condition": condition, 
 "Response": response, 
 "Response Time": responseTimes
})
df.to_csv(os.path.join(path, filename), sep=',', index=False)

#======================
# END OF EXPERIMENT
#======================        
# Present ending text
endingText.draw()
win.flip()
event.waitKeys()  #wait for keypress

#-close window    
win.close() #close the window after trials have looped 