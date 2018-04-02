'''
Created on May 7, 2011

@author: doronv
'''

def solve(inputFile, outputFile):
    # read case number
    T = int(inputFile.readline())

    # iterate on all cases
    for t in range(T):

        # get C and D
        values = inputFile.readline().split(' ')
        C = int(values[0])
        D = int(values[1])

        # reset point and vendor count arrays
        P = []
        V = []
    
        # load the data
        N = 0
        for c in xrange(C):
            # get P and V
            values = inputFile.readline().split(' ')
    
            P[c] = float(values[0])
            V[c] = int(values[1])
            N = N + V[c];
    
        # times and original positions for all vendors
        movement = [];
    
        # calculate pMax pMin and the time        
        pMin = min(P)
        pMax = max(P)
    
        # vendor index
        vI = 0
        for c in xrange(C):
            for _ in xrange(V[c]):
                # set movement as if the i-th vendor goes to vI * D
                movement[vI] = vI * D - P[c];
                vI = vI + 1
    
        time = max((pMax - pMin) / 2, 0)
    
        # Output case result
        OutputLine = 'Case #' + str(t + 1) + ': ' + '%.1f' % (float (time)) + '\n'
        outputFile.write(OutputLine)
    
    # close Input and Output 
    inputFile.close()
    outputFile.close()