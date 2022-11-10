from bs4 import BeautifulSoup
import requests
import time

# with open('index.html', 'r') as html_file:
#     content = html_file.read
#     soup = BeautifulSoup(content, 'lxml')
#     tags = soup.find_all('h5')
print('Put the skills you want to search for.')
user_skills = input('>')
# user_skills_str = ' '.join([str(elem) for elem in user_skills])


def job_find():
    print(f'Looking for jobs with {user_skills}')
    html_txt = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_txt, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        publish_date = job.find('span', class_='sim-posted').span.text
        if '4' in publish_date:
            company_name = job.find(
                'h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = job.find(
                'span', class_='srp-skills').text.replace(' ', '')
            info = job.header.h2.a['href']
            if user_skills in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f"Company Name:{company_name.strip()}\n")
                    f.write(f"Requried Skills: {skills.strip()}\n")
                    f.write(f"More Info: {info}")
                print(f'File saved: {index}')

            # print(f'''
            #     Company Name: {company_name}
            #     Requried Skills: {skills}''')
            print('')


if __name__ == '__main__':
    while True:
        job_find()
        time_wait = 60
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait*60)
