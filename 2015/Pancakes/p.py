from numpy import diff
from collections import Counter
from itertools import repeat

def main():

	NumberOfTestCases = int(raw_input())

	for T in range(1, NumberOfTestCases+1):
		raw_input()
		plates = map(int, raw_input().split())

		print 'Case #'+`T`+': '+`minTimesteps(plates)`


def minTimesteps(plates):

	deltas = diff([0]+sorted(list(set(plates))))
	# # the zip evaluates to ((value, numberOfTimesItAppears) howMuchBiggerItIsThanNextValue)
	THESTRUCTURE = sum([list(repeat((delta, value), times)) for (value, times), delta in zip( sorted(dict(Counter(plates)).items()), deltas)], [])
	
	max(THESTRUCTURE)
	# find this+ all the values greater. 
	# cut the largest, next, etc... create a list of scores for each of those cuts. 


	max(plates)


	return min(max(plates), 1+minTimesteps(plates with max cut ))






main()
