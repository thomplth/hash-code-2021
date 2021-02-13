"""
dataset_format = {
            'pizzas': [2, 5, 6, 8],  # Number of slices in each pizza
            'knapsize': 17           # Number of players
}

solution_format = [0, 2, 3]          # Index of each selected pizza

"""

import glob

import parser, solver, scorer, writer

for idx, filename in enumerate(glob.glob('datasets/*')):
    dataset = parser.parse(filename)
    solution = solver.solve(dataset)
    score = scorer.score(solution, dataset)
    print('Score for %s: %s/%s (%s to perfect score)' % (filename, score, dataset['knapsize'], dataset['knapsize'] - score))
    writer.write(solution, filename.replace('datasets','solutions'))