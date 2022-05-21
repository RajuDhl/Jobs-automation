import time

import pandas as pd

from static.others.states import states

csv_header = ["organization", "first_name", "last_name", 'headline', 'city', 'state', 'country', 'website',
              'linkedin_url', 'email_status']


def listify_companies(people, jobs):
    print("started to listify")
    companies_people = []
    companies_jobs = []
    for k, v in enumerate(people):
        if v and v not in companies_people:
            companies_people.append(v[0].lower())
    for k, v in enumerate(jobs):
        if v and v not in companies_jobs:
            companies_jobs.append(v[1].lower())
    index = {req_word: [idx for idx, word in enumerate(companies_people) if word == req_word] for req_word in
             set(companies_jobs)}
    return index


def filter_data(filepath, cwd):
    final_data = []
    processed = []
    processed_people = []
    path = f"{cwd}/data/static/processed/known_people.csv"
    people2 = f"{cwd}/data/static/processed/processed_people.csv"
    df = pd.read_csv(path, encoding='utf-8')
    df2 = pd.read_csv(people2, encoding='utf-8')
    df1 = pd.read_csv(filepath, encoding='utf-8')
    people = df.values.tolist()
    old_people = df2.values.tolist()
    for key, value in enumerate(old_people):
        processed_people.append(value)
    jobs = df1.values.tolist()
    people_list = listify_companies(people, jobs)
    for i, v in enumerate(jobs):
        data2 = []
        data3 = []
        temp = []
        if v[1].lower() in processed:
            pass
        else:
            company = v[1].lower()
            processed.append(company)
            try:
                raw_add = v[2].split(',')
            except:
                print("error in address ", i, v)
                time.sleep(5)
            city = raw_add[0]

            try:
                state = states[raw_add[1].strip(" ")]
                print("state is", state[raw_add[1].strip(" ")])
            except:
                state = ""
            # match = [x.lower() for x in v]
            try:
                d = people_list[company]
                for zz in d:
                    if people[zz][8] in processed_people:
                        pass
                    # print(state.lower(), two[zz][5].lower(), two[zz][4].lower())
                    # time.sleep(1)
                    else:
                        if state.lower() == people[zz][5].lower() and city.lower() == people[zz][4].lower():
                            print("Touched here")
                            data2.insert(0, people[zz])
                        elif state.lower() == people[zz][5].lower():
                            data2.insert(10, people[zz])
                        else:
                            data3.insert(10, people[zz])
            except:
                pass
            for row in data3:
                data2.append(row)
        data = data2[:4]
        if len(data) >= 1:
            for ind, row in enumerate(data):
                final_data.append(row)
                processed_people.append([row[8]])
    print(processed_people)
    df = pd.DataFrame(final_data)
    df2 = pd.DataFrame(processed_people)
    df = df.set_axis(csv_header, axis=1, inplace=False)
    print(df)
    df.to_csv("data/static/temp/state_separated.csv", index=False)
    df2.to_csv("data/static/processed/processed_people.csv", mode='a', encoding='utf-8',header=False, index=False)
    return "data/static/temp/state_separated.csv"

