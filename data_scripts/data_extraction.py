import sys
sys.path.append('../FROGTEK_TECHNICAL_ASSESSMENT')
import pandas as pd
import requests
from bs4 import BeautifulSoup


def soup(year):
    
    url = "https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page"
    
    print(f"Asking for http content from {url}")
    response = requests.get(url).text
    soup = BeautifulSoup(response, "html.parser")
    
    print(f"Filtering by year provided: {year}...")
    global year_html
    year_html = soup.find_all("div", id=f"faq{year}")[0] 
    print(f"html generated")



def single_month_links_df(year, month):
    
    months_available = [elem.get_text(strip=True) for elem in year_html.find_all(['b'])]
    
    print(f"Checking month requested {month} vs months available in the html content...")
    if month not in months_available:
        raise ValueError(f"month provided does not match with available months, check spelling {months_available}")
    
    print(f"Month provided is valid. Filtering by month...")
    filter_by_month = year_html.find(string=f"{month}").parent.findNext('ul')
    links = [elem.a['href'] for elem in filter_by_month.find_all('li')]
    description = [elem.a.text for elem in filter_by_month.find_all('li')]
    
    single_month_links = pd.DataFrame({'month': month, 'links': links, 'description': description})
    
    pd.set_option('display.max_colwidth', None)
    
    return single_month_links


def all_months_links_df(year, *month):
    
    links = pd.DataFrame()
    
    for elem in month:
        links = links.append(single_month_links_df(year, elem), ignore_index=True)
 
    print("Generating csv links table")
    
    return links