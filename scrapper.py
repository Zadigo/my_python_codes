import requests
from bs4 import BeautifulSoup
import json

class Job(dict):
    def __init__(self, text):
        self.update(
            {
                'text': text
            }
        )

    def write_job(self):
        with open('D:\\Programs\\Repositories\\my_python_codes\\test.json', 'w') as f:
            json.dump(self, f)

class Base:
    def create_request(self, url):
        response = requests.get(url)
        return BeautifulSoup(response.text, 'html.parser')        

class ParisJobs(Base):
    def get_job(self, url):
        soup = super().create_request(url)
        job_text = soup.find('div', id='annonce-detail').text.strip()

        job = Job(job_text)
        job.write_job()

ParisJobs().get_job('https://www.parisjob.com/emplois/stagiaire-attache-commercial-h-f-2625341.html')