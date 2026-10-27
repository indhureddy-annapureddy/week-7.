input_file = "input.txt"
output_file = "output.txt"

with open(input_file, "r") as file:
    words = file.read().split()

words_lower = [word.lower() for word in words]
words_lower.sort()

with open(output_file, "w") as file:
    file.write("\n".join(words_lower))

print("Sorted lowercase words written to output.txt")
