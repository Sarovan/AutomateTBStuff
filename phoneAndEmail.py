import pyperclip, re

phoneRegex = re.compile(
    r"""
    (\d{3}|\(\d{3}\))?              # area code
    (\s|-|.)?                       # separator
    (\d{3})                         # first 3 digits
    (\s|-|.)?                       # separator
    (\d{4})                         # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
                      """,
    re.VERBOSE,
)

# TODO: Create email regex
emailRegex = re.compile(
    r"""
    ([a-zA-z0-9_.-]+)               # username
    (@)                             # separator
    ([a-zA-z0-9-]+)                 # domain beginning
    (.com|.edu|.org)$               # domain ending
                      """,
    re.VERBOSE,
)

print(emailRegex.search("asdfasd akazmi001@gmail.com asdfasd"))

# TODO: Find matches in clipboard text

# TODO: Copy results to clipboard
