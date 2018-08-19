# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 17:31:49 2018

@author: ek028m

Socrata Open Data API for Austin Animal Shelter Data
"""

import pandas as pd
from sodapy import Socrata
from datetime import datetime

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

filePath = r'C:\Users\ek028m\Documents\PythonScripts\AustinAnimalShelterProject'
fileName = r'\animalDataset'
fileMerged = filePath + fileName
results_df.to_csv(fileMerged + Date + '.csv', index = False, encoding='utf-8', \
                  columns=columnsList)