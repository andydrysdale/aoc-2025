layout = []

# Read the file into a list of strings. Add a buffer of 1 unit of empty
# space (".") on all sides to avoid complicating the neighbour check.
with open("puzzledata.txt", "r", encoding="utf-8") as file:
    for line in file.readlines():
        line = line.strip()
        if len(layout) == 0:
            layout.append("." * (len(line) + 2))
        layout.append("." + line + ".")
layout.append(layout[0])

width = len(layout[0])
height = len(layout)

accessible_count = 0
for x in range(width):
    for y in range(height):
        if layout[y][x] == "@":
            # Count which of the 8 neighbours are occupied
            surrounding_count = 0
            if layout[y-1][x-1] == "@": surrounding_count += 1
            if layout[y-1][x] == "@": surrounding_count += 1
            if layout[y-1][x+1] == "@": surrounding_count += 1
            if layout[y][x-1] == "@": surrounding_count += 1
            if layout[y][x+1] == "@": surrounding_count += 1
            if layout[y+1][x-1] == "@": surrounding_count += 1
            if layout[y+1][x] == "@": surrounding_count += 1
            if layout[y+1][x+1] == "@": surrounding_count += 1
            
            if surrounding_count < 4: accessible_count += 1

print("Total accessible:", accessible_count)