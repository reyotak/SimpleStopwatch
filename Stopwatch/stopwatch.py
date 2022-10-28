# Python program to illustrate a stop watch
# using Tkinter
# importing the required libraries
import tkinter as Tkinter
import time

PRECISION = 1000 # ms
UNIT = "ms"
start_time = 0
running = False

def counter_label(label):
    def count():
        global start_time
        if running:
            # To manage the initial delay.
            if start_time == 0:            
                display = "Starting..."
                start_time = time.time()
            else:
                counter = round((time.time() - start_time) * PRECISION)
                display = str(counter) + UNIT
   
            label['text'] = display   # Or label.config(text=display)
   
            # label.after(arg1, arg2) delays by 
            # first argument given in milliseconds
            # and then calls the function given as second argument.
            # Generally like here we need to call the 
            # function in which it is present repeatedly.
            # Delays by 1000ms=1 seconds and call count again.
            label.after(1, count) 
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