import string

def print_rangoli(size):
    # all lowercase letters
    alpha = string.ascii_lowercase
    
    # total width of the rangoli
    width = 4 * size - 3
    
    # build each row
    rows = []
    for i in range(size):
        # descending part: from current letter down to 'a'
        left = alpha[size-1 : size-i-1 : -1]
        # ascending part: from 'a' back up to current letter
        right = alpha[size-i-1 : size]
        row = "-".join(left + right)
        rows.append(row.center(width, "-"))
    
    # print top + middle + bottom (mirror of top)
    print("\n".join(rows + rows[-2::-1]))

