# -*- coding: utf-8 -*-
"""
Created on Fri May 29 14:35:24 2020

@author: pc
"""
#import pandas as pd
#import matplotlib.pyplot as plt
#dataset = pd.read_excel("Data_Science_Internship_Assignment-1.xlsx" , sheetname = "Data")
#print(dataset.shape)
#print(dataset.head(20))
#print(dataset.info())
#print(dataset.columns)
#copydf = dataset.copy()
#copydf =copydf.drop(['HQ REGION','HQ COUNTRY', 'HQ CITY'],axis = 1)
#print(copydf["LAUNCH DATE"].str[:4])
##copydf['LAUNCH DATE'] = copydf['LAUNCH DATE'].astype(int)
##afterninetydf = copydf.filter(["LAUNCH DATE"]) 

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel("Data_Science_Internship_Assignment.xlsx" , sheetname = "Data")

edu_list = ['school','university','academy','training','nursery','tuition','learning','education',
           'institute','institution']
NGO_list = ['not-for-profit','non-profit','non-governmental']


def edu(name):
    for keyword in edu_list:
        if keyword in str(name):
            return True
    return False 

def NGO(name):
    for keyword in NGO_list:
        if keyword in str(name):
            
            return True
    return False 
def select_year(date):
    date = str(date)
    date= int(date[:4])
    return date
    
df['university']=df.NAME.str.lower().apply(edu)
df['govern_np']=df.NAME.str.lower().apply(NGO) | df["TAGLINE"].str.lower().apply(NGO) | df["TAGS"].str.lower().apply(NGO) | df.WEBSITE.str.contains(".gov")
df["year"]=df["LAUNCH DATE"].apply(select_year)
df["mature_company"]=(df["year"]<1990)& ( ~df['university'])&( ~df['govern_np'])
df["startsup"]=(df["year"]>=1990)& ( ~df['university'])&( ~df['govern_np'])
df["unclassified"]=(~df["mature_company"])&(~df["startsup"])& ( ~df['university'])&( ~df['govern_np'])

df["TYPE"]=df[['university','govern_np',"mature_company","startsup","unclassified"] ].idxmax(axis=1)

df = df.drop(['university','govern_np',"mature_company","startsup","unclassified","year"],axis = 1)
df_count = df["TYPE"].value_counts()

with pd.ExcelWriter("Data_Science_Internship_Assignment.xlsx", engine="openpyxl", mode="a") as writer:
    df.to_excel(writer, sheet_name="Data", startrow=0, startcol=0)
    df_count.to_excel(writer, sheet_name="Count", startrow=0, startcol=0)


print("Amount of companies according to their types:\n",df_count)

type_list = df["TYPE"].unique()

plt.title("Amount of companies according to their types")
colors = ['b','g','m','r']
plt.bar(type_list, df_count, color = colors)
plt.show()
    