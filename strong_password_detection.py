import re

password = "as7678asf!"


def assess_password(text):
    pw_check = re.compile(r"([a-zA-Z]*\d+[a-zA-Z]*)")
    if pw_check.search(text):
        return True


if assess_password(password):
    print("Strong!")
else:
    print("Weak!")
