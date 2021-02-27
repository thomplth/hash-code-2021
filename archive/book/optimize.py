
"""
Things to consider:
1. Time needed to scan all books in one library
2. Sign up time of the library
3. Scanning rate of the library
4. Distinct score of the entire library

5. scan in random order???

Steps:
1. Sort by lowest signup time + number of days required to scan all books
2. For each signed up library, first check the global shelf, then pop the book already scanned
3. scan the books in random order, update the global shelf
"""

def solve(data, shelf):
    current_day = 0
	signing_lib = {}
    next_sign_time = 0
	signed_lib = []
	solution = []

	lib_lowest_signup_time = data.lib.sort(lowest_signup_time_sort).sort(scanning_days_needed_sort)

    while current_day != data.nday:
        if current_day == next_sign_time:
            signed_lib.append(signing_lib)
            signing_lib = lib_lowest_signup_time.pop(0)
            next_sign_time += signing_lib.signup
        
        for lib in signed_lib:
            lib.books = filter(lambda x: return shelf.scan[x],lib.books)
            if not any(lib.index == x.index for x in solution):
                solution.append(lib)
            
            # Scan books by their order in the list
            for sol in solution:
                if sol.index == lib.index
                    sol.extend(lib.books[0:lib.ship]))
                    lib.books = lib.books[lib.ship:]
                
        current_day += 1
    
    return solution

def solve_sort_signup_and_sort_book_score(dataset):
	sorted_lib=data.lib.sort(scanning_days_needed_sort)


def scanning_days_needed_sort(a, b, order = 1):
    # default: highest first
	if len(a.books) / a.ship < len(b.books) / b.ship:
		return order
	elif len(a.books) / a.ship == len(b.books) / b.ship:
		return 0
	else: 
		return -order

def highest_scanning_rate_sort(a, b):
	if a.ship > b.ship:
		return 1
	elif a.ship == b.ship:
		return 0
	else: 
		return -1

def lowest_signup_time_sort(a, b):
	if a.sign_days < b.sign_days:
		return -1
	elif a.sign_days == b.sign_days:
		return 0
	else: 
		return 1

def highest_library_score_sort(a, b, shelf):
	a_score = sum(map(filter(a.books,lambda y: shelf.scan[y]),lambda x: shelf.score[x]))
	b_score = sum(map(filter(b.books,lambda y: shelf.scan[y]),lambda x: shelf.score[x]))
	if a_score > b_score:
		return 1
	elif a_score == b_score:
		return 0
	else: 
		return -1