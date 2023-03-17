# This dataset contains house sale prices for King County, which includes Seattle. It includes homes sold between May 2014 and May 2015.
import pipe as pipe


# Surpress warnings:
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
#%matplotlib inline

data = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/FinalModule_Coursera/data/kc_house_data_NaN.csv'

df = pd.read_csv(data)
print(df.head())

#Display the data types of each column using the function dtypes, then take a screenshot and submit it, include your code in the image.
print(df.dtypes)

#Drop the columns "id" and "Unnamed: 0" from axis 1 using the method drop(), then use the method describe() to obtain a statistical summary of the data.
df.drop(columns=['id', 'Unnamed: 0'],inplace=True)
df.describe()
print(df.head())

#We can see we have missing values for the columns  bedrooms and  bathrooms
print("number of NaN values for the column bedrooms :", df['bedrooms'].isnull().sum())
print("number of NaN values for the column bathrooms :", df['bathrooms'].isnull().sum())

#We can replace the missing values of the column 'bedrooms' with the mean of the column 'bedrooms'  using the method replace().
mean=df['bedrooms'].mean()
df['bedrooms'].replace(np.nan,mean, inplace=True)
mean=df['bathrooms'].mean()
df['bathrooms'].replace(np.nan,mean, inplace=True)

print("number of NaN values for the column bedrooms :", df['bedrooms'].isnull().sum())
print("number of NaN values for the column bathrooms :", df['bathrooms'].isnull().sum())

#Use the method value_counts to count the number of houses with unique floor values, use the method .to_frame() to convert it to a dataframe.
print(df['floors'].value_counts().to_frame())


#Use the function boxplot in the seaborn library to determine whether houses with a waterfront view or without a waterfront view have more price outliers.
sns.boxplot(df, x= 'waterfront', y ='price')

#Use the function regplot in the seaborn library to determine if the feature sqft_above is negatively or positively correlated with price.
sns.regplot(df, x='sqft_above', y='price')

#We can use the Pandas method corr() to find the feature other than price that is most correlated with price.
df.corr()['price'].sort_values()

#We can Fit a linear regression model to predict the 'price' using the feature 'sqft_living' then calculate the R^2.
X = df[['sqft_living']]
Y = df['price']
lm = LinearRegression()
lm.fit(X,Y)
lm.score(X, Y)

#Fit a linear regression model to predict the 'price' using the list of features:
features =["floors", "waterfront","lat" ,"bedrooms" ,"sqft_basement" ,"view" ,"bathrooms","sqft_living15","sqft_above","grade","sqft_living"]

for f in features:
    X = df[[f]]
    Y = df['price']
    lm = LinearRegression()
    lm.fit(X, Y)
    print('R^2: ', lm.score(X, Y))

#Use the list to create a pipeline object to predict the 'price', fit the object using the features in the list features, and calculate the R^2.
Input=[('scale',StandardScaler()),('polynomial', PolynomialFeatures(include_bias=False)),('model',LinearRegression())]
pipe = Pipeline(Input)

for f in features:
    X = df[[f]]
    Y = df['price']
    pipe.fit(X,Y)
    print('R^2: ',pipe.score(X,Y))

#Create and fit a Ridge regression object using the training data, set the regularization parameter to 0.1, and calculate the R^2 using the test data
X = df[features]
Y = df['price']

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.15, random_state=1)

print("number of test samples:", x_test.shape[0])
print("number of training samples:",x_train.shape[0])

ridgeModel = Ridge(alpha = 0.1)
ridgeModel.fit(x_train,y_train)
print('R^2: ',ridgeModel.score(x_test,y_test))

#Perform a second order polynomial transform on both the training data and testing data. Create and fit a Ridge regression object
# using the training data, set the regularisation parameter to 0.1, and calculate the R^2 utilising the test data provided

pr = PolynomialFeatures(degree=2)
x_train_pr = pr.fit_transform(x_train[features])
x_test_pr = pr.fit_transform(x_test[features])

ridgeModel = Ridge(alpha = 0.1)
ridgeModel.fit(x_train,y_train)
print('R^2: ',ridgeModel.score(x_test,y_test))

