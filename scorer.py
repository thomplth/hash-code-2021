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
			"time": int         // travelling time
		}, 
	]
	"cars" : [
		{
			"index": int,
			"start": int,       // start intersection
			("end"  : int,       // initialize sys.maxsize) //tbc
			"path" : [ str, str, str, ... ] // list of street names
		}
	]
}

solution format :


"""

""" def score(dataset):
	sim(dataset, sche)
	sum = 0
	nDuration = dataset.get("nDuration")
	nBouns = dataset.get("nBouns")
	cars = dataset.get("cars")

	for pui in cars:
		end = pui.get("end")
		if end <= nDuration:
			sum += nBouns
			sum += (nDuration - end)
		# test
		print(sum)
		# test end
	print("Score: ", sum)
	return sum """

def sim(dataset, sche):
	cars = dataset["cars"]
	streets = dataset["streets"]

	""" 
	[
		{
			"car_index": int,  
			"street_index": int
			"remaining_time": int
		}
	]
	"""
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

	print(score)
	return score