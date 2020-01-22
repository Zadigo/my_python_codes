import csv
import re

import requests
from bs4 import BeautifulSoup

import random


class EmailsExtractor:
    """This class sends a requests to the internet in order
    to extract the email addresses present on the website

    Parameters
    ----------

        url: is the url of the web page to parse
    """ 
    def __init__(self, url):
        response = requests.get(url)
        self.soup = BeautifulSoup(response.text, 'html.parser')
        self.document_body = self.soup.find('body')

    def regex_emails(self):
        """Returns a list of regexed emails"""
        links = self.soup.find_all('a')
        clean_links = self._check_links(links, only_href=True)
        return self.extract_emails(clean_links)

    def emails(self):
        """Returns a list of tuples resulting from
        the regexed links

        Result
        ------

            [(name.surname@gmail.com, name.surname, gmail.com)]
        """
        regexes = self.regex_emails()
        for regex in regexes:
            yield regex.groups()

    def emails_to_file(self, path_or_name):
        """Writes the collected emails to a csv file"""
        with open(path_or_name, 'w', newline='', encoding='utf-8') as f:
            fieldnames = ['name', 'email']
            csv_file = csv.DictWriter(f, fieldnames=fieldnames)
            csv_file.writeheader()
            for email in self.emails():
                csv_file.writerow({'name': email[1], 'email': email[0]})
        return True

    @staticmethod
    def extract_emails(values:list):
        """Gets the specific email portion of the string"""
        return [re.match(r'^(?:mailto\:)((.*)\@(.*))$', value) for value in values]

    @staticmethod
    def _check_links(links, only_href=False):
        """Checks the links and takes out those that
        starts with #, /, javascript and http in order 
        to keep the ones starting with mailto
        """
        clean_links = []
        for link in links:
            try:
                href = link['href']
            except:
                href = None

            if href:
                has_any_of_these_elements = any([href.startswith('#'), href.startswith('/'), \
                        href.startswith('http'), href.startswith('javascript')])
                if not has_any_of_these_elements:
                    clean_links.append(link['href'] if only_href else link)
        return clean_links

class ConstructFromExtraction(EmailsExtractor):
    """Construct a set of emails based on a single sample
    extract from a list of email extractions

    Parameters
    ----------

        file_path: the .txt file to use containing names to
        construct emails from
    """
    def __init__(self, file_path, new_file_name, url):
        super().__init__(url)

        # (name.surname@domain, name.surname, domain)
        sample_email = random.sample(self.emails(), 1)

        if len(sample_email) == 3:
            self.domain = sample_email[-1]
            self.separator = self.identify_separator(sample_email[1])

        with open(file_path, 'r', encoding='utf-8') as f:
            with open(new_file_name, 'w', encoding='utf-8') as n:
                csv_file = csv.writer(n)
                names = f.readlines()
                for name in names:
                    normalized_name = self.normalize_name(name)
                    splitted_names = normalized_name.split(' ')

                    if self.separator:
                        new_email = f'{self.separator}'.join(splitted_names)
                    else:
                        new_email = f''.join(splitted_names)
                    # [name, surname], [name.surname@domain] ->
                    # [name, surname, name.surname@domain]
                    csv_file.writerow(zip(splitted_names, [new_email]))

    @staticmethod
    def normalize_name(name):
        return name.lower().strip()

    @staticmethod
    def identify_separator(value):
        is_match = re.match(r'(\.|\_|-)', value)
        return is_match.group(0) if is_match else False



e = EmailsExtractor('https://facdedroit.univ-amu.fr/scolarite-formation/contacts/site-aix-en-provence')
print(e.emails_to_file('emails.csv'))
