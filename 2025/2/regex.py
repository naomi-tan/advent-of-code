import re

pattern = r'^(\d+)\1+$'
my_str = '123123123'
result = re.search(pattern, my_str)
print(result.group(), result.span())