def move_zeros(lst):
    new_lst = [int(x) for x in lst if x != 0]
    for x in range(lst.count(0)):
        new_lst.append(0)

    return new_lst


print(move_zeros([1, 2, 1, 0, 1, 0, 3, 0, 1, 0, 0, 0, 0]))

