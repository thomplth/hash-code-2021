

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
def solveGreedy(dataset):
	no_of_teams = optimize.defineTeam(dataset)
	sol = [[] * dataset['nOfPizzas']]
	for team in sol:
		team.append(dataset['pizzas'].pop(0))
	for team in sol[:no_of_teams[0]]: