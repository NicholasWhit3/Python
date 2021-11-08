def digital_root(n):
    x = sum(int(digit) for digit in str(n))
    if x < 10:
        return x
    else:
        return digital_root(x)
        
        
 #or
        
def number_splitting(num):
    numsList = []
    digitsSum = 0

    if num >= 10:
        for x in str(num):
            numsList.append(x)
            
    for x in numsList:
        digitsSum += int(x)
    numsList.clear()
    
    if digitsSum >= 10:
        digitsSum = number_splitting(digitsSum)
        return digitsSum
    return digitsSum
        
