# 10.10
with open("history_of_scientific_ideas.txt") as file_object:
    content = file_object.read()

approx_count = content.lower().count("the")
print(f"The word 'the' has been found {approx_count} times.")

count = content.lower().count("the ")
print(f"The word 'the ' has been found {count} times.")
