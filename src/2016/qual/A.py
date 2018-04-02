'''
@author: doronv
'''

import sys

def solve(inputFile, outputFile):
    # read number of cases
    T = int(inputFile.readline())
    
    # iterate on all cases
    for t in range(T):
        # read N
        N = int(inputFile.readline())

        if (N == 0):
            outStr = "INSOMNIA"
        else:
            digits = [0,1,2,3,4,5,6,7,8,9];

            M = 0
            # while we have remaining digits
            while digits:
                # check digits in M (=x*N)
                M += N
                for c in str(M) :
                    d = ord(c) - ord('0')
                    if d in digits :
                        digits.remove(d)
            outStr = str(M)
    
        # Output case result
        outputLine = 'Case #' + str(t + 1) + ': ' + outStr + '\n'
        outputFile.write(outputLine)
    
    # close ınputFıle and Output 
    inputFile.close()
    outputFile.close()