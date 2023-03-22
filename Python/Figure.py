import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns (optional)

dtype={""}

data = pd.read_csv(r"GameLogsCSV\DateFormat.csv") 

data.sort_values(["Date"], axis=0, ascending=[False], inplace=True)
data.sort_values(["NumberofGames"], axis=0, ascending=[False], inplace=True)
data.sort_values(["DayofWeek"], axis=0, ascending=[False], inplace=True)
data.sort_values(["VisitingTeam"], axis=0, ascending=[False], inplace=True)
data.sort_values(["VisitingTeamLeague"], axis=0, ascending=[False], inplace=True)
data.sort_values(["VisitingTeamGameNumber"], axis=0, ascending=[False], inplace=True)
data.sort_values(["HomeTeam"], axis=0, ascending=[False], inplace=True)
data.sort_values(["HomeTeamLeague"], axis=0, ascending=[False], inplace=True)
data.sort_values(["HomeTeamGameNumber"], axis=0, ascending=[False], inplace=True)
data.sort_values(["VistingTeamScore"], axis=0, ascending=[False], inplace=True)
data.sort_values(["HomeTeamScore"], axis=0, ascending=[False], inplace=True)
data.sort_values(["NumberofOuts"], axis=0, ascending=[False], inplace=True)
data.sort_values(["DayNight"], axis=0, ascending=[False], inplace=True)
data.sort_values(["Completition_Information"], axis=0, ascending=[False], inplace=True) # Misspelt index label 
data.sort_values(["Forfeit_Information"], axis=0, ascending=[False], inplace=True)
data.sort_values(["Protest_Information"], axis=0, ascending=[False], inplace=True)
data.sort_values(["BallParkID"], axis=0, ascending=[False], inplace=True)
data.sort_values(["Attendance"], axis=0, ascending=[False], inplace=True)

# NaN subject values - Drop 
data = data.fillna(0)

# Drop Labels: Completition_Information, Forfeit_Information, and Protes_ Information

# Add condition to certain Attendance values of NaN and/or the value of 0.0

print("\nSorting:")
print(data)





