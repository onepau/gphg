# gphg
Code and explanations for data mining and machine learning for the Grand Prix d'Horlogerie de Genève (GPHG)

This document contains some brief technical explanations of the procedure I used to scrape, combine and analyse historical data from the GPHG competitions with a view to applying machine learning techniques to the data in attempt to see how the data could be used to predict probabilities of winning the overall trophy.

I started by scraping the GPHG website (http://www.gphg.org) to obtain the necessary data. As of the year 2008, all data is encoded in the same HTML format, making it relatively easy to extract the individual features for each watch that has been entered in the competition. The website was scraped using the urllib2 module in Python, then the relevant features (technical specifications of a watch) filtered out using BeautifulSoup. I then created a Pandas DataFrame containing the data that I needed.

One major issue (yet to be resolved) is the unicode formatting in the output file, which I could not seem to convert for processing in Pandas. My workaround was to do various search and replaces in the CSV file in Excel - not ideal, I know - but it gave me more or less what I needed in a quicker time frame. If anyone has any ideas how to solve this, they are very welcome!

Another problem is the encoded data prior to around 2008, which is all contained in a single cell of the CSV file, rather than separated by features. In some cases, the relevant features can be found in the text. The next step, which I have yet to implement, is a tokenization of this text with a view to populating the relevant feature columns in the Pandas DataFrame.

I concatenated the individual CSV files into a global data file. There is an incomplete script (gphg-selector.py) to automatically add a binary value for each watch according to whether it was pre-selected for the final awards or not. I would like to do the same for the winners of the individual category prizes, too. Once this is complete the data will offer a more robust foundation for testing different machine learning models to the data to see what happens. 

I'm sure the code could be improved and simplified (I'm a relative newbie at python, data mining and machine learning). In particular, I have yet to grasp the construction and use of functions, which I'm sure would help here. Any comments are welcome.
