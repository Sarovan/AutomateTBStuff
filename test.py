import re

phoneNumRegex = re.compile(r"First Name: (.*) Last Name: (.*)")
mo = phoneNumRegex.search("First Name: Al Last Name: Sweigart")
if mo:
    print(mo.group())
