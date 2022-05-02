import os
import re

import pandas as pd

arg = re.compile(r'([\.0-9]+)$')


def findFloat(string):
    fl = arg.search(string)
    try:
        new = float(fl.group(1))
    except:
        old = str(fl.group(1))
        new = old[1:len(old)]
    return fl and float(new)


def text2csv(site):
    total = []
    newline = []
    di = os.getcwd()
    print(di)
    f = open('Indeed QA 13 Apr.txt', 'r+', encoding='utf-8')
    lines = f.readlines()
    if site == 'indeed':
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
        print(len(total))
        print("final data is", total)
        df = pd.DataFrame(total)
        df.to_csv('test.csv')


text2csv('indeed')
