def rec_count(map, y, x, y_len, x_len):
    global count
    map[y][x] = 0
    count += 1
    if y != 0:
        if map[y - 1][x] == 1:
            rec_count(map, y - 1, x, y_len, x_len)
    if x != 0:
        if map[y][x - 1] == 1:
            rec_count(map, y, x - 1, y_len, x_len)
    if x != x_len - 1:
        if map[y][x + 1] == 1:
            rec_count(map, y, x + 1, y_len, x_len)
    if y != y_len - 1:
        if map[y + 1][x] == 1:
            rec_count(map, y + 1, x, y_len, x_len)
    if x != 0 and y != 0:
        if map[y - 1][x - 1] == 1:
            rec_count(map, y - 1, x - 1, y_len, x_len)
    if x != 0 and y != y_len - 1:
        if map[y + 1][x - 1] == 1:
            rec_count(map, y + 1, x - 1, y_len, x_len)
    if x != x_len - 1 and y != 0:
        if map[y - 1][x + 1] == 1:
            rec_count(map, y - 1, x + 1, y_len, x_len)
    if x != x_len - 1 and y != y_len - 1:
        if map[y + 1][x + 1] == 1:
            rec_count(map, y + 1, x + 1, y_len, x_len)
    return count
def checkio(land_map):
    global count
    count = 0
    ans = []
    for i in range(len(land_map)):
        for j in range(len(land_map[i])):
            if land_map[i][j] == 1:
                ans.append(rec_count(land_map, i, j,len(land_map),len(land_map[i])))
                count = 0
    ans.sort()
    return ans
