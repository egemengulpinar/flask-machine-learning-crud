from io import BytesIO

import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets
from sklearn.inspection import DecisionBoundaryDisplay
import numpy as np
import pylab as pl
from sklearn import neighbors, datasets
def calculate_knn():
   
   
 

  
    iris = datasets.load_iris()
    X = iris.data[:, :2] 
    Y = iris.target

    h = .02

    knn=neighbors.KNeighborsClassifier()

    knn.fit(X, Y)

    x_min, x_max = X[:,0].min() - .5, X[:,0].max() + .5
    y_min, y_max = X[:,1].min() - .5, X[:,1].max() + .5
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])

 
    Z = Z.reshape(xx.shape)
  
    pl.scatter(X[:,0], X[:,1],c=Y )
    pl.xlabel('Sepal length')
    pl.ylabel('Sepal width')

    pl.xlim(xx.min(), xx.max())
    pl.ylim(yy.min(), yy.max())
    pl.xticks(())
    pl.yticks(())

    pl.savefig("chart.png")

    

    


  
  
    





