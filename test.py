import pyinputplus as pyip

number = pyip.inputNum(allowRegexes=[r"(I|V|X|L|C|D|M)+", r"zero"])
print(number)
