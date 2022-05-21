import csv
import json
import time
from multiprocessing import Pool

import requests

from deps import headers, Enrich_csv, extract_list

url = "https://api.apollo.io/v1/mixed_people/search"
final_data = []


def initialize(companies_path):
    temp = []
    original = open(companies_path, 'r+', encoding='utf8')  # websites
    reader = csv.reader(original)
    for row in reader:
        temp.append(row)
    enriched = Enrich_csv(temp)
    domain = enriched['domain_text']
    return domain


def search(page, domain, titles):
    time.sleep(60)
    print("at page", page)
    payload = json.dumps({
        "api_key": "xQx9DESeSh_ZQb39lIUVwQ",
        "q_organization_domains": domain,
        # "q_organization_domains": 'www.accenture.com',
        "person_titles": titles,
        "page": page,
        "per_page": "200",
    })

    response = requests.request("POST", url, headers=headers, data=payload)
    data = response.json()
    people = data['people']
    contact = data['contacts']
    total_entries = data['pagination']
    for cont in range(0, len(data['contacts'])):
        people.append(contact[cont])
    print("Total No. of pages", total_entries['total_pages'], total_entries['total_entries'])
    return {'data': people}


def start_process(start_page, total_pages):

    def check_data(result):
        data = result['data']
        # print(len(data))
        for cont in range(0, len(data)):
            try:
                if data[cont]['country'] != 'United States' or data[cont]['email_status'] == 'unavailable':
                    pass
                else:
                    org = data[cont]['organization']
                    data[cont]['organization'] = org['name']
                    data[cont]['website'] = org['website_url']
                    final_data.append(data[cont])
            except:
                pass

    return {'final_data': final_data}
