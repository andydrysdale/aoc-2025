fresh_ids = []
new_ids = []

# put the ranges into a list of tuples
with open("puzzledata.txt", "r", encoding="utf-8") as file:
    for line in file.readlines():
        line = line.strip()
        if "-" in line:
            parts = line.split('-')
            fresh_ids.append((int(parts[0]), int(parts[1])))

# sort the list by the first value in the tuple
# so that only need to check the end values
fresh_ids.sort()

# iterate through the sorted ranges
for id_range in fresh_ids:
    # check if there is anything to compare to yet
    if new_ids: 
        # if the current range overlaps with the last item in the 
        # list, combine them and replace the last item in the new list
        if id_range[0] <= new_ids[-1][1]:
            new_start = new_ids[-1][0]
            if new_ids[-1][1] > id_range[1]:
                new_end = new_ids[-1][1]
            else:
                new_end = id_range[1]
            new_ids.pop()
            new_ids.append((new_start, new_end))
        # if no overlap, add the range to the new list
        else: 
            new_ids.append(id_range)
    # put the first range in a new list
    else:
        new_ids.append(id_range)

# count the number of ids in each new range
running_total = 0
for new_range in new_ids:
    running_total += (new_range[1] - new_range[0] + 1)

print("Result:", running_total)