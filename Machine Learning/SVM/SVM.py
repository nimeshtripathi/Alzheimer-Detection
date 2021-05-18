import numpy as np
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC 
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.metrics import classification_report


data = pd.read_csv('Oasis_longitudinal.csv')
data = data.drop('G', axis=1)
data = data.drop('GN', axis=1)

# Replacing Missing Values
data = data.replace(np.NaN, 0)
var = data[1:]
data = data['G']
var_2 = data[2:]

train, test, label_tr, test_labels = train_test_split(var, var_2, test_size=0.4, random_state=3)


kernel_v = SVC(kernel='rbf', C=1.5)   
#kernel can be changed to poly, sigmoid, linear, by changing rbf to the other ones in the line above.

kernel_v = kernel_v.fit(train,label_tr)
y_analysis= kernel_v.predict(test)


#accuracy: print(accuracy(label_test, y_analysis)
