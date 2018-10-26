def first_unique_in_list(lst):
    counts = dict()
    for item in lst:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1

    for item in lst:
        if counts[item] == 1:
            return item
    return -1


assert first_unique_in_list([1,2,1,3,2,5]) == 3
assert first_unique_in_list([1,2,1,3,3,2,5]) == 5
assert first_unique_in_list([1,2,1,3,3,2,5,5]) == -1
assert first_unique_in_list([7]) == 7
assert first_unique_in_list("asd") == 'a'
print "Pass"
