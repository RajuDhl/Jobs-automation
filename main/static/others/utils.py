import csv
import time

import pandas as pd
from werkzeug.utils import secure_filename
import datetime as dt


def save_file(request):
    items = {}
    f = request.files
    print("incoming files", f)
    for filename, file in request.files.items():
        z = f.get(filename)
        file_name = secure_filename(z.filename)
        path = f"data/static/temp/{file_name}"
        z.save(path)
        items[filename] = path
    print(items)
    if len(items) == 1:
        return path
    else:
        return items


def Dataframe(data, cwd):
    date = dt.datetime.now()
    timestamp = date.timestamp()
    df1 = pd.read_csv(f"{cwd}/data/static/processed/processed_jobs.csv")
    csv_header = ['Position', 'Company Name', 'Location', 'Remote']
    df = pd.DataFrame(data)
    df = df.iloc[:, [0, 1, 2, 3]]
    df = df.set_axis(csv_header, axis=1, inplace=False)
    df.drop_duplicates(keep='first')
    temp = df1.iloc[:, [0, 1, 2, 3]]
    # final = df.merge(temp, indicator=True, how='outer').query('_merge=="left_only"').drop('_merge', axis=1)
    final = df
    final['timestamp'] = timestamp
    processed = pd.concat([df1, final], ignore_index=True)
    final.to_csv("data/static/temp/text2csv5.csv", index=False)
    # print("Final is", final)
    # processed.to_csv(f"{cwd}/data/static/processed/processed_jobs.csv", index=False)
    return final


def enrich_domains(file, cwd):
    print("file type is", cwd, type(file))
    if type(file) != list:
        try:
            head = ['Position', 'Company Name', 'Location', 'website']
            file = pd.read_csv(f"{cwd}/{file}")
            file = file.set_axis(head, axis=1, inplace=False)
        except:
            pass
    file = file[['Position', 'Company Name', 'Location']]
    # print(file)
    csv_header = ['Position', 'Company Name', 'Location', 'website']
    companies_df = pd.read_csv(f"{cwd}/data/static/processed/known_companies.csv", encoding="ISO-8859-1",
                               engine='python')
    companies_data_list = companies_df.values.tolist()
    jobs_data_list = file.values.tolist()
    # print(jobs_data_list)
    companies = [x.lower() for x in list(companies_df['Company'])]
    jobs = [x.lower() for x in list(file['Company Name'])]
    processed = []
    new_list = []
    i = 1
    for i, v in enumerate(jobs):
        if v not in processed:
        # if v:
            enrich = True
            processed.append(v)
            for i2, v2 in enumerate(companies):
                if v == v2:
                    new_list.append(jobs_data_list[i] + [companies_data_list[i2][1]])
                    enrich = False
            if enrich:
                new_list.append(jobs_data_list[i])
        else:
            print("In processed", i)
            i += 1
    # print(new_list)
    df = pd.DataFrame(new_list)
    # print(df)
    df = df.set_axis(csv_header, axis=1, inplace=False)
    print(len(df))
    df.drop_duplicates(subset=['Company Name'], keep='first')
    print(len(df))
    df.to_csv("data/static/temp/text2csv.csv", index=False)
    return "data/static/temp/text2csv.csv"
