def total_watched_time(input_data):
    watched_minutes = dict()
    for view in input_data:
        a, b = view
        for i in range(a, b):
            watched_minutes[i] = 1
    return len(watched_minutes)


print total_watched_time([(0,10), (13,18), (15,23), (21,26)])
