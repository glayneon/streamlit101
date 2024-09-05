from bs4 import BeautifulSoup
import requests
import sys

# variables
headers = {
    'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}

# for test
test_keywords = [
    'python',
    'java',
    'javascript',
]

class Wework:

    def __init__(self, headers=headers):
        self.job_data = []
        self.wework_url = 'https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term=YOURSEARCH'

        self.headers = headers

    def scrap_jobs(self, keyword):
        url = self.wework_url.replace('YOURSEARCH', keyword)
        
        # looping for scrapping jobs with pagination
        print(f"Scrapping {url}...")
        response = requests.get(url, headers=self.headers)

        # conditional for either the site is alive.
        if response.status_code != 200:
            print(f"Something Wrong!! \nStatus Code : {response.status_code}")
            sys.exit(1)
        else:
            print(f"Scrapping is done...")

        # conditional for pagination
        self.soup = BeautifulSoup(response.text, 'html.parser')

        jobs = self.soup.find_all('section', class_='jobs')
        for job in jobs:
            jj = job.find_all('li')
            for j in jj:
                try:
                    link = j.find_all('a')[1]['href']
                    company = j.find_all('a')[1].find('span', class_='company').text
                    title = j.find_all('a')[1].find('span', class_='title').text
                    location = j.find_all('a')[1].find('span', class_='region company').text
                    salary = 'no data'
                except:
                    continue
                
                self.job_data.append(
                    {
                        'title':title,
                        'company': company,
                        'location': location,
                        'salary': salary,
                        'link': 'https://weworkremotely.com' + link,
                    }
                )

    def show_jobs(self):
        if self.job_data:
            for job_info in self.job_data:
                print(job_info)
            print(len(self.job_data))
        else:
            print("no data..")


## the case for https://berlinstartupjobs.com/engineering/ and pagenation processing
# jobs = Wework()
# jobs.scrap_jobs('python')
# jobs.show_jobs()

## the case for keywords
# for keyword in test_keywords:
#     jobs = BerlinJobs()
#     jobs.scrap_jobs(keyword=keyword)
#     jobs.show_jobs()
