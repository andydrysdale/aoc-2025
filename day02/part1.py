file_string = ""
running_total = 0

with open("puzzledata.txt", "r", encoding="utf-8") as file:
    file_string = file.readline().strip()

sequence_strings = file_string.split(",")

for sequence in sequence_strings:
    parts = sequence.split("-")

    for number in range(int(parts[0]), int(parts[1]) + 1):
        number_string = str(number)
        if len(number_string) % 2 == 0:
            halfway = len(number_string) // 2  
            if number_string[:halfway] == number_string[halfway:]:
                print("invalid:", number_string)
                running_total += number

print("\nSum of invalid numbers:", running_total)
