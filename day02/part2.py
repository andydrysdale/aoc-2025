# use a set here so that invalid numbers are not double counted (eg 2222 is 2-2-2-2 and 22-22)
invalid_numbers_set = set()
sequence_strings = []

with open("puzzledata.txt", "r", encoding="utf-8") as file:
    file_string = file.readline().strip()
    sequence_strings = file_string.split(",")

for sequence in sequence_strings:
    print("********************************")
    print("checking:", sequence)
    print("********************************")

    parts = sequence.split("-")
    
    for number in range(int(parts[0]), int(parts[1]) + 1):
        number_string = str(number)
        string_length = len(number_string)

        # iterate through possibilities to see how the string divides nicely
        for possible_factor in range(1, string_length):
            if string_length % possible_factor == 0:

                # build up a set of the parts of the string
                parts_set= set()
                for i in range(string_length // possible_factor):
                    parts_set.add(number_string[(i*possible_factor):((i+1)*possible_factor)])
                
                # if this set only has 1 item, then all the parts must be the same
                if len(parts_set) == 1: 
                    print("invalid:", number_string)
                    invalid_numbers_set.add(number)

# total up the set of invalid numbers
running_total = 0
for num in invalid_numbers_set:
    running_total += num
print("\nSum of invalid numbers:", running_total)
