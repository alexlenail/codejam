

from collections import defaultdict

def main():

	NumberOfTestCases = int(input())

	for T in range(1, NumberOfTestCases+1):

		D, s = map(int, input().split())
		D = int(D)

		print('Case #'+str(K)+': '+minOrImpossible(D, s))

def minOrImpossible(D, s):

	if s.count('S') > D: return 'IMPOSSIBLE'

	factors = parse(s)


def parse(s):

	factors = defaultdict(int)
	intensity = 0

	for c in S:
		if c is 'C': intensity += 1
		elif c is 'S': factors[intensity] += 1



# def eval(factors): return

