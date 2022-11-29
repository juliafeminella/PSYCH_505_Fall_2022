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

                
    print(sub_resp, resp_time)

win.close()
```
## 2.
### 2.1 - Inside the loop
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

                
    print(sub_resp, resp_time)

win.close()
```
### 2.2 - Outside the loop
```
from psychopy import core, event, visual, monitors

mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1920, 1080])
win = visual.Window(monitor=mon, size=(400,400), color=[-1,-1,-1])

nTrials=10
my_text=visual.TextStim(win)

rt_clock = core.Clock()  # create a response time clock
cd_timer = core.CountdownTimer() #add countdown timer

event.clearEvents(eventType='keyboard')  # reset keys for every trial

for trial in range(nTrials):
    rt_clock.reset()  # reset timing for every trial
    cd_timer.add(2) #add 2 seconds

    
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

                
    print(sub_resp, resp_time)

win.close()
```
### 2.3 - Indentation
```
from psychopy import core, event, visual, monitors

mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1920, 1080])
win = visual.Window(monitor=mon, size=(400,400), color=[-1,-1,-1])

nTrials=10
my_text=visual.TextStim(win)

rt_clock = core.Clock()  # create a response time clock
cd_timer = core.CountdownTimer() #add countdown timer
event.clearEvents(eventType='keyboard')  # reset keys for every trial
for trial in range(nTrials):
    rt_clock.reset()  # reset timing for every trial
    cd_timer.add(2) #add 2 seconds

    
    
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
                
    print(sub_resp, resp_time)

win.close()
```

> For the indentation, even though I tried to press the keys, no response was stored. 

