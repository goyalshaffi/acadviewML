
import threading
from threading import current_thread
import time
class Mythread(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h=i
    def run(self):
        time.sleep(5)
        print("value send",self.h)

thread1=Mythread(1)
thread1.start()
thread2=Mythread(2)
thread2.start()
