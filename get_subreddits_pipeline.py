import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import ast

# ------------------------------------------------------------------------------------------------------------------------
# WEB SCRAPING
# ------------------------------------------------------------------------------------------------------------------------

url = "https://frontpagemetrics.com/top-sfw-subreddits"
response = requests.get(url)
html = response.text
### Parse HTML Contents
soup = BeautifulSoup(html, "html.parser")
### Set rows into list of lists
top_subreddits = []
for tr in soup.find_all('tr'):
    cols = []
    for td in tr.find_all(['td', 'th']):
        td_text = td.get_text(strip=True)
        if len(td_text):
            cols.append(td_text)
    top_subreddits.append(cols)

# ------------------------------------------------------------------------------------------------------------------------
# DATA PREPROCESSING
# ------------------------------------------------------------------------------------------------------------------------

top_reddits_names = [item[1] for item in top_subreddits]
top_reddits_names = top_reddits_names[1:]

other_subs = ['wallstreetbets', 'soccer']
for i in other_subs:
    top_reddits_names.append('{}'.format(i))

top_reddits_names = re.sub(r"/r/", "", str(top_reddits_names))
subreddit_list = ast.literal_eval(top_reddits_names)