def make_new_row(new_row):
    if new_row == []:
        return [1]
    row = [1, 1]
    a = len(new_row)
    for i in range(0, len(new_row)-1):
        num = new_row[i] + new_row[i+1]
        row.insert(i+1, num)
    return row


# Main program starts here - DO NOT CHANGE
height = int(input("Height of Pascal's triangle (n>=1): "))
new_row = []
for i in range(height):
    new_row = make_new_row(new_row)
    print(new_row)
