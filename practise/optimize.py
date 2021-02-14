# Let numOfPizza = n, numOfIngredient = d
import sys

def solution(pizzaData):
    twoSolution = []
    threeSolution = []
    fourSolution = []

    teamSize = define_team(pizzaData)

    nowMaxIndex = len(pizzaData.ingredients)-1
    nowMinIndex = 0

    for pizza in pizzaData.pizzas:
        if pizzaData.ingredients[0] in pizza and pizzaData.ingredients[nowMax] in pizza:
            if len(twoSolution) < teamSize[0]:
                twoSolution.append(pizza)
                for ingredient in pizza:
                    pizzaData.ingredients -= 1

        
        
        
        
"""
def sort_ingredient_list(pizzaData):
    minIngredientList = []
    minIngredientCount = sys.maxint
    for ingredient, count in pizzaData.ingredients.items():
        if count < minIngredientCount:
            minIngredientList = [ingredient]
        elif count == minIngredientCount:
            minIngredientList.append(ingredient)
    return [minIngredientList, minIngredientCount]
"""            


def countDistinctIngredients(pizzas):
    ingredients = set()
    for pizza in pizzas:
        for ingredient in pizza[1:]:
            ingredients.add(ingredient)
    return len(ingredients)


def define_team(pizzaData):
    # First, maximize number two person team
    twoPersonTeam = pizzaData.nOfTwo
    fourPersonTeam = 3 - ((pizzaData.nOfPizzas - 2 * pizzaData.nOfTwo) % 3)
    threePersonTeam = pizzaData.nOfPizzas - twoPersonTeam - fourPersonTeam
    return [twoPersonTeam,threePersonTeam,fourPersonTeam]

def hash_apporach_for_two(dataset):
    arr = [[0 for i in range(dataset['nOfPizzas'])] for j in range(dataset['nOfPizzas'])]
    for i in range(dataset['nOfPizzas']):
        i_total_ingra=1
        i_ingra=set()
        while i_total_ingra<(len(dataset['pizzas'][i])):
            i_ingra.add(dataset['pizzas'][i][i_total_ingra])
            i_total_ingra+=1
        
        for j in range(dataset['nOfPizzas']):
            if i==j:
                arr[dataset['pizzas'][i][0]][dataset['pizzas'][j][0]]=-1
            else:
                j_total_ingra=1
                j_ingra=set()
                while j_total_ingra<(len(dataset['pizzas'][i])):
                    j_ingra.add(dataset['pizzas'][j][j_total_ingra])
                    j_total_ingra+=1
                j_ingra=j_ingra.union(i_total_ingra)
                arr[dataset['pizzas'][i][0]][dataset['pizzas'][j][0]]=len(j_ingra)
    print(arr)