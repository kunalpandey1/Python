# thread =  a flow of execution. Like a separate order of instructions.
#                  However each thread takes a turn running to achieve concurrency
#                  GIL = (global interpreter lock),
#                  allows only one thread to hold the control of the Python interpreter at any one time

# cpu bound = program/task spends most of it's time waiting for internal events (CPU intensive)
#             use multiprocessing

# io bound = program/task spends most of it's time waiting for external events (user input, web scraping)
#            use multithreading

import threading
import time

#this is the example of io bound as drink_coffee is waiting for the external event like eat_breakfast to complete 

def eat_breakfast():
    time.sleep(3)
    print("You eat breakfast")


def drink_coffee():
    time.sleep(4)
    print("You drank coffee")


def study():
    time.sleep(5)
    print("You finish studying")



# eat_breakfast()
# drink_coffee()
# study()

#now using these you can dedicate threads to each of the function to work concurrently 

x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_coffee, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()


#Thread Synchronization

x.join()
y.join()
z.join()

print(threading.active_count()) # print the active thread which is running 
print(threading.enumerate()) # print all thread that are currently running
print(time.perf_counter()) 

   