import re
pattern= re.compile("^[a-z]+[0-9]{1,2}@{1}[a-z]{5,7}\.{1}[a-z]{2,3}$")
print(pattern.search("sanginitripathi8@gmail.com"))
print(pattern.search("sanginitripathi13@gmail.com"))
print(pattern.search("kashyaptripathiii@gmail.com"))
