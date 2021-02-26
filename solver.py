
"""
Easiest solution:
1. If the intersection only has one incoming lane, always on.
2. Otherwise, cycle the each traffic light in each intersection for 1s.

Better solution:
1. If the intersection only has one incoming lane, always on.
2. Each intersection will be a "queue"
3. Each street will be a "process". If the total time to completion (not number of path) 
is lower for all the waiting cars, it has a higher priority.

The "time to completion" should be added +1 by the time it is at the queue.

4. Keep one side always on, until there is now a queue with lower total time to completion.
"""

def find_adj_list(dataset):
	adjacency_list = []
	for i in range(0, dataset["nIntersection"]):
		adjacency_list.append(
			{"index": i, "in_streets": [], "out_streets": []})
	for street in dataset["streets"]:
		start_node = adjacency_list[street["start"]]
		if start_node not in adjacency_list[street["start"]]['out_streets']:
			adjacency_list[street["start"]]['out_streets'].append(street["index"])

		end_node = adjacency_list[street["end"]]
		if end_node not in adjacency_list[street["start"]]['in_streets']:
			adjacency_list[street["end"]]['in_streets'].append(street["index"])

	return adjacency_list


"""
adjacency_list = [
	{
		index: 0        // Index of intersection
		in_streets: [1, 3],
		out_streets: [4, 2]
	}
]

"""


def street_queue(dataset):
	s_queue = []
	for i in range(dataset['nCars']):
		street_idx = dataset['cars'][i]['path'][0]
		dataset['streets'][street_idx].append(i)

"""
"cars" : [
		{
			"index": int,
			"start": int,       // start intersection
			"end"  : int,       // (initialize sys.maxsize) //tbc
			"path" : [ str, str, str, ... ] // list of street names
			"curr" : int // index in path, indicate where the car is
		}
	]
"""

""" def sim(dataset, sche):
	cars = dataset["cars"]
	streets = dataset["streets"]

	
	[
		{
			"car_index": int,  
			"street_index": int
			"remaining_time": int
		}
	]
	
	travelling_cars = []
	intersection_open = []

	""
	finished_cars = []

	# Initilalize intersection list
	for i in range(len(sche)):
		intersection_open.append({"intersection_index":i,"open_street": sche["schedule"][i][0],"schedule_position":0,"remaining_time":sche["schedule"][i][1]})

	# for each time interval
	for i in range(dataset['nDuration']):
		travelling_cars_to_put = []
		#for green blub street:
		for intersection in sche:
			is_now = intersection_open[intersection["index"]]
			is_open_street = is_now["open_street"]
			
			leaving_car = streets[is_open_street]["queue"].pop(0)
			_ = car[leaving_car]["path"].pop(0)
			next_street = car[leaving_car]["path"][0]
			travelling_cars_to_put.append({
			"car_index": leaving_car,  
			"street_index": next_street,
			"remaining_time": streets[next_street]["time"]
			})

			if is_now["remaining_time"] != 0:
				is_now["remaining_time"] -= 1
			else:
				curr_sche_position = (is_now["schedule_position"] + 1) % len(sche["schedule"])
				is_now["schedule_position"] = curr_sche_position
				is_now["open_street"] = sche["schedule"][curr_sche_position][0]
				is_now["remaining_time"] = sche["remaining_time"][curr_sche_position][0]
				
				# dequeue street["queue"] -> car
				# vehicle = dataset["street"][intersection["index"]]["queue"].pop()
				# dequeue car["path"] -> road
				# road = 
				# tempList.append(car, road, road["time"]) -> cars travel
		
		# for all streets, cars travel: time - 1 ; time = 0 -> queue
		if len(travelling_cars) != 0:
			for car in travelling_cars:
				car["remaining_time"] -= 1
				if car["remaining_time"] == 0:
					dest_index = car["street_index"]
					veh_index = car["car_index"]
					dataset['streets'][dest_index]["queue"].insert(0, dataset['cars'][veh_index])
					travelling_cars.remove(car)
					# pop the car, and put it in the queue of its next destination

		travelling_cars.extend(travelling_cars_to_put)

		#for car in 
		for car in cars:
			if len(car["path"]) == 0:
				finished_cars.append({"car_index":car["index"],"finished_time":i})

	score = 0
	for c in finished_cars:
		score += dataset["nDuration"] - car["finished_time"]

	print(score) """

"""
			if intersection['rt']==0:
				intersection['curr_s'] +=1
				if intersection['curr_s']>= len(intersection['schedule']):
					intersection['curr_s']=0
				intersection['rt']=intersection['schedule'][intersection['curr_s']][1]
			curr_car=dataset['streets'][]
"""

"""
				intersection['rt']=intersection['schedule'][intersection['curr_s']][1]
			curr_car=dataset['streets'][]

"""
"""

[
	{
		index: int              // intersection index
		schedule: [             // this is an array of tuple
			(street_name1, time1),      // this is a tuple
			(street_name2, time2),
		]
	}
]
"""
"""
def solve(dataset):
	adj_list = find_adj_list(dataset)
	solution = []
	for v in adj_list:
		solution.append({"index": v['index'], "schedule": []})
	for intersection in adj_list:
		if len(intersection['in_streets']) == 1:
			solution[intersection["index"]]["schedule"] = [
				(intersection["in_streets"][0], 1)]
		elif len(intersection["in_streets"]) > 1:
			for street_index in intersection["in_streets"]:
				solution[intersection["index"]]["schedule"].append((street_index, 2))

	return solution
"""

import random
import math
import optimize

def gen_random_list(street_list):
	l_length = len(street_list)
	randomlist = []
	while len(randomlist) != l_length:
		good_index = random.randint(0,l_length)
		if street_list[good_index] not in randomlist:
			randomlist.append(street_list[good_index])
	return randomlist

def solve(dataset):
	adj_list = find_adj_list(dataset)
	solution = []
	for v in adj_list:
		solution.append({"index": v['index'], "schedule": []})
	for intersection in adj_list:
		if len(intersection['in_streets']) == 1:
			solution[intersection["index"]]["schedule"] = [(intersection["in_streets"][0], 1)]
		elif len(intersection["in_streets"]) > 1:     
			max_seconds = math.floor(dataset["nDuration"] / 500)
			if max_seconds < 1:
				max_seconds = 2
			random_list = gen_random_list(intersection["in_streets"])
			for street_index in random_list:
				solution[intersection["index"]]["schedule"].append((street_index, random.randint(1,max_seconds)))

	return solution

def shit_greedy_sovle(dataset):
	adj_list = find_adj_list(dataset)
	return shitty_greedy(dataset,adj_list)
	return optimize.ps(dataset,adj_list)