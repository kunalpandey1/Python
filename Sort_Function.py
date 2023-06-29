# sort() method   = used with lists

# sort() function = used with iterables



# sort method but it only work with lists 

students = ["Squidward","Sandy","Patrick","Spongebob","Mr.Krabs"]


students.sort()
students.sort(reverse=True)

for i in students:

    print(i)  


    students = [("Squidward", "F", 60),

            ("Sandy", "A", 33),

            ("Patrick","D", 36),

            ("Spongebob","B", 20),

            ("Mr.Krabs","C", 78)]
    

    grade = lambda grades:grades[1] # sorting by grades

    students.sort(key=grade)     
# students.sort(key=grade,reverse=True)     

for i in students:

    print(i)  

#----------------------------------------------------------------

# sort function

students = (("Squidward", "F", 60),

            ("Sandy", "A", 33),

            ("Patrick","D", 36),

            ("Spongebob","B", 20),

            ("Mr.Krabs","C", 78))



grade = lambda grades:grades[1] # sorting by grades

# students.sort(key=age)                                       # sorts current list

sorted_students = sorted(students,key=grade) # sorts and creates a new list



for i in sorted_students:

    print(i)  