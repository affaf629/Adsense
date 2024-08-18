import os
import re
from bs4 import BeautifulSoup


def extract_url(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    main_entity_tag = soup.find(string=re.compile('mainEntityOfPage|pageUrl'))
    if main_entity_tag:
        url = re.search(r'(mainEntityOfPage|pageUrl).*?"(https?://.*?)"', main_entity_tag)
        if url:
            main_url = url.group(2)
            return main_url
    return None

html_directory = '/Users/User/OneDrive/Desktop/link'


with open('urls.txt', 'w') as url_file:
    for filename in os.listdir(html_directory):
        if filename.endswith('.html'):
            file_path = os.path.join(html_directory, filename)
            with open(file_path, 'r') as file:
                html = file.read()
                url = extract_url(html)
                url_file.write(f'{filename}: {url}\n')




 





