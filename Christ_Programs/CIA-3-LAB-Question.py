# MainString: "I like carrots

# ["I", "like", "carrots"]

# convert all strings to lists

# Input String 1: "I like"(TRUE)
# Input String 2: "tomatoes and peas"(FALSE)

# USE REGEX TO REMOVE SMALL a-z from any string
# a-z


       
# def convert_String(convert,input_string):
#     s = list(convert)
    


 
def main():
  s = []

  no_of_strings = input("Enter the string")
  input_string =  input("Enter the string to search in the sublist")
  s=list(no_of_strings)
  for i in range(len(s)):
     print(s[i].split(" "))

#   convert_String(no_of_strings,input_string)

  if __name__ == "__main__":
    main()


