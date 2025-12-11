fresh_ids = []
fresh_total = 0

with open("puzzledata.txt", "r", encoding="utf-8") as file:
    for line in file.readlines():
        line = line.strip()
        if "-" in line:
            parts = line.split('-')
            fresh_ids.append((int(parts[0]), int(parts[1])))
        elif line == "":
            pass  # do nothing on blank line
        else:
            fresh = False
            for group in fresh_ids:
                if group[0] <= int(line) <= group[1]: fresh = True
            if fresh: fresh_total += 1
                 
print("Result:", fresh_total)