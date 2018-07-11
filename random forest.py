# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 09:33:29 2018

@author: xxiu
"""


import numpy as np
import helper 
from sklearn import cross_validation,preprocessing,svm
from sklearn.ensemble import RandomForestRegressor
from statistics import mean
from sklearn.tree import export_graphviz
import pydot
import matplotlib.pyplot as plt
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
    
    
    
header = ['course', 'school', 'sex', 'age','address', 'famsize', 'Pstatus', 'Medu', 'Fedu', 'Mjob', 'Fjob', 'reason', 'guardian', 'traveltime', 'studytime', 'failures', 'schoolsup', 'famsup', 'paid', 'activities', 'higher', 'internet', 'romantic', 'famrel', 'freetime', 'goout', 'Dalc', 'Walc', 'health', 'absences', 'G1', 'G2', 'G3']
feature_list = ['course', 'school', 'sex', 'age','address', 'famsize', 'Pstatus', 'Medu', 'Fedu', 'Mjob', 'Fjob', 'reason', 'guardian', 'traveltime', 'studytime', 'failures', 'schoolsup', 'famsup', 'paid', 'activities', 'higher', 'internet', 'romantic', 'famrel', 'freetime', 'goout', 'Dalc', 'Walc', 'health', 'absences', 'G1', 'G2']
df = helper.adding_header('data.csv',header)

df = helper.handle_non_numerical_data(df)

df = helper.preprocess(df)
y= np.array(df['G3'])
df = df.drop(columns =['G3'],axis =1)
X= np.array(df)


X_train, X_test, y_train, y_test = cross_validation.train_test_split(X,y,test_size = 0.2, random_state = 42)

baseline_pred = np.mean(y)
baseline_errors = abs(baseline_pred - y)

print('Average baseline error: ', round(np.mean(baseline_errors), 2))


#X_train = preprocessing.scale(X_train)
rf = RandomForestRegressor(n_estimators = 1000, random_state = 36)
rf.fit(X_train,y_train)

y_pred = rf.predict(X_test)


errors = abs(y_pred - y_test)
print('Mean Absolute Error:', mean(errors), 'degrees.')


#mean absolute percetage error
mape = (errors / y_test)
mape[mape > 1e308] = 0
# Calculate and display accuracy
accuracy = 100 - mean(mape)
print('Accuracy:', round(accuracy, 2), '%.')
plt.figure(1)
#plt.scatter(range(len(y_pred)),y_pred,c = 'g', alpha = 0.5,label = 'predicted value')
#plt.scatter(range(len(y_test)),y_test, c ='b',alpha = 0.5,label = 'actual value')

plt.scatter(range(len(y_pred)),y_pred,c='g')
plt.plot(range(len(y_test)),y_test)



tree = rf.estimators_[5]
# Import tools needed for visualization
tree = rf.estimators_[5]
# Export the image to a dot file
export_graphviz(tree, out_file = 'tree.dot', feature_names = feature_list, rounded = True, precision = 1)
# Use dot file to create a graph
(graph, ) = pydot.graph_from_dot_file('tree.dot')
# Write graph to a png file
graph.write_png('tree.png')

importances = list(rf.feature_importances_)
# List of tuples with variable and importance
feature_importances = [(feature, round(importance, 2)) for feature, importance in zip(feature_list, importances)]
# Sort the feature importances by most important first
feature_importances = sorted(feature_importances, key = lambda x: x[1], reverse = True)
# Print out the feature and importances 
[print('Variable: {:20} Importance: {}'.format(*pair)) for pair in feature_importances];

plt.figure(2)
plt.style.use('fivethirtyeight')
# list of x locations for plotting
x_values = list(range(len(importances)))
# Make a bar chart
plt.bar(x_values, importances, orientation = 'vertical')
# Tick labels for x axis
plt.xticks(x_values, feature_list, rotation='vertical')
# Axis labels and title
plt.ylabel('Importance'); plt.xlabel('Variable'); plt.title('Variable Importances');