import string
def reverse(text):
    return text[::-1]


def is_palindrome(text):
    return text == reverse(text)

something = input("Enter text: ")
#translator = str.maketrans('','',string.punctuation)
#something = something.translate(translator)
#something = something.translate(None, string.punctuation)
for ch in string.punctuation:
    something = something.replace(ch, "'")

if is_palindrome(something):
    print("Yes, it is a palindrome")

else:
    print("No, not a palindrome")

