import re

password = "as767Aaa"


def assess_password(text):
    check_upper = re.compile(r"[A-Z]")
    check_lower = re.compile(r"[a-z]")
    check_digit = re.compile(r"\d")
    if (
        len(text) > 7
        and check_upper.search(text)
        and check_lower.search(text)
        and check_digit.search(text)
    ):
        return True
    return False


if assess_password(password):
    print("Strong!")
else:
    print("Weak!")
