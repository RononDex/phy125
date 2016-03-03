# ---------------------------------------------------------------------------
# Calculates prime numbers in a defined range using the method of Eratosthenes
#
# Modul:   PHY125
# Author:  Tino Heuberger
# Email:   tino.heuberger@uzh.ch
# ---------------------------------------------------------------------------

#from threading import Thread
#import threading
import time

lock = threading.Lock()

# Moves through every element in the defined range using the method of Eratosthenes
# and removes the non-prime numbers.
# Return a list containing all prime numbers which are within the defined range
def SearchPrimesEratosthenes(start, end):
    
    searchRange = list(range(start, end))
    removeFunc = searchRange.remove

    for i in searchRange:
        if i == 1 or i == 0:
            removeFunc(i)
            continue

        # Using multithreading here causes way too many threads to be started,
        # which then lowers the performance instead of increasing it,
        # due to the big overhead that you get with that many threads. 
        # (May be processor dependent, tested on an i5 2 core (4 threads) processor

        #t = Thread(target=RemoveMultipleOf, args = (searchRange, i, end, removeFunc))
        #t.start()

        RemoveMultipleOf(searchRange, i, end, removeFunc)        

    return searchRange

# Removes all the multiples of a certain number from a list
def RemoveMultipleOf(list, number, end, removeFunc):
    global lock

    curValue = number + number
    while curValue < end:
        #lock.acquire() 
        if curValue in list:
            removeFunc(curValue)
        #lock.release()
        curValue += number

start = 0
end = 10000    # Takes around 1.7s on my laptop

print("Searching Prime numbers in range %i - %i" % (start, end))
print("")

# store the time when the executation starts, 
# so we can measure how long it took to calculate
startTime = time.time()

result = SearchPrimesEratosthenes(start, end)
print(result)

print("")
print("Took %s seconds" % (time.time() - startTime))

print("")
print("%i Primzahlen gefunden" % len(result))
print("")

p = 244
if len(result) >= p:
    print("p3244 = %s" % result[p])
else:
    print("Could not find p%s" % p)