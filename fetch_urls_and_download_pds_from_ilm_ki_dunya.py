import requests
from bs4 import BeautifulSoup

from time import sleep 
from os import mkdir, path


# Function to fetch and parse the table
def extract_links_from_table(url):
    # Fetch the webpage content
    response = requests.get(url)
    
    # Parse the webpage using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Locate the div containing the table
    subject_wrapper = soup.find('div', class_='subject-wrapper')
    
    # Find the table inside the subject-wrapper
    table = subject_wrapper.find('table')
    
    # Extract all the links from the table
    links = []
    for row in table.find_all('tr')[1:]:  # Skip the header row
        link_tag = row.find('a')  # Find <a> tags
        if link_tag and link_tag.has_attr('href'):
            links.append(link_tag['href'])  # Add the href attribute (link) to the list
    
    return links 


def get_name(url):
    return url.split("/")[-1]


def get_folder_input():
    _folder = input("Enter your subject folder name: ")
    return _folder.strip()



print("Program Started! \n")

webpage_url = input("Enter your url from ilm-ki-dunya : ").strip()

pdf_urls = extract_links_from_table(webpage_url)

folder_name = get_folder_input()

print(f"{mkdir(folder_name) = }")

print(f"Interating over urls...\n")

for url in pdf_urls:
    name = get_name(url)
    with open(path.join(folder_name, name), 'wb') as file:
        print(f"Start downloading: {name}")
        response = requests.get(url)
        file.write(response.content)
        sleep(1)
        print(f"Finished downloading: {name} \n")

print("Alls Downloads are completed!")

print('''
>> Saadullah Khan. 
|- Linkedin: https://www.linkedin.com/in/saadullahkhan3/
|- GitHub(Profile): https://www.github.com/saadullahkhan3/
|-Project GitHub link: https://github.com/Saadullahkhan3/Shared-Snippets/blob/main/fetch_urls_and_download_pds_from_ilm_ki_dunya.py
>> END :)
''')
