import sys
import math
import decimal

'''
	Problem Description: Among n people, let A be the event that at least two share a birthday.
						 Then, the complementary event, A_not, is the probability that no two 
						 share a birthday.

	The main logic that does the computation here is found in main() and the auxiliary helper
	functions are found directly below this comment.
'''

def stirlings_factorial(n):
	# math.sqrt(2 * math.pi) * (n ** (n + 0.5)) * (math.e ** (-1 * n)) 
	return math.sqrt(2 * math.pi) * (n ** (n + 0.5)) * (math.e ** (-1 * n)) 

def modified_factorial(n, k):
	''' 
		instead of computing n! / (n-k)! everytime, we can just compute
		the value of the wholistic value as n * (n-1) * ... * (n-k+1)
	'''
	result, i = 1, 0
	inverse_k = n-k

	while i < inverse_k:
		result *= (n-i)
		
		i += 1

	return result

def exp_by_squaring(x, n):
	'''
		The math.pow() function could not handle the size of exponentiation that
		was being done in this problem, so here is a recursive solution to implement
		exponentiation by squaring.
	'''
    if n == 0:
    	return  1
    elif n == 1:
    	return  x 
    elif n % 2 == 0:
    	return exp_by_squaring(x * x,  n / 2)
    else:
    	return x * exp_by_squaring(x * x, (n - 1) / 2)

def samp_no_replacement(n, set_size, set_factorial):
	temp = decimal.Decimal(set_factorial) / decimal.Decimal(math.factorial(set_size-n))
	return temp / decimal.Decimal(exp_by_squaring(set_size, n))

def main():
	# set precision of decimals of probabilities to be calculated
	decimal.getcontext().prec = 10

	i = 2
	days_in_year = 365

	days_factorial = math.factorial(days_in_year)

	file = open("birthdays.txt", "w")
	while i <= days_in_year:
		result = samp_no_replacement(i, days_in_year, days_factorial)
		inverse_result = 1-result

		file.write(str(i) + "," + str(result) + "," + str(inverse_result) + "\n")

		i += 1
	file.close()
	
if __name__ == "__main__":
    main()