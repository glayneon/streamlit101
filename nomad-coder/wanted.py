from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time
import csv
import sys

# variables
# HERE-PATTERN is the name you want to search on

class Wanted:

    def __init__(self, searching_delay=2, scroll_count=5):
        "Initialize data structure"
        # HERE-PATTERN can be the name you want to replace for searching on Wantted.co.kr
        self.wantted_url = 'https://www.wanted.co.kr'
        self.placeholder = 'HERE-KEYWORD'
        self.searching_pattern = f"/search?query={self.placeholder}&tab=position"
        self.searching_delay = searching_delay # time to sleep
        self.scroll_count = scroll_count
        self.job_data = []
        self.job_title = [
            "Title",
            "Company",
            "Reward",
            "Link",
        ]
    
    def job_searching(self, keyword):
        "Job searching using Playwright and BeautifulSoup4"

        if not isinstance(keyword, str):
            print(f"Keyword {keyword} is {type(keyword)}, it's wrong.")
            sys.exit(1)

        self.keyword = keyword

        p = sync_playwright().start()
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        self.searching_pattern = self.searching_pattern.replace(
            self.placeholder, keyword
            )
        page.goto(self.wantted_url + self.searching_pattern)
        time.sleep(self.searching_delay)

        for i in range(self.scroll_count):
            page.keyboard.down('End')
            time.sleep(self.searching_delay)

        # beautifulsoup4
        soup = BeautifulSoup(page.content(), 'html.parser')
        jobs = soup.find_all('div', class_='JobCard_container__REty8')

        for job in jobs:
            link = 'https://www.wanted.co.kr' + job.find('a')['href']
            title = job.find('a')['data-position-name']
            company = job.find('a')['data-company-name']
            reward = job.find('span', class_='JobCard_reward__cNlG5').text
            
            self.job_data.append([
                title,
                company,
                reward,
                link,
            ])
        
        print(f"job searching for {keyword} is done.")
        p.stop()
    
    def show_jobs(self):
        if not self.job_data:
            print("There's no data in Job Data. You need to search on somthing first!")
            sys.exit(1)
        
        for job in self.job_data:
            print(job)

    def tocsv(self):
        if not self.job_data:
            print("There's no data in Job Data. You need to search on somthing first!")
            sys.exit(1)
    
        filename = f"{self.keyword}.csv"
        f = open(filename, mode='w', encoding='utf-8')
        writter = csv.writer(f)

        # write headers to target csv file.
        writter.writerow(self.job_title)

        for job_row in self.job_data:
            writter.writerow(job_row)
        
        f.close()


w = Wanted()
w.job_searching('Python')
w.show_jobs()
w.tocsv()