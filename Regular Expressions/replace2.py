import re

str1 = "I am From Rajkot"

res = re.sub(r"[a-z]","0",str1)

print(res)

# output  :   I 00 F000 R00000