import requests
from bs4 import BeautifulSoup

def scrape_largest_companies_wikipedia(url):
    
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    
    table = soup.find('table', {'class': 'wikitable'})

   
    companies_data = []
    for row in table.find_all('tr')[1:]:  
        columns = row.find_all('td')
        rank = columns[0].text.strip()
        name = columns[1].text.strip()
        industry = columns[2].text.strip()
        revenue = columns[3].text.strip()
        revenue_growth = columns[4].text.strip()
        headquarters = columns[5].text.strip()

        company_info = {
            'Rank': rank,
            'Name': name,
            'Industry': industry,
            'Revenue': revenue,
            'Revenue Growth': revenue_growth,
            'Headquarters': headquarters
        }

        companies_data.append(company_info)

    return companies_data


url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
largest_companies_data = scrape_largest_companies_wikipedia(url)


for company in largest_companies_data:
    print(company)
