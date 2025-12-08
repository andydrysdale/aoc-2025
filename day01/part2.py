zero_count = 0
running_total = 50

with open("puzzledata.txt", "r", encoding="utf-8") as file:
    for line in file.readlines():
        line = line.strip()

        increment = int(line[1:])

        if line[0] == "L": 
            for i in range(increment):
                running_total -= 1
                if running_total % 100 == 0: zero_count += 1
        else:
            for i in range(increment):
                running_total += 1
                if running_total % 100 == 0: zero_count += 1

print(zero_count)
