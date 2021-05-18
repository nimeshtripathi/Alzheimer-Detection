from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

accuracy_list = []
opt_score = 0
opt_var=2.0
folds_no = 10  
Regression_1 = LogisticRegression(C=2)
#accuracy
metrics = cross_val_metrics_val(Regression_1, train_x, train_y, var1=folds_no,
                         flag='accuracy')  
#model
R = LogisticRegression(C=opt_var).fit(train_x_scaled, Y_trainval)

metric_x = LR.metrics_val(X_test_scaled, Y_test)
y_final = LR.predict(X_test_scaled)
#recall
recall_data_test = recall_metrics_val(Y_test, y_final, label_pos=1)


#metrics
print(metric_x)
print(recall_data_test)
