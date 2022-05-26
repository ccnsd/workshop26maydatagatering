#!/usr/bin/env python
# coding: utf-8

# # Scraping & Crawling an Alternative Tool #
# 
# Gain access to API is hard, and it can be slow. So, people make alternative ways as like as always. Scraping and crawling tools follow one another on the world wide web. With them, you can capture data at the accessibility level of web pages. However, these tools create to help developers test products.
# Besides, Scraping has some weak points, i.e.:
# 1. no stability
# 2. imperfect data
# 3. hard coding
# 
# Here we go to scrap the bibitem result at https://scholar.google.com and convert it to a bibliography file. It keeps the bibitem tag and creates a bib file.

# In[1]:


import re
import time
from selenium import webdriver ##
from selenium.webdriver.common.by import By ##
from selenium.common.exceptions import NoSuchElementException ##


# In[30]:


askfrom = 'https://scholar.google.com'
TARGET = 'Data/myrefs.tex'

with open(TARGET, 'r') as tfile:
    Sources = re.findall(r'\\bibitem{(.*?)}(.*)', tfile.read())
    
print('There are ' + str(len(Sources)) + ' Bibitems')


# ### Webdriver ###
# As below, you need to locate chromedriver synced with your chrome app. It is the Selenium which control the webdriver. Also, you can use any other browser you prefer. 

# In[31]:


browser = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')

browser.get(askfrom)

for item in Sources:
    if (True):
        browser.get('https://scholar.google.com')
        inputfield = browser.find_element(By.ID, 'gs_hdr_tsi')
        inputfield.send_keys(item[1])
        
        print(item[0], end='\r')
        browser.find_element(By.ID, 'gs_hdr_tsb').click()
        time.sleep(10)
        
        items = browser.find_elements(By.CLASS_NAME, 'gs_ri')

        for it in items:
            it.find_element(By.CLASS_NAME, 'gs_fl').find_element(By.CLASS_NAME, 'gs_nph').click()
            time.sleep(3)

            cites = browser.find_elements(By.CLASS_NAME, 'gs_citi')
            for ct in cites:
                if ct.text == 'BibTeX':
                    lref = ct.get_attribute('href')
                    break
            break
        
        browser.get(lref)
        
        bibtex = browser.find_element(By.TAG_NAME, 'pre').text
        
    pls = re.search(r'\w{(.*?),', bibtex)

    with open('Data/citation.bib', 'a') as wfile:
        wfile.write(bibtex[:pls.span()[0]+2]+item[0]+bibtex[pls.span()[1]-1:]+'\n\n')

browser.close()


# In[ ]:




