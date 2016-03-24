#!/usr/bin/env python3

# -------------
# Baby_Names.py
# -------------

##importing the required libraries##
import pandas as pd
import numpy as np
import glob
import matplotlib.pyplot as plt

train_DF_AK=pd.read_csv('namesbystate/AK.txt', delimiter=',', names=['State','Sex','Year Born','Name','Name Frequency'])

##Creating a big DataFrame (train_DF_popular) containing the data from all states##
train_DF_all=pd.DataFrame()
for fil in glob.glob('./namesbystate/*.TXT'):
     train_DF_all=train_DF_popular.append(pd.read_csv(fil, delimiter=',', names=['State','Sex','Year Born','Name',\
                                                     'Name Frequency']), ignore_index=True)



##Grouping by Name and couting the total frequency for each name to find the most popular name##
train_DF_total_freq=train_DF_all.groupby('Name').sum()['Name Frequency']
print "The most popular name of all time is:", train_DF_total_freq.idxmax(),'\n','With total count of:',\
train_DF_total_freq.ix[train_DF_total_freq.idxmax()]

female_names=pd.DataFrame(train_DF_all.ix[train_DF_all['Year Born']==2013]\
                          .groupby(['Sex','Name']).sum()['Name Frequency'].ix['F'])
male_names=pd.DataFrame(train_DF_all.ix[train_DF_all['Year Born']==2013]\
                        .groupby(['Sex','Name']).sum()['Name Frequency'].ix['M'])
male_female_inner_join=pd.concat([female_names, male_names], axis=1, join='inner')
print "The most gender ambiguos name in 2013 is:", male_female_inner_join.sum(axis=1).idxmax()
print male_female_inner_join.sum(axis=1).max()

female_names=pd.DataFrame(train_DF_all.ix[train_DF_all['Year Born']==1945]\
                          .groupby(['Sex','Name']).sum()['Name Frequency'].ix['F'])
male_names=pd.DataFrame(train_DF_all.ix[train_DF_all['Year Born']==1945]\
                        .groupby(['Sex','Name']).sum()['Name Frequency'].ix['M'])
male_female_inner_join=pd.concat([female_names, male_names], axis=1, join='inner')
print "The most gender ambiguos name in 1945 is:", male_female_inner_join.sum(axis=1).idxmax()
print male_female_inner_join.sum(axis=1).max()

names_1980 = pd.DataFrame(train_DF_all.ix[train_DF_all['Year Born']==1980].groupby('Name').sum()['Name Frequency'])
names_2014 = pd.DataFrame(train_DF_all.ix[train_DF_all['Year Born']==2014].groupby('Name').sum()['Name Frequency'])
names_1980_2014 = pd.merge(names_1980, names_2014, left_index=True, right_index=True, \
                           suffixes=['_1980', '_2014'], how='inner')
names_1980_2014['names_rate_increase']=100*(names_1980_2014['Name Frequency_2014']-\
                                    names_1980_2014['Name Frequency_1980'])/(names_1980_2014['Name Frequency_1980'])
largest_increase = names_1980_2014.ix[names_1980_2014['names_rate_increase'].idxmax()]
print "%s has had the largest increase of %d percent" %(names_1980_2014['names_rate_increase'].idxmax(),\
                                                        largest_increase['names_rate_increase'])

names_1980_2014['names_rate_decrease']=100*(names_1980_2014['Name Frequency_1980']-\
                                    names_1980_2014['Name Frequency_2014'])/(names_1980_2014['Name Frequency_2014'])
largest_decrease = names_1980_2014.ix[names_1980_2014['names_rate_decrease'].idxmax()]
print "%s has had the largest decrease of %f percent" %(names_1980_2014['names_rate_decrease']\
                                                        .idxmax(),largest_decrease['names_rate_decrease'])


names_1980 = pd.DataFrame(train_DF_all.ix[train_DF_all['Year Born']==1980].groupby('Name').sum()['Name Frequency'])
names_2014 = pd.DataFrame(train_DF_all.ix[train_DF_all['Year Born']==2014].groupby('Name').sum()['Name Frequency'])
names_1980_2014 = pd.merge(names_1980, names_2014, left_index=True, right_index=True, \
                           suffixes=['_1980', '_2014'], how='outer').fillna(0)
names_1980_2014['names_rate_increase']=100*(names_1980_2014['Name Frequency_2014']-\
                                    names_1980_2014['Name Frequency_1980'])/(1+names_1980_2014['Name Frequency_1980'])
largest_increase = names_1980_2014.ix[names_1980_2014['names_rate_increase'].idxmax()]
print "%s has had even larger increase of %d percent" %(names_1980_2014['names_rate_increase']\
                                                        .idxmax(),largest_increase['names_rate_increase'])


names_1980_2014['names_rate_decrease']=100*(names_1980_2014['Name Frequency_1980']-\
                                    names_1980_2014['Name Frequency_2014'])/(1+names_1980_2014['Name Frequency_2014'])
largest_decrease = names_1980_2014.ix[names_1980_2014['names_rate_decrease'].idxmax()]
print "%s has had even larger decrease of %f percent" %(names_1980_2014['names_rate_decrease']\
                                                        .idxmax(),largest_decrease['names_rate_decrease'])