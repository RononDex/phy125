# ---------------------------------------------------------------------------
# Calculates prime numbers in a defined range using the method of Eratosthenes
# Uses multi threading to get better performance
#
# Modul:   PHY125
# Author:  Tino Heuberger
# Email:   tino.heuberger@uzh.ch
# ---------------------------------------------------------------------------

from threading import Thread
from collections import deque
import multiprocessing
import threading
import time
import math

lock = threading.Lock()
threads = deque()

# Moves through every element in the defined range using the method of Eratosthenes
# and removes the non-prime numbers.
# Return a list containing all prime numbers which are within the defined range
def SearchPrimesEratosthenes(start, end):
    
    global number_of_threads
    global threads
    global useMultiThreading

    searchRange = list(range(start, end))
    removeFunc = searchRange.remove
    
    # we only need to remove multiples of 2... square root of end
    for i in range(2, int( math.sqrt(end)) + 1):
        if i not in searchRange:
            continue

        # Use Multithreading to start as many threads as we have cores on this machine
        if (useMultiThreading):
            # Create mew thread
            t = Thread(target=RemoveMultipleOf, args = (searchRange, i, end, removeFunc))
            if (len(threads)) == number_of_threads:  # Checks if there are already all threads started and if there are any aavailable available
                waitForThread = threads.popleft()    # Waits for the oldest thread to finish in order to start a new one
                if waitForThread.isAlive():
                    waitForThread.join()
            
            threads.append(t)
            t.start()
        # If Multithreading turned off, just use the "normal" main thread
        else:
            RemoveMultipleOf(searchRange, i, end, removeFunc)        

    return searchRange

# Removes all the multiples of a certain number from a list
def RemoveMultipleOf(list, number, end, removeFunc):
    global lock
     
    for i in range(2*number, end, number):
        lock.acquire() 
        if i in list:
            removeFunc(i)
        lock.release()

# Define boundaries for the prime numbers search
start = 2
end = 100000

# Set to true to use multithreading to use all availabe logical cores, false for no multithreading to only use 1 thread
# Performance results may vary depending on the amount of logical cpu cores in your machine, and their IPC and clockrate 
# in my case (using my laptop with an old i5, 4 cores) using multi threading gave me a boost of around 10-20%,
# also depends on how big the search range is because multithreading also creates some managing overhead.
# I noticed that on the openSuse clients in the computer lab multithreading performance was actually really bad
useMultiThreading = True

print("Searching Prime numbers in range %i - %i" % (start, end))
print("")

print("Using MultiThreading: %s" % useMultiThreading)

# Get amount of logical cpu cores on this system
if (useMultiThreading):
    number_of_cores = multiprocessing.cpu_count()
    number_of_threads = number_of_cores
    print("Running on %s cores, using %s threads" % (number_of_cores, number_of_threads))

# store the time when the executation starts, 
# so we can measure how long it took to calculate
startTime = time.time()

result = SearchPrimesEratosthenes(start, end)

print("")
print("Took %s seconds" % (time.time() - startTime))

print("")
print("%i Primzahlen gefunden" % len(result))
print("")

# Set p to the primeNumber iteration you want to read out
p = 840
if len(result) >= p:
    print("p%s = %s" % (p, result[p]))
else:
    print("Could not find p%s" % p)