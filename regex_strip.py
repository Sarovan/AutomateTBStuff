import re

text = input("Enter phrase: ")
removal = input("What to remove? ")


def regex_str(text, remove=""):
    if remove:
        remove_in = re.compile(remove)
        return remove_in.sub("", text)
    else:
        remove_pre = re.compile(r"^\s*")
        remove_post = re.compile(r"\s*$")
        return remove_pre.sub("", remove_post.sub("", text))


print(regex_str(text, removal))
