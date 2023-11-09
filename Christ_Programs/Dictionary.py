def create_student_record():
    name = input("Enter student's name: ")
    roll_number = int(input("Enter student's roll number: "))
    marks = int(input("Enter student's marks: "))
    return {"name": name, "roll_number": roll_number, "marks": marks}

def calculate_average(marks_dict):
    total_marks = sum(marks_dict.values())
    average_marks = total_marks / len(marks_dict)
    return average_marks

def count_vowels(input_string):
    vowels = "aeiou"
    vowel_count = {vowel: input_string.count(vowel) for vowel in vowels}
    return vowel_count

def create_dict(keys, values):
    return dict(zip(keys, values))

def find_duplicates(input_list):
    duplicate_count = {item: input_list.count(item) for item in set(input_list)}
    return duplicate_count

def remove_duplicates(input_list):
    return list(set(input_list))

def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

# Test the functions
student_record = create_student_record()
print("Student Record:", student_record)

marks = {"John": 85, "Alice": 92, "Bob": 78, "Emma": 95, "Tom": 88}
average_marks = calculate_average(marks)
print("Average Marks:", average_marks)

input_string = input("Enter a string: ")
vowel_count = count_vowels(input_string)
print("Vowel Count:", vowel_count)

keys = ["name", "age", "gender"]
values = ["John", 25, "Male"]
result_dict = create_dict(keys, values)
print("Resulting Dictionary:", result_dict)

input_list = [1, 2, 3, 4, 2, 3, 5]
duplicate_count = find_duplicates(input_list)
print("Duplicate Count:", duplicate_count)

unique_list = remove_duplicates(input_list)
print("List with Duplicates Removed:", unique_list)

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 20, "d": 40}
merged_dict = merge_dictionaries(dict1, dict2)
print("Merged Dictionary:", merged_dict)
