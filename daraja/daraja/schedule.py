import time
from threading import Timer

def func():
    print("start function now")

def schedule_an_event():
    import time
    from threading import Timer
    
    Timer(1, func).start()
    return "Done"

print(schedule_an_event())