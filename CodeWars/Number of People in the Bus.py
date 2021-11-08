def number(bus_stops):
    arr = ([])
    people = 0

    for i in bus_stops:
        arr = i
        people += arr[0] - arr[1] 
    
    return people
