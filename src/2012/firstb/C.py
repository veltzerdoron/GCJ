'''
Created on May 22, 2011

@author: doronv
'''
import itertools

# import section

def solve(inputFile, outputFile):
    # read case number
    T = int(inputFile.readline())

    # iterate on all cases
    for t in range(T):
        # get L, d, N and C (I call t, d to avoid name conflicts)
        values = inputFile.readline().split(' ')
        N = int(values[0])

        # get Vals
        Vals = [(int(values[1 + c])) for c in xrange(N)]

        outputLine = 'Case #' + str(t + 1) + ':\n'
        outputFile.write(outputLine)
        SSSs = {}
        result = False;
        for i in xrange(1, N):
            SSsN = set(itertools.combinations(Vals, i));
            while not SSsN == set():
                SS = SSsN.pop()
                SSS = sum(SS)
                if SSS in SSSs:
                    if set(SSSs[SSS]).isdisjoint(set(SS)):
                        outputLine = ''
                        for SI in SSSs[SSS]:
                            outputLine += str(SI) + ' '
                        outputFile.write(outputLine + '\n')
                        outputLine = ''
                        for SI in SS:
                            outputLine += str(SI) + ' '
                        outputFile.write(outputLine + '\n')
                        result = True;
                else:
                    SSSs[SSS] = SS;
                if result: break

            if result: break

        if not result: outputFile.write('Impossible \n')
        # Output case result