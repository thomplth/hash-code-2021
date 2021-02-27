"""
dataset_format = {
    "nbook" : int, // number of books
    "nlib": int, // number of librarys
    "nday": in // number of day allowed
    "lib": // list of dict of libraries and books data
        [
            {
                "index": int    //original index of the library
                "books": list<int>, // list of book indexs
                "signup": int, // days required for signup process
                "ship": int // books able to ship per day
            }
        ]
    "shelf": // list of dict of <book_index> as keys and <book_score> as values
        [
            {
                "score": int, // book score
                "scan": bool // book is scanned or not, default as true
            },
            {
                "score": 2,
                "scan": false
            }
        ]
}

"""
"""
solution format :
[
    {
    index: int,
    scanned: [...]
    },
    {
    index: int,
    scanned: [...]
    }
]
[{<index> : [<scanned book 1>, <scanned book 2>]}, {<index_2> : [<scanned book 1>, <scanned book 2>,...]}]

"""

import writer
import scorer
import solver
import parser
import time
import glob
#import optimize

#solution = solver.solve(parser.parse('datasets/a_example.txt'))
#print(solution)

for idx, filename in enumerate(sorted(glob.glob('datasets/*'))):
    dataset = parser.parse(filename)
    start_time = time.time()
    solution = solver.solve(dataset)
    # print(solution)
    print("--- %.10f seconds ---" % (time.time() - start_time))
    score = scorer.score(solution, dataset)
    #print('Score for %s: %s (%s pizzas for %s person)' % (
    #    filename[9:], score, dataset['nOfPizzas'], 2*dataset['nOfTwo']+3*dataset['nOfThree']+4*dataset['nOfFour']))
    writer.writing(solution, filename[9]+'.txt')

#Optimazation Part here
#opt_solution = optimize.solve(dataset)
#print(opt_solution)
#score = opt_scorer.score(opt_solution, dataset)

# dataset = parser.parse('datasets/a_example')
# solution = solver.solve(dataset)
# print(solution)
# score = scorer.score(solution, dataset)
# print("Score =",score)
