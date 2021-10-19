import re 

pattern = re.compile(r"(^[a-zA-Z0-9$%#@]{7,}[0-9])")
# [0-9] could be \d 
# End with num? Just use "\d$"
password = '32frd34refg1'
check= pattern.fullmatch(password)
print(check)