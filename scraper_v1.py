import requests
# from test1 import testConnect
from bs4 import BeautifulSoup

HEADERS = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding":"gzip, deflate, br",
    "Accpet-Language":"en-US,en;q=0.9",
    "Connection":"keep-alive",
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.32.119 Safari/537.36",
    "Cache-Control":"max-age=0, no-cache, no-store",
    "Upgrade-Insecure-Requests":"1"
}

# page = requests.get(f'https://www.yellowpages.com/oakland-ca/restaurants?page=1', headers=HEADERS)


businesses = []
ratings_list = []
years_open = []

num_pages = 100
for i in range(1,3):
    page = requests.get(f'https://www.yellowpages.com/oakland-ca/restaurants?page={i}', headers=HEADERS)
    pageContent = page.content
    soup = BeautifulSoup(page.content, 'html.parser')

    #Business Names
    business_name = soup.find_all('a', {'class':'business-name', 'href':True})
    for name in business_name:
        try: 
            businessNameText = name.find('span').text
            businesses.append(businessNameText)
            # print(businessNameText)
        except:
            businesses.append("No Name Found")
    
    # Restaurant Ratings
    ratings = soup.find_all('div', class_='ratings')
    # print(ratings)
    for item in ratings:
        try:
            tripadvisor = item['data-tripadvisor']
            ratings_list.append(tripadvisor)
            # print(tripadvisor)
        except:
            tripadvisor = None
            ratings_list.append("No Rating Found")
            # print("rating not available")

#     # Years In Business
    years_in_business = soup.find_all('div', class_='number')    
    for year in years_in_business:
        try:
            years_open_found = year.text
            years_open.append(years_open_found)
        except: 
            years_open.append("Years Open Unknown")
        # print(year.text)

print(len(businesses), len(ratings_list), len(years_open))