def find_missing(array1, array2):

   x = sorted(array1)  
   
   y = sorted(array2)

   if x==y:
    return 0
   else:
    for i in (set(y) -set(x)):
        return i
    