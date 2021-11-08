def namelist(names):
    cnt = 0
    firstNames = ''
    if len(names) == 1:
        firstNames += (names[cnt].get("name"))
    elif len(names) == 2:
        firstNames += (names[cnt].get("name"))
        firstNames += (" & ")
        firstNames += (names[cnt+1].get("name"))
    elif len(names) > 2:
            for i in range(0, len(names)-1):
                firstNames = firstNames + names[i].get("name") + ", "
            firstNames = firstNames[:-2] + " & " + names[len(names)-1].get("name")
    return firstNames
