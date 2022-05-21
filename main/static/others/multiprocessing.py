
import timeit

import pandas as pd

from workers import *

start = timeit.default_timer()
csv_header = ["organization", "first_name", "last_name", 'headline', 'city', 'state', 'country', 'website',
              'linkedin_url', 'email_status']


# initialize start page and total page as `1` to check how many data are there
start_page = 1
total_pages = 15  # Max 200 per hour limit
save = True  # False when testing, True to save
# data = start_process(1)
# print(data)

if __name__ == '__main__':
    def test():
        print("Process started")
        data = start_process(start_page, total_pages)
        output = data['final_data']
        # print(output)
        if save:
            dir = "C:\\Users\\dell\\PycharmProjects\\Jobs-automation\\main\\data\\static\\processed\\known_people.csv"
            # os.chdir(dir)
            # with open("known_people2.csv", 'a', encoding='UTF8', newline='') as save:
            #     writer = csv.writer()
            #     writer.writerows(output)
            df = pd.DataFrame(data['final_data'])
            df = df[csv_header]
            df.drop_duplicates(subset='linkedin_url', keep="first", inplace=True)
            df.to_csv(dir, mode='a', encoding='utf-8', index=False, header=False)
            print("Total new saves", len(df))


    test()
