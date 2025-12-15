maths = []

with open("puzzledata.txt", "r", encoding="utf-8") as file:
    for line in file.readlines():
        maths.append(line[:-1])

width = len(maths[0])
number_count = len(maths) - 1
running_total = 0
pointer = 0

while pointer < width:
    if maths[number_count][pointer] == "+":
        sum = 0
        gap_found = False
        while not gap_found:
            num_string = ""
            for i in range(number_count):
                num_string += maths[i][pointer]
            if num_string.strip() == "":
                gap_found = True
            else:
                sum += int(num_string)
            pointer += 1
        running_total += sum
            
    elif maths[number_count][pointer] == "*":
        product = 1
        gap_found = False
        while not gap_found:
            num_string = ""
            for i in range(number_count):
                num_string = num_string + maths[i][pointer]
            if num_string.strip() == "":
                gap_found = True
            else:
                product *= int(num_string)
            pointer += 1
        running_total += product

print("Result:", running_total)