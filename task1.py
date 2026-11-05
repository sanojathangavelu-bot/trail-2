#task1
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r"C:\Users\acer\Downloads\Train.csv")
print(df)
print(df.head(10))
print((df.columns))
print(df.dtypes)
print(df.isnull().sum())


#task2
print(df[df['Age'].isnull()])
df["Age"]=df["Age"].fillna(df["Age"].mean())
print(df["Age"])
print(df.duplicated().sum)
print(df.info())

#task3
arr=np.array([df["Age"]])
print(arr)
age=df['Age'].mean()
print(age)
age=(df['Age']>30)
print(age.sum)


#task4
passengers=len(df)
print(passengers)
survived=df['Survived']==1
print(survived.sum())
percentage=df['Survived']/passengers*100
print(percentage)
male=df['Sex']==("male")
print(male.sum())
print(male.mean())
sur=(df['Pclass']==1)&(df['Survived']==1)
print(sur.sum())
sur=(df['Pclass']==2)&(df['Survived']==1)
print(sur.sum())
sur=(df['Pclass']==3)&(df['Survived']==1)
print(sur.sum())

