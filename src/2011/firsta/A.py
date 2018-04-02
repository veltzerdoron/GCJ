'''
Created on May 7, 2011

@author: doronv
'''

def solve(inputFile, outputFile):
    # read case number
    T = int(inputFile.readline())
    
    # iterate on all cases
    for t in range(T):
    
        # read number of teams
        values = inputFile.readline().split(' ')
        N = int(values[0])
        Pd = int(values[1])
        Pg = int(values[2])

        possible = True
        if (Pg == 0):
            if (Pd > 0):
                possible = False
            # if Pd = 0 then this is always possible
        elif (Pg == 100):
            if (Pd < 100):
                possible = False
            # if Pd == 100 then this is always possible
        else:
            # general case
            possible = False
            D = 1
            while D <= N:
                if ((D * Pd) % 100 == 0):
                    possible = True
                    break;
                 

        # output case result
        if (possible):
            outputLine = 'Case #' + str(t + 1) + ': Possible\n'
        else:
            outputLine = 'Case #' + str(t + 1) + ': Broken\n'
        outputFile.write(outputLine)
    
    # close Input and output 
    inputFile.close()
    outputFile.close()