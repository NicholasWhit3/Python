class MyClass:

  def sortArr(self, arr):
    ifFirst = False
    last_int_index = None
    if (arr[0] == None): ifFirst = True
    for x in arr:
      if isinstance(x, str):
        arr.remove(x)
    for i in range(0, len(arr)):
      if isinstance(arr[i], int):
        last_int_index = i
      else:
        if last_int_index:
          arr[i] = arr[last_int_index]
        else: 
          pass
    
    
    return [x if isinstance(x, int) else arr[last_int_index] for x in arr] 

obj = MyClass()
my_arr = [None, None, 100, None, 2, 'jhjh', None, 3, 'oiuoiu', None, 'gjhghj', None]
print(obj.sortArr(my_arr))
