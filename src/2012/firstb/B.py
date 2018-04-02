'''
Created on May 22, 2011

@author: doronv
'''

import sys

def solve(inputFile, outputFile):
    # read case number
    T = int(inputFile.readline())

    # iterate on all cases
    for t in range(T):
        # read N
        values = inputFile.readline().split(' ')
        N = int(values[0])

        Ais = [int for _ in xrange(N)]
        Bis = [int for _ in xrange(N)]

        # load the ratings
        for n in reversed(xrange(N)):
            values = inputFile.readline().split(' ')
            Ais[n] = int(values[0])
            Bis[n] = int(values[1])

        # solve
        completed = 0
        competed = 0
        stars = 0
        while (completed < N):
            # if we can complete a 2 star level
            minimalBi = Bis.index(min(Bis))
            if (Bis[minimalBi] <= stars):
                # erase the stage and increment counters
                Ais[minimalBi] = sys.maxint
                Bis[minimalBi] = sys.maxint
                completed += 1
                competed += 1
                stars += 2
            else:
                maxBi = -1
                indexMaxBi = -1
                for n in xrange(N):
                    if (Ais[n] <= stars):
                        if (Bis[n] > maxBi):
                            maxBi = Bis[n]
                            indexMaxBi = n
                # if we found a possible 1 star stage
                if indexMaxBi >= 0:
                    # erase the 1 star stage and increment counters
                    Ais[indexMaxBi] = sys.maxint
                    competed += 1
                    stars += 1
                else:
                    competed = sys.maxint
                    break

        # Output case result
        OutputLine = 'Case #' + str(t + 1) + ': '
        if competed != sys.maxint:
            OutputLine += str(competed)
        else:
            OutputLine += 'Too Bad'
        OutputLine += '\n'
        outputFile.write(OutputLine)
    
    # close Input and Output 
    inputFile.close()
    outputFile.close()
