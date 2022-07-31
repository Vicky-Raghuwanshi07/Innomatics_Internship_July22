import string

lower_case = string.ascii_lowercase

def print_rangoli(size):
    # your code goes here
    rows = []
    for row in range(size):
        to_print = "-".join(lower_case[row:size])
        rows.append(to_print[::-1] + to_print[1:])
    width = len(rows[0])
    
    for row in range(size-1, 0, -1):
        print(rows[row].center(width, '-'))
        
    for row in range(size):
        print(rows[row].center(width, '-'))
        
