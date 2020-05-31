# -*- coding: utf-8 -*-
"""
Created on Thu May 28 17:30:51 2020

@author: pc
"""

import pandas as pd
import requests
import openpyxl

result = requests.get("https://api.ycombinator.com/companies/export.json") #scrapping data
df = pd.DataFrame(result.json()) #converting json and making dataframe  

## Load excel file, remove sheets to be updated, overwrite the file
book = openpyxl.load_workbook("Data_Science_Internship_Assignment.xlsx") 
book.remove(book["Scraping results"])
book.save("Data_Science_Internship_Assignment.xlsx")

with pd.ExcelWriter("Data_Science_Internship_Assignment.xlsx", engine="openpyxl", mode="a") as writer:
    df.to_excel(writer, sheet_name="Scraping results", startrow=0, startcol=0)
    writer.save()