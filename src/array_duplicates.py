def get_array_duplicates(arr):
    d = {}
    l = []
    for x in arr:
        d[x] = d.get(x, 0) + 1
        if d.get(x, 0) > 1:
            l.append(x)
    return l


print get_array_duplicates([1, 4, 45, 45, -45, 6, 4, 0, 19])