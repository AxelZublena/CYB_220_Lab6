# 10.2
file_path = 'learning_python.txt'

with open(file_path) as file_object:
    content = file_object.read()

print("Original content: ")
print(content)

print("Modified content: ")
with open(file_path) as file_object:
    for line in file_object:
        print(line.replace("Python", "C").rstrip())


