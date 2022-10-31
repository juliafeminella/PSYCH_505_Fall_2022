All the answers were included in the following code. For the import modules exercises, see #IMPORT MODULES. For the directory exercises, refer to #PATH SETTINGS and #PREPARE CONDITION LISTS. 

```
#=====================
#IMPORT MODULES
#=====================
#-import numpy and/or numpy functions *
import numpy as np

#-import psychopy functions
from psychopy import core, gui, visual, event

#-import file save functions
import json

#-(import other functions as necessary: os...)
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
#-create a dialogue box that will collect current participant number, age, gender, handedness
#get date and time
#-create a unique filename for the data

#=====================
#STIMULUS AND TRIAL SETTINGS
#=====================
#-number of trials and blocks *
nTrials = 10
nBlocks = 2

#-stimulus names (and stimulus extensions, if images) *
pics = []
for i in range (1,11):
  pics.append('pic'+"{}".format(i)+ '.png')

#-stimulus properties like size, orientation, location, duration *
s_size = [200,200]
s_location= [0,0]
s_duration = 1

#-start message text *
startMessage = "Hello! Press Enter to begin."

#=====================
#PREPARE CONDITION LISTS
#=====================
#-check if files to be used during the experiment (e.g., images) exist
ims_in_dir = sorted(os.listdir(image_dir))

for pic in pics :
  if pic == ims_in_dir:
    print("%i was found!" %pic)
  else :
    raise Exception("The image was not found!")

#-create counterbalanced list of all conditions *
conditions = pics.copy() # SInce there's only one stimuli being presented, the conditions would simply be a randomization of images
np.random.shuffle(conditions)

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
#-define the monitor settings using psychopy functions
#-define the window (size, color, units, fullscreen mode) using psychopy functions
#-define experiment start text unsing psychopy functions
#-define block (start)/end text using psychopy functions
#-define stimuli using psychopy functions
#-create response time clock
#-make mouse pointer invisible

#=====================
#START EXPERIMENT
#=====================
#-present start message text
#-allow participant to begin experiment with button press

#=====================
#BLOCK SEQUENCE
#=====================
#-for loop for nBlocks *
for block in nBlocks :
    #-present block start message
    print("This is the start of a new block")
    #-randomize order of trials here *
    np.random.shuffle(pics)

    #-reset response time clock here
    
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials *
    for trial in nTrials :
        #-set stimuli and stimulus properties for the current trial
        #-empty keypresses
        
        #=====================
        #START TRIAL
        #=====================   
        #-draw stimulus
        #-flip window
        #-wait time (stimulus duration)
        #-draw stimulus
        #-...
        
        #-collect subject response for that trial
        #-collect subject response time for that trial
        #-collect accuracy for that trial
        
#======================
# END OF EXPERIMENT
#======================        
#-write data to a file
#-close window
#-quit experiment
``` 
