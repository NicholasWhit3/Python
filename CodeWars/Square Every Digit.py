def square_digits(num):
    digits = [int(x) for x in str(num)]
    digitsList = []
    result = ""
    for i in digits:
        digitsList.append(i**2)
    for elem in digitsList:
        result += str(elem)

    return(int(result))

