# Based on https://www.geeksforgeeks.org/create-stopwatch-using-python/
# Some small changes to adapt to a ms precision stopwatch
# Python program to illustrate a stop watch
# using Tkinter
# importing the required libraries
import tkinter as Tkinter
import time
import sys

PRECISION = 1000 # ms
UNIT = "ms"
REFRESH_RATE = 60
start_time = 0
REFRESH_TIME = 1
running = False

def counter_label(label):
    def count():
        global start_time
        if running:
            # To manage the initial delay.
            if start_time == 0:            
                start_time = time.time()
                display = "0" + UNIT
            else:
                counter = round((time.time() - start_time) * PRECISION)
                display = str(counter) + UNIT
   
            label['text'] = display   # Or label.config(text=display)
   
            # label.after(arg1, arg2) delays by 
            # first argument given in milliseconds
            # and then calls the function given as second argument.
            # Generally like here we need to call the 
            # function in which it is present repeatedly.
            # Delays by monitor period
            label.after(REFRESH_TIME, count) 
    # Triggering the start of the counter.
    count()     
   
# start function of the stopwatch
def Start(label):
    global running
    running = True
    counter_label(label)
    start['state'] = 'disabled'
    reset['state'] = 'normal'
   
# Reset function of the stopwatch
def Reset(label):
    global running, start_time
    start['state'] = 'normal'
    reset['state'] = 'disabled'
    label['text'] = "0" + UNIT
    running = False
    start_time = 0
   
# init
n = len(sys.argv)
if n == 2:
    REFRESH_RATE = int(sys.argv[1])
    if REFRESH_RATE > 1000:
        print("Setting to Max refresh rate (1000)")
        REFRESH_RATE = 1000
    REFRESH_TIME = round(1000/REFRESH_RATE)
        
root = Tkinter.Tk()
root["bg"] = "black"
root.title("Stopwatch")
   
# Fixing the window size.
root.minsize(width=250, height=70)
label = Tkinter.Label(root, text="0" + UNIT, fg="red", bg="black", font="Verdana 30 bold")
label.pack()
f = Tkinter.Frame(root)
start = Tkinter.Button(f, text='Start', fg="red", bg="black", width=6, command=lambda:Start(label))
reset = Tkinter.Button(f, text='Reset', fg="red", bg="black", width=6, state='disabled', command=lambda:Reset(label))
f.pack(anchor = 'center',pady=5)
start.pack(side="left")
reset.pack(side="left")
root.mainloop()