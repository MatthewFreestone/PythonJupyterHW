import time
def primeGenRemove(primeCap):
    ''' starts with full list of numbers and removes them'''
    startTime = time.time()
    numberList = list(range(3,primeCap, 2))
    primeList = [2]
    for currentNum in numberList:
        primeList.append(currentNum)
        timesCap = (primeCap // currentNum)+1
        timesValues = list(range(2, timesCap))
        for factor in timesValues:
            try:
                numberList.remove(currentNum * factor)
            except ValueError:
                pass
    endTime = time.time()
   # print('Primes found: ', primeList)
    print('Time elapsed: ', float(endTime-startTime), '\n')

def primeGenEliminatedList(primeCap):
    startTime = time.time()
    primes = [2]
    removed = [False]*primeCap #0 and 1 removed, 2 stays
    i = 3
    while(i < primeCap):
        if (removed[i]!= True):
            primes.append(i)
            timesCap = (primeCap // i)+1
            timesValues = list(range(2, timesCap))
            for factor in timesValues:
                toBeRemoved=factor*i
                try:
                    removed[toBeRemoved] = True
                except IndexError:
                    pass
        i+=1

    endTime = time.time()
 #   print('Primes found: ', primes)
    print('Time elapsed: ', float(endTime-startTime), '\n')
            

running = True
print('Press enter to exit')
while(running):
    primeCapInput = input('Highest Number for primes: ')
    if primeCapInput == '':
        running = False
        break
    else:
        try:
            intPrimeNumCap = int(primeCapInput)
            #primeGenRemove(intPrimeNumCap)
            primeGenEliminatedList(intPrimeNumCap)
        except ValueError:
            print('Invalid input')
            pass


