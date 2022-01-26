#Name: Nishan Rajavasireddy
#Date: December 19, 2021

#imports
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


#read in data from our csv file
match_data = pd.read_csv("australian open match data - Sheet1 (1).csv")

#graph functions
def scatterplot(x, y, color):
    match_data.plot(kind="scatter", x=x, y=y, color=color)
    plt.show()

#scatterplots
scatterplot("1st Serve Average Speed(kmh)", "1st Serve % Won", "red")
scatterplot("2nd Serve Average Speed(kmh)", "2nd Serve % Won", "red")
scatterplot("1st Serve % In", "Outcome", "blue")

#serve speed regression model
X_servespeed_train, X_servespeed_test, y_speedoutcome_train, y_speedoutcome_test = train_test_split(match_data['1st Serve Average Speed(kmh)'],match_data['Outcome']
                , test_size = 0.2, shuffle = False)
X_servespeed_train = X_servespeed_train.values.reshape(-1,1)
servespeed_model = LogisticRegression()
servespeed_model.fit(X_servespeed_train, y_speedoutcome_train)

X_servespeed_test = X_servespeed_test.values.reshape(-1,1)
speed_predictedoutcome = servespeed_model.predict(X_servespeed_test)
speed_score = accuracy_score(y_speedoutcome_test, speed_predictedoutcome)
print(speed_score)

#serve accuracy regression model
X_serveaccuracy_train, X_serveaccuracy_test, y_accuracyoutcome_train, y_accuracyoutcome_test = train_test_split(match_data['1st Serve % In'],match_data['Outcome']
                , test_size = 0.2, shuffle = False)
X_serveaccuracy_train = X_serveaccuracy_train.values.reshape(-1,1)
serveaccuracy_model = LogisticRegression()
serveaccuracy_model.fit(X_serveaccuracy_train, y_accuracyoutcome_train)

X_serveaccuracy_test = X_serveaccuracy_test.values.reshape(-1,1)
accuracy_predictedoutcome = serveaccuracy_model.predict(X_serveaccuracy_test)
accuracy_score = accuracy_score(y_accuracyoutcome_test, accuracy_predictedoutcome)
print(accuracy_score)

#bar graph
labels = ["speed_score", "accuracy score"]
scores = [speed_score, accuracy_score]
plt.bar(labels, scores)
plt.show()

#getting the mode
print(match_data.mode())


