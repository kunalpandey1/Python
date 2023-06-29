# nested loop = A loop within another loop (outer, inner)

# outer loop:

# inner loop:


rows = int(input("Enter the # of rows: "))

columns = int(input("Enter the # of columns: "))

symbol = input("Enter a symbol to use: ")



for x in range(rows):

   for y in range(columns):

       print(symbol, end="")

   print() # for space in between

#-----------------------------------------
   # nested while loop

   i=0
   j=1
   while i<j:
       if i==5 and j>2 :
           break
       else:
           pass
       i+=3
       j-=4
       print('i=',i,'\tj=',j)