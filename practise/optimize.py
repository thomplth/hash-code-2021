# Let numOfPizza = n, numOfIngredient = d
import sys

ingredientCount = pizzaData.ingredient.copy()

def pickSmallestIngredient(pizzaData):
    minIngredientList = []
    minIngredientCount = sys.maxint
    for ingredient, count in pizzaData.ingredients.items():
        if count < minIngredientCount:
            minIngredientList = [ingredient]
        elif count == minIngredientCount:
            minIngredientList.append(ingredient)
    return [minIngredientList, minIngredientCount]


def countDistinctIngredients(pizzas):
    ingredients = set()



def defineTeam(pizzaData):
    # First, maximize number two person team
    twoPersonTeam = pizzaData.nOfTwo
    fourPersonTeam = 3 - ((pizzaData.nOfPizzas - 2 * pizzaData.nOfTwo) % 3)
    threePersonTeam = pizzaData.nOfPizzas - twoPersonTeam - fourPersonTeam
    return [twoPersonTeam,threePersonTeam,fourPersonTeam]

def hash_apporach_for_two(dataset):
    arr = [[0 for i in range(dataset['nOfPizzas'])] for j in range(dataset['nOfPizzas'])]
    for i in range(dataset['nOfPizzas']:
        i_total_ingra=0
        i_ingra={}
        while i_total_ingra<(len(dataset['pizzas'][i])-1):
            
        
        for j in range(dataset['nOfPizzas']):
            if i==j:
                arr[i][j]=-1
            else:
                temp_dict={}
                for k in 
                