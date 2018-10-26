# https://www.calculatorsoup.com/calculators/statistics/mean-median-mode.php
# Sort the list first before getting mid element
# Check if all elements of list are digits, raise exception if not

def get_median(input):
    input_len = len(input)
    if input_len == 0:
        return None
    else:
        input.sort()
        if input_len % 2 == 1:
            return input[input_len / 2]
        else:
            i = input_len / 2
            return (input[i - 1] + input[i]) / 2.0


assert get_median([-14,2,-4,6,100,100,0,14,14,4365,567,11,111]) == 14
assert get_median([-14,2,-4,6,100,100,0,14,12,4365,567,11,111]) == 12
assert get_median([]) == None
#assert get_median(['2','1']) == None

print "Pass"
