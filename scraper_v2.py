import csv
import requests
from bs4 import BeautifulSoup
from itertools import zip_longest

# Your HEADERS and URL
HEADERS = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding":"gzip, deflate, br",
    "Accpet-Language":"en-US,en;q=0.9",
    "Connection":"keep-alive",
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.32.119 Safari/537.36",
    "Cache-Control":"max-age=0, no-cache, no-store",
    "Upgrade-Insecure-Requests":"1"
}

businesses = []
categories_list = []
ratings_list = []
num_ratings_list = []
years_open = []
phone_number_list = []
street_address_list = []
locality_list = []
full_addy_list = []
price_list = []

num_pages = 100

for i in range(1, 3):
    page = requests.get(f'https://www.yellowpages.com/oakland-ca/restaurants?page={i}', headers=HEADERS)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Business Names
    business_name = soup.find_all('a', class_='business-name')
    businesses.extend([name.text if name.text else 'No Name Found' for name in business_name])

    # Business Categories
    business_categories = soup.find_all('div', class_='categories')
    for category in business_categories:
        try:
            category_links = category.find_all('a')
            category_list = [link.text for link in category_links]
            categories_list.append(category_list)
        except:
            categories_list.append(['Category Unknown'])

    # Restaurant Ratings
    rating = soup.find_all('div', class_='ratings')
    ratings_list.extend([item['data-tripadvisor'] if 'data-tripadvisor' in item.attrs else str({"rating":"","count":""}) for item in rating])
    
    # Years In Business
    years_in_business = soup.find_all('div', class_='number')
    years_open.extend([year.text if year.text else 'Years Open Unknown' for year in years_in_business])

    # Phone Number
    phone_number = soup.find_all('div', class_='phones phone primary')
    phone_number_list.extend([number.text if number.text else 'Phone Number Unknown' for number in phone_number])

    # Street Address
    street_address = soup.find_all('div', class_='street-address')
    street_address_list.extend([address.text if address.text else 'Address Unknown' for address in street_address])

    # Locality
    locality = soup.find_all('div', class_='locality')
    locality_list.extend([city.text if city.text else 'City Unknown' for city in locality])

    # Full Address
    full_addy = soup.find_all('p', class_='adr')
    full_addy_list.extend([addy.text if addy.text else 'City Unknown' for addy in full_addy])

    # Price
    price = soup.find_all('div', class_='price-range')
    price_list.extend([amount.text if amount.text else 'Price Unknown' for amount in price])

# Make sure all lists have the same length
max_length = max(len(businesses), len(ratings_list), len(years_open))
businesses = list(zip_longest(businesses, range(max_length), fillvalue=None))
ratings_list = list(zip_longest(ratings_list, range(max_length), fillvalue=None))
years_open = list(zip_longest(years_open, range(max_length), fillvalue=None))
phone_number_list = list(zip_longest(phone_number_list, range(max_length), fillvalue=None))
street_address_list = list(zip_longest(street_address_list, range(max_length), fillvalue=None))
locality_list = list(zip_longest(locality_list, range(max_length), fillvalue=None))
full_addy_list = list(zip_longest(full_addy_list, range(max_length), fillvalue=None))
price_list = list(zip_longest(price_list, range(max_length), fillvalue=None))
categories_list = list(zip_longest(categories_list, range(max_length), fillvalue=None))

data = {
    "business_name":businesses,
    "category":categories_list,
    "ratings":ratings_list,
    "years_open":years_open,
    "phone_number":phone_number_list,
    "full_address": full_addy_list,
    'street_address':street_address_list,
    'city':locality_list,
    'price':price_list
}

csv_file = "pre_cleaned_output.csv"

# Open the CSV file in write mode
with open(csv_file, mode="w", newline="") as file:

    # Create a CSV writer
    csv_writer = csv.writer(file)

    # Write the header row (keys of the dictionary)
    header = list(data.keys())
    csv_writer.writerow(header)

    # Write the data rows (values of the dictionary)
    # Transpose the data to align it correctly
    rows = zip(*data.values())
    csv_writer.writerows(rows)

print(f"Data has been exported to {csv_file}")
