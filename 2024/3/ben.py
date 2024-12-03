import re

f = open("input.txt", "r")
# f = open("data/3", "r")
data = f.read()
# print(data)
f.close()

def mul(mulString):
    first = re.search(r"\(\d+", mulString).group()[1:]
    second = re.search(r",\d+", mulString).group()[1:]
    # if len(first) > 3 or len(second) > 3:
    #     return 0
    return int(first) * int(second)

res = re.findall(r"mul\(\d+,\d+\)", data)
total = 0

for captured in res:
    total += mul(captured)

print(total)

# f = open("example-data/3-part2", "r")
f = open("input.txt", "r")
data = f"do()${f.read()}don\'t()"
# print(data)
f.close()

res = re.findall(r"do\(\)(.*?)don't\(\)", data)
# print(res)
total = 0
for captured in res:
    res2 = re.findall(r"mul\(\d+,\d+\)", captured)
    for captured2 in res2:
        # print(captured2)
        total += mul(captured2)
    # if re.search(r"don't", captured) is not None:
    #     pass
        # print(captured)

# 65373890 too low
print(total)