def writing(solution, filename):
    filename = 'output/' + filename
    with open(filename, 'w') as fo:
        fo.write(str(len(solution))+'\n')
        for library in solution:
            fo.write(str(library.keys()[0]) + ' ' + str(len(library['books'].values())) + '\n')
            for book in library.values():
                fo.write(str(book) + ' ')
            fo.write('\n')
