import pyperclip

text = pyperclip.paste()
text = text.split("\n")
new_text = []

for line in text:
    new_text.append(f"* {line}")

text = "\n".join(new_text)
pyperclip.copy(text)
