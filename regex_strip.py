import re

text = "\n\nasdfasdf\n\n"


def regex_str(text, remove=""):
    remove_pre = re.compile("^\s*")
    remove_post = re.compile("\s*$")
    return remove_pre.sub("", remove_post.sub("", text))


print(regex_str(text))
