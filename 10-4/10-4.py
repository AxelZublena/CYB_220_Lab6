# 10.4
while True:
    name = input("What is your name?: ")

    if name == "q":
        break

    with open("guest_book.txt", "a") as file_object:
        file_object.write(name + "\n")
