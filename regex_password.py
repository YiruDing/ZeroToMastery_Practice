import re 

check = re.compile(r"(^[a-zA-Z0-9$%#@]{8,})")

string = '32frd34refg'
a=check.search(string)
print(a)