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
"""
Some thoughts:
1. Make a matrix of each pizza and ingredient, like this

        onion       pepper      olive       mushroom        tomato      basil       chicken
0       1           1           1           0               0           0           0
1       0           1           0           1               1           1           0
...
(e.g. Pizza 0 has onion, pepper, olive.)

2. Count the occurence of each ingredient, so we know each ingredient can get how many times of points
(use hash map i think)

3. maximize the number distributed to 2-person teams rather than larger number teams, because of Pyth theorem? 
(sum of two squares likely > one square)
(2^2 + 2^2 = 8 < 16 = 4^2 wo, but I do agree smaller first.)

4. Count the occurence of each team, maximizing the number of two person teams (e.g. 500 65 60 60 --> 65 teams of 2, 58 teams of 3, 49 teams of 4)
--> Optimization: Actually to consider this. If variety of toppings is large, it's better to prioritize 4-person teams, else 2-person teams

- Calculate the max. total no. of toppings (sum of topping amounts)
- Find the number of toppin

5. Pick the topping with the lowest amount of topping (a), then see if there is a pizza with (a) and another topping
with the highest number (b). If no, try the next number of topping (c) [for 2 topping pizza].
Until it finds a pizza with 1x lowest topping and all other toppings are highest number.

6. Distribute the pizza to one 2-person team.

7. Find another pizza which satisfies the criteria in (5), distribute it to another 2-person team.

8. Repeat until all 2-person team gets 1 pizza.

9. Sort the 2-person team array by current distinct toppings first

10. Maximize distinct topping for the two-person team

"""
"""var = len(list)"""


import glob

import parser, solver, scorer, writer

# for idx, filename in enumerate(sorted(glob.glob('datasets/*'))):
#     dataset = parser.parse(filename)
#     solution = solver.solve(dataset)
#     score = scorer.score(solution, dataset)
#     # print('Score for %s: %s/%s (%s to perfect score)' % (filename, score, dataset['knapsize'], dataset['knapsize'] - score))
#     writer.write(solution, filename.replace('datasets','solutions'))
# 

dataset = parser.parse('datasets/a_example')
solution = solver.solve(dataset)
print(solution)
score = scorer.score(solution, dataset)
print("Score =",score)