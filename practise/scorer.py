"""
dataset_format = {
    'pizzas':
            [
                [3, 'onion', 'pepper', 'olive'], 
                [3, 'mushroom', 'tomato', 'basil']
            ],               # Number of ingredients in each pizza, followed by ingredients
    'nOfPizzas': 5,          # Number of pizzas
    'nOfTwo': 1,             # Number of 2-person teams
    'nOfThree': 2,           # Number of 3-person teams
    'nOfFour': 1,            # Number of 4-person teams
}

solution_format = [0, 2, 3]          # for indx team, which pizza to choose
"""

def score(solution, dataset):
    """For each delivery, the delivery score is the square of the total number of dierent ingredients of
all the pizzas in the delivery. The total score is the sum of the scores for all deliveries.
    """
    res = 0
    for idx in solution:
        pizza_type = []
        for piz_index in idx:
            ind = dataset['pizzas'][piz_index][1:]
            for i in ind:
                if i not in pizza_type:
                    pizza_type.append(i)
        #test
        #test end
        res += len(pizza_type) ** 2
    return res

    return 0
    """if res > dataset['knapsize']:
        return 0"""
    
