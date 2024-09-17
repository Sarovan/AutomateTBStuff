import pyperclip, re

phoneRegex = re.compile(
    r"""(
    (\d{3}|\(\d{3}\))+?              # area code
    (\s|-|\.)?                       # separator
    (\d{3})                         # first 3 digits
    (\s|-|\.)?                       # separator
    (\d{4})                         # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
                      )""",
    re.VERBOSE,
)

# Create email regex
emailRegex = re.compile(
    r"""(
    [a-zA-Z0-9._%+-]+               # username
    @                               # separator
    [a-zA-Z0-9-.]+                  # domain
    \.[a-zA-Z]{2,4}               # top level domain
                      )""",
    re.VERBOSE,
)


# Find matches in clipboard text
sitedata = str(pyperclip.paste())
matches = []
for phone in phoneRegex.findall(sitedata):
    phone_num = "-".join((phone[1], phone[3], phone[5]))
    matches.append(phone_num)
for email in emailRegex.findall(sitedata):
    matches.append(email)
print("Copied to clipboard:\n")
for match in matches:
    print(match)

# Copy results to clipboard
pyperclip.copy("\n".join(matches))
