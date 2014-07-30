import MapReduce
import sys

mr = MapReduce.MapReduce()


# We assume that matrix dimensions is known beforehand
# A  is MxK matrix, whereas B is KxN one
M = 5
K = 5
N = 5

def mapper(record):
    '''
    The input to the map function will be matrix row records formatted as lists.
    Each list will have the format [matrix, i, j, value] where matrix is a string and i, j, and value are integers.
    The first item, matrix, is a string that identifies which matrix the record originates from. This field has two possible values:
        'a' indicates that the record is from matrix A
        'b' indicates that the record is from matrix B
    '''
    matrix, row, col, value = record
    
    for n in range(N):
        if matrix == 'a':
            destination_cell = (row,n)
            matrix_position = 'L'
            serial_number = col
        else:
            destination_cell = (n,col)
            matrix_position = 'R'
            serial_number = row
        mr.emit_intermediate( destination_cell, (matrix_position ,serial_number, value) )
            

def reducer(key, list_of_values):
    '''
    The output from the reduce function will also be matrix row records formatted as tuples.
    Each tuple will have the format (i, j, value) where each element is an integer.
    '''
    
    left_matrix_value = [ (item[1],item[2]) for item in list_of_values if item[0] == 'L' ]
    right_matrix_value = [ (item[1],item[2]) for item in list_of_values if item[0] == 'R' ]

    result = 0

    for item_L in left_matrix_value:
        for item_R in right_matrix_value:
            if item_L[0] == item_R[0] :
                result += item_L[1] * item_R[1]

    mr.emit( ( key[0], key[1], result ) )

inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
