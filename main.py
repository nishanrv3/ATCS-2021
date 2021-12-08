import pandas as pd
import matplotlib.pyplot as plt

# Read in data from our csv file
match_data = pd.read_csv("australian open match data - Sheet1 (1).csv")

match_data.plot(kind="scatter", x="1st Serve Average Speed(kmh)", y="1st Serve % Won")
plt.show()

match_data.plot(kind="scatter", x="1st Serve Average Speed(kmh)", y="Outcome")
plt.show()

match_data.plot(kind="scatter", x="2nd Serve Average Speed(kmh)", y="2nd Serve % Won")
plt.show()

match_data.plot(kind="scatter", x="2nd Serve Average Speed(kmh)", y="Outcome")
plt.show()

match_data.plot(kind="scatter", x="1st Serve % In", y="Outcome")
plt.show()


print(match_data.mode())


