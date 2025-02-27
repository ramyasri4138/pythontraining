import threading
import time
def task(lock):
    with lock:
        print(f"{threading.current_thread().name} has acquired the lock")
        time.sleep(1)
        print(f"{threading.current_thread().name} has released the lock")
lock=threading.Lock()
t1=threading.Thread(target=task,args=(lock,))
t2=threading.Thread(target=task,args=(lock,))
t1.start()
t1.join()
t2.start()
#t1.join()
t2.join()
print("Main thread")