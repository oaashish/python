# https://www.calculatorsoup.com/calculators/statistics/mean-median-mode.php

input = [50,1,-3,2,-4,6,0,-14,2,4,-6,5,1,3,2,4,6,0,-14,2,-4,6,100,100,0,14,14,4365,567,11,111,111,111,111,111,111,111,111,111,111,111,111,111]
input_len = len(input)
print "Input length : {}".format(input_len)
input.sort()

if input_len % 2 == 1:
    print "Median : {}".format(input[input_len/2])
else:
    i = input_len/2
    print "Median : {}".format((ixinput[i-1] + input[i])/2.0)