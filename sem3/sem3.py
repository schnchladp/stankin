import re

file= open("sem3.txt",encoding='utf-8')

ErrorWarnPatt=r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} (ERROR|WARN)\s'

octet = r'(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])'
IpPatt = rf'\b({octet}\.){{3}}{octet}\b'

levels, ips =[], []

for s in file:
    if re.search(ErrorWarnPatt, s):
        levels.append(s)
    if re.search(IpPatt, s):
        ips.append(s)
file.close()

for line in levels:
    print(line.rstrip())
print()
for line in ips:
    print(line.rstrip())
