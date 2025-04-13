# -*- coding: utf-8 -*-
"""Lab_2_Kulubecioglu_Mehmet_Statistical_Methods_Of_ML

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xrByJQqunE35ZLaFuzqG1Ap9WqjZJVRj
"""

pip install pandas scikit-learn graphviz numpy

import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.model_selection import train_test_split
from IPython.display import Image
import graphviz

training = pd.read_csv("titanic-train.csv")
print(training.info())
print(training.head())

print(training.isnull().sum())

training["Age"] = training["Age"].fillna(training["Age"].mean())

training["Gender"] = training["Gender"].apply(lambda x: 0 if x == "male" else 1)

columns = ["Fare", "Pclass", "Gender", "Age", "SibSp"]
X_input = training[columns].values
y_target = training["Survived"].values

clf_train = tree.DecisionTreeClassifier(criterion="entropy", max_depth=3)
clf_train = clf_train.fit(X_input, y_target)

accuracy = clf_train.score(X_input, y_target)
print(f"Model success rate: {accuracy:.2%}")

with open("titanic.dot", 'w') as f:
    tree.export_graphviz(clf_train, out_file=f, feature_names=columns)

pip install graphviz

import subprocess
subprocess.run(["dot", "-Tpng", "titanic.dot", "-o", "titanic.png"], check=True)

testing = pd.read_csv("titanic-test.csv")

testing["Age"] = testing["Age"].fillna(testing["Age"].mean())
testing["Gender"] = testing["Gender"].apply(lambda x: 0 if x == "male" else 1)

X_test = testing[columns].values
target_labels = clf_train.predict(X_test)
testing["Est_Survival"] = target_labels

all_data = pd.read_csv("titanic_all.csv")
testing_results = pd.merge(testing, all_data[['Name', 'Survived']], on="Name")
acc = np.sum(testing_results["Est_Survival"] == testing_results["Survived"]) / len(testing_results)
print(f"Success rate compared to actual results: {acc:.2%}")

all_data = pd.read_csv("titanic_all.csv")
print(all_data.columns)

all_data = pd.read_csv("titanic_all.csv")

# Mevcut sütunları listele
print("Sütunlar:", all_data.columns.tolist())

# Dosyayı oku
all_data = pd.read_csv("titanic_all.csv")

# Sütun isimlerini düzenle
all_data.columns = all_data.columns.str.strip()  # Fazladan boşlukları temizle
all_data.columns = all_data.columns.str.lower()  # Küçük harfe çevir

# Düzeltilmiş sütunları göster
print( all_data.columns.tolist())

# Veriyi yükle
all_data = pd.read_csv("titanic_all.csv")
testing = pd.read_csv("titanic-test.csv")

# Sütun isimlerini temizle ve küçük harfe çevir
all_data.columns = all_data.columns.str.strip().str.lower()
testing.columns = testing.columns.str.strip().str.lower()

# Temizlenmiş sütunları kontrol et
print("all_data sütunları:", all_data.columns.tolist())
print("testing sütunları:", testing.columns.tolist())

all_data = pd.read_csv("titanic_all.csv", usecols=['Survived', 'Pclass', 'Gender', 'Age', 'SibSp', 'Fare'])
all_data["Gender"] = all_data["Gender"].apply(lambda x: 0 if x == "male" else 1)
all_data["Age"] = all_data["Age"].fillna(all_data["Age"].mean())


X = all_data[columns].values
y = all_data["Survived"].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)

clf_train = tree.DecisionTreeClassifier(criterion="entropy", max_depth=3)
clf_train = clf_train.fit(X_train, y_train)

train_score = clf_train.score(X_train, y_train)
test_score = clf_train.score(X_test, y_test)

print(f"Training accuracy rate: {train_score:.2%}")
print(f"Test accuracy rate: {test_score:.2%}")



"""**Question 9**"""

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd


data = pd.read_csv("titanic-train.csv")


data["Age"] = data["Age"].fillna(data["Age"].mean())
data["Gender"] = data["Gender"].apply(lambda x: 0 if x == "male" else 1)

X = data[["Fare", "Pclass", "Gender", "Age", "SibSp"]].values
y = data["Survived"].values


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


clf = DecisionTreeClassifier(criterion="entropy", max_depth=3)
clf.fit(X_train, y_train)


accuracy = clf.score(X_test, y_test)
print(f"Accuracy: {accuracy:.2%}")

"""**Question 10**"""

from sklearn.metrics import accuracy_score

# Evaluate the accuracy of the model
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2%}")

from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))