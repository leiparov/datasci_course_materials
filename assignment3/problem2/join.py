import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""
TABLE1 = 'order'
TABLE2 = 'line_item'

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    table_name = record[0]
    order_id  = record[1]
    table_fields = record[2:]
    
    mr.emit_intermediate(order_id, [table_name, table_fields])

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    #print list_of_values

    table1 = [table[1] for table in list_of_values if table[0] == TABLE1]
    table2 = [table[1] for table in list_of_values if table[0] == TABLE2]

    for record1 in table1:
        for record2 in table2:
            res = []
            res.append(TABLE1)
            res.append(key)
            res.extend(record1)
            res.append(TABLE2)
            res.append(key)
            res.extend(record2)

            mr.emit(res)


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
