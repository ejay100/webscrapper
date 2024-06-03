#from asyncio import main
from bs4 import BeautifulSoup
import requests
import time
import asyncio

print('Put some skills that your are not familiar with')
unfamiliar_skill = input('Unfamiliar skill>')
print(f'Filtering out {unfamiliar_skill}')
print('')

def find_jobs():
    #print(html_text.content)
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=&txtKeywords=python&txtLocation=')
    soup = BeautifulSoup(html_text.content, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted')
        if 'few' in published_date.span.text:
            #print(published_date.span.text)#print(published_date.)
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ','')
            skills = job.find('span', class_ ='srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open('posts/{index}.txt', 'w') as f:
                    f.write(f"Company Name: {company_name.strip()} \n")
                    f.write(f"Required Skill: {skills.strip()} \n")
                    f.write(f"More Information: {more_info.strip()} \n")
                print('File saved successfully: {index}')



if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)


