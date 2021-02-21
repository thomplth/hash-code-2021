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


import glob, time
import parser, solver, scorer, writer

for idx, filename in enumerate(sorted(glob.glob('datasets/*'))):
    dataset = parser.parse(filename)
    start_time = time.time()
    solution = solver.solveTemp(dataset)
    print("--- %.10f seconds ---" % (time.time() - start_time))
    score = scorer.score(solution, dataset)
    print('Score for %s: %s (%s pizzas for %s person)' % (filename[9:], score, dataset['nOfPizzas'], 2*dataset['nOfTwo']+3*dataset['nOfThree']+4*dataset['nOfFour']))
    writer.write(solution, filename[9]+'.txt')


# dataset = parser.parse('datasets/a_example')
# solution = solver.solve(dataset)
# print(solution)
# score = scorer.score(solution, dataset)
# print("Score =",score)