sentence = input("Enter a sentence: ").lower()
word = input("Word to search: ").lower()
print("Occurrences:", sentence.count(word))
print("Starts with word:", sentence.startswith(word))
