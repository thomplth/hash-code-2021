def parse(filename):
    with open(filename, 'r') as fi:
        nbook, nlib, nday = map(int, fi.readline().split())
        scores = list(map(int, fi.readline().split()))

        shelf = []
        for s in scores:
            item = {
                'score': s,
                'scan': False
            }
            shelf.append(item)

        lib = []
        count = 0
        for line in fi:
            lnbook, lnsign, lnship = map(int, line.split())
            item = {
                'index': count,
                'books': [],
                'signup': lnsign,
                'ship': lnship
            }

            count += 1
            nextline = next(fi)
            item['books'] = list(map(int, nextline.split()))
            
            lib.append(item)
            
        dataset = {
            "nbook": nbook,
            "nlib": nlib,
            "nday": nday,
            "lib": lib,
            "shelf": shelf
        }

        return dataset

print(parse('datasets/a_example.txt'))
# print(parse('datasets/b_read_on.txt'))
# print(parse('datasets/e_many_teams.in'))
