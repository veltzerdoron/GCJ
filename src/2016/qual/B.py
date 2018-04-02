'''
@author: doronv
'''

def solve(inputFile, outputFile):
    # read number of cases
    T = int(inputFile.readline())
    
    # iterate on all cases
    for t in range(T):
        # read N
        Pan = list(inputFile.readline().rstrip())

        i = 0
        # while exist non smiley side up
        while '-' in Pan :
            if (Pan[0] == '+') :
                # if must swap all the first pluses
                j = 0
                while (Pan[j] == '+'):
                    Pan[j] = '-'
                    j += 1
            else :
                # get the first "-" character
                j = len(Pan) - 1
                while Pan[j] == "+" :
                    j -= 1
                # flip at j
                k = 0
                while k < j:
                    ck = Pan[k]
                    cj = Pan[j]
                    Pan[k] = '+' if cj == '-' else '-'
                    Pan[j] = '+' if ck == '-' else '-'
                    k += 1
                    j -= 1
                if k == j:
                    Pan[k] = '+' if Pan[j] == '-' else '-'
            i += 1

        # outputFile case result
        outputLine = 'Case #' + str(t + 1) + ': ' + str(i) + '\n'
        outputFile.write(outputLine)

    # close inputFile and outputFile 
    inputFile.close()
    outputFile.close()