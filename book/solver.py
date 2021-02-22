"""Easiest solution: just put the lowest scanning time first

:returns:[{<index> : [<scanned book 1>, <scanned book 2>]}, {<index_2> : [<scanned book 1>, <scanned book 2>,...]}]

"""
def solve(dataset):
	signing_lib = 0
	remain_signing_day = dataset['lib'][signing_lib]['signup']
	signed = []
	# # solution = [[None]]*dataset['nday']
	solution = [[] for x in range(dataset['nlib'])]
	for i in range(dataset['nday']):
		if signed:
			for j in signed:
				for k in range(dataset['lib'][j]['ship']):
					curr_index=(i-dataset['lib'][j]['signup'])*dataset['lib'][j]['ship']+k
					if(curr_index<len(dataset['lib'][j]['books'])):
						if dataset['shelf'][dataset['lib'][j]['books'][curr_index]]['scan']!= True:
							solution[j].append(dataset['lib'][j]['books'][curr_index]) #here
							dataset['shelf'][dataset['lib'][j]['books'][curr_index]]['scan']= True
		remain_signing_day -= 1
		if(remain_signing_day == 0):
			signed.append(signing_lib)
			if signing_lib != (dataset['nlib']-1):
				signing_lib += 1
				remain_signing_day = dataset['lib'][signing_lib]['signup']
	return solution


"""Greedy solution
"""
def solveGreedy(dataset):
	sol = []

	# for i in range(dataset['nday']):
	item = {
		'index': dataset['lib'][0]['index'],
		'scanned': dataset['lib'][0]['books']
	}
	sol.append(item)
	return sol[item]


"""Randomised Greedy solution
"""
def solveRandom(dataset):
	pass