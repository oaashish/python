#count of unique words in a string
input = " hi hi monu becausae hi aashish ola ola  "
uniques = {}
duplicates = {}

if input.strip() == "":
    print "count of uniques is 0"
    print "count of duplicates 0"
else:
    input_part = input.split(" ")

    for x in input_part:
        if x == "":
            continue
        if x not in uniques:
            uniques[x] = 1
        else:
            duplicates[x] = 1

    print "count of uniques is {}".format(len(uniques))
    print "count of duplicates is {}".format(len(duplicates))