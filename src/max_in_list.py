# Don't initialize max with 0 (List will all negatives values)
# Check for empty list in beginning

def getMaxInList(input_list):
    if len(input_list) == 0:
        return None
    else:
        imax = input_list[0]
        for x in input_list:
            if x > imax:
                imax = x
        return imax


assert getMaxInList([-5,15,3,25,7,0,25]) == 25
assert getMaxInList([-5,-15]) == -5
assert getMaxInList([]) == None
print "Pass"


