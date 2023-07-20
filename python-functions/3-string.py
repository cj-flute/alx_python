#!/urs/bin/python3
def reverse_string(string):
    return string[::-1]

name = "chijioke"
reverse_string(name)

# def reverse_string(string):
#     word = []
#     for i in range(len(string)):
#         word.append(string[(len(string) - i) - 1])
#     reversed_string = ''.join(word)
#     return reversed_string
