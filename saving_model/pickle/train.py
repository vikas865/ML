import pandas as pd
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
import pickle


url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
names=['pre','plas', 'pres', 'skin', 'test','mass', 'pedi', 'age', 'class']


df= pd.read_csv(url, names=names)
print(df.head())
array=df.values
X,y=array[:,0:8],array[:,8]

X_train,X_test,Y_train,Y_test=model_selection.train_test_split(X,y, test_size=0.2, random_state=101)

model=LogisticRegression()
model.fit(X_train,Y_train)
print("info Model has trained")

#accyracy

result= model.score(X_test, Y_test)

print(f"model accauracy :{result}")


#model saving

fileName='dabetic_80.pkl'
pickle.dump(model, open(fileName, 'wb'))


