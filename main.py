"""
dataset_format = {
    "nDuration": int,           // the duration of the simulation, in seconds
    "nIntersection": int,       // the number of intersections
    "nStreet": int,             // the number of streets
    "nCars": int,               // the number of cars
    "nBouns": int,              // the bonus points for each car
    "streets": [
        {
            "index": int,
            "start": int,       // start intersection
            "end": int,         // end intersection
            "name": str,        // street
            "time": int,      // travelling time
            "queue": [car, car, car, ...]// list of car on that queue
        }, 
    ]
    "cars" : [
        {
            "index": int,
            "start": int,       // start intersection
            "end"  : int,       // (initialize sys.maxsize) //tbc
            "path" : [ str, str, str, ... ] // list of street names
            "curr" : int // index in path, indicate where the car is
        }
    ]
}

solution format :

[
    {
    index: int              // intersection index
    schedule: [
        (street_name1, time1),
        (street_name2, time2),
    ]
    }
]

"""

#import optimize

#solution = solver.solve(parser.parse('datasets/a_example.txt'))
# print(solution)

import writer
import scorer
import solver
import parser
import time
import glob
for idx, filename in enumerate(sorted(glob.glob('datasets/*'))):
    dataset = parser.parse(filename)


    # print(solution)

    # maybe no solution
    # score = scorer.score(dataset)
    # score = scorer.score(solution, dataset)
    
    best_solution = []
    best_score = 0
    for i in range(10):
        solution = solver.solve(dataset)
        start_time = time.time()
        print("--- %.10f seconds ---" % (time.time() - start_time))
        score = scorer.sim(dataset, solution)
        if score > best_score:
            best_solution = solution
    # print('Score for %s: %s (%s pizzas for %s person)' % (
    #    filename[9:], score, dataset['nOfPizzas'], 2*dataset['nOfTwo']+3*dataset['nOfThree']+4*dataset['nOfFour']))
    writer.writing(best_solution, dataset, filename[9]+'.txt')

# Optimazation Part here
#opt_solution = optimize.solve(dataset)
# print(opt_solution)
#score = opt_scorer.score(opt_solution, dataset)

# dataset = parser.parse('datasets/a_example')
# solution = solver.solve(dataset)
# print(solution)
# score = scorer.score(solution, dataset)
# print("Score =",score)

#loop 100 times
""" for i in range(100):
    score = 0
    for idx, filename in enumerate(sorted(glob.glob('datasets/*'))):
        dataset = parser.parse(filename)
        start_time = time.time()
        solution = solver.solve(dataset)
        score = scorer.sim(dataset, solution) """