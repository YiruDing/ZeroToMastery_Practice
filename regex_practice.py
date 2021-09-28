import re

pattern = re.compile(r"([a-zA-Z]).([a])")
# r means we wnat to check the raw/pure string
string = 'search this inside of this text please!'
a = pattern.search(string)
print(a.group(1))

# pattern = re.compile('this')
# a = pattern.search(string)
# b = pattern.findall(string)
# c = pattern.fullmatch(string)
# # c Must be fully matched.Otherwise will print 'None'
# d = pattern.match(string)
# # d Must match 0 or more characters at the begining of the string
# print('search' in string)
# # Result:True
# a = re.search('this',string)
# print(a.group())
# # Result:this
