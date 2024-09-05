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

class Web3:

    def __init__(self, headers=headers):
        self.job_data = []
        self.web3_url = 'https://web3.career/YOURSEARCH-jobs'

        self.headers = headers

    def scrap_jobs(self, keyword):
        url = self.web3_url.replace('YOURSEARCH', keyword)
        # pagenation_limit value let you control how many pages you can get
        pagenation_limit = 10
        is_looping = True
        current=1
        
        # looping for scrapping jobs with pagination
        while is_looping:
            page_uri = f"?page={current}"
            print(f"Scrapping {url}{page_uri}...")
            response = requests.get(url+page_uri, headers=self.headers)
    
            # conditional for either the site is alive.
            if response.status_code != 200:
                print(f"Something Wrong!! \nStatus Code : {response.status_code}")
                sys.exit(1)
            else:
                print(f"Scrapping is done...")

            # conditional for pagination
            self.soup = BeautifulSoup(response.text, 'html.parser')
            try:            
                is_end = len(self.soup.find('li', class_='page-item next disabled'))
            except TypeError:
                is_end = False

            jobs = self.soup.find_all('tr', class_='table_row')
            for job in jobs:
                # conditional for passing Ads
                try:
                    title = job.find('div', class_='mb-auto align-middle job-title-mobile').text.strip()
                except AttributeError:
                    continue
                link = job.find('div', class_='mb-auto align-middle job-title-mobile').find('a')['href']
                company = job.find_all('td', class_='job-location-mobile')[0].text.strip()
                location = job.find_all('td', class_='job-location-mobile')[1].text.strip()
                salary = job.find('p', class_='ps-0 mb-0 text-salary').text.strip()

                self.job_data.append(
                    {
                        'title':title,
                        'company': company,
                        'location': location,
                        'salary': salary,
                        'link': 'https://web3.career' + link,
                    }
                )

            if is_end:
                is_looping = False
            else:
                if current < pagenation_limit:
                    current += 1
                else:
                    is_looping = False

    def show_jobs(self):
        if self.job_data:
            for job_info in self.job_data:
                print(job_info)
            print(len(self.job_data))
        else:
            print("no data..")


## the case for https://berlinstartupjobs.com/engineering/ and pagenation processing
# jobs = Web3()
# jobs.scrap_jobs('python')
# jobs.show_jobs()

## the case for keywords
# for keyword in test_keywords:
#     jobs = BerlinJobs()
#     jobs.scrap_jobs(keyword=keyword)
#     jobs.show_jobs()
