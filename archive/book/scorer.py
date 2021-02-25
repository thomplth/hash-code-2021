"""
dataset_format = {
    "nbook" : int, // number of books
    "nlib": int, // number of librarys
    "nday": in // number of day allowed
    "lib": // libraries and books data
        [
            {
                "books": list<int>, // list of book indexs
                "signup": int, // days required for signup process
                "ship": int // days required for shipping
            }
        ]
    "shelf": // list of dict of <book_index> as keys and <book_score> as values
        [
            {
                "score": int, // book score
                "scan": bool // book is scannable or not, default as true
            },
            {
                "score": 2,
                "scan": true
            }
        ]
}
solution format : returns: [[<lib index>, <scanned book 1>, <scanned book 2>, ...],[...],...]

[{<index> : [<scanned book 1>, <scanned book 2>]}, {<index_2> : [<scanned book 1>, <scanned book 2>,...]}]
{ index : [book1 , book2], ...}
"""

def score(solution,dataset):
    """sum of the scores of all books that are scanned within D days. """
    sum = 0
    booknum = dataset.get("nbook")
    shelf = dataset.get("shelf")

    for idx in range(booknum):
        book = shelf[idx]
        scan = book.get("scan")
        if scan:
            value = book.get("score")
            sum += value
        #test
        #print(idx, sum)
        #test end
    print("Score: ",sum)
    return sum

