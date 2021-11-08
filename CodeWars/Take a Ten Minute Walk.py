def is_valid_walk(walk):
    ls = [str(x) for x in walk]
    if len(ls) > 10:
        return False
    else:
        for i in range(len(ls)):
            for j in range(i + 1, len(ls)):
                if str(ls[i]) == str(ls[j]):
                    return False
                return True
#2
def is_valid_walk2(walk):
    if (walk.count('n') == walk.count('s') and 
        walk.count('e') == walk.count('w') and
        len(walk) == 10):
            return True      
    return False
