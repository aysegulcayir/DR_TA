# -*- coding: utf-8 -*-
"""
Created on Wed May 27 13:55:57 2020

@author: pc
"""

#import pandas as pd
#import matplotlib.pyplot as plt
#
#dataset = pd.read_excel("Data_Science_Internship_Assignment.xlsx" , sheetname = "Data")
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
df = pd.read_csv('Book1.csv',sep=';')


edu_list = ['school','university','academy','training','nursery','tuition','learning','education',
           'institute','institution']
NGO_list = ['not-for-profit','non-profit','non-governmental']
def edu(name):
    for keyword in edu_list:
        if keyword in name:
            return True
    return False 

def NGO(name):
    for keyword in NGO_list:
        if keyword in name:
            return True
    return False 
def select_year(date):
    date= int(date[:4])
    return date
    
df['university']=df.NAME.str.lower().apply(edu)
df['govern_np']=df.NAME.str.lower().apply(NGO) | df.WEBSITE.str.contains(".gov")
df["year"]=df["LAUNCH DATE"].apply(select_year)
df["mature_company"]=(df["year"]<1990)& ( ~df['university'])&( ~df['govern_np'])
df["startsup"]=(df["year"]>=1990)& ( ~df['university'])&( ~df['govern_np'])
df["unclassified"]=(~df["mature_company"])&(~df["startsup"])& ( ~df['university'])&( ~df['govern_np'])

df["TYPE"]=df[['university','govern_np',"mature_company","startsup","unclassified"] ].idxmax(axis=1)

df = df.drop(['university','govern_np',"mature_company","startsup","unclassified","year"],axis = 1)
df_count = df["TYPE"].value_counts()

with pd.ExcelWriter("assignment.xlsx", engine="openpyxl", mode="a") as writer:
    df.to_excel(writer, sheet_name="Data", startrow=0, startcol=0)
    df_count.to_excel(writer, sheet_name="Count", startrow=0, startcol=0)


    
#for index, row in df.iterrows():
    
#    for i in edu_list:
#        for j in NGO_list:
#            if i in df.iloc[index,0].lower():
#                df.iloc[index,10] = 'university/school'
#            elif (j in str(df.iloc[index,2]).lower()) or (j in str(df.iloc[index,6]).lower()):
#                df.iloc[index,10] = 'government/non-profit'
#            elif int(df.iloc[index,7][:4]) < 1990:
#                df.iloc[index,10] = 'mature company'
#            elif  int(df.iloc[index,7][:4]) >= 1990:
#                df.iloc[index,10] = 'startup'
#            else:
#                df.iloc[index,10] = 'unclassified'
                
                

#df.TYPE.value_counts() # Count the number of university/school, government/NGO, mature companies
#
#df['TYPE'].isna().sum() # Total number of companies
#
## Number of start-ups = total number of companies - number of university/schools 
##                                                 - number of government/NP
##                                                 - number of mature companies
#
## Number of Unclassified = 0
#
#df.to_excel("output.xlsx")


