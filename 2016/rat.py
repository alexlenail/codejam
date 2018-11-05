from itertools import product as cross, combinations

def main():

	NumberOfTestCases = int(input())

	for T in range(1, NumberOfTestCases+1):

		num_ingredients, num_packages = map(int, input().split())
		recipe = list(map(int, input().split()))
		packages = [list(map(int, input().split())) for ingr in range(num_ingredients)]

		print( "Case #" + str(T) + ": " + str(pack( recipe, packages, num_packages )))


def pack(recipe, packages, num_packages):

	possibilities = list(cross(*packages))

	index = list(cross(*[range(len(package)) for package in packages]))

	y = list(zip(index, [yields(recipe, p) for p in possibilities]))

	print(y)

	nonzero = [a for a, b in y if b != 0]

	combs = flatten([combinations(nonzero, i) for i in range(1,num_packages+1)[::-1]])

	non_overlapping_combs =

	# find most non-overlapping entities in nonzero



def yields(recipe, ingr_set):

	ratios = [float(ingr) / float(r) for r, ingr in zip(recipe, ingr_set)]

	print('---------')
	print('ratios')
	print(ratios)
	print()

	print( [round(ratio) for ratio in ratios] )
	print( [(round(abs(ratio - round(ratio)), 3) <= round(ratio) / 10) for ratio in ratios] )
	print()

	if ( [round(ratio) for ratio in ratios] and
		(all([(round(abs(ratio - round(ratio)), 3) <= round(ratio) / 10) for ratio in ratios]))):

		return round(ratios[0])

	else: return 0


def flatten(l): return [item for sublist in l for item in sublist]


main()

