import threading    #1
import time  #2

print("Main thread started")

def single_task():
    print("Sub Task started")
    time.sleep(5)
    print("Sub task completed")
    
def second_task():
    print("Even numbers are")
    for i in range(10):
        if i%2==0:
            print(i)
    print("Second task completed")
def third_task():
    print("Odd numbers are")
    for i in range(10):
        if i%2!=0:
            print(i)    
    print("Third task completed")
    
#time.sleep(2)
thread1=threading.Thread(target=single_task)
thread1.start()
thread1.join()
thread2=threading.Thread(target=second_task)
thread2.start()
thread2.join()
thread3=threading.Thread(target=third_task)
thread3.start()
thread3.join()
#thread.join() #7 wait for the thread to finish before exiting
print("Main thread execution completed")


#2 friends  ---1 thread travelling in train and sub task of other thread to bring medicines
#if they join ---sub task gets completed first --i.e,giving medicines
#else: main task is completed 