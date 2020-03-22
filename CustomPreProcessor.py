#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
import numpy as np
from sklearn.utils import shuffle


# In[19]:


"""
This class is responsible for taken a csv, pre-processing the data, shuffling it, scaling the inputs and
returning a triple composed by the dataset, the scaled inputs, and the binary target 
(if Match is Over 2.5, target is 1, 0 otherwise)
"""
class CustomPreProcessor:
    
    def __init__(self, csv_file):
        self.csv_file = csv_file
    
    """
    This method:
    - reads the csv file
    - creates the target column from the total match goals column
    - drops the total goals column
    - shuffles the dataset randomly
    - extract the input columns and the target column
    - scale the inputs
    - drop unnecessary columns
    Returns the pre_processed data, the scaled inputs and the targets
    """
    def pre_process(self, inputs_index_begin, scaler):
        raw_dataset = pd.read_csv(self.csv_file)
        dataset = raw_dataset.copy()
        
        tgts = np.where(dataset['Tot_Goals'] > 2, 1, 0)
        dataset['Over2.5'] = tgts
        dataset.drop('Tot_Goals', axis=1, inplace=True)
        
        shuffled_data = shuffle(dataset)
        
        inputs = shuffled_data.iloc[:,inputs_index_begin:-1]
        targets = shuffled_data.iloc[:,-1]
        
        scaler.fit(inputs)
        scaled_inputs = scaler.transform(inputs)
        
        shuffled_data.iloc[:,3:-1] = scaled_inputs
        
        to_drop = ['match_id','home','away']
        shuffled_data.drop(to_drop, axis=1, inplace=True)

        return shuffled_data, scaled_inputs, targets

