import threading
import time
def daemon_task():
    while True:
        print("Daemon Thread is running")
        time.sleep(1)
        
daemon_thread=threading.Thread(target=daemon_task,daemon=True)
daemon_thread.start()
time.sleep(10)
print("main thread exiting")