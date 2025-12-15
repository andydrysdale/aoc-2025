from operator import add, mul


def process_block(data, op_func, start_pointer, init_value):
    """Process a block of numbers until a gap is found, applying op_func (+ or *)."""
    result = init_value
    pointer = start_pointer
    while True:
        num_string = "".join(data[i][pointer] for i in range(len(data) - 1))
        if not num_string.strip():
            break
        result = op_func(result, int(num_string))
        pointer += 1
    return result, pointer


def main():
    with open("puzzledata.txt", "r", encoding="utf-8") as file:
        data = [line.rstrip("\n") for line in file]

    running_total = 0
    pointer = 0

    while pointer < len(data[0]):
        symbol = data[len(data) - 1][pointer]
        if symbol == "+":
            block_sum, pointer = process_block(data, add, pointer, 0)
            running_total += block_sum
        elif symbol == "*":
            block_product, pointer = process_block(data, mul, pointer, 1)
            running_total += block_product
        else:
            pointer += 1  # skip unknown symbols
            
    print("Result:", running_total)


if __name__ == "__main__":
    main()