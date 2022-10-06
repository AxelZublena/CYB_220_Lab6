# 10.5
while True:
    reason = input("Why do you like programming?: ")

    if reason == "q":
        break

    with open("reasons.txt", "a") as file_object:
        file_object.write(reason + "\n")

    print(f"'{reason}' has been appended to reasons.txt.")
