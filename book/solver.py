import optimize

def solve_helper(dataset, tab, people, visited):
	ans=[]
	max_index=[]
	max_ingred=0
	num_of_p=dataset['nOfPizzas']
	for i in range(dataset[tab]):
		if dataset['nOfPizzas']< people:
			break
		temp_list=[]
		for j in range(people):
			max_index=0
			max_ingred=0
			count=0
			for k in dataset['pizzas']:
				if len(k)-1>max_ingred and visited[k[0]]==False:
					max_ingred=len(k)-1
					max_index=k[0]
				count+=1
			temp_list.append(max_index)
			visited[max_index]=True
			#dataset['pizzas'][max_index][0]=-1
			num_of_p-=1
		ans.append(temp_list)
	return ans


def solve(dataset):
	slices = 0
	solution = []
	max_index=[]
	max_ingred=0
	visited=[False]*dataset['nOfPizzas']
	solution.extend(solve_helper(dataset,'nOfTwo',2,visited))
	solution.extend(solve_helper(dataset,'nOfThree',3,visited))
	solution.extend(solve_helper(dataset,'nOfFour',4,visited))

	return solution


"""
:returns: [[<pizza-index>, ...], [..], ...]

"""
def solveTemp(dataset):
	count = 0
	no_of_teams = dataset['nOfTwo']+dataset['nOfThree']+dataset['nOfFour']
	no_of_people = 2*dataset['nOfTwo']+3*dataset['nOfThree']+4*dataset['nOfFour']
	pizzas = dataset['pizzas'].copy()
	sol = []
	for i in range(dataset['nOfTwo']):
		team = []
		try:
			team.append(pizzas.pop(0)[0])
			team.append(pizzas.pop(0)[0])
		except IndexError:
			return sol
		count += 1
		print(f'{count} processed out of {no_of_people}.', end='\r')
		sol.append(team)
	for i in range(dataset['nOfThree']):
		team = []
		try:
			team.append(pizzas.pop(0)[0])
			team.append(pizzas.pop(0)[0])
			team.append(pizzas.pop(0)[0])
		except IndexError:
			return sol
		count += 1
		print(f'{count} processed out of {no_of_people}.', end='\r')
		sol.append(team)
	for i in range(dataset['nOfFour']):
		team = []
		try:
			team.append(pizzas.pop(0)[0])
			team.append(pizzas.pop(0)[0])
			team.append(pizzas.pop(0)[0])
			team.append(pizzas.pop(0)[0])
		except IndexError:
			return sol
		count += 1
		print(f'{count} processed out of {no_of_people}.', end='\r')
		sol.append(team)

	return sol


def solveGreedy(dataset):
	count = 0
	no_of_teams = dataset['nOfTwo']+dataset['nOfThree']+dataset['nOfFour']
	no_of_people = 2*dataset['nOfTwo']+3*dataset['nOfThree']+4*dataset['nOfFour']
	pizzas = dataset['pizzas'].copy()
	sol = []
	for i in range(dataset['nOfTwo']):
		team = []
		try:
			team.append(pizzas.pop(0)[0])
			team.append(pizzas.pop(0)[0])
		except IndexError:
			return sol
		count += 1
		print(f'{count} processed out of {no_of_people}.', end='\r')
		sol.append(team)
	for i in range(dataset['nOfThree']):
		team = []
		try:
			team.append(pizzas.pop(0)[0])
			team.append(pizzas.pop(0)[0])
			team.append(pizzas.pop(0)[0])
		except IndexError:
			return sol
		count += 1
		print(f'{count} processed out of {no_of_people}.', end='\r')
		sol.append(team)
	for i in range(dataset['nOfFour']):
		team = []
		try:
			team.append(pizzas.pop(0)[0])
			team.append(pizzas.pop(0)[0])
			team.append(pizzas.pop(0)[0])
			team.append(pizzas.pop(0)[0])
		except IndexError:
			return sol
		count += 1
		print(f'{count} processed out of {no_of_people}.', end='\r')
		sol.append(team)

	return sol

# O(n ** m)
def findBestSet(dataset, m):
	for i in range(len(dataset['pizzas'])):
		pass


def solvemc(dataset):
    capa = dataset['knapsize']
    sol = []
    for i in range(len(dataset['pizzas'])-1, -1, -1):
        if random.getrandbits(2) and capa >= dataset['pizzas'][i]:
            sol.append(i)
            capa -= dataset['pizzas'][i]
    st = set(sol)
    for i in range(len(dataset['pizzas'])-1, -1, -1):
        if i not in st and capa >= dataset['pizzas'][i]:
            sol.append(i)
            capa -= dataset['pizzas'][i]
    return sol

    