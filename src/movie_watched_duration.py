def total_watched_time(input_data):
    watched_minutes = dict()
    for view in input_data:
        a, b = view
        for i in range(a, b):
            watched_minutes[i] = 1
    return len(watched_minutes)


def total_watched_time_v2(input_data):
    input_data.sort()
    watched_minutes = 0
    pointer = 0
    print "lenght is {}".format(len(input_data))
    for i in range(len(input_data)):
        if i == 0:
            s , e = input_data[0]
            watched_minutes += (e - s)
        else:
            s, e = input_data[i]
            sold, eold = input_data[i-1]
            if s >= eold:
                watched_minutes += (e - s)
            else:
                watched_minutes += (e - eold)
        print watched_minutes
    return watched_minutes


print total_watched_time_v2([(0,10), (13,18), (21,26), (15,23)])
