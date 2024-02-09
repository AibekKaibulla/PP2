def reverse_sentence(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

user_input = input("Enter a sentence: ")

result = reverse_sentence(user_input)
print(result)
