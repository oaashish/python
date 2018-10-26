def get_unique_list(arr):
    d = {}
    l = []
    for x in arr:
        d[x] = d.get(x, 0) + 1
        if d.get(x, 0) < 2:
            l.append(x)
    return l


print get_unique_list([1, 4, 45, 45])