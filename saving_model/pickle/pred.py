import pickle

model=pickle.load(open('dabetic_80.pkl','rb'))





data= model.predict([[6,3,1,4,5,6,7,8]])

if data[0]==0:
    print("Person is diabetic")
else:
    print("Person is not Diabetic")