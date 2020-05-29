# -*- coding: utf-8 -*-
"""
Created on Thu May 28 17:30:51 2020

@author: pc
"""

import pandas as pd
import matplotlib.pyplot as plt

from bs4 import BeautifulSoup
import requests

#r = requests.get("https://www.ycombinator.com/companies/")
#
#soup = BeautifulSoup(r.text)
#
#soup.findAll('script')

import json

zr = requests.get("https://api.ycombinator.com/companies/export.json")

df = pd.DataFrame(zr.json())
#display(df)
with pd.ExcelWriter("Data_Science_Internship_Assignment.xlsx", engine="openpyxl", mode="a") as writer:
    df.to_excel(writer, sheet_name="Scraping results", startrow=0, startcol=0)