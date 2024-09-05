from bs4 import BeautifulSoup
import requests

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


class BerlinJobs:

    def __init__(self, headers=headers):
        self.pages = 0
        self.job_data = []
        self.berlin_jobs = {
            'it': 'https://berlinstartupjobs.com/engineering/',
            'specific': 'https://berlinstartupjobs.com/skill-areas/XXXXXX/',
        }

        self.headers = headers

    def scrap_jobs(self, keyword='it'):
        if keyword == 'it':
            url = self.berlin_jobs['it']
        else:
            url = self.berlin_jobs['specific'].replace('XXXXXX', keyword)

        print(f"Scrapping {url}...")
        response = requests.get(url, headers=self.headers)

        # conditional for either the site is alive.
        if response.status_code != 200:
            print(f"Something Wrong!! \nStatus Code : {response.status_code}")
            sys.exit(1)
        else:
            print(f"Scrapping is done...")

        # conditional for pages
        self.soup = BeautifulSoup(response.text, 'html.parser')
        pages = len(self.soup.find_all(class_='page-numbers'))
        current = 1

        while True:
            # parsing the current page
            jobs = self.soup.find_all('div', class_='bjs-jlid__wrapper')
            for job in jobs:
                link = job.find('h4', class_='bjs-jlid__h').find('a')['href']
                title = job.find('h4', class_='bjs-jlid__h').text
                company = job.find('a', class_='bjs-jlid__b').text
                salary = 'no data'
                location = "no data"

                self.job_data.append(
                    {
                        'title':title,
                        'company': company,
                        'location': location,
                        'salary': salary,
                        'link': link,
                    }
                )
            # conditional for pagenation
            current += 1
            if pages != 0 and current != pages:
                url_page = url + f"page/{str(current)}"
                print(f"Scrapping {url_page}...")
                response = requests.get(url_page, headers=self.headers)
                self.soup = BeautifulSoup(response.text, 'html.parser')
            else:
                break

    def show_jobs(self):
        if self.job_data:
            for job_info in self.job_data:
                print(job_info)
        else:
            print("no data..")


## the case for https://berlinstartupjobs.com/engineering/ and pagenation processing
# jobs = BerlinJobs()
# jobs.scrap_jobs('python')
# jobs.show_jobs()
# print(len(jobs.job_data))
# ## the case for keywords
# for keyword in test_keywords:
#     jobs = BerlinJobs()
#     jobs.scrap_jobs(keyword=keyword)
#     jobs.show_jobs()
