# Find index of each element in list

def index_finder(list_value):
    result = []
    value_result = []
    for index, value in enumerate(list_value):
        result.append(index)
        value_result.append(value)
    return result, value_result
    
print(index_finder([1,2,4]))

# result
# ([0, 1, 2], [1, 2, 4])