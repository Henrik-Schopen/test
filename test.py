

def create_list(start, length):
    x = []

    count = start
    while len(x) + start <= length:
        x.append(count)
        count += 1

    print(x)


create_list(5, 20) #This list starts at 5 and ends at 20
