# 10.8
try:
    print("Cats names: ")
    with open("cats.txt") as file_object:
        print(file_object.read())

    print("Dogs names: ")
    with open("dogs.txt") as file_object:
        print(file_object.read())

except FileNotFoundError:
    print("The file could not be found.")
