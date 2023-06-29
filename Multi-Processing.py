# multiprocessing = running tasks in parallel on different cpu cores, bypasses GIL used for threading

#                   multiprocessing = better for cpu bound tasks (heavy cpu usage)

#                   multithreading = better for io bound tasks (waiting around)




# CPU count refers to the number of central processing units (CPUs) or processor cores present in a computer system. A CPU is the primary component responsible for executing instructions and performing calculations in a computer. Modern CPUs often have multiple cores, each capable of independently executing instructions, which allows for parallel processing and improved performance.


from multiprocessing import Process, cpu_count

import time


def counter(num):

    count = 0

    while count < num:

        count += 1


def main():

#If you have processes more than your cpu count then it will take longer time to count
    print("cpu count:", cpu_count())

    a = Process(target=counter, args=(500000000,))

    b = Process(target=counter, args=(500000000,))

    a.start()

    b.start()

    print("processing...")

    a.join()

    b.join()

    print("Done!")

    print("finished in:", time.perf_counter(), "seconds")


#it is mandatory to write this in windows when you are using multiprocessing

if __name__ == '__main__':

    main()



# A computer with a CPU count of 4 typically refers to a system that has four physical processor cores. This means that the computer has a quad-core CPU, which contains four individual processing units integrated into a single chip.

# Having a quad-core CPU provides the ability to execute multiple tasks simultaneously, as each core can handle its own set of instructions independently. This parallel processing capability can lead to improved multitasking performance and faster execution of software that is optimized for utilizing multiple cores.