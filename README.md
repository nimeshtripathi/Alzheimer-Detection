# Alzheimer-Detection

Note: For the Deep Learning Part of the project, access to ADNI dataset is required.



Note: The values in the hyperparameters for the code are set at optimal values, however, they can be changed.


Part 1: Machine Learning 

Objective: Early onset of Alzheimer’s can be predicted through machine learning algorithms, but are not to the state of art yet.
Accurately predicting the different stages of dementia is still being worked and improved upon.
The machine learning and deep learning algorithms, have proved certain success in this field, but its not scalable enough currently.
Medical practitioners are still searching for this to be downscaled enough (in terms of processing required) so that it is available easily.
The main goal of this project is to predict the early onset of Alzheimer’s.


Dataset:

The Datasets used in the project are from OASIS.
The data is longitudinal MRI scans ( 150 Scans), across different age groups.
The patients in the dataset, were all right handed and have been scanned at least once, per patient.
The classification categories in the Data are- 1. Demented 2. Non Demented 3. Converted.
The converted patients, were detected to be non-demented at the first visit, but were later found to have dementia, on a later visit.


Column Descriptors:

The column descriptors in the dataset are:


Clinical Dementia Rating

Socioeconomic Status

Years of Education

Mini-mental State Examination

Atlas Scaling Factor

Estimated Total Intracranial volume

Normalize whole brain volume



Exploratory Data Analysis( EDA)


While trying to work with the data, I referenced Kaggle, for getting better correlation in the data.
Kaggle had a detailed explanation on Exploratory Data Analysis, which I referenced.(https://www.kaggle.com/ekami66/detailed-exploratory-data-analysis-with-python)
With EDA, I found the minimum, maximum and average values of each of the column descriptors.
The effect of this was observed with different models, with the dependencies on different variables.


Missing Values
The dataset has 8 missing values, which can be solved by two ways. 
The first one is dropping the rows, containing the missing values, however since there are only 150 rows, dropping 8 rows, would be losing 5% of the dataset.
Hence the missing values were replaced. While replacing the values, certain columns had discrete values and needed to be replaced using the median values.
They were then grouped and replaced.


Logistic Regression:

Several Logistic Regression models were tested to get the optimal hyperparameter.
The hyperparameter tuning was done for obtaining the optimal value for parameter C(in the hyperparameter space), as the regularization parameter.
Overfitting and underfitting was a major problem, since with large values of the hyperparameter,the model was overfitting.


SVM

For support vector machine, I used 2 kernels, which were - Radial Basis Function(rbf) and the Linear Kernel(LK).
The different models had different kernels(rbf, LK),degrees, shrinking coefficients etc.
The different combinations were done to the minimize the classifications.


Decision Tree

Decision Trees cause the maximum separation,due to division of data into a tree-like structure. 
With its help, classification was done using Gini-impurity.






Part 2: Deep Learning CNN

Here, I attempted to detect whether the scans had Alzheimer’s or not.
The data used in this part of the project is from ADNI.


Model:

A 3-D CNN Model was used with the following parameters:
For each convolutional layer with 3x3x3 kernels of 64 layers.
Different Models were tried, but the best was achieved with λ=0.01 and p= 0.2
(λ= L2 regularization parameter, and p= dropout)
Two images, which were obtained from the same patient, with a year between were taken as the input.
Using subtraction of the two images, the decline in the gray matter in the brain is highlighted in red as the output image in the next slide.

Note: The detection is not optimized due to lack of GPU and processing resources, due to which, the image was segmented, and parts of the image were used for comparison after subtraction. However, for the areas under comparison were detected successfully with an overall accuracy of 62% while the best validation accuracy was 64%.


