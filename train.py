#import libraries
import bentoml 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import re 
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
print("libraries import successful")

#read the data
data=pd.read_csv("SMSSpamCollection",sep='\t',header=None,names=['Label', 'SMS'])
print("data read successfully")

## Randomise the dataset
randomised_data=data.sample(frac=1,random_state=1)

#convert the target(label) to numerical feature
randomised_data.Label=(randomised_data.Label=="spam").astype(int)

#train test split
data_train,data_test=train_test_split(randomised_data,test_size=0.2,random_state=1)
y_train=data_train["Label"]
y_test=data_test["Label"]
del data_train["Label"]
del data_test["Label"]


## Remove punctuatuions form sms
data_train["SMS"]=data_train["SMS"].replace("\W", " ", regex=True)
data_test["SMS"]=data_test["SMS"].replace("\W", " ", regex=True)

# transform letter to lower case
data_train["SMS"]=data_train["SMS"].str.lower()
data_test["SMS"]=data_test["SMS"].str.lower()

# transform letter to lower case
data_train["SMS"]=data_train["SMS"].str.lower()
data_test["SMS"]=data_test["SMS"].str.lower()


# data transformation
vectorizer = CountVectorizer()
X_train_encoded = vectorizer.fit_transform(data_train['SMS'])
X_test_encoded = vectorizer.transform(data_test['SMS'])
print("data transformed successfully")

#trainning the model
nb_model = MultinomialNB()
nb_model.fit(X_train_encoded, y_train)
y_pred = nb_model.predict_proba(X_test_encoded)[:, 1]
accuracy = nb_model.score(X_test_encoded, y_test)
print("Accuracy:", accuracy)
print("model is trained")

#saving the trained model to disk
saved_model=bentoml.sklearn.save_model("naive_bayes_model",nb_model , custom_objects={"countvectorizer":vectorizer})
saved_model

print("model is saved")