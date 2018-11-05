
def main():

	NumberOfTestCases = int(input())

	for T in range(1, NumberOfTestCases+1):

		row, K = input().split()

		print( "Case #" + str(T) + ": " + str(flip(row, int(K))))

def flip(row, K)







