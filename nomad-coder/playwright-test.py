from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time
import csv

p = sync_playwright().start()
browser = p.chromium.launch(headless=False)
page = browser.new_page()

page.goto('https://www.wanted.co.kr/jobsfeed')
time.sleep(3)

page.click("button.Aside_searchButton__rajGo") # Specifying tag class

time.sleep(3)

page.get_by_placeholder('검색어를 입력해 주세요.').fill("flutter")

time.sleep(1)

page.keyboard.down('Enter')

time.sleep(3)

page.click("a#search_tab_position")  # tag id with #(sharp)

time.sleep(3)

for i in range(5):
    page.keyboard.down('End')
    time.sleep(2)

# beautifulsoup

soup = BeautifulSoup(page.content(), 'html.parser')
jobs = soup.find_all('div', class_='JobCard_container__REty8')
# jobs = soup.find(
#     'div', 
#     class_='JobList_container__Hv_EA'
#     ).find_all('div', class_='JobCard_container__REty8')

job_data = []

for job in jobs:
    link = 'https://www.wanted.co.kr' + job.find('a')['href']
    title = job.find('a')['data-position-name']
    company = job.find('a')['data-company-name']
    reward = job.find('span', class_='JobCard_reward__cNlG5').text
    
    job_data.append([
        title,
        company,
        reward,
        link,
    ])

p.stop()

print(job_data)
print(len(job_data))


file = open('jobs.csv', mode='w', encoding='utf-8')
writter = csv.writer(file)

writter.writerow(['title', 'company', 'reward', 'link'])

for job_row in job_data:
    writter.writerow(job_row)

file.close()