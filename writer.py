"""

[
    {
        index: int              // intersection index
        schedule: [             // this is an array of tuple
            (street_name1, time1),      // this is a tuple
            (street_name2, time2),
        ]
		curr_s: int // current street idx
		rt: int // reminding time of current street
    }
]
"""


def writing(solution, dataset, filename):
    print(solution)
    filename = 'output/' + filename
    with open(filename, 'w') as fo:
        fo.write(str(len(solution))+'\n')
        for intersection in solution:
            fo.write(str(intersection["index"]) + '\n')
            fo.write(str(len(intersection["schedule"])) + '\n')
            for job in intersection["schedule"]:
                now = job[0]
                street_name = dataset['streets'][job[0]]["name"]
                fo.write(str(street_name) + ' ' + str(job[1]))
                fo.write('\n')