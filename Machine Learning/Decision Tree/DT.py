from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
import pandas as pd

data = pd.read_csv('Oasis_longitudinal.csv')

accuracy_list = []
opt_score = 0
opt_var=2.0
folds_no = 10 

aa= DecisionTreeClassifier() 
