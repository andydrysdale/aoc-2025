def find_max_joltage(battery_string):
    # count down through the possible first digits
    for joltage_tens in range(9, -1, -1):
        # iterate through the string (excluding the last digit) to see if that digit is present
        for i in range(len(line) - 2):  
            if battery_string[i] == str(joltage_tens):
                # once the max first digit is found, look for the max second digit
                for joltage_units in range(9, -1, -1):
                    # iterate through the remaining string to see if that digit is present
                    for j in range(i + 1, len(line) - 1):
                        # if the possible secong digit is present, 
                        # the max jotage has been found and is returned
                        if battery_string[j] == str(joltage_units):
                            joltage = (joltage_tens * 10) + joltage_units
                            return(joltage)


# Main routine
if __name__ == '__main__':
    running_total = 0

    with open("puzzledata.txt", "r", encoding="utf-8") as file:
        for line in file.readlines():
            joltage = find_max_joltage(line.strip())
            print(joltage)
            running_total += joltage
            
    print("\nResult:", running_total)