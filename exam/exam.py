import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score

data = pd.read_csv('salary_data.csv')
x= data[['age']] 
y = data['salary']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2,random_state=1)
model=LinearRegression()
model.fit(x_train, y_train)
y_pred=model.predict(x_test)

print(f"Intercept (a0): {model.intercept_}")
print(f"Slope (a1): {model.coef_}")
r2=r2_score(y_test, y_pred)

print (f"R-squared Score: ",r2)

user_age = float(input("Enter age to predict salary: "))

predicted_salary = model.predict(pd.DataFrame([[user_age]], columns=['age']))
print (f"The predicted salary for age {user_age} is:",predicted_salary)
plt.scatter (x_test, y_test, color='blue')
plt.plot(x_test, y_pred, color='red', linewidth=2, label='Predicted line')
plt.scatter (user_age, predicted_salary, color='green', s=100, label='User Prediction')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.title('Simple Linear Regression: Age vs Salary')
plt.legend()
plt.show()