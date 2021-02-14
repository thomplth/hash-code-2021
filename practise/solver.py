import optimize

def solve_helper(dataset, tab, people):
	ans=[]
	max_index=[]
	max_ingred=0
	for i in range(dataset[tab]):
		if dataset['nOfPizzas']< people:
			break
		temp_list=[]
		for j in range(people):
			max_index=0
			max_ingred=0
			count=0
			for k in dataset['pizzas']:
				if k[0]>max_ingred and k[0]!=-1:
					max_ingred=k[0]
					max_index=count
				count+=1
			temp_list.append(max_index)
			dataset['pizzas'][max_index][0]=-1
			dataset['nOfPizzas']-=1
		ans.append(temp_list)
	return ans


def solve(dataset):
	slices = 0
	solution = []
	max_index=[]
	max_ingred=0
	solution.extend(solve_helper(dataset,'nOfTwo',2))
	solution.extend(solve_helper(dataset,'nOfThree',3))
	solution.extend(solve_helper(dataset,'nOfFour',4))

	return solution


def solveGreedy(dataset):
	no_of_teams = optimize.defineTeam(dataset)

	for i in range(no_of_teams[0]):