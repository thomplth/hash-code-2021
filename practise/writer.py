def write(solution, filename):
    filename = 'output/' + filename
    with open(filename, 'w') as fo:
        fo.write(str(len(solution))+'\n')
        for elt in solution:
            fo.write(str(len(elt)) + ' ' + str(elt).strip('[]').replace(',', ''))
            fo.write('\n')
        fo.close
