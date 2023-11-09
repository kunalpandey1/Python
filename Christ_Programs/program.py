
import re
class Person:
    def __init__(self,name,email,contact):
        self.name=name
        self.email=email
        self.contact=contact
       
class Student(Person):
    def __init__(self,name,email,contact,regno,gpa):
        super().__init__(name,email,contact)
        self.regno=regno
        self.gpa=gpa
       
def selection_sort(records):
    n=len(records)
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if records[j].regno<records[min].regno:
                min=j
           
        records[i],records[min]=records[min],records[i]
   


def valid_email():
    email_pattern = r"^[a-z0-9.]+@bca\.in$"
    while True:
        email = input("Enter mail id : ")
        if re.match(email_pattern, email):
            return email
        else:
            print("Incorrect email : ")


def valid_contact():
    while True:
        contact = input("Enter phone number :")
        if len(contact) == 10 and contact.isdigit():
            return contact
        else:
            print("Please enter valid 10 digit number :")


def search_record(records):
    search = input("enter reg no  to search")
    for record in records:
        if re.search(search, record.name, re.IGNORECASE):
            print("Reg is : ", record.regno)
            print("Name is : ", record.name)
            print("Email is  :", record.email)
            print("Contact is :", record.contact)
            print("GPA is : ", record.gpa)


def display_data(records):
    for record in records:
        print("Reg is : ", record.regno)
        print("Name is : ", record.name)
        print("Email is  :", record.email)
        print("Contact is :", record.contact)
        print("GPA is : ", record.gpa)


def main():
    records = []
    no_of_record = int(input("Enter no of records :"))

    for i in range(no_of_record):
        regno = int(input("Enter registration number :"))
        name = input("Enter name :")
        email = valid_email()
        contact = valid_contact()
        gpa = float(input("Enter gpa :"))

        student = Student(name, email, contact, regno, gpa)
        records.append(student)

    selection_sort(records)
    display_data(records)
    search_record(records)


if __name__ == "__main__":
    main()