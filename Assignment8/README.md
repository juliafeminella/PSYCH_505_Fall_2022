# PsychoPy keypress exercises
## 1. 
```
from psychopy import core, event, visual, monitors

mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1920, 1080])
win = visual.Window(monitor=mon, size=(400,400), color=[-1,-1,-1])

nTrials=10
my_text=visual.TextStim(win)

rt_clock = core.Clock()  # create a response time clock
cd_timer = core.CountdownTimer() #add countdown timer

for trial in range(nTrials):
    rt_clock.reset()  # reset timing for every trial
    cd_timer.add(2) #add 2 seconds

    event.clearEvents(eventType='keyboard')  # reset keys for every trial
    
    count = -1 #start the counter for the while loop
    
    while cd_timer.getTime() > 0: #for 2 seconds

        my_text.text = "trial %i" % trial
        my_text.draw()
        win.flip()

        keys = event.getKeys(keyList=['1', '2'])  #collect keypresses after first flip

        if keys:
            count=count+1 #count up the number of times a key is pressed
            
            if count == 0: #if this is the first time a key is pressed
                resp_time = rt_clock.getTime() #get RT for first response in that loop
                sub_resp = keys #get key for only the first response in that loop
```

                
    print(sub_resp, resp_time)

win.close()
```
