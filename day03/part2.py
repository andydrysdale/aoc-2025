def find_max_joltage(batt_string, batt_count):
    joltage_digits = []
    batt_size = len(batt_string)
    string_position = 0

    # Move along the battery string
    while string_position < batt_size:
        digit_found = False
        digit = 9
        # Scan for a 9, if none is found then scan for an 8 and so on. The scan 
        # should start after the last found digit but end at a point where there 
        # will be room for the rest of the joltage digits.
        while not digit_found:
            scanning_pointer = string_position
            last_scan_position = batt_size - batt_count + len(joltage_digits)
            while not digit_found and scanning_pointer <= last_scan_position:
                # When the digit is found, add it to an array, move the pointer up to 
                # the current scanning position and reset the required digit back to 9.
                if batt_string[scanning_pointer] == str(digit):
                    digit_found = True
                    string_position = scanning_pointer
                    joltage_digits.append(batt_string[scanning_pointer])
                    # If all digits are found, join the up and return it as a number
                    if len(joltage_digits) == batt_count: 
                        return int("".join(joltage_digits))
                else:
                    scanning_pointer += 1
            digit -= 1           
        string_position += 1


# Main routine
if __name__ == '__main__':
    running_total = 0

    with open("puzzledata.txt", "r", encoding="utf-8") as file:
        for line in file.readlines():
            joltage = find_max_joltage(line.strip(), 12)
            print(joltage)
            running_total += joltage
        
    print("\nResult:", running_total)