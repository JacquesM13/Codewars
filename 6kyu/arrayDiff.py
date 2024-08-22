''' Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b keeping their order.

array_diff([1,2],[1]) == [2]

If a value is present in b, all of its occurrences must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3] '''

# My solution

def array_diff(a, b):
    out = []                    # Create an empty list which will store elements for return
    for i in a:                 # Iterate through a
        if i not in b:          # If the value is not in b...
            out.append(i)       # add it to the output list
    return out                  # Return list of unommon elements

# Good solution

'''
def array_diff(a, b):
    return [x for x in a if x not in b]

'''
