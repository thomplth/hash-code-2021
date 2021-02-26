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
            "queue": [car, car, car, ...]// list of car on that queue
        }, 
    ]
    "cars" : [
        {
            "index": int,
            "start": int,       // start intersection
            "end"  : int,       // (initialize sys.maxsize) //tbc
            "path" : [ str, str, str, ... ] // list of street names
        }
    ]
"""


def parse(filename):
    with open(filename, 'r') as fi:
        nDuration, nIntersection, nStreet, nCars, nBonus = map(
            int, fi.readline().split())
        streets, cars = [], []

        for i in range(nStreet):
            line = list(map(str, fi.readline().split()))
            item = {
                "index": i,
                "start": int(line[0]),
                "end": int(line[1]),
                "name": line[2],
                "time": int(line[3]),
                "queue": []
            }
            streets.append(item)

        for i in range(nCars):
            line = list(map(str, fi.readline().split()))
            item = {
                "index": i,
                "start": int(line[0]),
                "end"  : nDuration + 1,
                "path": line[1:]
            }
            for j in range(len(streets)):
                if streets[j]['name'] == line[1]:
                    streets[j]['queue'].append(i)
                    break
            cars.append(item)

        dataset = {
            "nDuration": nDuration,
            "nIntersection": nIntersection,
            "nStreet": nStreet,
            "nCars": nCars,
            "nBouns": nBonus,
            "streets": streets,
            "cars": cars
        }

        return dataset


# print(parse('datasets/a.txt'))
# print(parse('datasets/b.txt'))
# print(parse('datasets/c.txt'))
# print(parse('datasets/d.txt'))
# print(parse('datasets/e.txt'))
# print(parse('datasets/f.txt'))

