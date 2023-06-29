# daemon thread = a thread that runs in the background, not important for program to run

#                 your program will not wait for daemon threads to complete before exiting

#                 non-daemon threads cannot normally be killed, stay alive until task is complete

#

#                 ex. background tasks, garbage collection, waiting for input, long running processes



import threading

import time





def timer():

    print()

    count = 0

    while True:

        time.sleep(1)

        count += 1

        print("logged in for: ", count, "seconds")




#creating a thread that will be incharge of the timer
# x = threading.Thread(target=timer) # if you dont specify daemon = true the timer will continue running in the background 
x = threading.Thread(target=timer,daemon=True)

x.start()


  
# x.setDaemon(True) # alternative way

# Check your thread is daemon or not
print(x.isDaemon()) 



answer = input("Do you wish to exit?")


