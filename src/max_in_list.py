input_list = [-5,15,3,25,7,0,25]

print "Max using inbuild function is {}".format(max(input_list))

imax = 0

for x in input_list:
    if x > imax:
        imax = x

print "Max using function is {}".format(imax)


a = enumerate(input_list)

print max(a)