def disemvowel(string_):
    vowels = ['a','e','i','o','u']
    result =[letter for letter in string_ if letter.lower() not in vowels]
    result = ''.join(result)
    return result
