# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 22:09:44 2026

@author: tsow2
"""

import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd
import seaborn as sns 





# Préprocessing 
data=pd.read_csv(r"C:\Users\tsow2\OneDrive\Bureau\cours2iemeannee\Projets\Projet_Preprocessing\Projet Data analyst\customer_shopping_behavior.csv")
data.head
data.describe(include="all")
data.isnull().sum()

data["Review Rating"]=data.groupby(["Category"])["Review Rating"] .transform(lambda x: x.fillna(x.median()) )
data.isnull().sum()


data.columns=data.columns.str.lower()
data.columns=data.columns.str.replace(" ", "_")
data.columns
data=data.rename(columns={"purchase_amount_(usd)": "purchase_amount"})
data.columns


# Creation d'une colonne age_group
def repartition(age):
    if age<25 : 
        return "Young Adult"
    elif age<35 :
        return "Adult"
    elif age<50 :
        return "Middle Aged"
    else:
        return "senior"
data["age_groupe"]=data["age"].apply(repartition)

data.columns


# purchase_frequency_days
frequency_map={
    "Fortnightly":14 , 
    "Weekly": 7 , 
    "Quarterly":90  , 
    "Bi-weekly":15, 
    "Annualy":365 , 
    "Every 3 months": 90

}
data["purchase_frequency_days"]=data["frequency_of_purchases"].map(frequency_map)
data=data.drop("promo_code_used",axis=1, errors='ignore')
data.columns

# Sauvegarder le DataFrame traité en CSV
data.to_csv(r"C:\Users\tsow2\OneDrive\Bureau\cours2iemeannee\Projets\Projet_Preprocessing\Projet Data analyst\customer.csv", index=False, encoding='utf-8')



