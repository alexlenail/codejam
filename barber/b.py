from math import ceil


def main():

	NumberOfTestCases = int(raw_input())

	for T in range(1, NumberOfTestCases+1): 

		B, SpotInLine = map(int, raw_input().split())
		barbers = map(int, raw_input().split())

		avg = ceil(float(sum(barbers))/len(barbers))

		a = sorted(sum([findMultiplesOf(barber, SpotInLine*avg) for barber in barbers], []))

		print 'Case #'+`T`+': '#+`difference`





def findMultiplesOf(x, upto): return [a*x for a in range(1, int(ceil(float(upto)/x))+1)]







main()





