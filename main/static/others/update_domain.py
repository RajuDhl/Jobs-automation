import csv
import pandas as pd


header = ['Company', 'Website', 'Company Linkedin Url']


def update_domain(filepath, cwd):
    df = pd.read_csv(filepath)
    # print(df)
    original = f"{cwd}/data/static/processed/known_companies.csv"
    df1 = pd.read_csv(original, encoding='utf-8')
    # print(df1)
    merged = pd.merge(df, df1, how='outer')
    merged = merged.set_axis(header, axis=1, inplace=False)
    merged.to_csv(original, encoding='utf-8', index=False)
    print("Companies Updated")
    return True

