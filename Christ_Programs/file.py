# Step 1: Create a File (Use W, W+ mode)
file_name = "example.txt"
with open(file_name, "w") as file:
    pass

# Step 2: Write 5 sentences in the file.
with open(file_name, "w") as file:
    file.write("This is the first sentence.\n")
    file.write("Here comes the second sentence.\n")
    file.write("The third sentence is next.\n")
    file.write("This is the fourth sentence.\n")
    file.write("And finally, the fifth sentence.\n")

# Step 3: Display only two lines
with open(file_name, "r") as file:
    for _ in range(2):
        print(file.readline().strip())

# Step 4: Append 5 more lines
with open(file_name, "a") as file:
    file.write("Appending the sixth sentence.\n")
    file.write("Adding the seventh sentence.\n")
    file.write("This is the eighth sentence.\n")
    file.write("The ninth sentence is here.\n")
    file.write("Tenth and final sentence.\n")

# Step 5: Display everything
with open(file_name, "r") as file:
    print(file.read())

# Step 6: Open the same file and write the new content (Existing content should not be there)
with open(file_name, "w") as file:
    file.write("This is new content in the file.\n")

# Step 7: Read the same file in binary mode and text mode
# Binary Mode
with open(file_name, "rb") as file:
    binary_content = file.read()
    print("Binary Content:")
    print(binary_content)

# Text Mode
with open(file_name, "r") as file:
    text_content = file.read()
    print("Text Content:")
    print(text_content)

# Step 8: How to read a CSV file using pandas in Python
import pandas as pd

csv_file_name = "example.csv"
# Assuming you have a CSV file named "example.csv" with data
df = pd.read_csv(csv_file_name)
print(df)
