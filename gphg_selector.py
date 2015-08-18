########
# Script for joining multiple CSV files into a single dataframe

#import glob
#import pandas as pd
#
#allFiles = glob.glob("/*.csv")
#frame = pd.DataFrame()
#list_ = []
#for file_ in allFiles:
#    df = pd.read_csv(file_,index_col=None, header=0)
#    list_.append(df)
#	frame = pd.concat(list_)

### GPHG scraper, processor and predictor

### for the HTML processing
import urllib2
import re
from bs4 import BeautifulSoup as bs

# for the data processing and ML
import pandas as pd
import numpy as np

# Open the master file
data = pd.read_csv('all_gphg.csv')

# Get the URLs for all selected watches (2012-2014)
yrs = ['12', '13', '14']
selected_watch_base_url = ("http://www.gphg.org/horlogerie/en/prize-list/prize-list-")
selected_addresses = []
for yr in yrs:
	address = selected_watch_base_url + yr
	selected_addresses.append(address)


# Get the individual URLs for all selected watches in each year
for address in selected_addresses:
	page = urllib2.urlopen(address).read()
	soup = bs(page, features="xml")
	links = soup.find_all('a')
	for link in links:
		href = (link.get('href'))
		string = str(href)
		if string.startswith('/horlogerie/en/prize-list/'):
			url2 = 'http://www.gphg.org'+string
			page = urllib2.urlopen(url2).read()
			soup = bs(page, features="xml")
			reference = [ref.get_text() for ref in soup.find_all("div", class_="field field-name-field-reference field-type-text field-label-inline clearfix")]
			reference = str(reference).strip('[]')
			reference = str(reference).replace('\\nReference:', '')
			reference = str(reference).replace('\\n', '')
			references.append(reference)
			for reference in data['Reference']:
				data['Selected'] = 1

data.to_csv('all_gphg.csv')
