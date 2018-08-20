# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 17:31:49 2018

@author: ek028m

-Socrata Open Data API for Austin Animal Shelter Data
-Clean the dataset to format for visualization
"""

import pandas as pd

filePath = r'C:\Users\ek028m\Documents\PythonScripts\AustinAnimalShelterProject'
fileName = r'\animalDataset'
fileMerged = filePath + fileName

def getData():
    
    from sodapy import Socrata
    from datetime import datetime
    
    global columnsList
    #apiEndpoint = "https://data.austintexas.gov/resource/hcup-htgu.csv"
    
    Date = datetime.now().strftime('%Y%m%d')
    
    # set up a connection
    client = Socrata("data.austintexas.gov", None)
    
    # retrieve data from the animal shelter resource
    # will retrieve as json doc from API aka Python list of dictionaries via sodapy
    results = client.get("hcup-htgu")
    
    # convert to pandas dataframe
    results_df = pd.DataFrame.from_records(results)
    
    columnsList = list(results_df)
    
    results_df.to_csv(fileMerged + Date + '.csv', index = False, encoding='utf-8', \
                      columns=columnsList)
    return columnsList

#getData()

#results_df = pd.read_csv(r'C:\Users\ek028m\Documents\PythonScripts\AustinAnimalShelterProject\animalDataset20180819.csv')

#def convertYear(age):
#    age = int(age) * 365
#    return age

months = 30.4167

#def convertMonth(age):
#    age = int(age) * months
#    return age

weeks = 7

#def convertWeek(age):
#    age = int(age) * weeks
#    return age

# convert all ages to integer days
for index,row in results_df.iterrows():
    age = row.age_upon_outcome
    # convert the age
    if age.endswith('year'):
        age = age[:-5]
        age = int(age) * 365
    elif age.endswith('years'):
        age = age[:-6]
        age = int(age) * 365
    elif age.endswith('month'):
        age = age[:-6]
        age = int(age) * months
    elif age.endswith('months'):
        age = age[:-7]
        age = int(age) * months
    elif age.endswith('week'):
        age = age[:-5]
        age = int(age) * weeks
    elif age.endswith('weeks'):
        age = age[:-6]
        age = int(age) * weeks   
    elif age.endswith('day'):
        age = age[:-4]
    elif age.endswith('days'):
        age = age[:-5]
    row.age_upon_outcome = age   
    
results_df['age_upon_outcome'].apply(pd.to_numeric)        
        
# export the dataframe to csv
results_df.to_csv(fileMerged + '.csv', index = False, encoding='utf-8', \
                      columns=columnsList)      
