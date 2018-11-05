import math
import numpy as np
from itertools import product

def main():

	NumberOfTestCases = int(input())

	for T in range(1, NumberOfTestCases+1):

		A = int(input())

		dig(A)

# between 2 and 999
def dig(A):

	i = 2; j = 2; ip = 1; jp = 1

	plan_i_lo, plan_i_hi, plan_j_lo, plan_j_hi = make_plan(A)

	sofar = np.array([[False for j in range(plan_j_lo, plan_j_hi)] for i in range(plan_i_lo,plan_i_hi)])
	sofar2 = np.array([[9 for j in range(plan_j_lo+1, plan_j_hi-1)] for i in range(plan_i_lo+1,plan_i_hi-1)])

	while ip > 0 and jp > 0:

		print(str(i)+' '+str(j))

		# print(sofar)

		ip, jp = map(int, input().split())
		if ip < 1 or jp < 1: return

		was_already_dug = sofar[ip-1][jp-1]
		sofar[ip-1][jp-1] = True

		# print(all_sofar2_points_adjacent_to(ip,jp, plan_i_hi, plan_j_hi))
		if not was_already_dug:
			for ix,jx in all_sofar2_points_adjacent_to(ip,jp, plan_i_hi, plan_j_hi):
				sofar2[ix][jx] -= 1

		# print(sofar2)

		if not sofar.all():
			i, j = np.unravel_index(np.argmax(sofar2, axis=None), sofar2.shape)
			i += 2
			j += 2

	return


def make_plan(A):

	plan_i_lo = 0
	plan_j_lo = 0

	i = max( math.ceil(math.sqrt(A)),  3)
	j = max( (A // i) + 1, 			   3)

	plan_i_hi = plan_i_lo + i
	plan_j_hi = plan_j_lo + j

	return plan_i_lo, plan_i_hi, plan_j_lo, plan_j_hi


def all_sofar2_points_adjacent_to(ip,jp, plan_i_hi, plan_j_hi):

	# ip, jp are in 1-indexed space. translate to sofar2 space
	ip = ip-2
	jp = jp-2

	return [(i,j) for i,j in product([ip-1,ip,ip+1],[jp-1,jp,jp+1]) if 0 <= i < plan_i_hi-2 and 0 <= j < plan_j_hi-2]




main()






