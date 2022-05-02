import csv

import pandas as pd


def combine_data(filename, cwd):
    df = pd.read_csv(filename['jobsFile'], encoding='utf8')
    df1 = pd.read_csv(filename['emailFile'], encoding='utf8')
    # print(df.values.tolist())
    jobs = df.values.tolist()
    people = df1.values.tolist()
    final = []
    processed = []
    final_data = []
    for i, v in enumerate(jobs):
        start = True
        if v[1].lower() not in processed:
            processed.append(v[1].lower())
            for index, data in enumerate(people):
                # print(v[3], data[7])
                try:
                    if v[3].lower() == data[7].lower():
                        if start:
                            for z in range(1, 4):
                                final.append(" ")
                                start = False
                        final.append(v + data)
                except:
                    print("Error in", v[3], data[7])
    with open('data/static/temp/final.csv', 'w', encoding='UTF8', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(final)
    # df = pd.DataFrame(final_data)
    # print(df)
    # df.to_csv("data/static/temp/final.csv", index=False)
    return "data/static/temp/final.csv"

