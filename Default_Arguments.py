# Default Arguments = A default value for certain parameters default is used when that argument is omitted make your functions more flexible   

# 1 positional 2 Default 3 Keyword 4 arbitrary

#keep default arguments as right as possible make sure there is no positional arguments after it 

# ----- EXAMPLE -----

def net_price(list_price, discount=0, tax=0.05):

   return list_price * (1 - discount) * (1 + tax)



# print(net_price(500))

# print(net_price(500, 0.1))

# print(net_price(500, 0.1, 0))



# ----- EXERCISE -----

import time



def count(end, start=0): 

    for x in range(start, end+1):

        print(x)

        time.sleep(1)

    print("DONE!")



# count(10)

# count(30, 15)