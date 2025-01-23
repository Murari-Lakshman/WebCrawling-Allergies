# Importing all the required files
import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

# Reading the Links from the file
df = pd.read_csv(r'test.csv', header=None, names=['Link'])
# Defining the header or column heading
header = ['Name', 'Scientific Name', 'Occurrence', 'Allergen Name', 'Alternative Allergen Name', 'Allergen Designation', 'Protein Family', 'Sequence Known', 'Allergen Stability', 'Nature', 'Properties', 'Purification']
# Creating an empty set called value
value = []

# Using for loop to iterate over the links that we read from the file
for link in df['Link']:
    r = requests.get(link)
    content = r.content

    soup = BeautifulSoup(content, 'html.parser')

    fdata = soup.find(id='generalFoodData')
    n1 = fdata.find('span', string='Name:')
    name = n1.find_next('span').get_text(strip=True) if n1 else ''

    s1 = fdata.find('span', string='Scientific Name:')
    scientific_name = s1.find_next('span').get_text(strip=True) if s1 else ''

    o1 = fdata.find('span', string='Occurrence')
    occurrence = s1.find_next('span').get_text(strip=True) if o1 else ''

    sdata = soup.find_all(class_='tab-pane')

    tvalue = []

    for data in sdata:
        a1 = data.find('span', string='Allergen Name:')
        allergen_name = a1.find_next('span').get_text(strip=True) if a1 else ''

        a2 = data.find('span', string='di Alternatve Allergen Names:')
        alt_allergen_name = a1.find_next('span').get_text(strip=True) if a2 else ''

        d1 = data.find('span', string='Allergen Designation:')
        allergen_designation = d1.find_next('span').get_text(strip=True) if d1 else ''

        p1 = data.find('span', string='Protein Family:')
        protien_fam = p1.find_next('span').get_text(strip=True)if p1 else ''

        s1 = data.find('span', string='Sequence Known?:')
        sequence = s1.find_next('span').get_text(strip=True)if s1 else ''

        as1 = data.find('span', string='Allergen stability:')
        allergen_stability = as1.find_next('span').get_text(strip=True) if as1 else ''

        cr1 = data.find('span', string='Nature of main cross-reacting proteins:')
        cross_reacting_protien = cr1.find_next('span').get_text(strip=True) if cr1 else ''

        p2 = data.find('span', string='Allergen properties &amp; biological function:')
        properties = p2.find_next('span').get_text(strip=True) if p2 else ''

        p3 = data.find('span', string='Allergen purification:')
        purification = p3.find_next('span').get_text(strip=True) if p3 else ''

        tvalue.append([name, scientific_name, occurrence, allergen_name, alt_allergen_name, allergen_designation, protien_fam, sequence, allergen_stability, cross_reacting_protien, properties, purification])

    value.extend(tvalue)

fname = 'data.csv'

with open(fname, 'w', newline='', encoding='utf-8')as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(value)