# indexing = accessing elements of a sequence using [] (indexing operator)

#                     [start : end : step]


#for step we need two colons ::

#we don't require the starting of theindex but we do need the end of the index

#like  this print(credit_number[:4]) 
#here the ending index is 4




credit_number = "1234-5678-9012-3456"



print(credit_number[0])

print(credit_number[0:4])

print(credit_number[:4])

print(credit_number[4:8])

print(credit_number[4:])

print(credit_number[-1]) #last number

print(credit_number[-4:])

print(credit_number[::2]) #print every second character

print(credit_number[::3])



# EXERCISE 1

credit_number = "1234-5678-9012-3456"

# last_digits = credit_number[-4:]

# print(f"XXXX-XXXX-XXXX-{last_digits}")

#o/p - xxxx-xxxx-xxxx-3456


# EXERCISE 2  

credit_number = "1234-5678-9012-3456"
credit_number = "1234-5678-9012-3456"
credit_number[::-1]

print(credit_number)

#o/p - 6543-2109-8765-4321
