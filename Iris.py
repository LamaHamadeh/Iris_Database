#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 10:47:53 2017

@author: lamahamadeh
"""

#Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from matplotlib.colors import ListedColormap
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression 

#-------------------------------------------------
print('Reading the Dataframe \n')

#Read the dataframe
iris = load_iris()
X = iris.data
df = pd.DataFrame(X)
df.columns = iris ['feature_names']
df['target'] = iris ['target']
print(df.head())
#-------------------------------------------------

#================Apply Clustering / kmeans algorithm===========================
print('KMeans Algorithm ... \n')

#Apply KMeans algorithm
kmeans_model = KMeans(n_clusters = 3, init = 'random', n_init = 60, max_iter = 400, random_state = 43)
kmeans_model.fit(X)
centroids = kmeans_model.cluster_centers_
KM_labels = kmeans_model.labels_ #tese are the labels generated from the KMeans clustering method
OR_labels = df.target #these are the original labels provided by the dataset
df['kMean predicted label'] = kmeans_model.labels_ #Here we add to the iris dataset a column that 
#contains the KMeans prediction labels in order to compare between the target column and the kmean clustering perdication
print (df.head())

#Plotting and visulisation

#Scatter plot of the original labels provided by the dataset: OR_labels
colormap=np.array(['Green', 'Blue', 'Red'])
fig = plt.figure()
plt.subplot(4, 3, 1)
plt.scatter(df['sepal length (cm)'], y=df['sepal width (cm)'], c=colormap[OR_labels], s=40)
plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')

plt.subplot(4, 3, 2)
plt.scatter(df['sepal length (cm)'], y=df['petal length (cm)'], c=colormap[OR_labels], s=40)
plt.xlabel('sepal length (cm)')
plt.ylabel('petal length (cm)')
plt.title('Iris Data Clusters Before Applying KMeans Method',fontsize=16)

plt.subplot(4, 3, 3)
plt.scatter(df['sepal length (cm)'], y=df['petal width (cm)'], c=colormap[OR_labels], s=40)
plt.xlabel('sepal length (cm)')
plt.ylabel('petal width (cm)')

plt.subplot(4, 3, 4)
plt.scatter(df['sepal width (cm)'], y=df['sepal length (cm)'], c=colormap[OR_labels], s=40)
plt.xlabel('sepal width (cm)')
plt.ylabel('sepal length (cm)')

plt.subplot(4, 3, 5)
plt.scatter(df['sepal width (cm)'], y=df['petal length (cm)'], c=colormap[OR_labels], s=40)
plt.xlabel('sepal width (cm)')
plt.ylabel('petal length (cm)')

plt.subplot(4, 3, 6)
plt.scatter(df['sepal width (cm)'], y=df['petal width (cm)'], c=colormap[OR_labels], s=40)
plt.xlabel('sepal width (cm)')
plt.ylabel('petal width (cm)')

plt.subplot(4, 3, 7)
plt.scatter(df['petal length (cm)'], y=df['sepal length (cm)'], c=colormap[OR_labels], s=40)
plt.xlabel('petal length (cm)')
plt.ylabel('sepal length (cm)')

plt.subplot(4, 3, 8)
plt.scatter(df['petal length (cm)'], y=df['sepal width (cm)'], c=colormap[OR_labels], s=40)
plt.xlabel('petal length (cm)')
plt.ylabel('sepal width (cm)')

plt.subplot(4, 3, 9)
plt.scatter(df['petal length (cm)'], y=df['petal width (cm)'], c=colormap[OR_labels], s=40)
plt.xlabel('petal length (cm)')
plt.ylabel('petal width (cm)')

plt.subplot(4, 3, 10)
plt.scatter(df['petal width (cm)'], y=df['sepal length (cm)'], c=colormap[OR_labels], s=40)
plt.xlabel('petal width (cm)')
plt.ylabel('sepal length (cm)')

plt.subplot(4, 3, 11)
plt.scatter(df['petal width (cm)'], y=df['sepal width (cm)'], c=colormap[OR_labels], s=40)
plt.xlabel('petal width (cm)')
plt.ylabel('sepal width (cm)')

plt.subplot(4, 3, 12)
plt.scatter(df['petal width (cm)'], y=df['petal length (cm)'], c=colormap[OR_labels], s=40)
plt.xlabel('petal width (cm)')
plt.ylabel('petal length (cm)')
    
#Scatter plots of the labels generated by KMeans clustering method: KM_labels
fig = plt.figure()
plt.subplot(4, 3, 1)
plt.scatter(df['sepal length (cm)'], y=df['sepal width (cm)'], c=colormap[KM_labels], s=40)
plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')

plt.subplot(4, 3, 2)
plt.scatter(df['sepal length (cm)'], y=df['petal length (cm)'], c=colormap[KM_labels], s=40)
plt.xlabel('sepal length (cm)')
plt.ylabel('petal length (cm)')
plt.title('Iris Data Clusters After Applying KMeans Method',fontsize=16)

plt.subplot(4, 3, 3)
plt.scatter(df['sepal length (cm)'], y=df['petal width (cm)'], c=colormap[KM_labels], s=40)
plt.xlabel('sepal length (cm)')
plt.ylabel('petal width (cm)')

plt.subplot(4, 3, 4)
plt.scatter(df['sepal width (cm)'], y=df['sepal length (cm)'], c=colormap[KM_labels], s=40)
plt.xlabel('sepal width (cm)')
plt.ylabel('sepal length (cm)')

plt.subplot(4, 3, 5)
plt.scatter(df['sepal width (cm)'], y=df['petal length (cm)'], c=colormap[KM_labels], s=40)
plt.xlabel('sepal width (cm)')
plt.ylabel('petal length (cm)')

plt.subplot(4, 3, 6)
plt.scatter(df['sepal width (cm)'], y=df['petal width (cm)'], c=colormap[KM_labels], s=40)
plt.xlabel('sepal width (cm)')
plt.ylabel('petal width (cm)')

plt.subplot(4, 3, 7)
plt.scatter(df['petal length (cm)'], y=df['sepal length (cm)'], c=colormap[KM_labels], s=40)
plt.xlabel('petal length (cm)')
plt.ylabel('sepal length (cm)')

plt.subplot(4, 3, 8)
plt.scatter(df['petal length (cm)'], y=df['sepal width (cm)'], c=colormap[KM_labels], s=40)
plt.xlabel('petal length (cm)')
plt.ylabel('sepal width (cm)')

plt.subplot(4, 3, 9)
plt.scatter(df['petal length (cm)'], y=df['petal width (cm)'], c=colormap[KM_labels], s=40)
plt.xlabel('petal length (cm)')
plt.ylabel('petal width (cm)')

plt.subplot(4, 3, 10)
plt.scatter(df['petal width (cm)'], y=df['sepal length (cm)'], c=colormap[KM_labels], s=40)
plt.xlabel('petal width (cm)')
plt.ylabel('sepal length (cm)')

plt.subplot(4, 3, 11)
plt.scatter(df['petal width (cm)'], y=df['sepal width (cm)'], c=colormap[KM_labels], s=40)
plt.xlabel('petal width (cm)')
plt.ylabel('sepal width (cm)')

plt.subplot(4, 3, 12)
plt.scatter(df['petal width (cm)'], y=df['petal length (cm)'], c=colormap[KM_labels], s=40)
plt.xlabel('petal width (cm)')
plt.ylabel('petal length (cm)')

plt.figure()
plt.subplot(2,2,1)
plt.hist(df['sepal length (cm)'],color = '#43E5C9')
plt.title('sepal length (cm)')

plt.subplot(2,2,2)
plt.hist(df['sepal width (cm)'],color = '#43E5C9')
plt.title('sepal width (cm)')

plt.subplot(2,2,3)
plt.hist(df['petal length (cm)'],color = '#43E5C9')
plt.title('petal length (cm)')

plt.subplot(2,2,4)
plt.hist(df['petal width (cm)'],color = '#43E5C9')
plt.title('petal width (cm)')


plt.show()

#It is worth mentioning that the labels might change colour/numeric value between
#the original and KMeans labels, but the idea here is to see if the clustering 
#methos of KMeans produces the same groups as the original lables. 
#-------------------------------------------------

#================Apply Classification / knn algorithm==========================
print('Knn Algorithm ... \n')

X = iris.data[:, :2]  # we only take the first two features.
y = iris.target
 
h = .02  # step size in the mesh
 
# Create color maps
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])


# apply Neighbours Classifier and fit the data.
Knn = KNeighborsClassifier(n_neighbors = 15)
Knn.fit(X, y)
 
# Plot the decision boundary. For that, we will assign a color to each
# point in the mesh [x_min, m_max]x[y_min, y_max].
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))
Z = Knn.predict(np.c_[xx.ravel(), yy.ravel()])
 
# Put the result into a color plot
Z = Z.reshape(xx.shape)
plt.figure()
plt.pcolormesh(xx, yy, Z, cmap=cmap_light)
 
# Plot also the training points
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold)
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.xlabel('sepal length (cm)')
plt.ylabel('petal width (cm)')
plt.title('K = 15')

plt.show()
#-------------------------------------------------

#================Apply Classification / regression algorithm==========================
print('Linear Regression Algorithm ... \n')

#define two features from the original dataframe
X1 = df[['petal length (cm)']]
y1 = df[['petal width (cm)']]

#apply linear regression algorithm
X_train1, X_test1, y_train1, y_test1 = train_test_split(X1, y1, test_size = 0.3, random_state =7)
Reg_model = LinearRegression()
fit_model = Reg_model.fit(X_train1, y_train1)
score1 = Reg_model.score(X_test1, y_test1)
print('the score of the regression model is ', score1) #0.941869014915

#print the coeffieicnt of the regression line
print ('The regression line equation is : f(x) = ax+b,\n'
       'where a is the slope of the line and b is the \n'
       'intersction point with the y axis' )
print ('the slope value of the regression line a = ' , fit_model.intercept_)
print ('the intersection point with the y axis b = ' , fit_model.coef_)

#plotting the data with the regression line
plt.figure()
plt.scatter(x=df["petal length (cm)"], y=df["petal width (cm)"],color = 'blue')
plt.plot(X1, Reg_model.predict(X1), color='black', linewidth=3)
plt.xlabel('sepal length (cm)')
plt.ylabel('petal width (cm)')
plt.title('Linear Regression')
plt.show()

#-------------------------------------------------
