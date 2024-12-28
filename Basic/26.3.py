# enumerate function

# Find index of each element in list

def index_finder(list_value):
    result = []
    for index in enumerate(list_value):
        result.append(index)
        
    return result
    
print(index_finder([1,2,4]))

# result
# [(0, 1), (1, 2), (2, 4)]