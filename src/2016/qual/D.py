'''
@author: doronv
'''

import math

def solve(inputFile, outputFile):
    # read number of cases
    T = int(inputFile.readline())

    # iterate on all cases
    for t in range(T):
        # read K, C & S
        lineSplit = inputFile.readline().split(' ')
        K = int(lineSplit[0])
        C = int(lineSplit[1])
        S = int(lineSplit[2])

        # we only need to disambiguate the K cases where 1 tile in the original pattern is golden (1 bit is on)
        # all other tile patterns are "entailed by these patterns,
        # now, for C complexity we can disambiguate exactly C (arbitrary) such patterns using 1 tile check (1 assistant from S)
        # this is done by setting the K remainder and the division by K^1,..., K^C-1 coeficients to be the required disambiguated patterns
        # so we take K and divide it into K/C tile checks, where the i-th guess is given by the formula 
        # Gi = i * C + K * (i*C + 1) + ... + K^(C-1) * (i*C + C-1)
        # number of guesses
        G = int(math.ceil((1.0) * K / C));
        if G > S :
            outStr = 'IMPOSSIBLE'
        else :
            outStr = ''
            for i in range(G): # G is Coat least 1
                Gi = 1
                for c in range(i*C, min((i+1)*C, K)):
                    Gi += pow(K, c % C) * c
                outStr += str(Gi) # they count from 1
                if i < range(K/C):
                    outStr += ' '
        # outputFile case result
        outputLine = 'Case #' + str(t + 1) + ': ' + outStr + '\n'
        outputFile.write(outputLine)
    
    # close ınputFıle and outputFile 
    inputFile.close()
    outputFile.close()