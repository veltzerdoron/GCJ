'''
@author: doronv
'''
import sys

def isprime(n):
    """Returns 0 if n is prime otherwise a divisor."""
    if n == 2:
        return 0
    if n == 3:
        return 0
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3

    i = 5
    w = 2

    while pow(i,8) <= n: # if it doesn't go easy leave it
        if n % i == 0:
            return i
        i += w
        w = 6 - w

    return 0

def solve(inputFile, outputFile):
    # read number of cases
    T = int(inputFile.readline())
    
    # iterate on all cases
    for t in range(T):
        # read N and J
        lineSplit = inputFile.readline().split(' ')
        N = int(lineSplit[0])
        J = int(lineSplit[1])

        i = int('1' + '0'*(N - 2) + '1', 2);
        j = 0
        jamCoins = ['' for x in range(J)]
        divisors = [[0 for x in range(9)] for x in range(J)]
        while j < J :
            divisors[j][0] = isprime(i)
            if (divisors[j][0] > 0):
                jamCoins[j] = "{0:b}".format(i);
                prime = False
                for base in range(3,11):
                    divisors[j][base - 2] = isprime(int(jamCoins[j],base))
                    if (divisors[j][base - 2] == 0):
                        prime = True
                        break
                if not prime:
                    j += 1
            i += 2 # add 2 so as not to have a 0 first bit
        #Start generating Jam Coins 
    
        # outputFile case result
        outputLine = 'Case #' + str(t + 1) + ':' + '\n'
        for j in range(J):
            outputLine += str(jamCoins[j]) + ' '
            for base in range(9):
                outputLine += str(divisors[j][base])
                if base < 8:
                     outputLine += ' '
            if j < (J-1):
                outputLine += '\n'
        outputFile.write(outputLine)
    
    # close inputFile and outputFile 
    inputFile.close()
    outputFile.close()