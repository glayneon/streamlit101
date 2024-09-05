# class implementation
from bs4 import BeautifulSoup
import requests as reqs
import sys
# import tocsv as csv

# variables
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}

example_keywords = [
    'flutter',
    'devops',
]


class RemoteOK:

    def __init__(self, header=headers):
        self.job_data = []
        # Specifying HERE-PATTERN on URL
        self.remoteok = 'https://remoteok.com/remote-HERE-PATTERN-jobs'
        self.header = header

    def scrap_page_wt(self, keyword):
        if not isinstance(keyword, str):
            print(f"Keyword {keyword} is not a type of STR.")
            sys.exit(0)

        url = self.remoteok.replace('HERE-PATTERN', keyword)

        print(f"Searching jobs - {keyword} on remoteok.com ...")
        response = reqs.get(url, headers = self.header)

        if not response.status_code == 200:
            print(f"Error - {response.status_code}")
            sys.exit(0)

        soup = BeautifulSoup(response.text, 'html.parser')

        # remove ads with [1:]
        jobs = soup.find('table', id='jobsboard'
                        ).find_all('td', class_='company position company_and_position')[1:]

        for job in jobs:
            link = 'https://remoteok.com' + job.find('a')['href']
            title = job.find('h2').text.strip('\n')
            company = job.find('h3').text.strip()
            location = job.find('div', class_='location').text.strip()

            try:
                salary = job.find('div', class_='location tooltip').text.strip()
            except AttributeError:
                salary = 'no data'

            self.job_data.append(
                {
                    'title':title,
                    'company': company,
                    'location': location,
                    'salary': salary,
                    'link': link,
                 }
            )
        
        # filename = csv.save_to_csv(keyword, self.job_data)
        # print(f"All results are stored as {filename}...")

    def show_jobs(self):
        if self.job_data:
            for job in self.job_data:
                print(job.values())
        else:
            print("No jobs found.")


# main
# jobsearching = RemoteOK()

# for keyword in example_keywords:
#     jobsearching.scrap_page_wt(keyword)

# jobsearching.show_jobs()

