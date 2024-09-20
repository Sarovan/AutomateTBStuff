message = (
    input("Enter the English message to translate into Pig Latin: ").rstrip(".").split()
)

translated_message = ""
vowels = ("a", "e", "i", "o", "u", "y")

for word in message:
    if word[0].isdecimal():
        translated_message += word + " "
        continue
    elif word[0] in vowels:
        word += "yay"
        translated_message += word + " "
    else:
        print(translated_message)
