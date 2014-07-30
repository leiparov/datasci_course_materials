import MapReduce
import sys

mr = MapReduce.MapReduce()


def mapper(record):
    '''
    The input is a 2 element list: [sequence id, nucleotides]
        sequence id: Unique identifier formatted as a string
        nucleotides: Sequence of nucleotides formatted as a string
    '''
    trimmed_nucleotide = record[1][:-10]
    mr.emit_intermediate( trimmed_nucleotide, 1 )

def reducer(key, list_of_values):
    '''
    The output should be the unique trimmed nucleotide strings.
    '''        
    mr.emit( key )

inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
