### GPHG scraper, processor and predictor

### for the HTML processing
import urllib2
import re

### for the HTML parsing
import nltk
import enchant
from enchant.checker import SpellChecker
from bs4 import BeautifulSoup as bs
from bs4 import SoupStrainer as strain
from bs4 import Comment, Tag

# for the data processing and ML
import pandas as pd
import numpy as np

data = pd.read_csv('all_gphg.csv')

address = ("http://www.gphg.org/watches/en/grand-prix-dhorlogerie-de-geneve/2012/PRE")
page = urllib2.urlopen(address).read()
soup = bs(page, features="xml")

#get links for use later
links = soup.find_all('a')
print("No. of links found: ", len(links))

urls = []
for link in links:
	href = (link.get('href'))
	urls.append(href)

urls = set(urls)
urls = list(urls)

parse_links = []

for url in urls:
	string = str(url)
	if string.startswith('/watches/en/node/'):
		string = "http://www.gphg.org"+string
		parse_links.append(string)

x = len(data)+1

for link in parse_links:		
	page = urllib2.urlopen(link).read()
	soup = bs(page, features="xml")
	print("Parsing: "), link
	brand = [brand.get_text() for brand in soup.find_all("div", class_="brand")]
	brand = str(brand).strip('[]')
	brand = str(brand).replace('\\n', '')
	data.loc[x, "Brand"] = brand
	model = [model.get_text() for model in soup.find_all("div", class_="title")]
	model = str(model).strip('[]')
	model = str(model).replace('\\n', '')
	data.loc[x, "Model"] = model
	case = [case.get_text() for case in soup.find_all("div", class_="field field-name-field-case-material field-type-list-text field-label-inline clearfix")]
	case = str(case).strip('[]')
	case = str(case).replace('\\nCase:', '')
	case = str(case).replace('\\n', '')
	data.loc[x, "Case"] = case
	strap = [strap.get_text() for strap in soup.find_all("div", class_="field field-name-field-bracelet-strap-material field-type-list-text field-label-inline clearfix")]
	strap = str(strap).strip('[]')
	strap = str(strap).replace('\\nBracelet strap:', '')
	strap = str(strap).replace('\\n', '')
	data.loc[x, "Strap"] = strap
	buckle = [buckle.get_text() for buckle in soup.find_all("div", class_="field field-name-field-bracelet-buckle-type field-type-list-text field-label-inline clearfix")]
	buckle = str(buckle).strip('[]')
	buckle = str(buckle).replace('\\nBuckle:', '')
	buckle = str(buckle).replace('\\n', '')
	data.loc[x, "Buckle"] = buckle
	setting = [setting.get_text() for setting in soup.find_all("div", class_="field field-name-field-setting field-type-list-text field-label-inline clearfix")]
	setting = str(setting).strip('[]')
	setting = str(setting).replace('\\nSetting:', '')
	setting = str(setting).replace('\\n', '')
	data.loc[x, "Setting"] = setting
	water_resistance = [wr.get_text() for wr in soup.find_all("div", class_="field field-name-field-water-resistance field-type-text field-label-inline clearfix")]
	water_resistance = str(water_resistance).strip('[]')
	water_resistance = str(water_resistance).replace('\\nWaterproofness:', '')
	water_resistance = str(water_resistance).replace('\\', '')
	data.loc[x, "Water resistance"] = water_resistance
	size = [size.get_text() for size in soup.find_all("div", class_="field field-name-field-size field-type-text field-label-inline clearfix")]
	size = str(size).strip('[]')
	size = str(size).replace('\\nSize:', '')
	size = str(size).replace('\\n', '')
	data.loc[x, "Size"] = size
	thickness = [thickness.get_text() for thickness in soup.find_all("div", class_="field field-name-field-case-thickness field-type-text field-label-inline clearfix")]
	thickness = str(thickness).strip('[]')
	thickness = str(thickness).replace('\\nThickness:', '')
	thickness = str(thickness).replace('\\n', '')
	data.loc[x, "Thickness"] = thickness
	movement = [movement.get_text() for movement in soup.find_all("div", class_="group-movement field-label-inline")]
	movement = str(movement).strip('[]')
	movement = str(movement).replace('\\nMovement:', '')
	movement = str(movement).replace('\\n', '')
	movement = str(movement).replace('\\n', '')
	data.loc[x, "Movement"] = movement
	functions = [function.get_text() for function in soup.find_all("div", class_="field field-name-field-functions field-type-list-text field-label-inline clearfix")]
	functions = str(functions).strip('[]')
	functions = str(functions).replace('\\nFunctions:', '')
	functions = str(functions).replace('\\n', '')
	functions = str(functions).replace('\t', '')
	data.loc[x, "Functions"] = functions
	reference = [ref.get_text() for ref in soup.find_all("div", class_="field field-name-field-reference field-type-text field-label-inline clearfix")]
	reference = str(reference).strip('[]')
	reference = str(reference).replace('\\nReference:', '')
	reference = str(reference).replace('\\n', '')
	data.loc[x, "Reference"] = reference
	year = [year.get_text() for year in soup.find_all("div", class_="field field-name-field-year field-type-text field-label-inline clearfix")]
	year = str(year).strip('[]')
	year = str(year).replace('\\nYear:', '')
	year = str(year).replace('\\n', '')
	data.loc[x, "Year"] = year
	collection = [collection.get_text() for collection in soup.find_all("div", class_="field field-name-field-collection field-type-text field-label-inline clearfix")]
	collection = str(collection).strip('[]')
	collection = str(collection).replace('\\nCollection:', '')
	collection = str(collection).replace('\\n', '')
	collection = str(collection).replace('\t', '')
	data.loc[x, "Collection"] = collection
	price = [price.get_text() for price in soup.find_all("div", class_="field field-name-field-price-chf field-type-text field-label-inline clearfix")]
	price = str(price).strip('[]')
	price = str(price).replace('\\nPrice:', '')
	price = str(price).replace('CHF', '')
	price = str(price).replace('\\n', '')
	data.loc[x, "Price"] = price
	description = [brand.get_text() for brand in soup.find_all("div", class_="field field-name-body field-type-text-with-summary field-label-inline clearfix")]
	description = str(description).strip('[]')
	description = str(description).replace('\\nDescription:', '')
	description = str(description).replace('\\n', '')
	description = str(description).replace('\\n', '')
	data.loc[x, "Description"] = description
	height = [brand.get_text() for brand in soup.find_all("div", class_="field field-name-field-case-height field-type-text field-label-inline clearfix")]
	height = str(height).strip('[]')
	height = str(height).replace('\\nCase height:', '')
	height = str(height).replace('\\n', '')
	data.loc[x, "Case height"] = height
	x = x+1


# print("Finished parsing, total watches: ", x)
print("Size of data: "), len(data)

data.to_csv('all-gphg.csv')
	
