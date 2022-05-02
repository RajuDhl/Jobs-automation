from operator import itemgetter
import re

arg = re.compile(r'([\.0-9]+)$')


def findFloat(string):
    fl = arg.search(string)
    try:
        new = float(fl.group(1))
    except:
        old = str(fl.group(1))
        new = old[1:len(old)]
    return fl and float(new)


header = ['Position', 'Company Name', 'Location', 'Remote']


def text2csv(filepath, site, isloggedin):
    total = []
    newline = []
    f = open(filepath, 'r+', encoding='utf-8')
    lines = f.readlines()
    if site == 'linkedin':
        if isloggedin:
            for row in lines:
                row = row.strip('\n')
                if 'hide job' in row.lower():
                    pass
                else:
                    newline.append(row)
                    if 'logo' in row.lower():
                        total.append(newline)
                        newline = []
        else:
            for line in f:
                if line != '\n':
                    line = line.strip('\n')
                    newline.append(line)
                else:
                    total.append(newline)
                    newline = []
            total.pop(0)
            try:
                total.sort(key=itemgetter(1))
            except:
                pass

    elif site == 'dice':
        for i in range(0, len(lines)):
            line = lines[i].strip('\n')
            if "  " in line:
                y = line.split("  ")
                for z in y:
                    newline.append(z)
            else:
                newline.append(line)
            try:
                if 'logo' in lines[i + 3].lower():
                    total.append(newline)
                    newline = []
            except:
                pass

    elif site == 'indeed':
        for x in lines:
            if x != '\n':
                y = x.split()
                if 'new' in y:
                    pass
                else:
                    if x.isalpha():
                        pass
                    else:
                        try:
                            x = x.replace(str(findFloat(x)), "")
                        except:
                            pass
                    x = x.strip('\n')
                    newline.append(x)
            else:
                if len(newline) > 3:
                    total.append(newline)
                newline = []
        # print(len(total))

    elif site == 'glassdoor':
        print("data from glassdoor")


    total.pop(0)
    try:
        total.sort(key=itemgetter(1))
    except:
        print("not Sorted")

    return total
