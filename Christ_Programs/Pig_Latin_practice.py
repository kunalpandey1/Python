#• If the word begins with a consonant (including y), then all letters at the beginning of the word, up to the first vowel (excluding y), are removed and then added to the end of the word, followed by ay. For example, computer becomes omputercay and think becomes inkthay.
#• If the word begins with a vowel (not including y), then way is added to the end of the word. For example, algorithm becomes algorithmway and office becomes officeway.
#Write a program that reads a line of text from the user. Then your program should translate the line into Pig Latin and display the result. Validate  - the string entered by the user only contains lowercase letters and spaces.

def pig_latin(text):
    print(text)
    vowels = ['a', 'e', 'i', 'o', 'u']
    if text[0] in vowels:
       text = text + "way" 
       return text 
    else:
       i=0
       while(i<(len(text)-2)):
          if(text[i] in vowels):
            break
          i+=1           # 0 to i-1
       text = text[i:] + text[:i] + "ay"
       return text

if __name__=="__main__":
     st = input("Enter the text")
     print(pig_latin(st))
    