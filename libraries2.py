# THIRD PARTY PYTHON LIBRARIES
#a numpy : numerical computation
import numpy as np


arr =np.array([1,2,3])
print(arr)

#b pandas: data manipulation 
import pandas as pd


data = {'Name': ['Alice','Bob'],'Age':[25,30]}
df =pd.DataFrame(data)
print(df)

#c matplotlib
import matplotlib.pyplot as plt


x =[1,2,3,4]
y = [10,20,25,40]
plt.plot(x,y)
plt.show()

#d requests:HTTP Requests
import requests

response = requests.get('http://api.github.com')
print(response.status_code)

#e beautifulsoup:web scraping
from bs4 import BeautifulSoup
import requests


page =requests.get("http://Example.com")
soup =BeautifulSoup(page.content,'html.parser')
print(soup.title.text)