from threading import Thread, current_thread

def disp():
    print("child Thread object", current_thread())
    
t = Thread(target = disp)
t.start()

print("Main Thread", current_thread())