# 3. Recording data
```
from psychopy import core, event, visual, monitors

#monitor specs
mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1920, 1080])
win = visual.Window(monitor=mon, size=(400,400), color=[-1,-1,-1])

#blocks, trials, stims, and clocks
nBlocks=2
nTrials=4
my_text=visual.TextStim(win)
rt_clock = core.Clock()  # create a response time clock
cd_timer = core.CountdownTimer() #add countdown timer

#prefill lists for responses
sub_resp = [[0]*nTrials]*nBlocks
sub_acc = [[0]*nTrials]*nBlocks
prob = [[0]*nTrials]*nBlocks
corr_resp = [[0]*nTrials]*nBlocks

#create problems and solutions to show
math_problems = ['1+3=','1+1=','3-2=','4-1='] #write a list of simple arithmetic
solutions = [4,2,1,3] #write solutions
prob_sol = list(zip(math_problems,solutions))

for block in range(nBlocks):
    for trial in range(nTrials):
        #what problem will be shown and what is the correct response?
        prob[block][trial] = prob_sol[np.random.choice(4)]
        corr_resp[block][trial] = prob[block][trial][1]
        
        rt_clock.reset()  # reset timing for every trial
        cd_timer.add(3) #add 3 seconds

        event.clearEvents(eventType='keyboard')  # reset keys for every trial
        
        count=-1 #for counting keys
        while cd_timer.getTime() > 0: #for 3 seconds

            my_text.text = prob[block][trial][0] #present the problem for that trial
            my_text.draw()
            win.flip()

            #collect keypresses after first flip
            keys = event.getKeys(keyList=['1','2','3','4','escape'])

            if keys:
                count=count+1 #count up the number of times a key is pressed

                if count == 0: #if this is the first time a key is pressed
                    #get RT for first response in that loop
                    resp_time[block][trial] = rt_clock.getTime()
                    #get key for only the first response in that loop
                    sub_resp[block][trial] = keys[0] #remove from list

        #record subject accuracy
        #correct- remembers keys are saved as strings
        if sub_resp[block][trial] == str(corr_resp[block][trial]):
            sub_acc[block][trial] = 1 #arbitrary number for accurate response
        #incorrect- remember keys are saved as strings              
        elif sub_resp[block][trial] != str(corr_resp[block][trial]):
            sub_acc[block][trial] = 2 #arbitrary number for inaccurate response 
                                    #(should be something other than 0 to distinguish 
                                    #from non-responses)
        
        #save data
        data_as_dict = []
            for a,b,c,d in zip(prob[block], corr_resp[block], sub_resp[block], sub_acc[block]):
                #the names listed here do not need to be the samr as the variable names
                data_as_dict.append({'problem':a,'corr_resp':b,'sub_resp':c,'sub_acc':d})
        #print results
        print(data_as_dict) 

win.close()
```
# 4. Save as csv
```
from psychopy import core, event, visual, monitors

#monitor specs
mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1920, 1080])
win = visual.Window(monitor=mon, size=(400,400), color=[-1,-1,-1])

#blocks, trials, stims, and clocks
nBlocks=2
nTrials=4
my_text=visual.TextStim(win)
rt_clock = core.Clock()  # create a response time clock
cd_timer = core.CountdownTimer() #add countdown timer

#prefill lists for responses
sub_resp = [[0]*nTrials]*nBlocks
sub_acc = [[0]*nTrials]*nBlocks
prob = [[0]*nTrials]*nBlocks
corr_resp = [[0]*nTrials]*nBlocks

#create problems and solutions to show
math_problems = ['1+3=','1+1=','3-2=','4-1='] #write a list of simple arithmetic
solutions = [4,2,1,3] #write solutions
prob_sol = list(zip(math_problems,solutions))

for block in range(nBlocks):
    for trial in range(nTrials):
        #what problem will be shown and what is the correct response?
        prob[block][trial] = prob_sol[np.random.choice(4)]
        corr_resp[block][trial] = prob[block][trial][1]
        
        rt_clock.reset()  # reset timing for every trial
        cd_timer.add(3) #add 3 seconds

        event.clearEvents(eventType='keyboard')  # reset keys for every trial
        
        count=-1 #for counting keys
        while cd_timer.getTime() > 0: #for 3 seconds

            my_text.text = prob[block][trial][0] #present the problem for that trial
            my_text.draw()
            win.flip()

            #collect keypresses after first flip
            keys = event.getKeys(keyList=['1','2','3','4','escape'])

            if keys:
                count=count+1 #count up the number of times a key is pressed

                if count == 0: #if this is the first time a key is pressed
                    #get RT for first response in that loop
                    resp_time[block][trial] = rt_clock.getTime()
                    #get key for only the first response in that loop
                    sub_resp[block][trial] = keys[0] #remove from list

        #record subject accuracy
        #correct- remembers keys are saved as strings
        if sub_resp[block][trial] == str(corr_resp[block][trial]):
            sub_acc[block][trial] = 1 #arbitrary number for accurate response
        #incorrect- remember keys are saved as strings              
        elif sub_resp[block][trial] != str(corr_resp[block][trial]):
            sub_acc[block][trial] = 2 #arbitrary number for inaccurate response 
                                    #(should be something other than 0 to distinguish 
                                    #from non-responses)
        
        #save data
        data_as_dict = []
            for a,b,c,d in zip(prob[block], corr_resp[block], sub_resp[block], sub_acc[block]):
                #the names listed here do not need to be the samr as the variable names
                data_as_dict.append({'problem':a,'corr_resp':b,'sub_resp':c,'sub_acc':d})
        #print results
        print(data_as_dict) 

win.close()
```
# 5. Save JSON
```
from psychopy import core, event, visual, monitors

#monitor specs
mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1920, 1080])
win = visual.Window(monitor=mon, size=(400,400), color=[-1,-1,-1])

#blocks, trials, stims, and clocks
nBlocks=2
nTrials=4
my_text=visual.TextStim(win)
rt_clock = core.Clock()  # create a response time clock
cd_timer = core.CountdownTimer() #add countdown timer

#prefill lists for responses
sub_resp = [[0]*nTrials]*nBlocks
sub_acc = [[0]*nTrials]*nBlocks
prob = [[0]*nTrials]*nBlocks
corr_resp = [[0]*nTrials]*nBlocks

#create problems and solutions to show
math_problems = ['1+3=','1+1=','3-2=','4-1='] #write a list of simple arithmetic
solutions = [4,2,1,3] #write solutions
prob_sol = list(zip(math_problems,solutions))

for block in range(nBlocks):
    for trial in range(nTrials):
        #what problem will be shown and what is the correct response?
        prob[block][trial] = prob_sol[np.random.choice(4)]
        corr_resp[block][trial] = prob[block][trial][1]
        
        rt_clock.reset()  # reset timing for every trial
        cd_timer.add(3) #add 3 seconds

        event.clearEvents(eventType='keyboard')  # reset keys for every trial
        
        count=-1 #for counting keys
        while cd_timer.getTime() > 0: #for 3 seconds

            my_text.text = prob[block][trial][0] #present the problem for that trial
            my_text.draw()
            win.flip()

            #collect keypresses after first flip
            keys = event.getKeys(keyList=['1','2','3','4','escape'])

            if keys:
                count=count+1 #count up the number of times a key is pressed

                if count == 0: #if this is the first time a key is pressed
                    #get RT for first response in that loop
                    resp_time[block][trial] = rt_clock.getTime()
                    #get key for only the first response in that loop
                    sub_resp[block][trial] = keys[0] #remove from list

        #record subject accuracy
        #correct- remembers keys are saved as strings
        if sub_resp[block][trial] == str(corr_resp[block][trial]):
            sub_acc[block][trial] = 1 #arbitrary number for accurate response
        #incorrect- remember keys are saved as strings              
        elif sub_resp[block][trial] != str(corr_resp[block][trial]):
            sub_acc[block][trial] = 2 #arbitrary number for inaccurate response 
                                    #(should be something other than 0 to distinguish 
                                    #from non-responses)
        
    #CSV
    import csv
    filename = 'savecsv_exercise' #leave off the extension for now, since saving multiple files
    data_dir = os.path.join(main_dir,'exp','data',filename)
    
    field_names =["problem","correct response","subject response","subject accuracy"]

    data_as_dict = []
    for a,b,c,d in zip(prob[block], corr_resp[block], sub_resp[block], sub_acc[block]):
        #the names listed here do not need to be the samr as the variable names
        data_as_dict.append({'problem':a,'corr_resp':b,'sub_resp':c,'sub_acc':d})
    with open('Names.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = field_names)
    writer.writeheader()
    writer.writerows(data_as_dict)    
    
win.close()
```
6. Read JSON
## 1. 
```
import pandas as pd #shorten name for ease of reference
df = pd.read_json(data_dir+'_block1.txt')
print(df)

print("RT mean is" + (sum(df["resp_time"])/len(df["resp_time"]))
print("Correct response mean is" + (sum(df["corr_resp"])/len(df["corr_resp"]))
print("Mean subject accuracy is" + (sum(df["sub_acc"])/len(df["sub_acc"]))
print("Mean subject response is" + (sum(df["sub_resp"])/len(df["sub_resp"]))

print("Pearson r:")
print(pd.DataFrame.corr(df,method='pearson'))
print("Spearman rho:")
print(pd.DataFrame.corr(df,method='spearman'))
```
## 2. 
```
import pandas as pd #shorten name for ease of reference
df = pd.read_json(data_dir+'_block1.txt')

acc_trials = df.loc[df['sub_acc'] == 1] #show only trials on which subject was correct
print(acc_trials)

print("RT mean is" + (sum(acc_trials["resp_time"])/len(acc_trials["resp_time"]))
print("Correct response mean is" + (sum(acc_trials["corr_resp"])/len(acc_trials["corr_resp"]))
print("Mean subject accuracy is" + (sum(acc_trials["sub_acc"])/len(acc_trials["sub_acc"]))
print("Mean subject response is" + (sum(acc_trials["sub_resp"])/len(acc_trials["sub_resp"]))

print("Pearson r:")
print(pd.DataFrame.corr(acc_trials,method='pearson'))
print("Spearman rho:")
print(pd.DataFrame.corr(acc_trials,method='spearman'))
```
## 3. 
```
import pandas as pd #shorten name for ease of reference
df = pd.read_json(data_dir+'_block1.txt')

resp_trials = df.loc[df['sub_acc'] != 0] #show only trials on which subject was correct
print(resp_trials)

print("RT mean is" + (sum(resp_trials["resp_time"])/len(resp_trials["resp_time"]))
print("Correct response mean is" + (sum(resp_trials["corr_resp"])/len(resp_trials["corr_resp"]))
print("Mean subject accuracy is" + (sum(resp_trials["sub_acc"])/len(resp_trials["sub_acc"]))
print("Mean subject response is" + (sum(resp_trials["sub_resp"])/len(resp_trials["sub_resp"]))

print("Pearson r:")
print(pd.DataFrame.corr(resp_trials,method='pearson'))
print("Spearman rho:")
print(pd.DataFrame.corr(resp_trials,method='spearman'))
```
