import csv
from operator import itemgetter


header = ['Position', 'Company Name', 'Location', 'Remote']

f = open("QA automatic and manual Raw data.txt", 'r')
total = []
newline = []
for line in f:
    line = line.strip('\n')
    # print(line.strip('\n'))
    if 'hide job' in line.lower():
        pass
    else:
        newline.append(line)
        if 'logo' in line.lower():
            total.append(newline)
            newline = []

print("total", total)
total.pop(0)
total.sort(key=itemgetter(1))
print("new total", total)
# print("data", data)
with open("Final.csv", "w", encoding='UTF8', newline='') as r:
    writer = csv.writer(r)
    writer.writerow(header)
    writer.writerows(total)



