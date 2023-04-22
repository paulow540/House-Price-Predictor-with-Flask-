import numpy as np
import pandas as pd
# %matplotlib inline
# import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle

housing = pd.read_csv("Housing.csv")
housing.head(5)

categorical_features = ["mainroad", "guestroom", "basement", "hotwaterheating", "airconditioning", "prefarea", "furnishingstatus"]

for i in categorical_features:
    data = housing[i].replace(housing[i].unique(),
                             range(len(housing[i].unique())), inplace=True)

X = housing.drop(["price","area"], axis=1)
y = housing["price"]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
# X_test.isnull()
print(X_train)

lm = LinearRegression()
lm.fit(X_train, y_train)


pickle.dump(lm, open("model.pkl","wb"))
model = pickle.load(open("model.pkl", "rb"))

