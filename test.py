# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = r"(\b[^\s]+\b)|\(\d+:\d+\)"

test_str = "(190:50) hi so (4:2) I"

matches = [test_str[match.start():match.end()] for match in list(re.finditer(regex, test_str, re.MULTILINE))]
print(matches)
# print([test_str[match.start():match.end()] for match in list(matches)])


# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.
