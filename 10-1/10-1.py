# 10.1
file_path = 'learning_python.txt'

print("\nRead entire file.")
with open(file_path) as file_object:
    print(file_object.read())

print("\nLoop over the file object.")
with open(file_path) as file_object:
    for line in file_object:
        print(line)

print("\nStore lines in list and using loop to display them.")
with open(file_path) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line)

