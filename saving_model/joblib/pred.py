import joblib

model=joblib.load('dabetic_80.pkl')





data= model.predict([[6,3,1,4,5,6,7,8]])

if data[0]==0:
    print("Person is diabetic")
else:
    print("Person is not Diabetic")