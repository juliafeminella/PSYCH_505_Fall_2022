# Dialog box exercises

```
from psychopy import gui
from psychopy import core
from psychopy import visual, monitors
from datetime import datetime
import os

#create dictionary
exp_info = {'session':1,'subject_nr':0, 'age':0, 'handedness':('right','left','ambi'), 
            'gender':'' 
            }

print(exp_info)

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

# Monitor exercises

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
