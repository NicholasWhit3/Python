def descending_order(num):
    num_to_list = [str(x) for x in str(num)]
    return int("".join(list(reversed(sorted(num_to_list)))))
    
    
'''
Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. 
Essentially, rearrange the digits to create the highest possible number.
'''
