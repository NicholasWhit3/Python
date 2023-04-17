def likes(names):
    if len(names) == 0:
        return "no one likes this"
    else:
        match len(names):
            case 1:
                return f"{names[0]} likes this"
            case 2:
                return f"{names[0]} and {names[1]} like this"
            case 3:
                return f"{names[0]}, {names[1]} and {names[2]} like this"
            case _:
                return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"


print(likes(['Alex', 'Jacob', 'Mark', 'Max']))


