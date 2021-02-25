"""
dataset_format = {
    'pizzas':
            [
                [1, 'onion', 'pepper', 'olive'], 
                [2, 'mushroom', 'tomato', 'basil']
            ],               # Index of each pizza, followed by ingredients, ordered decendingly by number of ingredients
    'nOfPizzas': 5,          # Number of pizzas
    'nOfTwo': 1,             # Number of 2-person teams
    'nOfThree': 2,           # Number of 3-person teams
    'nOfFour': 1,            # Number of 4-person teams
    'ingredients':
            {
                'onion': 1,
                'pepper': 2,
            }                # occurance of ingredients in all pizzas, accending order by occurance
}

# for indx team, which pizza to chosolution_format = [0, 2, 3]          # Index of each selected pizza, followed by which pizza should choose
 0, 2, 3{}[]0, 2, 3,[]1,4  \2D list, 
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
    
