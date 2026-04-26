import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

data = {
    "Study_Hours":[5,2,4,1,6,2,3,5,1,4,6,2,3,4,5,7,3,2,6,4,5,1,3,6,4,2,5,7,3,4],
    "Screen_Time":[3,8,4,7,2,6,5,3,9,4,2,7,6,4,3,2,5,8,3,4,3,9,6,2,5,7,4,2,6,5],
    "Assignment_Delay":[0,3,1,4,0,2,1,0,5,1,0,3,2,1,0,0,2,3,0,1,0,4,2,0,1,3,1,0,2,1],
    "Sleep_Hours":[7,5,6,5,8,6,7,7,4,6,8,5,6,7,7,8,6,5,7,6,7,4,6,8,6,5,7,8,6,7],
    "Status":[0,1,0,1,0,1,0,0,1,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,1,0,0,1,0]
}

df = pd.DataFrame(data)

s

X = df[["Study_Hours","Screen_Time","Assignment_Delay","Sleep_Hours"]]
y = df["Status"]



X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)



model = SVC(kernel='linear')

model.fit(X_train,y_train)



y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test,y_pred)

print("\nModel Accuracy:", round(accuracy*100,2), "%")



print("\nEnter New Student Details")

study = float(input("Study Hours per day: "))
screen = float(input("Screen Time (hours): "))
delay = float(input("Assignment Delay (days): "))
sleep = float(input("Sleep Hours: "))



new_data = [[study,screen,delay,sleep]]

prediction = model.predict(new_data)

print("\nPredicted Class:", prediction[0])

if prediction[0] == 0:
    print("Student is Productive")
else:
    print("Student is Procrastinating")