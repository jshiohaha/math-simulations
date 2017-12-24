import sys
import math
import decimal
import time

def modified_factorial(n, k):
    ''' 
        instead of computing n! / (n-k)! everytime, we can just compute
        the value of the wholistic value as n * (n-1) * ... * (n-k+1)
    '''
    result, i = 1, 0
    # inverse_k = n-k

    while i < k:
        result *= (n-i)
        i += 1
    return decimal.Decimal(result) * decimal.Decimal(1)

def n_divide_nminusk(n, k):
    return decimal.Decimal(math.factorial(n)) / decimal.Decimal(math.factorial(n-k))

def main():
    # set precision of decimals of probabilities to be calculated
    decimal.getcontext().prec = 10

    upper_bound, t0 = 300, 0

    file = open("timing.txt", "w")
    file.write("normal,modified,diff\n")
    for i in range(upper_bound):

        t0 = time.time()
        result_mod = modified_factorial(upper_bound, i)
        tmod = time.time() - t0

        t0 = time.time()
        result_norm = n_divide_nminusk(upper_bound, i)
        tnorm = time.time() - t0

        if result_mod != result_norm:
            print("i: " + str(i) + "\n")
            print(str(result_mod) + " vs " + str(result_norm))
            sys.exit(0)

        diff = abs(result_norm-result_mod)
        if result_norm < result_mod:
            print("norm wins: " + str(diff))
        else:
            print("mod wins: " + str(diff))

        file.write(str(tnorm) + "," + str(tmod) + "," + str(diff) + "\n")
    file.close()
    
if __name__ == "__main__":
    main()