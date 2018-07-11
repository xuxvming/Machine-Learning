# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 09:19:00 2018

@author: xxiu
"""
import pandas as pd
import numpy as np
 

def handle_non_numerical_data(df):
    
    columns = df.columns.values
    
    for column in columns:
        #creating a dictionary with text and numerical values
        text_digit_vals = {}
        def convert_to_int(val):
            #for every column, create a function to convert that into integer values
            return text_digit_vals[val]
        
        #determin the value of each column, if not integer or float. it is char
        if df[column].dtype != np.int64 and df[column].dtype!=np.float64:
            #getting all unique non repteative values 
            column_contents = df[column].values.tolist()
            unique_elements = set(column_contents)
            
            x= 0
            #if the unique value is not in the dictionary, put it in
            for unique in unique_elements:
                if unique not in text_digit_vals:
                    text_digit_vals[unique] = x
                    x+=1
            #reseting the comlumn by mapping the function with that column       
            df[column] = list(map(convert_to_int,df[column]))
            
            
    return df



def adding_header(file_name,column_names):
    df = pd.read_csv(file_name)
    df.columns = column_names 
    
    
    return df

def preprocess (df):
    df['traveltime'] = df['traveltime'] / 60
    df['studytime'] = df['studytime'] /60
    df['absences'] = df['absences'] / 10
    df['G1'] = df['G1']/10
    df['G2'] = df['G2']/10
    df['G3'] = df['G3']/10
    return df

