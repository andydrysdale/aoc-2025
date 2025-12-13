maths = []

with open("puzzledata.txt", "r", encoding="utf-8") as file:
    for line in file.readlines():
        maths.append(line.strip().split())

sum_count = len(maths[0])
number_count = len(maths) - 1
running_total = 0

for i in range(sum_count):
    if maths[number_count][i] == "+":
        sum = 0
        for x in range(number_count):
            sum += int(maths[x][i])
        running_total += sum
    elif maths[number_count][i] == "*":
        product = 1
        for x in range(number_count):
            product *= int(maths[x][i])
        running_total += product
    else:
        print("unexpected symbol: ", maths[number_count][i])
        exit(1)

print("Result:", running_total)