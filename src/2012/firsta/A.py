'''
Created on May 22, 2011

@author: doronv
'''

def solve(inputFile, outputFile):
    # read case number
    T = int(inputFile.readline())
    
    # iterate on all cases
    for t in range(T):
    
        # read A and B
        values = inputFile.readline().split(' ')
        A = int(values[0])
        B = int(values[1])

        # read probabilities
        values = inputFile.readline().split(' ')
        Ps = [(float(values[a])) for a in xrange(A)]

        # enter right away
        strokes = 1 + B + 1
        # delete 0 up to A characters
        P = 1
        for a in xrange(A):
            P *= Ps[a]
            strokes = min(strokes, B - a + A - a - 1 + (1 - P) * (B + 1))

        # output case result
        outputLine = 'Case #' + str(t + 1) + ': ' + '%0.6f' % (strokes) + '\n'
        outputFile.write(outputLine)
    
    # close Input and output 
    inputFile.close()
    outputFile.close()