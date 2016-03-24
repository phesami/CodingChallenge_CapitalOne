#!/usr/bin/env python3

# -------------
# Regression.py
# -------------


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn import preprocessing
from sklearn.cross_validation import train_test_split
from sklearn.decomposition import PCA
from sklearn.ensemble.forest import RandomForestRegressor
from sklearn.cross_validation import cross_val_score
from sklearn.metrics import mean_squared_error

import operator

##importing the data into a pandas data frame##
train_DF=pd.read_csv('codetest_train.txt', delimiter='\t')

##splitting the data into train/test set to have a set for performance evaluation##
X_train, X_test, y_train, y_test = train_test_split(train_DF.iloc[:,1:255], train_DF['target'], test_size=0.2)

##data_refine function will: 1-find the non-numeric columns, 2- fill the NaN in non-numeric columns with
#the most used element 3- transform the non-numeric columns to numeric values using LabelEncoder method
#from SKLearn, 4- fill the NaN values in the numeric columns using the mean value of them##
def data_refine(train_DF):
    #1-find the non-numeric columns#
    real_or_str=train_DF.applymap(np.isreal).all(0)
    non_num_feature=real_or_str[~real_or_str].keys()
    le = preprocessing.LabelEncoder()
    for col in non_num_feature:
        #2- fill the NaN in non-numeric columns with the most used element#
        train_DF[col].fillna(train_DF[col].describe().top, inplace=True)
        #3- transform the non-numeric columns to numeric values using LabelEncoder method from SKLearn#
        train_DF[col]=le.fit_transform(train_DF[col])
    #4- fill the NaN values in the numeric columns using the mean value of them
    train_DF.fillna(train_DF.mean(), inplace=True)
    return train_DF

X_train_refined=data_refine(X_train)
X_test_refined=data_refine(X_test)


##trying different values for n_estimators parameters (number of trees in the forrest) and evaluating the performance
#using a 5-folded cross validation on the training set##
est_list=[10,20,50,100,200]
score={}
for est in est_list:
    rfr = RandomForestRegressor(n_estimators=est, random_state=0)
    rfr.fit(X_train_refined, y_train)
    score[est]=cross_val_score(rfr, X_train_refined, y_train, cv=5).mean()

    ##finding the optimal value of n_estimators##
n_est=max(score.iteritems(), key=operator.itemgetter(1))[0]
print "the optimal value of n_estimators=%d"%(n_est)

##Using a Random Forest Regressor with the optimal C and epsilon parameters##
rfr = RandomForestRegressor(n_estimators=n_est, random_state=0)
rfr.fit(X_train_refined, y_train)
print ("score on the training set using optimal value of n_estimators is:\n"),\
mean_squared_error(y_train, rfr.predict(X_train_refined))
print ("score on the test set using optimal value of n_estimators is:\n"), \
mean_squared_error(y_test, rfr.predict(X_test_refined))

##predicting the target on the given test set and writing the output into a text file##
final_test_DF=pd.read_csv('codetest_test.txt', delimiter='\t')
X_test_final_refined=data_refine(final_test_DF)
predictions=rfr.predict(X_test_final_refined)
f = open('predicted_target_test.txt', 'w')
for pre in predictions:
    f.writelines(str(pre)+'\n')
f.close()