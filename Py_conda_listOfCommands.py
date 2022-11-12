#studying call for xQL servers
#using https://www.sqlite.org/index.html
#following https://www.edureka.co/blog/python-anaconda-tutorial/

#sqlite presenter$ Python3 txt.py
# the Python library we will be using to connect to the database
import sqlite
# open a database connection
connection = sqlite3.connect('chinook.db')
# ask the connection for a <strong>cursor object</strong>
# the cursor object is used to interact with the DB and execute queries
cursor = connection.cursor()
# run a query
result_set = cursor.execute('SELECT * FROM Track') 
#cursor will execute the query and store results in the <strong>result set</strong>
for row in result_set:
      # row = <strong>tuple object</strong> where each element is a value
     print (row)
# <strong>close the cursor</strong>
cursor.close()   # once closed, a cursor object cannot be used again. We have to get a new cursor from the connection
# <strong>close the database connection</strong>
connection.close()    # this is to tell the database that we are done working with it and it can release any memory and resources associated with this connection.




#######################################               conda variables and commands            ####################################
#variable declaration
name = "Edureka"
f = 1991
print("python was founded in"  , f)
#data types
a = [1,2,3,4,5,6,7]
b = {1 : 'edureka' , 2: 'python'}
c = (1,2,3,4,5)
d = {1,2,3,4,5}
print("the list is" , a)
print("the dictionary is" , b)
print("the tuple is" , c)
print("the set is " , d)

a = 10
b = 15
#arithmetic operator
print(a + b)
print(a - b)
print(a * b)
#assignment operator
a += 10
print(a)
#comparison operator
#a != 10
#b == a
#logical operator
a > b and a > 10
#this will return true if both the statements are true.

#funcions
name = 'edureka'
for i in name:
     if i == 'a':
         break
     else:
         print(i)

#funcions 2
def func(a):
    return a ** a


res = func(10)
print(res)

#classes

class Parent:
    def func(self):
        print('this is parent')


class Child(Parent):
    def func1(self):
        print('this is child')


ob = new
Child()
ob.func()


#colleting data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('filename.csv')
print(df.head(5))

#filter data
print(df.isnull().sum())
#this will give the sum of all the null values in the dataset.
df1 = df.dropna(axis=0 , how= 'any')
#this will drop rows with null values.

#boxplot
sns.boxplot(x=df['Salary Range From'])
sns.boxplot(x=df['Salary Range To'])

#scatterplot
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(16,8))
ax.scatter(df['Salary Range From'] , df['Salary Range To'])
ax.set_xlabel('Salary Range From')
ax.set_ylabel('Salary Range TO')
plt.show()

#visualisation
sns.countplot(x= "Full-Time/Part-Time indicator" , data= df)
sns.countplot(x="Full-Time/Part-Time indicator" , hue="Salary Frequency" , data= df)
sns.countplot(hue="Full-Time/Part-Time indicator", x="Posting Type" ,data= df)
df["Salary Range From"].plot.hist()
df["Salary Range To"].plot.hist()

#heat-scheme
import matplotlib.pyplot as plt
fig = plt.figure(figsize = (10,10))
ax = fig.gca()
sns.heatmap(df1.corr(), annot=True, fmt=".2f")
plt.title("Correlation",fontsize=5)
plt.show()
