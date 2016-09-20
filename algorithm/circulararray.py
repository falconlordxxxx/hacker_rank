def take_input():
    """Takes in input from Watson and 
    gathers necessary information!"""
    array_len,operation_count,query_count=input().split(' ')
    return int(array_len),int(operation_count),int(query_count)
def take_query(query_count):
    """ query_count:- number of times to ask for query
    returns input query by user!!!"""
    queries=[]
    for i in range(int(query_count)):
        query=input().strip()
        query=int(query)
        queries.append(query)
    return queries
 
def index_manipulation(queries,operation,array_len):
    """ queries:- indeces to load items from rotated list
    operation:- number of time list is going to be rotated
    array_len:- length of an array
    returns indexes that load items for rotated list"""
    
    
    
    

def main():
    array_len,operation_count,query_count=take_input()
    array=input().split(' ')
    queries=take_query(query_count)
    rotated_queries=index_manipulation(queries,operation_count,array_len)
    for i in rotated_queries:
        print (array[i])

main()
