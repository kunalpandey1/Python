class PyramidPattern:
    def __init__(self, height):
        self.height = height

    def print_pattern(self):
        for i in range(self.height):
            print(" " * (self.height - i - 1) + "* " * (i + 1))
        for i in range(self.height - 2, -1, -1):
            print(" " * (self.height - i - 1) + "* " * (i + 1))


class WordPattern:
    def __init__(self, word):
        self.word = word

    def print_pattern(self):
        word_length = len(self.word)
        height = word_length + 2

        for i in range(height):
            if i == height // 2:
                print("*  *  * {} *  *  *".format(self.word))
            else:
                print(" " * (height - i - 1) + "* " * (i + 1))


class NumberPattern:
    def __init__(self, height):
        self.height = height

    def print_pattern(self):
        num = 1
        for i in range(self.height // 2):
            print(" " * (self.height - i - 1) + "".join(str(x) for x in range(num, num + 2 * i + 1)))
            num += 2
        for i in range(self.height // 2, -1, -1):
            print(" " * (self.height - i - 1) + "".join(str(x) for x in range(num, num + 2 * i + 1)))
            num += 2


while True:
    print("Select a pattern:")
    print("1. Pyramid Pattern")
    print("2. Word Pattern")
    print("3. Number Pattern")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        height = int(input("Enter height for the pyramid pattern: "))
        pattern1 = PyramidPattern(height)
        pattern1.print_pattern()
    elif choice == '2':
        word = input("Enter a word (five characters) for the pattern: ")
        if len(word) == 5:
            pattern2 = WordPattern(word)
            pattern2.print_pattern()
        else:
            print("Please enter a word with exactly five characters.")
    elif choice == '3':
        height = int(input("Enter height for the number pattern: "))
        pattern3 = NumberPattern(height)
        pattern3.print_pattern()
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
