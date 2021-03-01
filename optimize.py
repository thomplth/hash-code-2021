"""
Principle 1: See the number of cars in each intersection, and give higher weight to that queue.
"""


"""
Priority of street: for each intersection,
    let s be the number of incoming street,
        d be the simulation duration,
    by looking at first d/s car of every incoming street, more short distance car at first d/s car, higher proirity 
    define short distance: random number?

    
"""
import random
import math, time

import writer
import scorer
import parser
import time
import glob

# def shit_sort_key(t):
#     return t[1]


# def ps(dataset,a_list):
#     base_time=random.randint(1,10)
#     short_dis=random.randint(1,5)
#     solution=[]
#     for v in a_list:
#         solution.append({"index": v['index'], "schedule": []})
#     for i in a_list:
#         num_of_short=[]
#         for j in range(len(i['in_streets'])):
#             num_of_short.append((i['in_streets'][j],0))
#             for k in range(min(len(dataset['streets'][j]['queue']),int(dataset['nDuration']/len(i['in_streets'])))):
#                 curr_car_idx=dataset['streets'][j]['queue'][k]
#                 path_len=len(dataset['cars'][curr_car_idx]['path'])
#                 if path_len<=short_dis:
#                     num_of_short[j][1]+=1
#         num_of_short.sort(key=shit_sort_key,reverse=True)
#         for j in range(len(i['in_streets'])):
#             solution[i["index"]]["schedule"].append((num_of_short[j][0], j+1))
#     return solution



# def shitty_greedy(dataset,a_list):
#     base_time=random.randint(1,10)
#     short_dis=random.randint(1,5)
#     solution=[]
#     for v in a_list:
#         solution.append({"index": v['index'], "schedule": []})
#     for i in a_list:
#         car_len=[]
#         for j in range(len(i['in_streets'])):
#             car_len.append((j,len(dataset['streets'][j]['queue'])))
#         car_len.sort(key=shit_sort_key,reverse=True)
#         for j in range(len(i['in_streets'])):
#             solution[i["index"]]["schedule"].append((i['in_streets'][car_len[j][0]], int(car_len[j][1])))
#     return solution


def shitty_dynamic(dataset):
    sol = []
    score, queues = {}, {}
    streets = dataset['streets'].copy()
    cars = dataset['cars'].copy()

    for d in streets:
        if d['name'] not in score:
            score[d['name']] = len(d['queue'])
        if d['name'] not in queues:
            queues[d['name']] = d['queue']

    for i in range(dataset['nDuration']):
        for d in streets:
            if not queues[d['name']]:
                continue
            car_idx = queues[d['name']].pop(0)
            if not cars[car_idx]['path']:
                continue
            strt_name = cars[car_idx]['path'].pop(0)
            queues[strt_name].append(car_idx)
            score[d['name']] += len(d['queue'])

    for i in range(dataset["nIntersection"]):
        item = {'index': i, 'schedule': []}
        strt = {}
        for d in dataset['streets']:
            if d['end'] == i:
                strt[d['name']] = score[d['name']]
        if sum(strt.values()) != 0:
            base = int(dataset['nDuration'] / 100)
            base = int(dataset['nDuration'] / 10) if base == 0 else base
            base = 1 if base == 0 else base
            for key in strt.keys():
                time = int(base * (strt[key]/sum(strt.values())))
                if time == 0:
                    continue
                tup = (key, time)
                item['schedule'].append(tup)
            sol.append(item)
    return sol


def write(solution, dataset, filename):
    filename = 'output2/' + filename
    with open(filename, 'w') as fo:
        fo.write(str(len(solution))+'\n')
        for intersection in solution:
            fo.write(str(intersection["index"]) + '\n')
            fo.write(str(len(intersection["schedule"])) + '\n')
            for job in intersection["schedule"]:
                street_name = job[0]
                fo.write(str(street_name) + ' ' + str(job[1]) + '\n')


for idx, filename in enumerate(sorted(glob.glob('datasets/*'))):
    dataset = parser.parse(filename)
    start_time = time.time()
    solution = shitty_dynamic(dataset)
    print("--- %.10f seconds ---" % (time.time() - start_time))
    # score = scorer.sim(dataset, solution)
    write(solution, dataset, filename[9]+'.txt')