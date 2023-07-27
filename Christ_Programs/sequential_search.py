import numpy as np
def sequential_search(var,search):
    for i in range (len(var)):
     if search == var[i]:
         return True 
    return False
var = input("Enter the array").split()
var = np.array(var,dtype='int16')
search = int(input("Enter the number which you want to search for"))
if sequential_search(var, search):
                print ("Element found")
else :
                 print("Not Found!")
