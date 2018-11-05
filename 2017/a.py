

from collections import defaultdict

def main():

	NumberOfTestCases = int(input())

	for T in range(1, NumberOfTestCases+1):

		D, s = input().split(' ')
		D = int(D)

		print('Case #'+str(T)+': '+minOrImpossible(D, s))


def minOrImpossible(D, s):

	if s.count('S') > D: return 'IMPOSSIBLE'

	factors = parse(s)

	iterations = 0

	while eval(factors) > D:

		iterations += 1
		m = max(factors)
		factors[m] -= 1
		factors[m-1] += 1
		if factors[m] == 0: del factors[m]

	return str(iterations)


def parse(s):

	factors = defaultdict(int)
	intensity = 0

	for c in s:
		if c is 'C': intensity += 1
		elif c is 'S': factors[intensity] += 1

	return factors

def eval(factors): return sum([2**key * value for key, value in factors.items()])


main()

# minOrImpossible(2, 'CS')
# minOrImpossible(1, 'SS')
# minOrImpossible(6, 'SCCSSC')
# minOrImpossible(2, 'CC')
# minOrImpossible(3, 'CSCSS')
