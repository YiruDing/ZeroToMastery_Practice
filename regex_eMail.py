import re

check = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
# ^"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
# Q:Why can't I do "(^[\w.+-]+@[\w-]+?\.[\w-.)+$"
string = 'a@a.com'
a=check.search(string)
print(a)