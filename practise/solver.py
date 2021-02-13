def solve(dataset):
	slices = 0
	solution = []
	for i in range(len(dataset['pizzas'])):
		if slices + dataset['pizzas'][i] <= dataset['knapsize']:
			solution.append(i)
	return solution